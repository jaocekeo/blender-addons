# SPDX-License-Identifier: GPL-2.0-or-later

# Tuple of tuples:
# ((msgctxt, msgid), (sources, gen_comments), (lang, translation, (is_fuzzy, comments)), ...)
translations_tuple = (
    (("*", ""),
     ((), ()),
     ("fr_FR", "Project-Id-Version: Sun Position 3.1.2 (0)\nReport-Msgid-Bugs-To: \nPOT-Creation-Date: 2022-06-30 15:02:06.261278\nPO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\nLast-Translator: FULL NAME <EMAIL@ADDRESS>\nLanguage-Team: LANGUAGE <LL@li.org>\nLanguage: __POT__\nMIME-Version: 1.0\nContent-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit",
               (False,
                ("Blender's translation file (po format).",
                 "Copyright (C) 2022 The Blender Foundation.",
                 "This file is distributed under the same license as the Blender package.",
                 "Damien Picard <dam.pic@free.fr>, 2022."))),
    ),
    (("*", "Azimuth and elevation info"),
     (("bpy.types.SunPosAddonPreferences.show_az_el",),
      ()),
     ("fr_FR", "Infos d’azimut et de hauteur",
               (False, ())),
    ),
    (("*", "Show azimuth and solar elevation info"),
     (("bpy.types.SunPosAddonPreferences.show_az_el",),
      ()),
     ("fr_FR", "Afficher les infos d’azimut et de hauteur du soleil",
               (False, ())),
    ),
    (("*", "Daylight savings"),
     (("bpy.types.SunPosAddonPreferences.show_daylight_savings",
       "bpy.types.SunPosProperties.use_daylight_savings"),
      ()),
     ("fr_FR", "Heure d’été",
               (False, ())),
    ),
    (("*", "Show daylight savings time choice"),
     (("bpy.types.SunPosAddonPreferences.show_daylight_savings",),
      ()),
     ("fr_FR", "Afficher l’option de changement d’heure",
               (False, ())),
    ),
    (("*", "D° M' S\""),
     (("bpy.types.SunPosAddonPreferences.show_dms",),
      ()),
     ("fr_FR", "",
               (False, ())),
    ),
    (("*", "Show lat/long degrees, minutes, seconds labels"),
     (("bpy.types.SunPosAddonPreferences.show_dms",),
      ()),
     ("fr_FR", "Afficher les étiquettes de latitude et longitude en degrés, minutes, secondes",
               (False, ())),
    ),
    (("*", "Show North"),
     (("bpy.types.SunPosAddonPreferences.show_north",
       "bpy.types.SunPosProperties.show_north"),
      ()),
     ("fr_FR", "Afficher le nord",
               (False, ())),
    ),
    (("*", "Show north offset choice and slider"),
     (("bpy.types.SunPosAddonPreferences.show_north",),
      ()),
     ("fr_FR", "Afficher l’option et le curseur de décalage du nord",
               (False, ())),
    ),
    (("*", "Refraction"),
     (("bpy.types.SunPosAddonPreferences.show_refraction",),
      ()),
     ("fr_FR", "Réfraction",
               (False, ())),
    ),
    (("*", "Show sun refraction choice"),
     (("bpy.types.SunPosAddonPreferences.show_refraction",),
      ()),
     ("fr_FR", "Afficher l’option de réfraction du soleil",
               (False, ())),
    ),
    (("*", "Sunrise and sunset info"),
     (("bpy.types.SunPosAddonPreferences.show_rise_set",),
      ()),
     ("fr_FR", "Infos de lever et coucher",
               (False, ())),
    ),
    (("*", "Show sunrise and sunset labels"),
     (("bpy.types.SunPosAddonPreferences.show_rise_set",),
      ()),
     ("fr_FR", "Afficher les informations de lever et coucher du soleil",
               (False, ())),
    ),
    (("*", "Time and place presets"),
     (("bpy.types.SunPosAddonPreferences.show_time_place",),
      ()),
     ("fr_FR", "Préréglages d’heure et de lieu",
               (False, ())),
    ),
    (("*", "Show time/place presets"),
     (("bpy.types.SunPosAddonPreferences.show_time_place",),
      ()),
     ("fr_FR", "Afficher les préréglages d’heure et de lieu",
               (False, ())),
    ),
    (("*", "Sun Position"),
     (("bpy.types.Scene.sun_pos_properties",
       "bpy.types.SUNPOS_PT_Panel"),
      ()),
     ("fr_FR", "Position du Soleil",
               (False, ())),
    ),
    (("*", "Sun Position Settings"),
     (("bpy.types.Scene.sun_pos_properties",),
      ()),
     ("fr_FR", "Options de Position du Soleil",
               (False, ())),
    ),
    (("*", "Sun Position Presets"),
     (("bpy.types.SUNPOS_MT_Presets",),
      ()),
     ("fr_FR", "Préréglages de position du Soleil",
               (False, ())),
    ),
    (("Operator", "Synchroniser Soleil et texture"),
     (("bpy.types.WORLD_OT_sunpos_show_hdr",),
      ()),
     ("fr_FR", "",
               (False, ())),
    ),
    (("*", "UTC zone"),
     (("bpy.types.SunPosProperties.UTC_zone",),
      ()),
     ("fr_FR", "Fuseau horaire",
               (False, ())),
    ),
    (("*", "Time zone: Difference from Greenwich, England in hours"),
     (("bpy.types.SunPosProperties.UTC_zone",),
      ()),
     ("fr_FR", "Fuseau horaire : différence avec Greenwich, Angleterre, en heures",
               (False, ())),
    ),
    (("*", "If true, Environment texture moves with sun"),
     (("bpy.types.SunPosProperties.bind_to_sun",),
      ()),
     ("fr_FR", "Si actif, la texture d’environnement tourne avec le Soleil",
               (False, ())),
    ),
    (("*", "Enter coordinates"),
     (("bpy.types.SunPosProperties.co_parser",),
      ()),
     ("fr_FR", "Saisir coordonnées",
               (False, ())),
    ),
    (("*", "Enter coordinates from an online map"),
     (("bpy.types.SunPosProperties.co_parser",),
      ()),
     ("fr_FR", "Saisir des coordonnées depuis une carte",
               (False, ())),
    ),
    (("*", "Day"),
     (("bpy.types.SunPosProperties.day",),
      ()),
     ("fr_FR", "Jour",
               (False, ())),
    ),
    (("*", "Day of year"),
     (("bpy.types.SunPosProperties.day_of_year",),
      ()),
     ("fr_FR", "Jour de l’année",
               (False, ())),
    ),
    (("*", "Rotation angle of sun and environment texture"),
     (("bpy.types.SunPosProperties.hdr_azimuth",),
      ()),
     ("fr_FR", "Angle de rotation du Soleil et de la texture d’environnement",
               (False, ())),
    ),
    (("*", "Elevation"),
     (("bpy.types.SunPosProperties.hdr_elevation",),
      ()),
     ("fr_FR", "Hauteur",
               (False, ())),
    ),
    (("*", "Elevation angle of sun"),
     (("bpy.types.SunPosProperties.hdr_elevation",),
      ()),
     ("fr_FR", "Angle de hauteur du Soleil",
               (False, ())),
    ),
    (("*", "Name of texture to use. World nodes must be enabled and color set to Environment Texture"),
     (("bpy.types.SunPosProperties.hdr_texture",),
      ()),
     # TODO
     ("fr_FR", "Nom de la texture à utiliser. Les nœuds de shader du monde doivent être activés, et la couleur utiliser une texture d’environnement",
               (False, ())),
    ),
    (("*", "Latitude"),
     (("bpy.types.SunPosProperties.latitude",),
      ()),
     ("fr_FR", "Latitude",
               (False, ())),
    ),
    (("*", "Latitude: (+) Northern (-) Southern"),
     (("bpy.types.SunPosProperties.latitude",),
      ()),
     ("fr_FR", "Latitude : (+) nord (-) sud",
               (False, ())),
    ),
    (("*", "Longitude"),
     (("bpy.types.SunPosProperties.longitude",),
      ()),
     ("fr_FR", "Longitude",
               (False, ())),
    ),
    (("*", "Longitude: (-) West of Greenwich (+) East of Greenwich"),
     (("bpy.types.SunPosProperties.longitude",),
      ()),
     ("fr_FR", "Longitude : (-) ouest depuis Greenwich (+) est depuis Greenwich",
               (False, ())),
    ),
    (("*", "Month"),
     (("bpy.types.SunPosProperties.month",),
      ()),
     ("fr_FR", "Mois",
               (False, ())),
    ),
    (("*", "North Offset"),
     (("bpy.types.SunPosProperties.north_offset",),
      ()),
     ("fr_FR", "Décalage du nord",
               (False, ())),
    ),
    (("*", "Rotate the scene to choose North direction"),
     (("bpy.types.SunPosProperties.north_offset",),
      ()),
     ("fr_FR", "Tourner la scène pour choisir la direction du nord",
               (False, ())),
    ),
    (("*", "Collection of objects used to visualize sun motion"),
     (("bpy.types.SunPosProperties.object_collection",),
      ()),
     ("fr_FR", "Collection d’objets utilisée pour visualiser la trajectoire du Soleil",
               (False, ())),
    ),
    (("*", "Show object collection as sun motion"),
     (("bpy.types.SunPosProperties.object_collection_type",),
      ()),
     ("fr_FR", "Afficher la collection en tant que",
               (False, ())),
    ),
    (("*", "Analemma"),
     (("bpy.types.SunPosProperties.object_collection_type:'ANALEMMA'",),
      ()),
     ("fr_FR", "Analemme",
               (False, ())),
    ),
    (("*", "Diurnal"),
     (("bpy.types.SunPosProperties.object_collection_type:'DIURNAL'",),
      ()),
     ("fr_FR", "Diurne",
               (False, ())),
    ),
    (("*", "Draw line pointing north"),
     (("bpy.types.SunPosProperties.show_north",),
      ()),
     ("fr_FR", "Afficher une ligne pointant le nord",
               (False, ())),
    ),
    (("*", "Name of sky texture to be used"),
     (("bpy.types.SunPosProperties.sky_texture",),
      ()),
     ("fr_FR", "Nom de la texture à utiliser",
               (False, ())),
    ),
    (("*", "Distance to sun from origin"),
     (("bpy.types.SunPosProperties.sun_distance",),
      ()),
     ("fr_FR", "Distance entre l’origine et le Soleil",
               (False, ())),
    ),
    (("*", "Sun Object"),
     (("bpy.types.SunPosProperties.sun_object",
       "scripts/addons/sun_position/ui_sun.py:101"),
      ()),
     ("fr_FR", "Objet soleil",
               (False, ())),
    ),
    (("*", "Sun object to set in the scene"),
     (("bpy.types.SunPosProperties.sun_object",),
      ()),
     ("fr_FR", "Objet soleil à utiliser dans la scène",
               (False, ())),
    ),
    (("*", "Day Time"),
     (("bpy.types.SunPosProperties.UTC_zone",),
      ()),
     ("fr_FR", "Heure",
               (False, ())),
    ),
    (("*", "Time of the day"),
     (("bpy.types.SunPosProperties.time",),
      ()),
     ("fr_FR", "Heure du jour",
               (False, ())),
    ),
    (("*", "Time Spread"),
     (("bpy.types.SunPosProperties.time_spread",),
      ()),
     ("fr_FR", "Plage horaire",
               (False, ())),
    ),
    (("*", "Time period in which to spread object collection"),
     (("bpy.types.SunPosProperties.time_spread",),
      ()),
     ("fr_FR", "Plage horaire à visualiser par les objets de la collection",
               (False, ())),
    ),
    (("*", "Usage mode"),
     (("bpy.types.SunPosProperties.usage_mode",),
      ()),
     ("fr_FR", "Mode",
               (False, ())),
    ),
    (("*", "Operate in normal mode or environment texture mode"),
     (("bpy.types.SunPosProperties.usage_mode",),
      ()),
     ("fr_FR", "Passer en mode normal ou texture d’environnement",
               (False, ())),
    ),
    (("*", "Sun + HDR texture"),
     (("bpy.types.SunPosProperties.usage_mode:'HDR'",),
      ()),
     ("fr_FR", "Soleil + texture HDRI",
               (False, ())),
    ),
    (("*", "Use day of year"),
     (("bpy.types.SunPosProperties.use_day_of_year",),
      ()),
     ("fr_FR", "Utiliser le jour de l’année",
               (False, ())),
    ),
    (("*", "Use a single value for day of year"),
     (("bpy.types.SunPosProperties.use_day_of_year",),
      ()),
     ("fr_FR", "Utiliser une seule valeur pour le jour de l’année",
               (False, ())),
    ),
    (("*", "Daylight savings time adds 1 hour to standard time"),
     (("bpy.types.SunPosProperties.use_daylight_savings",),
      ()),
     ("fr_FR", "L’heure d’été ajoute une heure à l’heure standard",
               (False, ())),
    ),
    (("*", "Use refraction"),
     (("bpy.types.SunPosProperties.use_refraction",),
      ()),
     ("fr_FR", "Utiliser la réfraction",
               (False, ())),
    ),
    (("*", "Show apparent sun position due to refraction"),
     (("bpy.types.SunPosProperties.use_refraction",),
      ()),
     ("fr_FR", "Afficher la position apparente du Soleil due à la réfraction",
               (False, ())),
    ),
    (("*", "Year"),
     (("bpy.types.SunPosProperties.year",),
      ()),
     ("fr_FR", "Année",
               (False, ())),
    ),
    (("*", "Could not find 3D View"),
     (("scripts/addons/sun_position/hdr.py:262",),
      ()),
     ("fr_FR", "Impossible de trouver la vue 3D",
               (False, ())),
    ),
    (("*", "Please select an Environment Texture node"),
     (("scripts/addons/sun_position/hdr.py:268",),
      ()),
     ("fr_FR", "Veuillez utiliser un nœud de texture d’environnement",
               (False, ())),
    ),
    (("*", "Unknown projection"),
     (("scripts/addons/sun_position/hdr.py:180",),
      ()),
     ("fr_FR", "Projection inconnue",
               (False, ())),
    ),
    (("*", "Show options or labels:"),
     (("scripts/addons/sun_position/properties.py:241",),
      ()),
     ("fr_FR", "Afficher les options et étiquettes :",
               (False, ())),
    ),
    (("*", "Usage Mode"),
     (("scripts/addons/sun_position/ui_sun.py:71",),
      ()),
     ("fr_FR", "Mode",
               (False, ())),
    ),
    (("*", "Environment Texture"),
     (("scripts/addons/sun_position/ui_sun.py:85",),
      ()),
     ("fr_FR", "Texture d’environnement",
               (False, ())),
    ),
    (("*", "Enter Coordinates"),
     (("scripts/addons/sun_position/ui_sun.py:174",),
      ()),
     ("fr_FR", "Saisir coordonnées",
               (False, ())),
    ),
    (("*", "Local:"),
     (("scripts/addons/sun_position/ui_sun.py:269",),
      ()),
     ("fr_FR", "Locale :",
               (False, ())),
    ),
    (("*", "UTC:"),
     (("scripts/addons/sun_position/ui_sun.py:270",),
      ()),
     ("fr_FR", "UTC : ",
               (False, ())),
    ),
    (("*", "Sunrise:"),
     (("scripts/addons/sun_position/ui_sun.py:285",),
      ()),
     ("fr_FR", "Lever : ",
               (False, ())),
    ),
    (("*", "Sunset:"),
     (("scripts/addons/sun_position/ui_sun.py:288",),
      ()),
     ("fr_FR", "Coucher : ",
               (False, ())),
    ),
    (("*", "Please select World in the World panel."),
     (("scripts/addons/sun_position/ui_sun.py:95",
       "scripts/addons/sun_position/ui_sun.py:153"),
      ()),
     ("fr_FR", "Veuillez sélecttionner le monde dans le panneau Monde",
               (False, ())),
    ),
    (("*", "Azimuth:"),
     (("scripts/addons/sun_position/ui_sun.py:206",),
      ()),
     ("fr_FR", "Azimut :",
               (False, ())),
    ),
    (("*", "Elevation:"),
     (("scripts/addons/sun_position/ui_sun.py:209",),
      ()),
     ("fr_FR", "Hauteur :",
               (False, ())),
    ),
    (("*", "Please activate Use Nodes in the World panel."),
     (("scripts/addons/sun_position/ui_sun.py:92",
       "scripts/addons/sun_position/ui_sun.py:150"),
      ()),
     ("fr_FR", "Veuillez activer Utiliser nœuds dans le panneau Monde",
               (False, ())),
    ),
)

translations_dict = {}
for msg in translations_tuple:
    key = msg[0]
    for lang, trans, (is_fuzzy, comments) in msg[2:]:
        if trans and not is_fuzzy:
            translations_dict.setdefault(lang, {})[key] = trans
