# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

"""
Pose Library mockup - functions.
"""

import dataclasses
import functools
import re
from typing import Any, Optional, FrozenSet, Set, Tuple, Union, Iterable, cast

if "functions" not in locals():
    from . import functions
else:
    import importlib

    functions = importlib.reload(functions)

import bpy
from bpy.types import (
    Action,
    Area,
    Bone,
    Context,
    FCurve,
    Image,
    Keyframe,
    Window,
)

FCurveValue = Union[float, int]

pose_bone_re = re.compile(r'pose.bones\["([^"]+)"\]')
"""RegExp for matching FCurve data paths."""


@dataclasses.dataclass(unsafe_hash=True, frozen=True)
class PoseCreationParams:
    armature_ob: bpy.types.Object
    src_action: Optional[Action]
    src_frame_nr: float
    bone_names: FrozenSet[str]
    new_asset_name: str


class UnresolvablePathError(ValueError):
    """Raised when a data_path cannot be resolved to a current value."""


@dataclasses.dataclass(unsafe_hash=True)
class PoseActionCreator:
    """Create an Action that's suitable for marking as Asset.

    Does not mark as asset yet, nor does it add asset metadata.
    """

    params: PoseCreationParams

    # These were taken from Blender's Action baking code in `anim_utils.py`.
    _bbone_prop_names = [
        "bbone_curveinx",
        "bbone_curveoutx",
        "bbone_curveiny",
        "bbone_curveouty",
        "bbone_rollin",
        "bbone_rollout",
        "bbone_scaleinx",
        "bbone_scaleoutx",
        "bbone_scaleiny",
        "bbone_scaleouty",
        "bbone_easein",
        "bbone_easeout",
    ]

    def create(self) -> Optional[Action]:
        """Create a single-frame Action containing only the given bones, or None if no anim data was found."""

        try:
            dst_action = self._create_new_action()
            self._store_pose(dst_action)
        finally:
            # Prevent next instantiations of this class from reusing pointers to
            # bones. They may not be valid by then any more.
            self._find_bone.cache_clear()

        if len(dst_action.fcurves) == 0:
            bpy.data.actions.remove(dst_action)
            return None

        return dst_action

    def _create_new_action(self) -> Action:
        dst_action = bpy.data.actions.new(self.params.new_asset_name)
        if self.params.src_action:
            dst_action.id_root = self.params.src_action.id_root
        dst_action.user_clear()  # actions.new() sets users=1, but marking as asset also increments user count.
        return dst_action

    def _store_pose(self, dst_action: Action) -> None:
        """Store the current pose into the given action."""
        self._store_bone_pose_parameters(dst_action)
        self._store_animated_parameters(dst_action)
        self._store_parameters_from_callback(dst_action)

    def _store_bone_pose_parameters(self, dst_action: Action) -> None:
        """Store loc/rot/scale/bbone values in the Action."""

        for bone_name in sorted(self.params.bone_names):
            self._store_location(dst_action, bone_name)
            self._store_rotation(dst_action, bone_name)
            self._store_scale(dst_action, bone_name)
            self._store_bbone(dst_action, bone_name)

    def _store_animated_parameters(self, dst_action: Action) -> None:
        """Store the current value of any animated bone properties."""
        if self.params.src_action is None:
            return

        armature_ob = self.params.armature_ob
        for fcurve in self.params.src_action.fcurves:
            match = pose_bone_re.match(fcurve.data_path)
            if not match:
                # Not animating a bone property.
                continue

            bone_name = match.group(1)
            if bone_name not in self.params.bone_names:
                # Bone is not our export set.
                continue

            if dst_action.fcurves.find(fcurve.data_path, index=fcurve.array_index):
                # This property is already handled by a previous _store_xxx() call.
                continue

            try:
                value = self._current_value(armature_ob, fcurve.data_path, fcurve.array_index)
            except UnresolvablePathError:
                # A once-animated property no longer exists. Ignore for now.
                # TODO(Sybren): maybe use the animated value instead? Not sure what for though.
                continue

            dst_fcurve = dst_action.fcurves.new(
                fcurve.data_path, index=fcurve.array_index, action_group=bone_name
            )
            dst_fcurve.keyframe_points.insert(self.params.src_frame_nr, value=value)
            dst_fcurve.update()

    def _store_parameters_from_callback(self, dst_action: Action) -> None:
        """Store extra parameters in the pose based on arbitrary callbacks.

        Not implemented yet, needs a proper design & some user stories.
        """
        pass

    def _store_location(self, dst_action: Action, bone_name: str) -> None:
        """Store bone location."""
        self._store_bone_array(dst_action, bone_name, "location", 3)

    def _store_rotation(self, dst_action: Action, bone_name: str) -> None:
        """Store bone rotation given current rotation mode."""
        bone = self._find_bone(bone_name)
        if bone.rotation_mode == "QUATERNION":
            self._store_bone_array(dst_action, bone_name, "rotation_quaternion", 4)
        elif bone.rotation_mode == "AXIS_ANGLE":
            self._store_bone_array(dst_action, bone_name, "rotation_axis_angle", 4)
        else:
            self._store_bone_array(dst_action, bone_name, "rotation_euler", 3)

    def _store_scale(self, dst_action: Action, bone_name: str) -> None:
        """Store bone scale."""
        self._store_bone_array(dst_action, bone_name, "scale", 3)

    def _store_bbone(self, dst_action: Action, bone_name: str) -> None:
        """Store bendy-bone parameters."""
        for prop_name in self._bbone_prop_names:
            self._store_bone_property(dst_action, bone_name, prop_name)

    def _store_bone_array(
        self, dst_action: Action, bone_name: str, property_name: str, array_length: int
    ) -> None:
        """Store all elements of an array property."""
        for array_index in range(array_length):
            self._store_bone_property(dst_action, bone_name, property_name, array_index)

    def _store_bone_property(
        self,
        dst_action: Action,
        bone_name: str,
        property_path: str,
        array_index: int = -1,
    ) -> None:
        """Store the current value of a single bone property."""

        bone = self._find_bone(bone_name)
        value = self._current_value(bone, property_path, array_index)

        # Get the full 'pose.bones["bone_name"].blablabla' path suitable for FCurves.
        rna_path = bone.path_from_id(property_path)

        fcurve: Optional[FCurve] = dst_action.fcurves.find(rna_path, index=array_index)
        if fcurve is None:
            fcurve = dst_action.fcurves.new(rna_path, index=array_index, action_group=bone_name)

        fcurve.keyframe_points.insert(self.params.src_frame_nr, value=value)
        fcurve.update()

    @classmethod
    def _current_value(
        cls, datablock: bpy.types.ID, data_path: str, array_index: int
    ) -> FCurveValue:
        """Resolve an RNA path + array index to an actual value."""
        value_or_array = cls._path_resolve(datablock, data_path)

        # Both indices -1 and 0 are used for non-array properties.
        # -1 cannot be used in arrays, whereas 0 can be used in both arrays and non-arrays.

        if array_index == -1:
            return cast(FCurveValue, value_or_array)

        if array_index == 0:
            value_or_array = cls._path_resolve(datablock, data_path)
            try:
                # MyPy doesn't understand this try/except is to determine the type.
                value = value_or_array[array_index]  # type: ignore
            except TypeError:
                # Not an array after all.
                return cast(FCurveValue, value_or_array)
            return cast(FCurveValue, value)

        # MyPy doesn't understand that array_index>0 implies this is indexable.
        return cast(FCurveValue, value_or_array[array_index])  # type: ignore

    @staticmethod
    def _path_resolve(
        datablock: bpy.types.ID, data_path: str
    ) -> Union[FCurveValue, Iterable[FCurveValue]]:
        """Wrapper for datablock.path_resolve(data_path).

        Raise UnresolvablePathError when the path cannot be resolved.
        This is easier to deal with upstream than the generic ValueError raised
        by Blender.
        """
        try:
            return datablock.path_resolve(data_path)  # type: ignore
        except ValueError as ex:
            raise UnresolvablePathError(str(ex)) from ex

    @functools.lru_cache(maxsize=1024)
    def _find_bone(self, bone_name: str) -> Bone:
        """Find a bone by name.

        Assumes the named bone exists, as the bones this class handles comes
        from the user's selection, and you can't select a non-existent bone.
        """

        bone: Bone = self.params.armature_ob.pose.bones[bone_name]
        return bone


def create_pose_asset(
    context: Context,
    params: PoseCreationParams,
) -> Optional[Action]:
    """Create a single-frame Action containing only the pose of the given bones.

    DOES mark as asset, DOES NOT add asset metadata.
    """

    creator = PoseActionCreator(params)
    pose_action = creator.create()
    if pose_action is None:
        return None

    functions.asset_mark(context, pose_action)
    return pose_action


def create_pose_asset_from_context(context: Context, new_asset_name: str) -> Optional[Action]:
    """Create Action asset from active object & selected bones."""

    bones = context.selected_pose_bones_from_active_object
    bone_names = {bone.name for bone in bones}

    params = PoseCreationParams(
        context.object,
        getattr(context.object.animation_data, "action", None),
        context.scene.frame_current,
        frozenset(bone_names),
        new_asset_name,
    )

    return create_pose_asset(context, params)


def copy_fcurves(
    dst_action: Action,
    src_action: Action,
    src_frame_nr: float,
    bone_names: Set[str],
) -> int:
    """Copy FCurves, returning number of curves copied."""
    num_fcurves_copied = 0
    for fcurve in src_action.fcurves:
        match = pose_bone_re.match(fcurve.data_path)
        if not match:
            continue

        bone_name = match.group(1)
        if bone_name not in bone_names:
            continue

        # Check if there is a keyframe on this frame.
        keyframe = find_keyframe(fcurve, src_frame_nr)
        if keyframe is None:
            continue
        # Create an FCurve and copy some properties.
        src_group_name = fcurve.group.name if fcurve.group else ""
        dst_fcurve = dst_action.fcurves.new(
            fcurve.data_path, index=fcurve.array_index, action_group=src_group_name
        )
        for propname in {"auto_smoothing", "color", "color_mode", "extrapolation"}:
            setattr(dst_fcurve, propname, getattr(fcurve, propname))

        dst_keyframe = dst_fcurve.keyframe_points.insert(
            keyframe.co.x, keyframe.co.y, keyframe_type=keyframe.type
        )

        for propname in {
            "amplitude",
            "back",
            "easing",
            "handle_left",
            "handle_left_type",
            "handle_right",
            "handle_right_type",
            "interpolation",
            "period",
        }:
            setattr(dst_keyframe, propname, getattr(keyframe, propname))
        dst_fcurve.update()
        num_fcurves_copied += 1
    return num_fcurves_copied


def find_keyframe(fcurve: FCurve, frame: float) -> Optional[Keyframe]:
    # Binary search adapted from https://pythonguides.com/python-binary-search/
    keyframes = fcurve.keyframe_points
    low = 0
    high = len(keyframes) - 1
    mid = 0

    # Accept any keyframe that's within 'epsilon' of the requested frame.
    # This should account for rounding errors and the likes.
    epsilon = 1e-4
    frame_lowerbound = frame - epsilon
    frame_upperbound = frame + epsilon
    while low <= high:
        mid = (high + low) // 2
        keyframe = keyframes[mid]
        if keyframe.co.x < frame_lowerbound:
            low = mid + 1
        elif keyframe.co.x > frame_upperbound:
            high = mid - 1
        else:
            return keyframe
    return None


def viewport_for_preview(context: Context) -> Tuple[Optional[Window], Optional[Area]]:
    """Return the viewport suitable for generating previews."""

    # print("\n=== Finding viewport:")
    first_viewport: Optional[Area] = None
    first_window: Optional[Window] = None
    for widx, window in enumerate(context.window_manager.windows):
        for aidx, area in enumerate(window.screen.areas):
            if area.type != "VIEW_3D":
                continue
            if first_viewport is None:
                first_viewport = area
                first_window = window
            space = area.spaces[0]
            # print(f"Window[{widx}].screen.areas[{aidx}]")
            # print(f"                .type = {area.type}")
            # print(f"               .space = {space}")
            # print(f"               camera = {space.camera}")
            # print(f"     use_local_camera = {space.use_local_camera}")
            # print(f"     view_perspective = {space.region_3d.view_perspective}")
            if space.region_3d and space.region_3d.view_perspective == "CAMERA":
                return window, area
    return first_window, first_viewport


def render_preview(context: Context) -> Image:
    """OpenGL-render a viewport.

    Return the Image datablock with the render result. This must be saved to
    disk and loaded from there in order to access the actual pixel data.
    """

    window, area = viewport_for_preview(context)
    if area is None:
        # TODO: just deal with this, instead of bothering users.
        raise RuntimeError("unable to find 3D view to render")

    # print(f"Found area: {area}")
    # print("Regions:")
    for ridx, region in enumerate(area.regions):
        # print(f"    {ridx}: {region.type}")
        if region.type == "WINDOW":
            break
    else:
        # TODO: just deal with this, instead of bothering users.
        raise RuntimeError("unable to find region to render")

    render_ctx = {
        **context.copy(),
        "area": area,
        "region": region,
        "window": window,
    }
    result = bpy.ops.render.opengl(
        render_ctx,
        animation=False,
        view_context=True,
        sequencer=False,
        write_still=False,
    )
    print(f"Rendered preview, result={result}")
    return bpy.data.images["Render Result"]


def assign_tags_from_asset_browser(asset: Action, asset_browser: bpy.types.Area) -> None:
    # TODO(Sybren): implement
    return
