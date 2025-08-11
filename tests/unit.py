import sys
from pathlib import Path

# Set the main path up the hierarchy so we can import modules directly from Retool
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))

import modules.constants as const
from modules.config.config import Config
from modules.input import UserInput
from modules.titletools import TitleTools
from modules.utils import Font, eprint

# -------------------------------------
# Boilerplate to run functions directly
# -------------------------------------

# Create the config object
config: Config = Config(
    const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION,
    const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY,
    const.PROGRAM_DOWNLOAD_LOCATION,
    const.PROGRAM_DOWNLOAD_LOCATION_KEY,
    const.CONFIG_FILE,
    const.DAT_FILE_TAGS_KEY,
    const.IGNORE_TAGS_KEY,
    const.DISC_RENAME_KEY,
    const.VERSION_IGNORE_KEY,
    const.BUDGET_EDITIONS_KEY,
    const.PROMOTE_EDITIONS_KEY,
    const.DEMOTE_EDITIONS_KEY,
    const.MODERN_EDITIONS_KEY,
    const.LANGUAGES_KEY,
    const.REGION_ORDER_KEY,
    const.VIDEO_ORDER_KEY,
    const.CLONE_LISTS_KEY,
    const.METADATA_KEY,
    const.MIAS_KEY,
    const.RA_KEY,
    const.USER_CONFIG_KEY,
    const.USER_LANGUAGE_ORDER_KEY,
    const.USER_REGION_ORDER_KEY,
    const.USER_LOCALIZATION_ORDER_KEY,
    const.USER_VIDEO_ORDER_KEY,
    const.USER_LIST_PREFIX_KEY,
    const.USER_LIST_SUFFIX_KEY,
    const.USER_OVERRIDE_EXCLUDE_KEY,
    const.USER_OVERRIDE_INCLUDE_KEY,
    const.USER_FILTER_KEY,
    const.USER_GUI_SETTINGS_KEY,
    const.SYSTEM_SETTINGS_PATH,
    const.SANITIZED_CHARACTERS,
    const.RESERVED_FILENAMES,
    UserInput(),
)

# -------------------------------------
# Version normalization tests
# -------------------------------------


def test_version_normalization(name: str) -> dict[str, str | bool]:
    """
    Extracts versions from a title's full name and normalizes them.

    Args:
        name (str): The title's full name.

    Returns:
        list[str]: The versions in the title.
    """
    versions: dict[str, str | bool] = TitleTools.get_normalized_version(name, config)
    eprint(f'Name: {name}\nVersion: {versions}\n', wrap=False)
    return versions


eprint(f'{Font.bold}\nRUNNING TEST: Version normalization{Font.end}')

# Nintendo mastering code
assert test_version_normalization('Test Title (Japan) (AFMJ)') == {'version': 'AFMJ'}
assert test_version_normalization('Test Title (Europe) (En,Fr,De,Es,It,Nl,Sv,No,Da,Fi) (AEFP)') == {
    'version': 'AEFP'
}
assert test_version_normalization('Test Title (Europe) (En,Fr,De,Es,It,Nl,Sv,No,Da,Fi) (AEFZ)') == {
    'version': 'AEFZ'
}
assert test_version_normalization('Test Title (Europe) (B8HP)') == {'version': 'B8HP'}
assert test_version_normalization('Test Title (Europe) (B8HX)') == {'version': 'B8HX'}
assert test_version_normalization('Test Title (Japan) (BDQJ)') == {'version': 'BDQJ'}
assert test_version_normalization('Test Title (Japan) (BFWJ)') == {'version': 'BFWJ'}
assert test_version_normalization('Test Title (Japan) (BTPJ)') == {'version': 'BTPJ'}
assert test_version_normalization('Test Title (Japan) (CX2J)') == {'version': 'CX2J'}
assert test_version_normalization('Test Title (Japan) (CX4J)') == {'version': 'CX4J'}
assert test_version_normalization('Test Title (USA) (En,Fr) (SKUE)') == {'version': 'SKUE'}
assert test_version_normalization('Test Title (USA) (En,Fr) (SKUZ)') == {'version': 'SKUZ'}
assert test_version_normalization('Test Title (Japan) (TACJ)') == {'version': 'TACJ'}
assert test_version_normalization('Test Title (Japan) (TCJJ)') == {'version': 'TCJJ'}
assert test_version_normalization('Test Title (Japan) (TJAJ)') == {'version': 'TJAJ'}
assert test_version_normalization('Test Title (Japan) (TJBJ)') == {'version': 'TJBJ'}
assert test_version_normalization('Test Title (Japan) (TJCJ)') == {'version': 'TJCJ'}
assert test_version_normalization('Test Title (Japan) (TJDJ)') == {'version': 'TJDJ'}
assert test_version_normalization('Test Title (Japan) (TJEJ)') == {'version': 'TJEJ'}
assert test_version_normalization('Test Title (Japan) (TQ8J)') == {'version': 'TQ8J'}
assert test_version_normalization('Test Title (Japan) (TQAJ)') == {'version': 'TQAJ'}
assert test_version_normalization('Test Title (Japan) (TQEJ)') == {'version': 'TQEJ'}
assert test_version_normalization('Test Title (Japan) (TQFJ)') == {'version': 'TQFJ'}
assert test_version_normalization('Test Title (Japan) (TQJJ)') == {'version': 'TQJJ'}
assert test_version_normalization('Test Title (Japan) (TQKJ)') == {'version': 'TQKJ'}
assert test_version_normalization('Test Title (Japan) (TQNJ)') == {'version': 'TQNJ'}
assert test_version_normalization(
    'Test Title (Europe) (En,Fr,De,Es,It,Nl) (VBTP) (NDSi Enhanced)'
) == {'version': 'VBTP'}
assert test_version_normalization(
    'Test Title (Europe) (En,Fr,De,Es,It,Nl) (VBTX) (NDSi Enhanced)'
) == {'version': 'VBTX'}
assert test_version_normalization('Test Title (Europe) (En,De) (VESP) (NDSi Enhanced)') == {
    'version': 'VESP'
}
assert test_version_normalization('Test Title (Europe) (En,Fr) (VESV) (NDSi Enhanced)') == {
    'version': 'VESV'
}
assert test_version_normalization('Test Title (Europe) (En,Fr) (VESX) (NDSi Enhanced)') == {
    'version': 'VESX'
}
assert test_version_normalization('Test Title (Europe) (En,Fr,De) (VJVP) (NDSi Enhanced)') == {
    'version': 'VJVP'
}
assert test_version_normalization('Test Title (Europe) (En,Fr,De) (VJVV) (NDSi Enhanced)') == {
    'version': 'VJVV'
}
assert test_version_normalization('Test Title (USA) (En,Fr) (VKUE) (NDSi Enhanced)') == {
    'version': 'VKUE'
}
assert test_version_normalization('Test Title (USA) (En,Fr) (VKUY) (NDSi Enhanced)') == {
    'version': 'VKUY'
}
assert test_version_normalization('Test Title (Europe) (En,De) (VLIP) (NDSi Enhanced)') == {
    'version': 'VLIP'
}
assert test_version_normalization('Test Title (Europe) (En,De) (VLIV) (NDSi Enhanced)') == {
    'version': 'VLIV'
}
assert test_version_normalization('Test Title (Europe) (De,Es,It) (VMZP) (NDSi Enhanced)') == {
    'version': 'VMZP'
}
assert test_version_normalization('Test Title (Europe) (De,Es,It) (VMZX) (NDSi Enhanced)') == {
    'version': 'VMZX'
}
assert test_version_normalization('Test Title (Europe) (En,Fr,Nl) (VMZY) (NDSi Enhanced)') == {
    'version': 'VMZY'
}
assert test_version_normalization('Test Title (Europe) (En,De) (VWVP) (NDSi Enhanced)') == {
    'version': 'VWVP'
}
assert test_version_normalization('Test Title (Europe) (En,De) (VWVV) (NDSi Enhanced)') == {
    'version': 'VWVV'
}
assert test_version_normalization('Test Title (Europe) (En,Fr,Es,It,Nl) (YWDZ)') == {
    'version': 'YWDZ'
}
assert test_version_normalization('1111 - Test Title (Japan) (YXAJ)') == {'version': 'YXAJ'}
assert test_version_normalization('9999 - Test Title (Japan) (YXBJ)') == {'version': 'YXBJ'}
assert test_version_normalization('Test Title (Japan) (YXGJ)') == {'version': 'YXGJ'}
assert test_version_normalization('Test Title (Japan) (YXPJ)') == {'version': 'YXPJ'}
assert test_version_normalization('Test Title (Japan) (YXQJ)') == {'version': 'YXQJ'}

# FM Towns/Pippin version
assert test_version_normalization('Test Title V1.1 L10 (Japan) (Rev A)') == {
    'version': '1.1L10',
    'revision': 'A',
}
assert test_version_normalization('Test Title V1.1 L10 (Japan) (Rev C)') == {
    'version': '1.1L10',
    'revision': 'C',
}
assert test_version_normalization(
    'Test Title Version 3.1 L11 Operating System (Japan) (Setup CD-ROM)'
) == {'version': '3.1L11'}

# Dreamcast version
assert test_version_normalization('Test Title V50 L10') == {'version': '50L10'}

# Standard version
assert test_version_normalization('Test Title (v1.1.0)') == {'version': '1.1.0'}
assert test_version_normalization('Test Title (v1.01.0)') == {'version': '1.01.0'}
assert test_version_normalization('Test Title (v1.0100.0)') == {'version': '1.0100.0'}
assert test_version_normalization('Doom (v1.666.1)') == {'version': '1.6.6.6.1'}

# Long version
assert test_version_normalization('Test Lovers - Test Test') == {}
assert test_version_normalization('REVERSAO') == {}
assert test_version_normalization('Test Title Ver.-FAKE TYPE.') == {}
assert test_version_normalization('Test Title Ver. - Test (Japan)') == {}
assert test_version_normalization('Test Tile - Version Or Test') == {}
assert (
    test_version_normalization(
        'Test Title (USA) (Sample) (Possibly a version given out to press at E3 or an E3 demo)'
    )
    == {}
)
assert test_version_normalization('Test Title - Ver. Test (Japan)') == {}
assert test_version_normalization('Test Title - Versione Testino (Italy)') == {}
assert test_version_normalization('Virtua Striker 3 Ver. 2002') == {}
assert test_version_normalization('Virtua Striker 4 Ver. 2006 (Japan)') == {}
assert test_version_normalization('Pokemon - Black Version 2') == {}
assert test_version_normalization('Pokemon - White Version 2') == {}
assert test_version_normalization('Panel de Pon - Event Version 2') == {}
assert test_version_normalization('Sutte Hakkun - BS Version 2') == {}
assert test_version_normalization('Wario no Mori - Event Version 2') == {}
assert test_version_normalization('Interactive Multi-Game Demo Disc Version 10 (USA)') == {
    'version': '10'
}
assert test_version_normalization('Test Title (Europe) (Unl) (Version 1.0E)') == {'version': '1.0E'}
assert test_version_normalization('Test Title (Europe) (Unl) (Version 1.14b)') == {
    'version': '1.14b'
}
assert test_version_normalization('Test Title Version 19 (USA)') == {'version': '19'}
assert test_version_normalization('Test Title Ver. A (USA) (En,Fr,Es)') == {'version': 'A'}
assert test_version_normalization('Test Title Ver. 1.31 (USA)') == {'version': '1.31'}
assert test_version_normalization('Test Title - Version 1.3 (Japan) (Unl)') == {'version': '1.3'}

# Famicom Disk System version
assert test_version_normalization('Test Title (Japan) (DV 10)') == {'version': '10'}

# HyperScan version
assert test_version_normalization('Test Title (USA) (USE2)') == {'version': 'USE2'}

# Revision
assert test_version_normalization('Test Title (USA) (Rev A)') == {'revision': 'A'}
assert test_version_normalization('Test Title (USA) (v1.1) (Rev B)') == {
    'version': '1.1',
    'revision': 'B',
}

# Preproduction/alternate
assert test_version_normalization('Test Title (USA) (Beta)') == {'beta': '0', 'preproduction': True}
assert test_version_normalization('Test Title (USA) (Alpha)') == {
    'alpha': '0',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Proto)') == {
    'proto': '0',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Prototype)') == {
    'proto': '0',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Alt)') == {'alt': '0'}
assert test_version_normalization('Test Title (USA) (Beta 2)') == {
    'beta': '2',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Alpha 3)') == {
    'alpha': '3',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Proto 9)') == {
    'proto': '9',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Prototype 3)') == {
    'proto': '3',
    'preproduction': True,
}
assert test_version_normalization('Test Title (USA) (Build 6)') == {'build': '6'}
assert test_version_normalization('Test Title (USA) (Alt 7)') == {'alt': '7'}

# Sega/Panasonic ring code
assert test_version_normalization('Test Title (USA) (RE)') == {'sega': '0'}
assert test_version_normalization('Test Title (USA) (Version 2.10) (RE2)') == {
    'version': '2.10',
    'sega': '2',
}
assert test_version_normalization('Test Title (Europe) (RE-1)') == {'sega': '1'}
assert test_version_normalization('Test Title (USA) (5R, 6R)') == {'sega': '6'}
assert test_version_normalization('Test Title (Japan) (Disc 1) (7M, 9M, 10M)') == {'sega': '10'}
assert test_version_normalization('Test Title (Japan) (Rev B) (39B)') == {
    'revision': 'B',
    'sega': '39',
}
assert test_version_normalization('Test Title (Europe) (En,Fr,Es,It) (4S)') == {'sega': '4'}
assert test_version_normalization('Test Title (Japan) (5A)') == {'sega': '5'}

# NEC mastering code
assert test_version_normalization('Test Title (Japan) (FAAT)') == {'nec': 'FAAT'}
assert test_version_normalization('Test Title (Japan) (FAAT, FACT)') == {'nec': 'FACT'}
assert test_version_normalization('Test Title (Japan) (FABT)') == {'nec': 'FABT'}
assert test_version_normalization('Test Title (Japan) (FADT)') == {'nec': 'FADT'}
assert test_version_normalization('Test Title (Japan) (FAFT)') == {'nec': 'FAFT'}
assert test_version_normalization('Test Title (Japan) (FABT, FACT, FAET, FAFT)') == {
    'nec': 'FAFT'
}
assert test_version_normalization('Test Title (Japan) (SAAS)') == {'nec': 'SAAS'}
assert test_version_normalization('Test Title (Japan) (SABS)') == {'nec': 'SABS'}
assert test_version_normalization('Test Title (Japan) (SACS)') == {'nec': 'SACS'}
assert test_version_normalization('Test Title (Japan) (SADS, SAES)') == {'nec': 'SAES'}

# PlayStation Firmware
assert test_version_normalization('Test Title (USA) (v2.00) (FW3.96)') == {
    'version': '2.00',
    'firmware': '3.96',
}

# PlayStation 1 & 2 ID
assert test_version_normalization('Test Title (Unknown) (LDTL-00001)') == {
    'playstation': 'LDTL-00001'
}
assert test_version_normalization('Test Title (Japan) (PAPX-00001)') == {
    'playstation': 'PAPX-00001'
}
assert test_version_normalization('Test Title (Europe) (PBPX-00001)') == {
    'playstation': 'PBPX-00001'
}
assert test_version_normalization('Test Title (Japan) (PCPX-00001)') == {
    'playstation': 'PCPX-00001'
}
assert test_version_normalization('Test Title (Japan) (PCPD-00001)') == {
    'playstation': 'PCPD-00001'
}
assert test_version_normalization('Test Title (Japan) (PDPX-00001)') == {
    'playstation': 'PDPX-00001'
}
assert test_version_normalization('Test Title (Europe) (PEPX-00001)') == {
    'playstation': 'PEPX-00001'
}
assert test_version_normalization('Test Title (Japan, Asia) (PSXC-00001)') == {
    'playstation': 'PSXC-00001'
}
assert test_version_normalization('Test Title (Japan) (PTPX-00001)') == {
    'playstation': 'PTPX-00001'
}
assert test_version_normalization('Test Title (USA) (PUPX-00001)') == {'playstation': 'PUPX-00001'}
assert test_version_normalization('Test Title (Asia) (SCAJ-00001)') == {'playstation': 'SCAJ-00001'}
assert test_version_normalization('Test Title (China) (SCCS-00001)') == {
    'playstation': 'SCCS-00001'
}
assert test_version_normalization('Test Title (Europe) (SCES-00001)') == {
    'playstation': 'SCES-00001'
}
assert test_version_normalization('Test Title (Europe, Australia) (SCED-00001)') == {
    'playstation': 'SCED-00001'
}
assert test_version_normalization('Test Title (Korea) (SCKA-00001)') == {
    'playstation': 'SCKA-00001'
}
assert test_version_normalization('Test Title (Japan) (Multi Tap (SCPH-00001) Doukonban)') == {
    'playstation': 'SCPH-00001'
}
assert test_version_normalization('Test Title (Japan) (SCPM-00001)') == {
    'playstation': 'SCPM-00001'
}
assert test_version_normalization('Test Title (Prerelease) (Japan) (Disc 2) (SCPN-00001)') == {
    'playstation': 'SCPN-00001',
    'preproduction': True,
}
assert test_version_normalization('Test Title (Asia) (SCPS-00001)') == {'playstation': 'SCPS-00001'}
assert test_version_normalization('Test Title (USA) (SCUS-00001)') == {'playstation': 'SCUS-00001'}
assert test_version_normalization('Test Title (Japan) (SCZS-00001)') == {
    'playstation': 'SCZS-00001'
}
assert test_version_normalization('Test Title (Japan) (SIPS-00001)') == {
    'playstation': 'SIPS-00001'
}
assert test_version_normalization('Test Title (Japan) (SLAJ-00001)') == {
    'playstation': 'SLAJ-00001'
}
assert test_version_normalization('Test Title (France) (SLED-00001)') == {
    'playstation': 'SLED-00001'
}
assert test_version_normalization('Test Title (Europe) (SLES-00001)') == {
    'playstation': 'SLES-00001'
}
assert test_version_normalization('Test Title (Korea) (SLKA-00001)') == {
    'playstation': 'SLKA-00001'
}
assert test_version_normalization('Test Title (Japan) (SLPM-00001)') == {
    'playstation': 'SLPM-00001'
}
assert test_version_normalization('Test Title (Japan) (SLPN-00001)') == {
    'playstation': 'SLPN-00001'
}  # SerialStation shows no titles for this prefix
assert test_version_normalization('Test Title (Japan) (SLPS-00001)') == {
    'playstation': 'SLPS-00001'
}
assert test_version_normalization('Test Title (Japan) (SLUS-00001)') == {
    'playstation': 'SLUS-00001'
}
assert test_version_normalization('Test Title (Japan) (SRPM-00001)') == {
    'playstation': 'SRPM-00001'
}
assert test_version_normalization('Test Title (Europe) (TCES-00001)') == {
    'playstation': 'TCES-00001'
}
assert test_version_normalization('Test Title (Europe) (TLES-00001)') == {
    'playstation': 'TLES-00001'
}

# PlayStation 3 ID
assert test_version_normalization('Test Title (USA) (BCAS-00001)') == {'playstation': 'BCAS-00001'}
assert test_version_normalization('Test Title (Japan) (BCAX-00001)') == {
    'playstation': 'BCAX-00001'
}
assert test_version_normalization('Test Title (Europe) (BCED-00001)') == {
    'playstation': 'BCED-00001'
}
assert test_version_normalization('Test Title (Europe) (BCES-00001)') == {
    'playstation': 'BCES-00001'
}
assert test_version_normalization('Test Title (Europe) (BCET-00001)') == {
    'playstation': 'BCET-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJB-00001)') == {
    'playstation': 'BCJB-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJS-00001)') == {
    'playstation': 'BCJS-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJD-00001)') == {
    'playstation': 'BCJD-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJS-00001)') == {
    'playstation': 'BCJS-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJV-00001)') == {
    'playstation': 'BCJV-00001'
}  # SerialStation shows no titles for this prefix
assert test_version_normalization('Test Title (Japan) (BCJX-00001)') == {
    'playstation': 'BCJX-00001'
}
assert test_version_normalization('Test Title (Japan) (BCJZ-00001)') == {
    'playstation': 'BCJZ-00001'
}  # SerialStation shows no titles for this prefix
assert test_version_normalization('Test Title (Korea) (BCKS-00001)') == {
    'playstation': 'BCKS-00001'
}
assert test_version_normalization('Test Title (USA) (BCUS-00001)') == {'playstation': 'BCUS-00001'}
assert test_version_normalization('Test Title (Japan) (BLAS-00001)') == {
    'playstation': 'BLAS-00001'
}
assert test_version_normalization('Test Title (Europe) (BLED-00001)') == {
    'playstation': 'BLED-00001'
}
assert test_version_normalization('Test Title (Europe) (BLES-00001)') == {
    'playstation': 'BLES-00001'
}
assert test_version_normalization('Test Title (Europe) (BLET-00001)') == {
    'playstation': 'BLET-00001'
}
assert test_version_normalization('Test Title (Japan) (BLJB-00001)') == {
    'playstation': 'BLJB-00001'
}
assert test_version_normalization('Test Title (Japan) (BLJM-00001)') == {
    'playstation': 'BLJM-00001'
}
assert test_version_normalization('Test Title (Japan) (BLJS-00001)') == {
    'playstation': 'BLJS-00001'
}
assert test_version_normalization('Test Title (Japan) (BLJX-00001)') == {
    'playstation': 'BLJX-00001'
}
assert test_version_normalization('Test Title (Korea) (BLKS-00001)') == {
    'playstation': 'BLKS-00001'
}
assert test_version_normalization('Test Title (USA) (BLUD-00001)') == {'playstation': 'BLUD-00001'}
assert test_version_normalization('Test Title (USA) (BLUS-00001)') == {'playstation': 'BLUS-00001'}
assert test_version_normalization('Test Title (USA) (MCAD-00001)') == {'playstation': 'MCAD-00001'}
assert test_version_normalization('Test Title (USA) (MRTC-00001)') == {'playstation': 'MRTC-00001'}
assert test_version_normalization('Test Title (Europe) (XCES-00001)') == {
    'playstation': 'XCES-00001'
}
assert test_version_normalization('Test Title (Japan) (XCJS-00001)') == {
    'playstation': 'XCJS-00001'
}
assert test_version_normalization('Test Title (USA) (XCUS-00001)') == {'playstation': 'XCUS-00001'}

# PlayStation 3 digital ID
assert test_version_normalization('Test Title (Europe) (NPEA-00001)') == {
    'playstation': 'NPEA-00001'
}
assert test_version_normalization('Test Title (Asia) (NPHZ-00001)') == {'playstation': 'NPHZ-00001'}
assert test_version_normalization('Test Title (World) (NPIB-00001)') == {
    'playstation': 'NPIB-00001'
}
assert test_version_normalization('Test Title (Japan) (NPJX-00001)') == {
    'playstation': 'NPJX-00001'
}
assert test_version_normalization('Test Title (Korea) (NPKL-00001)') == {
    'playstation': 'NPKL-00001'
}
assert test_version_normalization('Test Title (USA, Japan) (NPMF-00001)') == {
    'playstation': 'NPMF-00001'
}
assert test_version_normalization('Test Title (USA) (NPNT-00001)') == {'playstation': 'NPNT-00001'}
assert test_version_normalization('Test Title (USA, Europe) (NPOP-00001)') == {
    'playstation': 'NPOP-00001'
}
assert test_version_normalization('Test Title (Japan) (NPPD-00001)') == {
    'playstation': 'NPPD-00001'
}
assert test_version_normalization('Test Title (Asia) (NPQQ-00001)') == {'playstation': 'NPQQ-00001'}
assert test_version_normalization('Test Title (USA) (NPUA-00001)') == {'playstation': 'NPUA-00001'}
assert test_version_normalization('Test Title (USA) (NPVA-00001)') == {'playstation': 'NPVA-00001'}
assert test_version_normalization('Test Title (Hong Kong) (NPWA-00001)') == {
    'playstation': 'NPWA-00001'
}
assert test_version_normalization('Test Title (Unknown) (NPXA-00001)') == {
    'playstation': 'NPXA-00001'
}

# PlayStation 4 ID
assert test_version_normalization('Test Title (USA) (CUSA-00001)') == {'playstation': 'CUSA-00001'}
assert test_version_normalization('Test Title (Asia) (PCAS-00001)') == {'playstation': 'PCAS-00001'}
assert test_version_normalization('Test Title (China) (PCCS-00001)') == {
    'playstation': 'PCCS-00001'
}
assert test_version_normalization('Test Title (Japan) (PCJB-00001)') == {
    'playstation': 'PCJB-00001'
}
assert test_version_normalization('Test Title (Japan) (PCJS-00001)') == {
    'playstation': 'PCJS-00001'
}
assert test_version_normalization('Test Title (Japan) (PCJZ-00001)') == {
    'playstation': 'PCJZ-00001'
}
assert test_version_normalization('Test Title (Korea) (PCKS-00001)') == {
    'playstation': 'PCKS-00001'
}
assert test_version_normalization('Test Title (Asia) (PLAS-00001)') == {'playstation': 'PLAS-00001'}
assert test_version_normalization('Test Title (China) (PLCS-00001)') == {
    'playstation': 'PLCS-00001'
}
assert test_version_normalization('Test Title (Japan) (PLJM-00001)') == {
    'playstation': 'PLJM-00001'
}
assert test_version_normalization('Test Title (Japan) (PLJS-00001)') == {
    'playstation': 'PLJS-00001'
}
assert test_version_normalization('Test Title (Korea) (PLKS-00001)') == {
    'playstation': 'PLKS-00001'
}

# PlayStation 5 ID
assert test_version_normalization('Test Title (USA) (ECAS-00001)') == {'playstation': 'ECAS-00001'}
assert test_version_normalization('Test Title (Japan) (ECJS-00001)') == {
    'playstation': 'ECJS-00001'
}
assert test_version_normalization('Test Title (Asia) (ELAS-00001)') == {'playstation': 'ELAS-00001'}
assert test_version_normalization('Test Title (Japan) (ELJM-00001)') == {
    'playstation': 'ELJM-00001'
}
assert test_version_normalization('Test Title (Japan) (ELJS-00001)') == {
    'playstation': 'ELJS-00001'
}
assert test_version_normalization('Test Title (Any country) (PPSA-00001)') == {
    'playstation': 'PPSA-00001'
}
assert test_version_normalization('Test Title (Any country) (PPSA-00001)') == {
    'playstation': 'PPSA-00001'
}

# PlayStation Portable ID
assert test_version_normalization('Test Title (Asia) (UCAM-00001)') == {'playstation': 'UCAM-00001'}
assert test_version_normalization('Test Title (Asia) (UCAS-00001)') == {'playstation': 'UCAS-00001'}
assert test_version_normalization('Test Title (Europe) (UCED-00001)') == {
    'playstation': 'UCED-00001'
}
assert test_version_normalization('Test Title (Europe) (UCES-00001)') == {
    'playstation': 'UCES-00001'
}
assert test_version_normalization('Test Title (Europe) (UCET-00001)') == {
    'playstation': 'UCET-00001'
}
assert test_version_normalization('Test Title (Japan) (UCJB-00001)') == {
    'playstation': 'UCJB-00001'
}
assert test_version_normalization('Test Title (Japan) (UCJP-00001)') == {
    'playstation': 'UCJP-00001'
}
assert test_version_normalization('Test Title (Japan) (UCJS-00001)') == {
    'playstation': 'UCJS-00001'
}
assert test_version_normalization('Test Title (Japan) (UCJX-00001)') == {
    'playstation': 'UCJX-00001'
}
assert test_version_normalization('Test Title (Korea) (UCKM-00001)') == {
    'playstation': 'UCKM-00001'
}
assert test_version_normalization('Test Title (Korea) (UCKS-00001)') == {
    'playstation': 'UCKS-00001'
}
assert test_version_normalization('Test Title (USA, Canada) (UCUS-00001)') == {
    'playstation': 'UCUS-00001'
}
assert test_version_normalization('Test Title (Asia) (ULAS-00001)') == {'playstation': 'ULAS-00001'}
assert test_version_normalization('Test Title (Europe) (ULED-00001)') == {
    'playstation': 'ULED-00001'
}
assert test_version_normalization('Test Title (Europe) (ULES-00001)') == {
    'playstation': 'ULES-00001'
}
assert test_version_normalization('Test Title (Europe) (ULET-00001)') == {
    'playstation': 'ULET-00001'
}
assert test_version_normalization('Test Title (Japan, Asia) (ULJM-00001)') == {
    'playstation': 'ULJM-00001'
}
assert test_version_normalization('Test Title (Japan, Asia) (ULJP-00001)') == {
    'playstation': 'ULJP-00001'
}
assert test_version_normalization('Test Title (Japan, Asia) (ULJS-00001)') == {
    'playstation': 'ULJS-00001'
}
assert test_version_normalization('Test Title (Korea) (ULKS-00001)') == {
    'playstation': 'ULKS-00001'
}
assert test_version_normalization('Test Title (USA) (ULUS-00001)') == {'playstation': 'ULUS-00001'}
assert test_version_normalization('Test Title (USA) (ULUX-00001)') == {'playstation': 'ULUX-00001'}
assert test_version_normalization('Test Title (Japan) (UMDT-00001)') == {
    'playstation': 'UMDT-00001'
}
assert test_version_normalization('Test Title (USA) (UTST-00001)') == {'playstation': 'UTST-00001'}

# PlayStation Vita ID
assert test_version_normalization('Test Title (USA) (PCSA-00001)') == {'playstation': 'PCSA-00001'}
assert test_version_normalization('Test Title (USA, Europe) (PCSB-00001)') == {
    'playstation': 'PCSB-00001'
}
assert test_version_normalization('Test Title (Japan) (PCSC-00001)') == {
    'playstation': 'PCSC-00001'
}
assert test_version_normalization('Test Title (Japan) (PCSC-00001)') == {
    'playstation': 'PCSC-00001'
}
assert test_version_normalization('Test Title (Asia) (PCSD-00001)') == {'playstation': 'PCSD-00001'}
assert test_version_normalization('Test Title (USA) (PCSE-00001)') == {'playstation': 'PCSE-00001'}
assert test_version_normalization('Test Title (Europe, Australia) (PCSF-00001)') == {
    'playstation': 'PCSF-00001'
}
assert test_version_normalization('Test Title (Japan) (PCSG-00001)') == {
    'playstation': 'PCSG-00001'
}  # Japan digital
assert test_version_normalization('Test Title (Asia, Korea) (PCSH-00001)') == {
    'playstation': 'PCSH-00001'
}  # Asia or Korea digital
assert test_version_normalization('Test Title (World) (PCSI-00001)') == {
    'playstation': 'PCSI-00001'
}  # World digital
assert test_version_normalization('Test Title (Asia) (VCAS-00001)') == {'playstation': 'VCAS-00001'}
assert test_version_normalization('Test Title (China) (VCCS-00001)') == {
    'playstation': 'VCCS-00001'
}
assert test_version_normalization('Test Title (Japan) (VCJS-00001)') == {
    'playstation': 'VCJS-00001'
}
assert test_version_normalization('Test Title (Japan) (VCJX-00001)') == {
    'playstation': 'VCJX-00001'
}
assert test_version_normalization('Test Title (Korea) (VCKS-00001)') == {
    'playstation': 'VCKS-00001'
}
assert test_version_normalization('Test Title (Asia) (VLAS-00001)') == {'playstation': 'VLAS-00001'}
assert test_version_normalization('Test Title (Japan) (VLJM-00001)') == {
    'playstation': 'VLJM-00001'
}
assert test_version_normalization('Test Title (Japan) (VLJS-00001)') == {
    'playstation': 'VLJS-00001'
}
assert test_version_normalization('Test Title (Korea) (VLKS-00001)') == {
    'playstation': 'VLKS-00001'
}

eprint(f'{Font.success}\nPASSED: Version normalization{Font.end}\n')
