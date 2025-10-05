from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from functools import reduce
from typing import TYPE_CHECKING, Any

from strictyaml import YAML, Map, MapPattern, Seq, Str  # type: ignore

import modules.constants as const

if TYPE_CHECKING:
    from modules.config.config import Config
    from modules.dat.process_dat import Dat

from modules.clone_lists.clone_list import CloneList
from modules.config.read_write_config import read_config
from modules.utils import Font, SmartFormatter, download, eprint, minimum_version, regex_test


class UserInput:
    def __init__(
        self,
        input_file_name: str = '',
        update: bool = False,
        no_1g1r: bool = False,
        filter_languages: bool = False,
        oldest: bool = False,
        retroachievements: bool = False,
        local_names: bool = False,
        region_bias: bool = False,
        legacy: bool = False,
        demote_unl: bool = False,
        modern: bool = False,
        compilations: str = '',
        no_applications: bool = False,
        no_audio: bool = False,
        no_bad_dumps: bool = False,
        no_bios: bool = False,
        no_coverdiscs: bool = False,
        no_demos: bool = False,
        no_add_ons: bool = False,
        no_educational: bool = False,
        no_aftermarket: bool = False,
        no_games: bool = False,
        no_mia: bool = False,
        no_manuals: bool = False,
        no_multimedia: bool = False,
        no_bonus_discs: bool = False,
        no_pirate: bool = False,
        no_preproduction: bool = False,
        no_promotional: bool = False,
        no_unlicensed: bool = False,
        no_video: bool = False,
        clone_list: str = '',
        user_config: str = '',
        metadata: str = '',
        mia: str = '',
        ra: str = '',
        no_overrides: bool = False,
        list_names: bool = False,
        report: bool = False,
        machine_not_game: bool = False,
        label_mia: bool = False,
        label_retro: bool = False,
        original_header: bool = False,
        output_folder_name: str = '',
        user_output_folder: str = '',
        output_region_split: bool = False,
        output_remove_dat: bool = False,
        replace: bool = False,
        reprocess_dat: bool = False,
        verbose: bool = False,
        warningpause: bool = False,
        single_cpu: bool = False,
        trace: str = '',
        excludes: str = '',
        dev_mode: bool = False,
        user_options: str = '',
        user_clone_list_location: str = '',
        user_clone_list_metadata_download_location: str = '',
        user_metadata_location: str = '',
        user_mia_location: str = '',
        user_ra_location: str = '',
        test: bool = False,
    ) -> None:
        """
        Stores user input values, including what types of titles to exclude.

        Args:
            input_file_name (str, optional): The path to the input DAT file. Defaults to
                `''`.

            update (bool, optional): Calls the clone list update function. Defaults to
                `False`.

            no_1g1r (bool, optional): Disables 1G1R processing. Defaults to `False`.

            filter_languages (bool, optional): Filters by languages, removing any title
                that doesn't support the languages in the supplied list. Defaults to
                `False`.

            local_names (bool, optional): Uses local names for titles if available. For
                example, `ダイナマイト　ヘッディー (Japan): instead of `Dynamite Headdy
                (Japan)`.

            oldest (bool, optional): Prefers oldest production versions of titles instead
                of newest.

            retroachievements (bool, optional): Prefers titles with RetroAchievements.

            region_bias (bool, optional): Prefers regions over languages. Defaults to
                `False`.

            legacy (bool, optional): Outputs the DAT file in legacy mode, complete with
                parent/clone tags. Only useful for clone list maintainers who want to
                track changes between DAT releases. Defaults to `False`.

            demote_unl (bool, optional): Demotes unlicensed, aftermarket, and pirate
                titles if a production version of a title is found in another region.
                Defaults to `False`.

            modern (bool, optional): Whether to choose a version of a title ripped from a
                modern rerelease (e.g. Steam, Virtual Console) over the original title.
                Defaults to `False`.

            compilations (str, optional): What compilations mode to set Retool to.
                Defaults to ''.

            no_applications (bool, optional): Excludes applications. Defaults to `False`.

            no_audio (bool, optional): Excludes audio. Defaults to `False`.

            no_bad_dumps (bool, optional): Excludes bad dumps. Defaults to `False`.

            no_bios (bool, optional): Excludes BIOS and other chip-based titles. Defaults
                to `False`.

            no_coverdiscs (bool, optional): Excludes coverdiscs. Defaults to `False`.

            no_demos (bool, optional): Excludes demos. Defaults to `False`.

            no_add_ons (bool, optional): Excludes add-ons. Defaults to `False`.

            no_educational (bool, optional): Excludes educational titles. Defaults to
                `False`.

            no_aftermarket (bool, optional): Excludes aftermarket titles. Defaults to
                `False`.

            no_games (bool, optional): Excludes games. Defaults to `False`.

            no_mia (bool, optional): Excludes MIA titles. Defaults to `False`.

            no_manuals (bool, optional): Excludes manuals. Defaults to `False`.

            no_multimedia (bool, optional): Excludes multimedia titles. Defaults to
                `False`.

            no_bonus_discs (bool, optional): Excludes bonus discs. Defaults to `False`.

            no_pirate (bool, optional): Excludes pirate titles. Defaults to `False`.

            no_preproduction (bool, optional): Excludes preproduction titles. Defaults to
                `False`.

            no_promotional (bool, optional): Excludes promotional titles. Defaults to
                `False`.

            no_unlicensed (bool, optional): Excludes unlicensed, aftermarket, and pirate
                titles. Defaults to `False`.

            no_video (bool, optional): Excludes video titles. Defaults to `False`.

            clone_list (str, optional): The path to a clone list to load, overriding the
                default selection. Defaults to `''`.

            user_config (str, optional): The path to a user config file to load,
                overriding the default selection. Defaults to `''`.

            metadata (str, optional): The path to a metadata file to load, overriding the
                default selection. Defaults to `''`.

            mia (str, optional): The path to an MIA file to load, overriding the default
                selection. Defaults to `''`.

            ra (str, optional): The path to a RetroAchievements file to load, overriding
                the default selection. Defaults to `''`.

            no_overrides (bool, optional): Disables global and system overrides. Defaults
                to `False`.

            list_names (bool, optional): Additionally outputs a file that contains just
                the names of the 1G1R titles found after processing. Defaults to `False`.

            report (bool, optional): Additionally outputs a file that shows what titles
                have been kept and removed. Defaults to `False`.

            machine_not_game (bool, optional): Uses the MAME standard of <machine> for
                title nodes in the output DAT file instead of <game>. Defaults to `False`.

            label_mia (bool, optional): Adds MIA attributes to ROMs or titles. Defaults to
                `False`.

            label_retro (bool, optional): Adds RetroAchievements attributes to titles.
                Defaults to `False`.

            original_header (bool, optional): Uses the header from the input DAT in the
                output DAT. Useful to update original No-Intro and Redump DATs already
                loaded in CLRMAMEPro. Defaults to `False`.

            output_folder_name (str, optional): Sets the folder DATs are written to.
                Defaults to `''`.

            user_output_folder (str, optional): Whether the output folder is user
                provided. Defaults to ''.

            output_region_split (bool, optional): Produces multiple DAT files split by
                region, instead of just a single DAT file. Defaults to `False`.

            output_remove_dat (bool, optional): Additionally outputs a DAT that contains
                all the titles Retool has removed as part of its process. Defaults to
                `False`.

            replace (bool, optional): Delete the input DAT file and create Retool files in
                the same folder. Defaults to `False`.

            reprocess_dat (bool, optional): Let DAT files be processed even if Retool has
                already processed them. Defaults to `False`.

            verbose (bool, optional): Displays warnings when clone list errors occur.
                Defaults to `False`.

            warningpause (bool, optional): Pauses Retool when a clone list error is
                reported. Defaults to `False`.

            single_cpu (bool, optional): Uses a single CPU to do the processing, instead
                of using all available processors. Defaults to `False`.

            trace (str, optional): Traces a title through Retool's process, using the
                supplied string as regex. Defaults to `''`.

            excludes (str, optional): A string representation of all the exclusion options
                as single letters. Used in naming the output DAT file as a way to
                determine what options generated the file. Defaults to `''`.

            dev_mode (bool, optional): Enables dev mode. Displays some extra messages to
                help troubleshoot code issues. Defaults to `False`.

            user_options (str, optional): If a user has enabled single letter user options
                (-delryz), adds them to the output filename. Defaults to `''`.

            user_clone_list_location (str, optional): A user-defined folder for where
                clone lists live. Only settable in the GUI. Defaults to `''`.

            user_clone_list_metadata_download_location (str, optional): A user-defined URL
                for where to download clone list and metadata updates from. Only settable
                in the GUI. Defaults to `''`.

            user_metadata_location (str, optional): A user-defined folder for where
                metadata files live. Only settable in the GUI. Defaults to `''`.

            user_mia_location (str, optional): A user-defined folder for where MIA files
                live. Only settable in the GUI. Defaults to `''`.

            user_ra_location (str, optional): A user-defined folder for where
                RetroAchievements files live. Only settable in the GUI. Defaults to `''`.

            test (bool, optional): Runs tests helpful to Retool's development. Defaults to
                `False`.
        """
        # Positional
        self.input_file_name: str = input_file_name

        # Optional
        self.no_1g1r: bool = no_1g1r
        self.legacy: bool = legacy
        self.filter_languages: bool = filter_languages
        self.local_names: bool = local_names
        self.oldest: bool = oldest
        self.retroachievements: bool = retroachievements
        self.no_mia: bool = no_mia
        self.region_bias: bool = region_bias
        self.demote_unl: bool = demote_unl
        self.modern: bool = modern
        self.compilations: str = compilations

        # Excludes
        self.no_add_ons: bool = no_add_ons
        self.no_aftermarket: bool = no_aftermarket
        self.no_applications: bool = no_applications
        self.no_audio: bool = no_audio
        self.no_bad_dumps: bool = no_bad_dumps
        self.no_bios: bool = no_bios
        self.no_bonus_discs: bool = no_bonus_discs
        self.no_coverdiscs: bool = no_coverdiscs
        self.no_demos: bool = no_demos
        self.no_educational: bool = no_educational
        self.no_games: bool = no_games
        self.no_manuals: bool = no_manuals
        self.no_multimedia: bool = no_multimedia
        self.no_pirate: bool = no_pirate
        self.no_preproduction: bool = no_preproduction
        self.no_promotional: bool = no_promotional
        self.no_unlicensed: bool = no_unlicensed
        self.no_video: bool = no_video

        # Inputs
        self.clone_list: str = clone_list
        self.user_config: str = user_config
        self.metadata: str = metadata
        self.mia: str = mia
        self.ra: str = ra
        self.user_clone_list_location: str = user_clone_list_location
        self.user_clone_list_metadata_download_location: str = (
            user_clone_list_metadata_download_location
        )
        self.user_metadata_location: str = user_metadata_location
        self.user_mia_location: str = user_mia_location
        self.user_ra_location: str = user_ra_location
        self.no_overrides: bool = no_overrides

        # Outputs
        self.list_names: bool = list_names
        self.report: bool = report
        self.machine_not_game: bool = machine_not_game
        self.label_mia: bool = label_mia
        self.label_retro: bool = label_retro

        # ROMs need to be labeled MIA for them to be removed
        if self.no_mia:
            self.label_mia = True

        # Titles need to be labeled for RetroAchievements for them to be selected
        if self.retroachievements:
            self.label_retro = True

        self.original_header: bool = original_header
        self.output_folder_name: str = output_folder_name
        self.user_output_folder: bool = bool(user_output_folder)
        self.output_region_split: bool = output_region_split
        self.output_remove_dat: bool = output_remove_dat
        self.replace: bool = replace
        self.reprocess_dat: bool = reprocess_dat

        # Debug
        self.verbose: bool = verbose
        self.warningpause: bool = warningpause
        self.single_cpu: bool = single_cpu
        self.trace: str = trace

        # Internal
        self.user_options: str = user_options
        self.excludes: str = excludes
        self.dev_mode: bool = dev_mode
        self.test: bool = test
        self.update: bool = update

        # Check for valid regex in the trace
        if self.trace:
            trace_test: list[str] = regex_test([self.trace], '', 'trace')

            if not trace_test:
                self.trace = ''
            else:
                # Enable single CPU, as the regex is valid and multiprocessor doesn't
                # like the output provided by the trace
                self.single_cpu = True


def check_input() -> UserInput:
    """Checks user input values, and creates a UserInput object for Retool to use."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        usage='\n\n%(prog)s <input DAT/folder> <options>\n\nOR to download updated clone lists:\n\n%(prog)s --update',
        allow_abbrev=False,
        formatter_class=SmartFormatter,
        add_help=False,
    )

    # Help text order is determined by the group order here
    exclusions: Any = parser.add_argument_group('exclusions')
    outputs: Any = parser.add_argument_group('outputs')
    debug: Any = parser.add_argument_group('debug')
    system: Any = parser.add_argument_group('system')

    parser.add_argument(
        'Input',
        metavar='<input DAT/folder>',
        type=str,
        help='R|The path to the DAT file, or folder of DAT files you\nwant to process.\n',
        nargs='?',
    )

    parser.add_argument(
        '-h', '--help', '-?', action='help', default=argparse.SUPPRESS, help=argparse.SUPPRESS
    )

    parser.add_argument(
        '-c',
        action='store_true',
        help='R|Prefer titles with RetroAchievements.\n\n',
    )

    parser.add_argument(
        '-d',
        action='store_true',
        help='R|Disable 1G1R filtering. Clone lists are ignored, and each'
        '\ntitle is treated as unique. User settings and excludes are'
        '\nstill respected. Useful if you want to keep everything'
        '\nfrom a specific set of regions and/or languages. Not'
        '\ncompatible with -x.'
        '\n\n',
    )

    parser.add_argument(
        '-l',
        action='store_true',
        help=f'R|Filter by languages using a list. If a title doesn\'t'
        '\nsupport any of the languages on the list, it\'s removed'
        f'\n(see {Font.b}config/user-config.yaml{Font.be}).'
        '\n\n',
    )

    parser.add_argument(
        '-n',
        action='store_true',
        help=f'R|Use local names for titles if available. For example,'
        '\nシャイニング●フォースⅡ 『古の封印』 instead of'
        '\nShining Force II - Inishie no Fuuin'
        f'\n(see {Font.b}config/user-config.yaml{Font.be}).'
        '\n\n',
    )

    parser.add_argument(
        '-o',
        action='store_true',
        help='R|Prefer oldest production versions instead of newest.'
        '\nUseful for speedrunners and those concerned about censorship,'
        '\nwho often want unpatched versions of games.'
        '\n\n',
    )

    parser.add_argument(
        '-r',
        action='store_true',
        help='R|Prefer regions over languages. By default, if a title'
        '\nfrom a higher priority region doesn\'t support your'
        '\npreferred languages but a lower priority region does,'
        '\nRetool selects the latter. This option disables this'
        '\nbehavior, forcing strict adherence to region priority'
        '\nregardless of language support. This option also'
        '\noverrides similar behavior in superset selection, which'
        '\nmeans you might get a title that was released in your'
        '\npreferred region that has less content, instead of one'
        '\nthat was released in another region that contains more'
        '\ncontent and supports your preferred languages.'
        '\n\n',
    )

    parser.add_argument(
        '-y',
        action='store_true',
        help='R|Prefer licensed versions over unlicensed, aftermarket,'
        '\nor pirate titles. This might select titles with lower'
        '\npriority regions or languages, or with less features.'
        '\n\n',
    )

    parser.add_argument(
        '-z',
        action='store_true',
        help='R|Prefer titles ripped from modern rereleases over original'
        '\nsystem releases, such as those found in Virtual Console'
        '\n(ripped titles might not work in emulators).'
        '\n\n',
    )

    parser.add_argument(
        '--compilations',
        action='extend',
        metavar='',
        help='R|How compilations should be handled. By default, Retool chooses'
        '\nindividual titles most of the time. It only chooses compilations'
        '\nwhen they have a higher region, language, or clone list priority,'
        '\nor contain unique titles. When choosing a compilation for unique'
        '\ntitles, if other titles in the compilation have individual'
        '\nequivalents, the individual titles are also included, leading to'
        '\nsome title duplication.'
        '\n'
        '\nTo change this behavior, use this flag and add one of the'
        '\nfollowing single letters afterwards to select a mode:'
        '\n\ni\tAlways prefer individual titles. Choose individual titles'
        '\n \tregardless of region, language, and clone list priorities,'
        '\n \tand discard compilations unless they contain unique games.'
        '\n \tYou\'re likely to prefer this mode if you use ROM hacks or'
        '\n \tRetroAchievements. When choosing a compilation for unique'
        '\n \ttitles, if other titles in the compilation have individual'
        '\n \tequivalents, the individual titles are also included, leading'
        '\n \tto some title duplication.'
        '\n\nk\tKeep individual titles and compilations. Ignores the'
        '\n \trelationship between individual titles and compilations, meaning'
        '\n \tindividual titles are only compared against other individual'
        '\n \ttitles, and compilations against other compilations. This option'
        '\n \thas the most title duplication.'
        f'\n\no\t{Font.b}(Beta){Font.be} Optimize for the least possible title duplication. Not'
        '\n \trecommended. While this mode can save disk space, it can be hard'
        '\n \tto tell what compilations contain based on their filename. This'
        '\n \tmode might not choose the optimal solution when supersets or'
        '\n \tclone list priorities are involved.'
        '\n\n',
        nargs=1,
    )

    parser.add_argument(
        '--nooverrides', action='store_true', help='R|Don\'t load global and system overrides.\n'
    )

    parser.add_argument('-q', action='store_true', help=argparse.SUPPRESS)

    parser.add_argument('--test', action='store_true', help=argparse.SUPPRESS)

    outputs.add_argument(
        '--labelmia',
        action='store_true',
        help='R|Mark files as MIA with an mia="yes" attribute. Don\'t use this if you\'re '
        '\na DATVault subscriber.'
        '\n\n',
    )

    outputs.add_argument(
        '--labelretro',
        action='store_true',
        help='R|Mark titles with a retroachievements="yes" attribute.\n\n',
    )

    outputs.add_argument(
        '--listnames',
        action='store_true',
        help='R|Also output a TXT file of just the kept title names. See'
        f'\n{Font.b}config/user-config.yaml{Font.be} to add a prefix and/or suffix'
        '\nto each line.'
        '\n\n',
    )

    outputs.add_argument(
        '--machine',
        action='store_true',
        help='R|Export each title node to the output DAT file using the MAME'
        '\nstandard of <machine> instead of <game>.'
        '\n\n',
    )

    outputs.add_argument(
        '--originalheader',
        action='store_true',
        help='R|Use the original input DAT headers in output DAT files.'
        '\nUseful if you want to load Retool DATs as an update'
        '\nto original Redump and No-Intro DATs already in CLRMAMEPro.'
        '\n\n',
    )

    outputs.add_argument(
        '--output',
        metavar='<folder>',
        type=str,
        help='R|Set an output folder where the new 1G1R DAT/s will be\ncreated.'
        '\n\nNot compatible with --replace.'
        '\n\n',
    )

    outputs.add_argument(
        '--regionsplit',
        action='store_true',
        help='R|Split the result into multiple DATs based on region. Use '
        '\nwith -d to only split by region with no 1G1R processing.'
        '\n\nNot compatible with --legacy.'
        '\n\n',
    )

    outputs.add_argument(
        '--removesdat',
        action='store_true',
        help='R|Also output DAT files containing titles that were'
        '\nremoved from 1G1R DAT files.'
        '\n\n',
    )

    outputs.add_argument(
        '--replace',
        action='store_true',
        help='R|Replace input DAT files with Retool versions. Only use this if'
        '\nyou can recover the original DAT files from elsewhere. Useful'
        '\nfor RomVault or DatVault users operating directly on their'
        '\nDatRoot files.'
        '\n\nNot compatible with --output.'
        '\n\n',
    )

    outputs.add_argument(
        '--report',
        action='store_true',
        help='R|Also output a report of the titles that have been kept,'
        '\nremoved, and set as clones.'
        '\n\n',
    )

    outputs.add_argument(
        '--reprocess',
        action='store_true',
        help='R|Let DAT files be processed even if Retool has already\nprocessed them.\n',
    )

    debug.add_argument(
        '--config',
        metavar='<file>',
        type=str,
        help='R|Set a custom user config file to use instead of the\ndefault.\n\n',
    )

    debug.add_argument(
        '--clonelist',
        metavar='<file>',
        type=str,
        help='R|Set a custom clone list to use instead of the default.'
        '\nUseful if you want to use your own, or if Redump or'
        '\nNo-Intro renames their DAT, and the clone list isn\'t'
        '\nautomatically detected anymore. Often used together with'
        '\n--metadata, --mia, and --ra.'
        '\n\n',
    )

    debug.add_argument(
        '--legacy',
        action='store_true',
        help='R|Output DAT files in legacy parent/clone format.'
        '\n\nNot compatible with -d.'
        '\n\n',
    )

    debug.add_argument(
        '--metadata',
        metavar='<file>',
        type=str,
        help='R|Set a custom metadata file to use instead of the default.'
        '\nUseful if you want to use your own, or if Redump or'
        '\nNo-Intro renames their DAT, and the metadata file isn\'t'
        '\nautomatically detected anymore. Often used together with'
        '\n--clonelist, --mia, and --ra.'
        '\n\n',
    )

    debug.add_argument(
        '--mia',
        metavar='<file>',
        type=str,
        help='R|Set a custom MIA file to use instead of the default.'
        '\nUseful if you want to use your own, or if Redump or'
        '\nNo-Intro renames their DAT, and the MIA file isn\'t'
        '\nautomatically detected anymore. Often used together with'
        '\n--clonelist, --metadata, and --ra.'
        '\n\n',
    )

    debug.add_argument(
        '--ra',
        metavar='<file>',
        type=str,
        help='R|Set a custom RetroAchievements file to use instead of the'
        '\ndefault. Useful if you want to use your own, or if Redump or'
        '\nNo-Intro renames their DAT, and the RetroAchievements file'
        '\n isn\'t automatically detected anymore. Often used together'
        '\nwith --clonelist, --metadata, and --mia.'
        '\n\n',
    )

    debug.add_argument(
        '--singlecpu', action='store_true', help='R|Disable multiprocessor usage.\n\n'
    )

    debug.add_argument(
        '--trace',
        action='extend',
        metavar='',
        help='R|Trace a title through the Retool process for debugging.'
        '\nTo function properly, this disables using multiple'
        '\nprocessors during parent selection.'
        '\n\nUsage: --trace "regex of titles to trace"'
        '\n\n',
        nargs='+',
    )

    debug.add_argument(
        '--warnings',
        action='store_true',
        help='R|Report clone list warnings during processing.\n\n',
    )

    debug.add_argument(
        '--warningpause',
        action='store_true',
        help='R|Pause when a clone list warning is found. Useful when\nbatch processing DATS.'
        '\n\n',
    )

    exclusions.add_argument(
        '--exclude',
        action='extend',
        metavar='',
        help='R|Add the following single letter filters after the\n'
        'exclude option to exclude different title types:\n'
        '\na\tApplications'
        '\nA\tAudio (might include game soundtracks)'
        '\nb\tBad dumps'
        '\nB\tBIOS and other chips'
        '\nc\tCoverdiscs (discs on the front of '
        'magazines)'
        '\nd\tDemos, kiosks, and samples'
        '\nD\tAdd-ons (expansion packs, additional material)'
        '\ne\tEducational titles'
        '\nf\tAftermarket titles'
        '\ng\tGames'
        '\nk\tTitles with MIA ROMs'
        '\nm\tManuals'
        '\nM\tMultimedia titles (might include games)'
        '\no\tBonus discs'
        '\np\tPirate titles'
        '\nP\tPreproduction titles (alphas, betas, prototypes)'
        '\nr\tPromotional titles'
        '\nu\tUnlicensed (unl) titles'
        '\nv\tVideo'
        '\n',
        nargs='+',
    )

    system.add_argument('--update', action='store_true', help=argparse.SUPPRESS)

    if len(sys.argv) == 1:
        sys.exit(1)

    args: argparse.Namespace = parser.parse_args()

    # Make sure incompatible flags aren't used, and handle other edge case situations
    if args.legacy and args.d:
        eprint('• -d and --legacy modes can\'t be used together. Exiting...', level='warning')
        sys.exit(1)

    if args.legacy and args.regionsplit:
        eprint(
            '• --regionsplit and --legacy modes can\'t be used together. Exiting...',
            level='warning',
        )
        sys.exit(1)

    if args.replace and args.output:
        eprint('• --replace and --output can\'t be used together. Exiting...', level='warning')
        sys.exit(1)

    if not args.update and args.Input is None:
        eprint(
            '• Unless you\'re updating clone lists, you must specify an input DAT or folder.',
            level='warning',
        )
        eprint(
            f'\nUsage: {pathlib.Path(sys.argv[0]).name} <input DAT/folder> <options>'
            f'\n\nType {Font.b}{pathlib.Path(sys.argv[0]).name} -h{Font.be} for all '
            'options\n',
            wrap=False,
        )
        sys.exit(1)

    # Set warnings and legacy to always be true if in dev environment
    dev_mode: bool = False

    if pathlib.Path('.dev').is_file() and not args.q:
        dev_mode = True
        setattr(args, 'legacy', True)
        if not args.test:
            setattr(args, 'warnings', True)
            setattr(args, 'warningpause', True)
            eprint(f'• {Font.b}Operating in dev mode{Font.be}', level='warning')
        else:
            eprint(f'• {Font.b}Operating in test mode{Font.be}', level='warning')
            eprint(f'• {Font.b}Running Python version: {sys.version}{Font.be}', level='warning')
        eprint('')

    # Compensate for trailing backslash in Windows
    if args.Input is not None:
        if sys.platform.startswith('win') and '"' in args.Input:
            args.Input = re.sub('".*', '', args.Input)
    else:
        args.Input = ''

    # Validate the output folder the user specified
    if args.output is not None:
        if pathlib.Path(args.output).is_file():
            eprint(
                f'Can\'t output to {Font.b}"{args.output}"{Font.be}, as it\'s a file, '
                'not a folder.\n',
                indent=0,
                level='error',
            )
            sys.exit(1)
        elif not pathlib.Path(args.output).exists():
            eprint(f'• Creating folder "{Font.b}{args.output}{Font.be}"')
            pathlib.Path(args.output).mkdir(parents=True, exist_ok=True)
    else:
        args.output = ''

    # Validate that user specified files exist
    def validate_user_file(user_file_path: str | None, user_file_type: str) -> str:
        """
        Check that a file path provided by the user exists, otherwise ignore it.

        Args:
            user_file_path (str | None): The path to the user file.

            user_file_type (str): A description of the file. Used in messages to the user.

        Returns:
            str: The file path the user provided.
        """
        if user_file_path is not None:
            if pathlib.Path(user_file_path).is_file():
                eprint(f'• Custom {user_file_type} found: "{Font.b}{user_file_path}{Font.be}".')
            else:
                eprint(
                    f'• Can\'t find the specified {user_file_type}: '
                    f'"{Font.b}{user_file_path}{Font.be}". Ignoring...',
                    level='warning',
                )
        else:
            user_file_path = ''

        return user_file_path

    args.clonelist = validate_user_file(args.clonelist, 'clone list')
    args.metadata = validate_user_file(args.metadata, 'metadata file')
    args.mia = validate_user_file(args.mia, 'MIA file')
    args.ra = validate_user_file(args.ra, 'RetroAchievements file')

    # Create user options string
    user_options: list[str] = []
    hidden_options: tuple[str, ...] = (
        'Input',
        'output',
        'clonelist',
        'compilations',
        'config',
        'e',
        'exclude',
        'legacy',
        'labelmia',
        'labelretro',
        'listnames',
        'machine',
        'metadata',
        'mia',
        'mianooverrides',
        'originalheader',
        'q',
        'regionsplit',
        'removesdat',
        'replace',
        'report',
        'reprocess',
        'retroachievements',
        'singlecpu',
        'test',
        'trace',
        'warnings',
        'warningpause',
    )

    for arg in vars(args):
        if arg not in hidden_options and getattr(args, arg):
            user_options.append(arg)

    # Add another marker for legacy output DATs
    if args.legacy:
        user_options.append('x')

    args_set: set[str] = set()

    if not args.exclude:
        args.exclude = []
    else:
        args_set = set(args.exclude[0])

    compilations: str = ''

    if args.compilations:
        compilations = args.compilations[0][0:1]

    if not args.config:
        args.config = ''
    else:
        args.config = pathlib.Path(args.config).resolve()

        if not pathlib.Path(args.config).is_file():
            eprint(
                f'• The user config file you specified, '
                f'{Font.b}{args.config}{Font.be}, doesn\'t exist. '
                'Using the default config/user-config.yaml.',
                level='warning',
            )
            args.config = pathlib.Path('config/user-config.yaml').resolve()

    if not args.trace:
        args.trace = []

    user_options_string: str = ''

    if user_options != []:
        user_options_string = (
            f' (-{"".join(sorted(user_options, key=lambda s: (s.lower(), s[0].isupper())))})'
        )

    return UserInput(
        input_file_name=str(pathlib.Path(args.Input).resolve()),
        update=args.update,
        no_1g1r=args.d,
        filter_languages=args.l,
        local_names=args.n,
        oldest=args.o,
        retroachievements=args.c,
        region_bias=args.r,
        legacy=args.legacy,
        demote_unl=args.y,
        modern=args.z,
        compilations=compilations,
        no_applications=bool('a' in args_set),
        no_audio=bool('A' in args_set),
        no_bad_dumps=bool('b' in args_set),
        no_bios=bool('B' in args_set),
        no_coverdiscs=bool('c' in args_set),
        no_demos=bool('d' in args_set),
        no_add_ons=bool('D' in args_set),
        no_educational=bool('e' in args_set),
        no_aftermarket=bool('f' in args_set),
        no_games=bool('g' in args_set),
        no_mia=bool('k' in args_set),
        no_manuals=bool('m' in args_set),
        no_multimedia=bool('M' in args_set),
        no_bonus_discs=bool('o' in args_set),
        no_pirate=bool('p' in args_set),
        no_preproduction=bool('P' in args_set),
        no_promotional=bool('r' in args_set),
        no_unlicensed=bool('u' in args_set),
        no_video=bool('v' in args_set),
        clone_list=str(pathlib.Path(args.clonelist).resolve()),
        user_config=args.config,
        metadata=str(pathlib.Path(args.metadata).resolve()),
        mia=str(pathlib.Path(args.mia).resolve()),
        ra=str(pathlib.Path(args.ra).resolve()),
        no_overrides=args.nooverrides,
        list_names=args.listnames,
        report=args.report,
        machine_not_game=args.machine,
        label_mia=args.labelmia,
        label_retro=args.labelretro,
        original_header=args.originalheader,
        output_folder_name=str(pathlib.Path(args.output).resolve()),
        user_output_folder=args.output,
        output_region_split=args.regionsplit,
        output_remove_dat=args.removesdat,
        replace=args.replace,
        reprocess_dat=args.reprocess,
        verbose=args.warnings,
        warningpause=args.warningpause,
        single_cpu=args.singlecpu,
        trace=' '.join(args.trace),
        excludes=''.join(sorted(args_set, key=lambda s: (s.lower(), s[0].isupper()))),
        dev_mode=dev_mode,
        user_options=user_options_string,
        user_clone_list_location='',
        user_clone_list_metadata_download_location='',
        user_metadata_location='',
        user_mia_location='',
        user_ra_location='',
        test=args.test,
    )


def get_config_value(
    config_object: tuple[Any, ...], key: str, default_value: str, is_path: bool = True
) -> str:
    """
    Gets a value for a specific key in an object out of `user-config.yaml` and system
    config files.

    Args:
        config_object (tuple[Any, ...]): A YAML object from a config file.

        key (str): The key in the YAML object to query.

        default_value (str): The equivalent default value as found in
            `internal-config.json`.

        is_path (bool, optional): Whether to process the value as a path. Defaults to
            `True`.
    """
    key_and_value: list[dict[str, Any]] = [
        x for x in config_object if key in x and x != {f'"{key}": ""'}
    ]

    value: str = ''

    if is_path:
        if key_and_value:
            if key_and_value[0][key] != str(pathlib.Path(default_value).resolve()):
                value = key_and_value[0][key]
        else:
            if default_value:
                value = str(pathlib.Path(default_value).resolve())
    else:
        if key_and_value:
            if key_and_value[0][key] != default_value:
                value = key_and_value[0][key]
        else:
            value = default_value

    return value


def import_clone_list_mia_ra(input_dat: Dat, gui_input: UserInput | None, config: Config) -> CloneList:
    """
    Imports a clone list, RetroAchievements and MIAs from the relevant files and sets them
    up for use in Retool.

    Args:
        input_dat (Dat): The Retool input_dat object.

        gui_input (UserInput): Used to determine if the function is being called from the
            GUI.

        config (Config): The Retool config object.

    Raises:
        ExitRetool: Silently exit if run from the GUI, so UI elements can re-enable.

    Returns:
        CloneList: A CloneList object which is used to enable custom matching of titles,
        pioritization of titles, assignment of new categories, and more.
    """
    # Grab local file path where clone lists are found
    clone_list_path: str = str(config.path_clone_list)

    if config.user_input.user_clone_list_location:
        clone_list_path = config.user_input.user_clone_list_location

    clone_file: str = ''

    # Import the clone list
    if config.system_clone_list and {'override': 'true'} in config.system_user_path_settings:
        # If a user has set a custom clone list for a system through a config file
        clone_file = config.system_clone_list
    elif config.user_input.clone_list and config.user_input.clone_list != str(
        pathlib.Path('').resolve()
    ):
        # If a user has set a custom clone list using the CLI
        clone_file = config.user_input.clone_list
    else:
        # Load the default clone list, which has the same name as input_dat.search_name.json.
        clone_list_name: str = input_dat.search_name

        if 'MAME Redump' in input_dat.search_name:
            clone_list_name = input_dat.search_name.replace(' (MAME Redump)', ' (Redump)')

        if config.user_input.test:
            clone_file = f'tests/clonelists/{clone_list_name}.json'
        else:
            clone_file = f'{clone_list_path}/{clone_list_name}.json'

    clonedata: dict[str, Any] = load_data(clone_file, 'clone list', config)

    min_version: str = ''
    variants: list[dict[str, Any]] = []

    if 'variants' in clonedata:
        variants = clonedata['variants']
    if 'description' in clonedata:
        if 'minimumVersion' in clonedata['description']:
            min_version = clonedata['description']['minimumVersion']
            minimum_version(min_version, clone_file, gui_input)

    # Grab local file path where MIAs are found
    mias: list[dict[str, str]] = []

    if config.user_input.label_mia:
        mia_path: str = str(config.path_mia)

        if config.user_input.user_mia_location:
            mia_path = config.user_input.user_mia_location

        mia_file: str = ''

        # Import the MIA file
        if config.system_mia_file and {'override': 'true'} in config.system_user_path_settings:
            # If a user has set a custom MIA file for a system through a config file
            mia_file = config.system_mia_file
        elif config.user_input.mia and config.user_input.mia != str(pathlib.Path('').resolve()):
            # If a user has set a custom MIA file using the CLI
            mia_file = config.user_input.mia
        else:
            # Load the default MIA list, which has the same name as input_dat.search_name.json
            mia_file_name: str = input_dat.search_name

            if config.user_input.test:
                mia_file = f'tests/mias/{mia_file_name}.json'
            else:
                mia_file = f'{mia_path}/{mia_file_name}.json'

        mia_data: dict[str, list[dict[str, str]]] = load_data(mia_file, 'MIA file', config)

        if 'mias' in mia_data:
            mias = mia_data['mias']

    # Grab local file path where RetroAchievements are found
    retroachievements: list[dict[str, str]] = []

    if config.user_input.label_retro:
        ra_path: str = str(config.path_ra)

        if config.user_input.user_ra_location:
            ra_path = config.user_input.user_ra_location

        ra_file: str = ''
        ra_chd_file: str = ''
        retroachievements_data: dict[str, list[dict[str, str]]] = {}

        # Import the RetroAchievements data
        if config.system_ra_file and {'override': 'true'} in config.system_user_path_settings:
            # If a user has set a custom RetroAchievements file for a system through a config
            # file
            ra_file = config.system_ra_file
        elif config.user_input.ra and config.user_input.ra != str(pathlib.Path('').resolve()):
            # If a user has set a custom RetroAchievements file using the CLI
            ra_file = config.user_input.ra
        else:
            # Load the default RetroAchievments list
            ra_file_name: str = (
                input_dat.search_name.replace('Non-Redump - ', '')
                .replace(' (No-Intro)', '')
                .replace(' (Redump)', '')
                .replace(' (MAME Redump)', '')
            )

            if config.user_input.test:
                ra_file = f'tests/retroachievements/{ra_file_name}.json'
            else:
                ra_file = f'{ra_path}/{ra_file_name}.json'
                ra_chd_file = f'{ra_path}/{ra_file_name} (CHD).json'

        retroachievements_data = load_data(ra_file, 'RetroAchievements file', config)

        if 'retroachievements' in retroachievements_data:
            retroachievements = retroachievements_data['retroachievements']

        # Some RetroAchievements have CHD equivalents, so import those digests too
        if ra_chd_file and pathlib.Path(ra_chd_file).exists():
            retroachievements_data = load_data(ra_chd_file, 'RetroAchievements CHD file', config)

            if 'retroachievements' in retroachievements_data:
                retroachievements.extend(retroachievements_data['retroachievements'])

    return CloneList(min_version, mias, retroachievements, variants)


def import_metadata(input_dat: Dat, config: Config) -> dict[str, dict[str, str]]:
    """
    Imports metadata scraped from Redump and No-Intro's sites from the
    relevant file, so Retool has more language information to work with.

    Args:
        input_dat (Dat): The Retool input_dat object.

        config (Config): The Retool config object.

    Returns:
        dict (dict[str, dict[str, str]]): A dictionary that contains metadata for all the
        titles in the DAT.
    """
    # Grab local file path where metadata files are found
    metadata_path: str = str(config.path_metadata)

    if config.user_input.user_metadata_location:
        metadata_path = config.user_input.user_metadata_location

    metadata_file: str = ''

    # Import the metadata file
    if config.system_metadata_file and {'override': 'true'} in config.system_user_path_settings:
        # If a user has set a custom metadata file for a system through a config file
        metadata_file = config.system_metadata_file
    elif config.user_input.metadata and config.user_input.metadata != str(
        pathlib.Path('').resolve()
    ):
        # If a user has set a custom metadata file using the CLI
        metadata_file = config.user_input.metadata
    else:
        # Load the default metadata file. Import JSON file that has the same name as input_dat.search_name.json.
        metadata_file_name: str = input_dat.search_name

        if 'MAME Redump' in input_dat.search_name:
            metadata_file_name = input_dat.search_name.replace(' (MAME Redump)', ' (Redump)')

        if config.user_input.test:
            metadata_file = f'tests/metadata/{metadata_file_name}.json'
        else:
            metadata_file = f'{metadata_path}/{metadata_file_name}.json'

    metadata: dict[str, Any] = load_data(metadata_file, 'metadata file', config)

    return metadata


def import_system_settings(
    config: Config,
    search_name: str,
    system_language_order_key: str,
    system_region_order_key: str,
    system_localization_order_key: str,
    system_video_order_key: str,
    system_list_prefix_key: str,
    system_list_suffix_key: str,
    system_override_exclude_key: str,
    system_override_include_key: str,
    system_filter_key: str,
    system_exclusions_options_key: str,
) -> None:
    """
    Imports system settings from the relevant file.

    Args:
        config (Config): The Retool config object.

        search_name (str): The name of the system file, based on the DAT's system.

        system_language_order_key (str): The key in the system config that specifies the
            language order as defined by the user.

        system_region_order_key (str): The key in the system config that specifies the
            region order as defined by the user.

        system_localization_order_key (str): The key in the system config that specifies
            the localization order as defined by the user.

        system_video_order_key (str): The key in the system config that specifies the
            order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM as defined
            by the user.

        system_list_prefix_key (str): The key in the system config that specifies the
            prefix used when the user specifies `--listnames`.

        system_list_suffix_key (str): The key in the system config that specifies the
            suffix used when the user specifies `--listnames`.

        system_override_exclude_key (str): The key in the system config that specifies
            the exclude overrides set by the user.

        system_override_include_key (str): The key in the system config that specifies
            the include overrides set by the user.

        system_filter_key (str): The key in the system config that specifies the post
            filters set by the user.

        system_exclusions_options_key (str): They key in the system config that specifies
            settings used by the GUI.
    """
    # Reset system settings
    config.system_user_path_settings = ()
    config.system_exclusions_options = ()
    config.system_output = ''
    config.system_clone_list = ''
    config.system_metadata_file = ''
    config.system_mia_file = ''
    config.system_ra_file = ''
    config.system_exclude = []
    config.system_include = []
    config.system_filter = []
    config.system_region_order_user = []
    config.system_languages_user_found = False
    config.system_language_order_user = []
    config.system_localization_order_user = []
    config.system_user_prefix = ''
    config.system_user_suffix = ''
    config.system_video_order_user = []

    if pathlib.Path(f'{config.system_settings_path}/{search_name}.yaml').is_file():
        schema = Map(
            {
                'config version': Str(),
                'paths': Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_language_order_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_region_order_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_localization_order_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_video_order_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_list_prefix_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_list_suffix_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_override_exclude_key: Seq(Str()) | Str(),
                system_override_include_key: Seq(Str()) | Str(),
                system_filter_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
                system_exclusions_options_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
            }
        )

        system_config_file: str = f'{config.system_settings_path}/{search_name}.yaml'
        system_settings: YAML = read_config(schema, system_config_file, config)

        # Get system paths
        config.system_user_path_settings = system_settings.data['paths']

        config.system_clone_list = get_config_value(
            config.system_user_path_settings, 'clone list', '.', True
        )
        config.system_metadata_file = get_config_value(
            config.system_user_path_settings, 'metadata file', '.', True
        )
        config.system_mia_file = get_config_value(
            config.system_user_path_settings, 'mia file', '.', True
        )
        config.system_ra_file = get_config_value(
            config.system_user_path_settings, 'retroachievements file', '.', True
        )
        config.system_output = get_config_value(
            config.system_user_path_settings, 'output', '.', True
        )

        # Get system region, language, and video standard orders
        config.system_language_order_user = list(system_settings.data[system_language_order_key])
        config.system_region_order_user = list(system_settings.data[system_region_order_key])
        config.system_localization_order_user = list(
            system_settings.data[system_localization_order_key]
        )
        config.system_video_order_user = list(system_settings.data[system_video_order_key])

        # Compensate for No-Intro using "United Kingdom", and Redump using "UK"
        if 'UK' in config.system_region_order_user:
            uk_index: int = config.system_region_order_user.index('UK')
            config.system_region_order_user[uk_index + 1 : uk_index + 1] = ['United Kingdom']

        # Change the user languages list to be regex strings instead of language
        # names
        language_list: list[str | dict[str, str]] = []

        def implied_languages() -> None:
            if {'override': 'true'} in config.system_region_order_user:
                region_list = [
                    str(x) for x in config.system_region_order_user if 'override' not in x
                ]

                for region in region_list:
                    language_list.extend(config.languages_filter[region])
            else:
                for region in config.region_order_user:
                    language_list.extend(config.languages_filter[region])

        if {'override': 'true'} in config.system_language_order_user:
            if not [x for x in config.system_language_order_user if 'override' not in x]:
                implied_languages()
            else:
                config.system_languages_user_found = True

                language_list.extend(
                    [x for x in config.system_language_order_user if 'override' in x]
                )

                for language in [
                    str(x) for x in config.system_language_order_user if 'override' not in x
                ]:
                    if language in config.languages:
                        language_list.append(config.languages[language])

            if {'override': 'true'} not in language_list:
                language_list.append({'override': 'true'})
        else:
            implied_languages()

        # Make sure language entries are unique
        language_list = reduce(lambda x, y: [*x, y] if y not in x else x, language_list, [])

        config.system_language_order_user = list(language_list)

        # Change the user localization list to be regex strings instead of language
        # names
        localization_list: list[str | dict[str, str]] = []

        if {'override': 'true'} in config.system_localization_order_user:
            if [x for x in config.system_localization_order_user if 'override' not in x]:
                localization_list.extend(
                    [x for x in config.system_localization_order_user if 'override' in x]
                )

                for language in [
                    str(x) for x in config.system_localization_order_user if 'override' not in x
                ]:
                    if language in config.languages:
                        localization_list.append(config.languages[language])

            if {'override': 'true'} not in localization_list:
                localization_list.append({'override': 'true'})

        config.system_localization_order_user = list(localization_list)

        # Get list prefix and suffix
        config.system_user_prefix = ''.join(system_settings.data['list prefix'])
        config.system_user_suffix = ''.join(system_settings.data['list suffix'])

        # Get exclusions and options
        config.system_exclusions_options = system_settings.data[const.SYSTEM_EXCLUSIONS_OPTIONS_KEY]

        # Get include/exclude overrides
        config.system_exclude = system_settings.data['exclude']
        config.system_include = system_settings.data['include']

        # Get system post filters
        config.system_filter = system_settings.data['filters']

        # TODO: Fix this so the option is stored in the correct place
        # A weird exception for the replace input DAT files option, as storing it
        # in paths is a pain
        if {'override': 'true'} in config.system_user_path_settings:
            config.user_input.replace = False
            for option in config.system_exclusions_options:
                if option == 'replace':
                    config.user_input.replace = True

        # Override global inputs based on system settings
        if {'override exclusions': 'true'} in config.system_exclusions_options:
            config.user_input.no_add_ons = False
            config.user_input.no_applications = False
            config.user_input.no_audio = False
            config.user_input.no_bad_dumps = False
            config.user_input.no_bios = False
            config.user_input.no_bonus_discs = False
            config.user_input.no_coverdiscs = False
            config.user_input.no_demos = False
            config.user_input.no_educational = False
            config.user_input.no_games = False
            config.user_input.no_mia = False
            config.user_input.no_manuals = False
            config.user_input.no_multimedia = False
            config.user_input.no_bonus_discs = False
            config.user_input.no_pirate = False
            config.user_input.no_preproduction = False
            config.user_input.no_promotional = False
            config.user_input.no_unlicensed = False
            config.user_input.no_video = False

            excludes: list[str] = []

            item: dict[str, str]
            for item in config.system_exclusions_options:
                if isinstance(item, dict):
                    if 'exclude' in item.keys():
                        for value in item.values():
                            if 'a' in value:
                                config.user_input.no_applications = True
                                excludes.append('a')
                            if 'A' in value:
                                config.user_input.no_audio = True
                                excludes.append('A')
                            if 'b' in value:
                                config.user_input.no_bad_dumps = True
                                excludes.append('b')
                            if 'B' in value:
                                config.user_input.no_bios = True
                                excludes.append('B')
                            if 'c' in value:
                                config.user_input.no_coverdiscs = True
                                excludes.append('c')
                            if 'd' in value:
                                config.user_input.no_demos = True
                                excludes.append('d')
                            if 'D' in value:
                                config.user_input.no_add_ons = True
                                excludes.append('D')
                            if 'e' in value:
                                config.user_input.no_educational = True
                                excludes.append('e')
                            if 'f' in value:
                                config.user_input.no_aftermarket = True
                                excludes.append('f')
                            if 'g' in value:
                                config.user_input.no_games = True
                                excludes.append('g')
                            if 'k' in value:
                                config.user_input.no_mia = True
                                excludes.append('k')
                            if 'm' in value:
                                config.user_input.no_manuals = True
                                excludes.append('m')
                            if 'M' in value:
                                config.user_input.no_multimedia = True
                                excludes.append('M')
                            if 'o' in value:
                                config.user_input.no_bonus_discs = True
                                excludes.append('o')
                            if 'p' in value:
                                config.user_input.no_pirate = True
                                excludes.append('p')
                            if 'P' in value:
                                config.user_input.no_preproduction = True
                                excludes.append('P')
                            if 'r' in value:
                                config.user_input.no_promotional = True
                                excludes.append('r')
                            if 'u' in value:
                                config.user_input.no_unlicensed = True
                                excludes.append('u')
                            if 'v' in value:
                                config.user_input.no_video = True
                                excludes.append('v')

                            config.user_input.excludes = ''.join(excludes)

        if {'override options': 'true'} in config.system_exclusions_options:
            config.user_input.demote_unl = False
            config.user_input.legacy = False
            config.user_input.list_names = False
            config.user_input.report = False
            config.user_input.machine_not_game = False
            config.user_input.label_mia = False
            config.user_input.label_retro = False
            config.user_input.oldest = False
            config.user_input.retroachievements = False
            config.user_input.original_header = False
            config.user_input.modern = False
            config.user_input.no_1g1r = False
            config.user_input.no_overrides = False
            config.user_input.compilations = ''
            config.user_input.output_region_split = False
            config.user_input.output_remove_dat = False
            config.user_input.reprocess_dat = False
            config.user_input.region_bias = False
            config.user_input.verbose = False
            config.user_input.warning_pause = False
            config.user_input.single_cpu = False
            config.user_input.trace = ''

            options: list[str] = []

            for option in config.system_exclusions_options:
                if option == 'c':
                    config.user_input.retroachievements = True
                    options.append('c')
                if option == 'd':
                    config.user_input.no_1g1r = True
                    options.append('d')
                if option == 'legacy':
                    config.user_input.legacy = True
                    options.append('x')
                if option == 'listnames':
                    config.user_input.list_names = True
                if option == 'report':
                    config.user_input.report = True
                if option == 'machine':
                    config.user_input.machine_not_game = True
                if option == 'labelmia':
                    config.user_input.label_mia = True
                if option == 'labelretro':
                    config.user_input.label_retro = True
                if option == 'o':
                    config.user_input.oldest = True
                    options.append('o')
                if option == 'originalheader':
                    config.user_input.original_header = True
                if option == 'nooverrides':
                    config.user_input.no_overrides = True
                if option == 'r':
                    options.append('r')
                    config.user_input.region_bias = True
                if option == 'regionsplit':
                    config.user_input.output_region_split = True
                if option == 'removesdat':
                    config.user_input.output_remove_dat = True
                if option == 'reprocess':
                    config.user_input.reprocess_dat = True
                if option == 'singlecpu':
                    config.user_input.single_cpu = True
                if option == 'warningpause':
                    config.user_input.warning_pause = True
                if option == 'warnings':
                    config.user_input.verbose = True
                if option == 'y':
                    options.append('y')
                    config.user_input.demote_unl = True
                if option == 'z':
                    config.user_input.modern = True
                    options.append('z')

            config.user_input.compilations = get_config_value(
                config.system_exclusions_options, 'compilations', '', is_path=False
            )

            config.user_input.trace = get_config_value(
                config.system_exclusions_options, 'trace', '', is_path=False
            )

            config.user_input.user_options = f' (-{"".join(sorted(options))})'


def load_data(data_file: str, file_type: str, config: Config) -> dict[str, Any]:
    """
    Opens clone list or metadata files, and gives the user the option to redownload
    them if the JSON is invalid.

    Args:
        data_file (str): The file to open.

        file_type (str): The file type, either `clone list` or `metadata file`.

        config (Config): The Retool config object.

    Returns:
        dict (dict[str, Any]): The JSON representation of the file.
    """
    data_content: dict[str, Any] = {}

    if pathlib.Path(data_file).is_file():
        try:
            with open(pathlib.Path(data_file), encoding='utf-8') as input_file:
                data_content = json.load(input_file)

        except ValueError:
            download_data_file: str = ''

            while not download_data_file or not (
                download_data_file == 'y' or download_data_file == 'n'
            ):
                eprint(
                    f'• {Font.b}Warning{Font.be}: The {Font.b}{data_file}{Font.be} '
                    f'{file_type} contains invalid JSON. Retool won\'t '
                    'be able to detect clones as accurately. Would you like to redownload '
                    f'the {file_type} to fix this? (y/n)',
                    level='warning',
                )

                eprint('\n  > ')
                download_data_file = input()

            if download_data_file == 'y':
                eprint(
                    f'\n• Downloading {Font.b}{data_file}{Font.be}... ',
                    sep=' ',
                    end='',
                    flush=True,
                )
                download(
                    (
                        f'{config.clone_list_metadata_download_location}/{data_file}',
                        str(pathlib.Path(f'{data_file}')),
                    ),
                    False,
                )
                eprint('done.')
                data_content = load_data(data_file, file_type, config)

        except OSError as e:
            eprint(f'• {Font.error_bold}Error{Font.be}: {e!s}\n', level='error')
            raise

    return data_content
