import os

import _renames # Dupes that have different names in different regions
import _compilations # Compilations that don't have unique titles
import _supersets # Things like Game of the Year Editions, collections
import _overrides # When all else fails, manual overrides

# Establish a class for clone lists
class CloneLists:
    # dupe_list {dict}
    # comp_list [list]
    # superset_list {dict}
    # override_list {dict}
    def __init__(self, dupe_list, comp_list, superset_list, override_list, superset_override_list):
        self.dupe = dupe_list
        self.comp = comp_list
        self.super = superset_list
        self.override = override_list
        self.superoverride = superset_override_list

def clonelist(dat_name):
    if dat_name == 'Arcade - Sega - Chihiro':
        return CloneLists(
            {},
            [],
            _supersets.chihiro_superset_list(),
            {},
            {}
        )
    if dat_name == 'Apple - Macintosh':
        return CloneLists(
            _renames.mac_rename_list(),
            _compilations.mac_compilation_list(),
            _supersets.mac_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Commodore - Amiga CD':
        return CloneLists(
            _renames.amiga_cd_rename_list(),
            _compilations.amiga_cd_compilation_list(),
            _supersets.amiga_cd_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Commodore - Amiga CD32':
        return CloneLists(
            _renames.cd32_rename_list(),
            _compilations.cd32_compilation_list(),
            _supersets.cd32_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Commodore - Amiga CDTV':
        return CloneLists(
            _renames.cdtv_rename_list(),
            _compilations.cdtv_compilation_list(),
            _supersets.cdtv_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Fujitsu - FM-Towns':
        return CloneLists(
            _renames.fmt_rename_list(),
            _compilations.fmt_compilation_list(),
            _supersets.fmt_superset_list(),
            {},
            {}
        )
    elif dat_name == 'IBM - PC compatible':
        return CloneLists(
            _renames.ibm_rename_list(),
            _compilations.ibm_compilation_list(),
            _supersets.ibm_superset_list(),
            _overrides.ibm_override_list(),
            {}
        )
    elif dat_name == 'Microsoft - Xbox':
        return CloneLists(
            _renames.xbox_rename_list(),
            _compilations.xbox_compilation_list(),
            _supersets.xbox_superset_list(),
            {},
            {}
        )
    elif dat_name == 'NEC - PC Engine CD & TurboGrafx CD':
        return CloneLists(
            _renames.pce_rename_list(),
            _compilations.pce_compilation_list(),
            _supersets.pce_superset_list(),
            {},
            {}
        )
    elif (dat_name == 'Nintendo - GameCube'
        or dat_name == 'Nintendo - GameCube - NKit GCZ'
        or dat_name == 'Nintendo - GameCube - NKit ISO'
        or dat_name == 'Nintendo - GameCube - NASOS'):
        return CloneLists(
            _renames.gamecube_rename_list(),
            _compilations.gamecube_compilation_list(),
            _supersets.gamecube_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Panasonic - 3DO Interactive Multiplayer':
        return CloneLists(
            _renames.threedo_rename_list(),
            _compilations.threedo_compilation_list,
            _supersets.threedo_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Philips - CD-i':
        return CloneLists(
            _renames.cdi_rename_list(),
            _compilations.cdi_compilation_list(),
            _supersets.cdi_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Philips - CD-i Digital Video':
        return CloneLists(
            _renames.cdi_dv_rename_list(),
            [],
            {},
            {},
            {}
        )
    elif dat_name == 'Sega - Dreamcast':
        return CloneLists(
            _renames.dreamcast_rename_list(),
            _compilations.dreamcast_compilation_list(),
            _supersets.dreamcast_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Sega - Mega CD & Sega CD':
        return CloneLists(
            _renames.segacd_rename_list(),
            _compilations.segacd_compilation_list(),
            _supersets.segacd_superset_list(),
            {},
            {}
        )
    elif dat_name == 'Sega - Saturn':
        return CloneLists(
            _renames.saturn_rename_list(),
            _compilations.saturn_compilation_list(),
            _supersets.saturn_superset_list(),
            _overrides.saturn_override_list(),
            {}
        )
    elif dat_name == 'SNK - Neo Geo CD':
        return CloneLists(
            _renames.neogeo_rename_list(),
            _compilations.neogeo_compilation_list(),
            _supersets.neogeo_superset_list(),
            _overrides.neogeo_override_list(),
            {}
        )
    elif dat_name == 'Sony - PlayStation':
        return CloneLists(
            _renames.psx_rename_list(),
            _compilations.psx_compilation_list(),
            _supersets.psx_superset_list(),
            _overrides.psx_override_list(),
            {}
        )
    elif dat_name == 'Sony - PlayStation 2':
        return CloneLists(
            _renames.ps2_rename_list(),
            _compilations.ps2_compilation_list(),
            _supersets.ps2_superset_list(),
            _overrides.ps2_override_list(),
            _overrides.ps2_superset_override_list()
        )
    elif dat_name == 'VTech - V.Flash & V.Smile Pro':
        return CloneLists(
            _renames.vtech_rename_list(),
            _compilations.vtech_compilation_list(),
            _supersets.vtech_superset_list(),
            {},
            {}
        )
