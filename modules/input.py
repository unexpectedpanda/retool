from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

from strictyaml import load, Map, MapPattern, Str, Seq, YAMLError
from typing import Any, TYPE_CHECKING

from modules.clonelists import CloneList
from modules.dats import Dat
from modules.utils import eprint, ExitRetool, Font, download, printwrap, SmartFormatter

if TYPE_CHECKING:
    from modules.config import Config

class UserInput:
    def __init__(self,
                 input_file_name: str = '',
                 update: bool = False,
                 no_1g1r: bool = False,
                 empty_titles: bool = False,
                 filter_languages: bool = False,
                 region_bias: bool = False,
                 legacy: bool = False,
                 demote_unl: bool = False,
                 modern: bool = False,
                 no_applications: bool = False,
                 no_audio: bool = False,
                 no_bad_dumps: bool = False,
                 no_bios: bool = False,
                 no_coverdiscs: bool = False,
                 no_demos: bool = False,
                 no_add_ons: bool = False,
                 no_educational: bool = False,
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
                 no_filters: bool = False,
                 list_names: bool = False,
                 log: bool = False,
                 output_folder_name: str = '',
                 output_region_split: bool = False,
                 output_remove_dat: bool = False,
                 verbose: bool = False,
                 warningpause: bool = False,
                 single_cpu: bool = False,
                 trace: str = '',
                 no_dtd: bool = False,
                 excludes: str = '',
                 dev_mode: bool = False,
                 user_options: str = '',
                 user_clone_list_location: str = '',
                 user_clone_list_metadata_download_location: str = '',
                 user_metadata_location: str = '',
                 test: bool = False) -> None:
        """ Stores user input values, including what types of titles to exclude.

        Args:
            `input_file_name (str, optional)`: The path to the input DAT file. Defaults to
            `''`.
            `update (bool, optional)`: Calls the clone list update function. Defaults to
            `False`.
            `no_1g1r (bool, optional)`: Disables 1G1R processing. Defaults to `False`.
            `empty_titles (bool, optional)`: Includes titles that don't have hashes or a
            size. Defaults to `False`.
            `filter_languages (bool, optional)`: Filters by languages, removing any title
            that doesn't support the languages in the supplied list. Defaults to `False`.
            `region_bias (bool, optional)`: Prefers regions over languages. Defaults to
            `False`.
            `legacy (bool, optional)`: Outputs the DAT file in legacy mode, complete with
            parent/clone tags. Only useful for clone list maintainers who want to trac
            changes between DAT releases. Defaults to `False`.
            `demote_unl (bool, optional)`: Demotes unlicensed, aftermarket, and homebrew
            titles if a production version of a title is found in another region. Defaults
            to `False`.
            `modern (bool, optional)`: Whether to choose a version of a title ripped
            from a modern rerelease (e.g. Steam, Virtual Console) over the original
            title. Defaults to `False`.
            `no_applications (bool, optional)`: Excludes applications. Defaults to
            `False`.
            `no_audio (bool, optional)`: Excludes audio. Defaults to `False`.
            `no_bad_dumps (bool, optional)`: Excludes bad dumps. Defaults to `False`.
            `no_bios (bool, optional)`: Excludes BIOS and other chip-based titles.
            Defaults to `False`.
            `no_coverdiscs (bool, optional)`: Excludes coverdiscs. Defaults to `False`.
            `no_demos (bool, optional)`: Excludes demos. Defaults to `False`.
            `no_add_ons (bool, optional)`: Excludes add-ons. Defaults to `False`.
            `no_educational (bool, optional)`: Excludes educational titles. Defaults to
            `False`.
            `no_mia (bool, optional)`: Excludes MIA titles. Defaults to `False`.
            `no_manuals (bool, optional)`: Excludes manuals. Defaults to `False`.
            `no_multimedia (bool, optional)`: Excludes multimedia titles. Defaults to
            `False`.
            `no_bonus_discs (bool, optional)`: Excludes bonus discs. Defaults to `False`.
            `no_pirate (bool, optional)`: Excludes pirated titles. Defaults to `False`.
            `no_preproduction (bool, optional)`: Excludes preproduction titles. Defaults to
            `False`.
            `no_promotional (bool, optional)`: Excludes promotional titles. Defaults to
            `False`.
            `no_unlicensed (bool, optional)`: Excludes unlicensed, aftermarket, and
            homebrew titles. Defaults to `False`.
            `no_video (bool, optional)`: Excludes video titles. Defaults to `False`.
            `clone_list (str, optional)`: The path to a clone list to load, overriding
            the default selection. Defaults to `''`.
            `user_config (str, optional)`: The path to a user config file to load,
            overriding the default selection. Defaults to `''`.
            `metadata (str, optional)`: The path to a metadata file to load, overriding the
            default selection. Defaults to `''`.
            `no_filters (bool, optional)`: Disables global and system user filters.
            Defaults to `False`.
            `list_names (bool, optional)`: Additionally outputs a file that contains just
            the names of the 1G1R titles found after processing. Defaults to `False`.
            `log (bool, optional)`: Additionally outputs a file that shows what titles
            have been kept and removed. Defaults to `False`.
            `output_folder_name (str, optional)`: Sets the folder DATs are written to.
            Defaults to `''`.
            `output_region_split (bool, optional)`: Produces multiple DAT files split by
            region, instead of just a single DAT file. Defaults to `False`.
            `output_remove_dat (bool, optional)`: Additionally outputs a DAT that contains
            all the titles Retool has removed as part of its process. Defaults to `False`.
            `verbose (bool, optional)`: Displays warnings when clone list errors occur.
            Defaults to `False`.
            `warningpause (bool, optional)`: Pauses Retool when a clone list error is
            reported. Defaults to `False`.
            `single_cpu (bool, optional)`: Uses a single CPU to do the processing, instead
            of using all available processors. Defaults to `False`.
            `trace (str, optional)`: Traces a title through Retool's process, using the
            supplied string as regex. Defaults to `''`.
            `no_dtd (bool, optional)`: Bypasses DTD validation. Defaults to `False`.
            `excludes (str, optional)`: A string representation of all the exclusion
            options as single letters. Used in naming the output DAT file as a way to
            determine what options generated the file. Defaults to `''`.
            `dev_mode (bool, optional)`: Enables dev mode. Displays some extra messages to
            help troubleshoot code issues. Defaults to `False`.
            `user_options (str, optional)`: If a user has enabled single letter user
            options (-delryz), adds them to the output filename. Defaults to `''`.
            `user_clone_list_location (str, optional)`: A user-defined folder for where
            clone lists live. Only settable in the GUI. Defaults to `''`.
            `user_clone_list_metadata_download_location (str, optional)`: A user-defined
            URL for where to download clone list and metadata updates from. Only settable
            in the GUI. Defaults to `''`.
            `user_metadata_location (str, optional)`: A user-defined folder for where
            metadata files live. Only settable in the GUI. Defaults to `''`.
            `test (bool, optional)`: Runs tests helpful to Retool's development. Defaults
            to `False`.
        """

        # Positional
        self.input_file_name: str = input_file_name

        # Optional
        self.no_1g1r: bool = no_1g1r
        self.empty_titles: bool = empty_titles
        self.legacy: bool = legacy
        self.filter_languages: bool = filter_languages
        self.no_mia: bool = no_mia
        self.region_bias: bool = region_bias
        self.demote_unl: bool = demote_unl
        self.modern: bool = modern

        # Excludes
        self.no_add_ons: bool = no_add_ons
        self.no_applications: bool = no_applications
        self.no_audio: bool = no_audio
        self.no_bad_dumps: bool = no_bad_dumps
        self.no_bios: bool = no_bios
        self.no_bonus_discs: bool = no_bonus_discs
        self.no_coverdiscs: bool = no_coverdiscs
        self.no_demos: bool = no_demos
        self.no_educational: bool = no_educational
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
        self.user_clone_list_location: str = user_clone_list_location
        self.user_clone_list_metadata_download_location: str = user_clone_list_metadata_download_location
        self.user_metadata_location: str = user_metadata_location
        self.no_filters: bool = no_filters

        # Outputs
        self.list_names: bool = list_names
        self.log: bool = log
        self.output_folder_name: str = output_folder_name
        self.output_region_split: bool = output_region_split
        self.output_remove_dat: bool = output_remove_dat

        # Debug
        self.verbose: bool = verbose
        self.warningpause: bool = warningpause
        self.single_cpu: bool = single_cpu
        self.trace: str = trace
        self.no_dtd: bool = no_dtd

        # Internal
        self.user_options: str = user_options
        self.excludes: str = excludes
        self.dev_mode: bool = dev_mode
        self.update: bool = update

        # TODO: Are these needed?
        self.test: bool = test


def check_input() -> UserInput:
    """ Checks user input values, and creates a UserInput object for Retool to use. """

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        usage=f'\n\n%(prog)s <input DAT/folder> <options>\n\nOR to download updated clone lists:\n\n%(prog)s --update',
        allow_abbrev=False,
        formatter_class=SmartFormatter,
        add_help=False)

    # Help text order is determined by the group order here
    exclusions: Any = parser.add_argument_group('exclusions')
    inputs: Any = parser.add_argument_group('inputs')
    outputs: Any = parser.add_argument_group('outputs')
    debug: Any = parser.add_argument_group('debug')
    system: Any = parser.add_argument_group('system')

    parser.add_argument('Input',
                        metavar='<input DAT/folder>',
                        type=str,
                        help='R|The path to the DAT file, or folder of DAT files you'
                             '\nwant to process.',
                        nargs='?')

    parser.add_argument('-h', '--help', '-?', action='help', default=argparse.SUPPRESS,
                        help=argparse.SUPPRESS)

    parser.add_argument('-d',
                        action='store_true',
                        help='R|Disable 1G1R filtering. Clone lists are ignored, and each'
                             '\ntitle is treated as unique. User settings and excludes are'
                             '\nstill respected. Useful if you want to keep everything'
                             '\nfrom a specific set of regions and/or languages. Not'
                             '\ncompatible with -x.')

    parser.add_argument('-e',
                        action='store_true',
                        help='R|Include titles that don\'t have hashes or sizes'
                             '\nspecified in the input DAT.')

    parser.add_argument('-l',
                        action='store_true',
                        help=f'R|Filter by languages using a list. If a title doesn\'t'
                             '\nsupport any of the languages on the list, it\'s removed'
                             f'\n(see {Font.bold}config/user-config.yaml{Font.end}).')

    parser.add_argument('-r',
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
                             '\ncontent and supports your preferred languages.')

    parser.add_argument('-y',
                        action='store_true',
                        help='R|Demote Unlicensed, Aftermarket, or Homebrew titles if'
                             '\nproduction versions are found in another region. This'
                             '\nmight select titles with lower priority languages, or'
                             '\nless features.')

    parser.add_argument('-z',
                        action='store_true',
                        help='R|Titles ripped from modern platform rereleases, such as'
                             '\nthose found in Virtual Console, replace standard '
                             '\neditions (ripped titles might not work in emulators).')

    parser.add_argument('-q',
                        action='store_true',
                        help=argparse.SUPPRESS)

    parser.add_argument('--test',
                        action='store_true',
                        help=argparse.SUPPRESS)

    outputs.add_argument('--listnames',
                        action='store_true',
                        help='R|Also output a TXT file of just the kept title names. See'
                             f'\n{Font.bold}config/user-config.yaml{Font.end} to add a prefix and/or suffix'
                             '\nto each line.')

    outputs.add_argument('--log',
                        action='store_true',
                        help='R|Also output a TXT file of what titles have been kept,'
                             '\nremoved, and set as clones.')

    outputs.add_argument('--output',
                        metavar='<folder>',
                        type=str,
                        help='R|Set an output folder where the new 1G1R DAT/s will be'
                             '\ncreated.')

    outputs.add_argument('--regionsplit',
                        action='store_true',
                        help='R|Split the result into multiple DATs based on region. Use '
                             '\nwith -d to only split by region with no 1G1R processing.'
                             '\nNot compatible with -x.')

    outputs.add_argument('--removesdat',
                        action='store_true',
                        help='R|Also output a DAT containing the titles that were'
                             '\nremoved from the 1G1R DAT.')

    inputs.add_argument('--clonelist',
                        metavar='<file>',
                        type=str,
                        help='R|Set a custom clone list to use instead of the default.'
                              '\nUseful if you want to use your own, or if Redump or'
                              '\nNo-Intro renames their DAT, and the clone list isn\'t'
                              '\nautomatically detected anymore. Often used together with'
                              '\n--metadata.')

    inputs.add_argument('--config',
                        metavar='<file>',
                        type=str,
                        help='R|Set a custom user config file to use instead of the'
                             '\ndefault. Useful for testing.')

    inputs.add_argument('--metadata',
                        metavar='<file>',
                        type=str,
                        help='R|Set a custom metadata file to use instead of the default.'
                              '\nUseful if you want to use your own, or if Redump or'
                              '\nNo-Intro renames their DAT, and the metadata file isn\'t'
                              '\nautomatically detected anymore. Often used together with'
                              '\n--clonelist.')

    inputs.add_argument('--nofilters',
                        action='store_true',
                        help='R|Don\'t load global and system user filters.')

    debug.add_argument('--warnings',
                        action='store_true',
                        help='Report clone list warnings during processing.')

    debug.add_argument('--warningpause',
                        action='store_true',
                        help='R|Pause when a clone list warning is found. Useful when\n'
                             'batch processing DATS.')

    debug.add_argument('--legacy',
                        action='store_true',
                        help='R|Output DAT/s in legacy parent/clone format. Not'
                             '\ncompatible with -d.')

    debug.add_argument('--nodtd',
                        action='store_true',
                        help='R|Bypass DTD validation.')

    debug.add_argument('--singlecpu',
                        action='store_true',
                        help='R|Disable multiprocessor usage.')

    debug.add_argument('--trace',
                        action='extend',
                            metavar='',
                            help='R|Trace a title through the Retool process for debugging.'
                            '\nTo function properly, this disables using multiple'
                            '\nprocessors during parent selection.'
                            '\n\nUsage: --trace "regex of titles to trace"',
                            nargs='+')

    exclusions.add_argument('--exclude',
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
                                 '\nk\tMIA titles and individual MIA ROMs'
                                 '\nm\tManuals'
                                 '\nM\tMultimedia titles (might include games)'
                                 '\no\tBonus discs'
                                 '\np\tPirated titles'
                                 '\nP\tPreproduction titles (alphas, betas, prototypes)'
                                 '\nr\tPromotional titles'
                                 '\nu\tUnlicensed, aftermarket, and homebrew titles'
                                 '\nv\tVideo\n',
                            nargs='+')

    system.add_argument('--update',
                    action='store_true',
                    help=argparse.SUPPRESS)

    if len(sys.argv) == 1:
        sys.exit(1)

    args: argparse.Namespace = parser.parse_args()

    # Make sure incompatible flags aren't used, and handle other edge case situations
    if args.legacy and args.d:
        eprint(f'{Font.warning_bold}* -d and -x modes can\'t be used together. Exiting...{Font.end}')
        sys.exit()

    if args.legacy and args.regionsplit:
        eprint(f'{Font.warning_bold}* --regionsplit and -x modes can\'t be used together. Exiting...{Font.end}')
        sys.exit()

    if not args.update and args.Input is None:
        eprint(f'{Font.error_bold}* Unless you\'re updating clone lists, you must specify an input DAT or '
              f'folder.{Font.end}')
        eprint(
                f'\nUsage: {pathlib.Path(sys.argv[0]).name} <input DAT/folder> <options>'
                f'\n\nType {Font.bold}{pathlib.Path(sys.argv[0]).name} -h{Font.end} for all '
                'options\n')
        sys.exit()

    # Set warnings and legacy to always be true if in dev environment
    dev_mode: bool = False

    if pathlib.Path('.dev').is_file() and not args.q:
        dev_mode = True
        setattr(args, 'legacy', True)
        setattr(args, 'warnings', True)
        setattr(args, 'warningpause', True)
        eprint(f'{Font.warning_bold}* Operating in dev mode{Font.end}')
        eprint('')

    # Compensate for trailing backslash in Windows
    if args.Input is not None:
        if (
            sys.platform.startswith('win')
            and '"' in args.Input):
                args.Input = re.sub('".*', '', args.Input)
    else:
        args.Input = ''

    # Validate the output folder the user specified
    if args.output is not None:
        if pathlib.Path(args.output).is_file():
            eprint(
                f'\n{Font.error}Can\'t output to {Font.error_bold}"{args.output}"'
                f'{Font.error}, as it\'s a file, not a folder.{Font.end}\n')
            sys.exit()
        elif not pathlib.Path(args.output).exists():
            eprint(f'* Creating folder "{Font.bold}{args.output}{Font.end}"')
            pathlib.Path(args.output).mkdir(parents=True, exist_ok=True)
    else:
        args.output = ''

    # Validate the clone list the user specified exists
    if args.clonelist is not None:
        if pathlib.Path(args.clonelist).is_file():
            eprint(
                f'* Custom clone list found: '
                f'"{Font.bold}{args.clonelist}{Font.end}".')
        else:
            eprint(
                f'{Font.warning}* Can\'t find the specified clone list: '
                f'"{Font.bold}{args.clonelist}{Font.warning}". Ignoring...{Font.end}')
    else:
        args.clonelist = ''

    # Validate the metadata file the user specified exists
    if args.metadata is not None:
        if pathlib.Path(args.metadata).is_file():
            eprint(
                f'* Custom metadata file found: '
                f'"{Font.bold}{args.metadata}{Font.end}".')
        else:
            eprint(
                f'{Font.warning}* Can\'t find the specified metadata file: '
                f'"{Font.bold}{args.metadata}{Font.warning}". Ignoring...{Font.end}')
    else:
        args.metadata = ''

    # Create user options string
    user_options: list[str] = []
    hidden_options: tuple[str, ...] = (
        'Input',
        'output',
        'clonelist',
        'config',
        'exclude',
        'q',
        'warnings',
        'warningpause',
        'legacy',
        'log',
        'metadata',
        'nofilters',
        'nodtd',
        'listnames',
        'regionsplit',
        'removesdat',
        'singlecpu',
        'trace',
        'test',
        'e')

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
        args_set = set([x for x in args.exclude[0]])

    if not args.config:
        args.config = ''
    else:
        args.config = pathlib.Path(args.config).resolve()

        if not pathlib.Path(args.config).is_file():
            printwrap(f'{Font.warning}* The user config file you specified, '
                      f'{Font.warning_bold}{args.config}{Font.warning}, doesn\'t exist. '
                      'Using the default config/user-config.yaml.')
            args.config = pathlib.Path('config/user-config.yaml').resolve()

    if not args.trace:
        args.trace = []

    user_options_string: str = ''

    if user_options != []:
        user_options_string = f' (-{"".join(sorted([x for x in "".join(user_options)], key=str.casefold))})'

    return UserInput(
            input_file_name = pathlib.Path(args.Input).resolve(),
            update = args.update,
            no_1g1r = args.d,
            empty_titles = args.e,
            filter_languages = args.l,
            region_bias = args.r,
            legacy = args.legacy,
            demote_unl = args.y,
            modern = args.z,
            no_applications = True if 'a' in args_set else False,
            no_audio = True if 'A' in args_set else False,
            no_bad_dumps = True if 'b' in args_set else False,
            no_bios = True if 'B' in args_set else False,
            no_coverdiscs = True if 'c' in args_set else False,
            no_demos = True if 'd' in args_set else False,
            no_add_ons = True if 'D' in args_set else False,
            no_educational = True if 'e' in args_set else False,
            no_mia = True if 'k' in args_set else False,
            no_manuals = True if 'm' in args_set else False,
            no_multimedia = True if 'M' in args_set else False,
            no_bonus_discs = True if 'o' in args_set else False,
            no_pirate = True if 'p' in args_set else False,
            no_preproduction = True if 'P' in args_set else False,
            no_promotional = True if 'r' in args_set else False,
            no_unlicensed = True if 'u' in args_set else False,
            no_video = True if 'v' in args_set else False,
            clone_list = pathlib.Path(args.clonelist).resolve(),
            user_config = args.config,
            metadata = pathlib.Path(args.metadata).resolve(),
            no_filters = args.nofilters,
            list_names = args.listnames,
            log = args.log,
            output_folder_name = pathlib.Path(args.output).resolve(),
            output_region_split = args.regionsplit,
            output_remove_dat = args.removesdat,
            verbose = args.warnings,
            warningpause = args.warningpause,
            single_cpu = args.singlecpu,
            trace = ' '.join(args.trace),
            no_dtd = args.nodtd,
            excludes = ''.join(sorted(args_set, key=str.casefold)),
            dev_mode = dev_mode,
            user_options = user_options_string,
            user_clone_list_location = '',
            user_clone_list_metadata_download_location = '',
            user_metadata_location = '',
            test = args.test)


def import_clone_list(input_dat: Dat, gui_input: UserInput, config: Config) -> CloneList:
    """ Imports a clone list from the relevant file and sets it up for use in Retool.

    Args:
        `input_dat (Dat)`: The Retool input_dat object.
        `gui_input (UserInput)`: Used to determine whether or not the function is being
        called from the GUI.
        `config (Config)`: The Retool config object.

    Raises:
        `ExitRetool`: Silently exit if run from the GUI, so UI elements can
        re-enable.

    Returns:
        `CloneList`: A CloneList object which is used to enable custom matching
        of titles, pioritization of titles, assignment of new categories, and
        more.
    """

    # Grab local file path where clone lists are found
    clone_list_path: str = config.config_file_content['clone_lists']['local_dir']

    if config.user_input.user_clone_list_location:
        clone_list_path = config.user_input.user_clone_list_location

    clone_file: str = ''

    # Import JSON files that have the same name as input_dat.search_name.json
    if (
        not config.user_input.clone_list
        or config.user_input.clone_list == pathlib.Path('').resolve()):

            if not clone_file:
                # Support for specialized DATs like Redump conversions from https://dats.site
                if (
                'GameCube' in input_dat.search_name
                and (
                    'NKit GCZ' in input_dat.search_name
                    or 'NKit ISO' in input_dat.search_name
                    or 'NKit RVZ' in input_dat.search_name
                    or 'NASOS' in input_dat.search_name
                )):
                    clone_file = f'{clone_list_path}/Nintendo - GameCube (Redump).json'
                elif (
                    'Wii' in input_dat.search_name
                    and (
                        'NKit GCZ' in input_dat.search_name
                        or 'NKit ISO' in input_dat.search_name
                        or 'NKit RVZ' in input_dat.search_name
                        or 'NASOS' in input_dat.search_name
                    )):
                    clone_file = f'{clone_list_path}/Nintendo - Wii (Redump).json'
                elif (
                    'Wii U' in input_dat.search_name
                    and 'WUX' in input_dat.search_name):
                        clone_file = f'{clone_list_path}/Nintendo - Wii U (Redump).json'
                else:
                    clone_file = f'{clone_list_path}/{input_dat.search_name}.json'
    else:
        clone_file = config.user_input.clone_list

    clonedata: dict[str, Any] = load_data(clone_file, 'clone list', config)

    min_version: str = ''
    categories: dict[str, dict[str, Any]] = {}
    mias: list[str] = []
    overrides: dict[str, dict[str, Any]] = {}
    renames: dict[str, list[dict[str, Any]]] = {}
    removes: dict[str, dict[str, Any]] = {}

    if 'categories' in clonedata:
        categories = clonedata['categories']
    if 'mias' in clonedata:
        mias = clonedata['mias']
    if 'overrides' in clonedata:
        overrides = clonedata['overrides']
    if 'renames' in clonedata:
        renames = clonedata['renames']
    if 'removes' in clonedata:
        removes = clonedata['removes']
    if 'description' in clonedata:
        if 'minimum version' in clonedata['description']:
            min_version = clonedata['description']['minimum version']
            # Convert old versions to new versioning system
            if len(re.findall('\\.', min_version)) < 2:
                min_version = f'{min_version}.0'

            # Make sure current Retool version is new enough to handle the clone list
            out_of_date: bool = False

            clone_list_version_major = f'{min_version.split(".")[0]}.{min_version.split(".")[1]}'
            clone_list_version_minor = f'{min_version.split(".")[2]}'
            if clone_list_version_major > config.version_major:
                out_of_date = True
            elif clone_list_version_major == config.version_major:
                if clone_list_version_minor > config.version_minor:
                    out_of_date = True

            if out_of_date:
                out_of_date_response: str = ''

                while not (out_of_date_response == 'y' or out_of_date_response == 'n'):
                    printwrap(
                        f'{Font.warning_bold}* This clone list requires Retool '
                        f'{str(min_version)} or higher. Behaviour might be unpredictable. '
                        'Please update Retool to fix this.',
                        'error'
                    )

                    eprint(f'\n  Continue? (y/n) {Font.end}')
                    out_of_date_response = input()

                if out_of_date_response == 'n':
                    if gui_input:
                        raise ExitRetool
                    else:
                        sys.exit()
                else:
                    eprint('')

    return CloneList(
        min_version,
        categories,
        mias,
        overrides,
        renames,
        removes
    )


def import_metadata(input_dat: Dat, config: Config) -> dict[str, dict[str, str]]:
    """ Imports metadata scraped from Redump and No-Intro's sites from the
    relevant file, so Retool has more language information to work with.

    Args:
        `input_dat (Dat)`: The Retool input_dat object.
        `config (Config)`: The Retool config object.

    Returns:
        `dict[str, dict[str, str]]`: A dictionary that contains metadata for all
        the titles in the DAT.
    """

    metadata_path: str = config.config_file_content['metadata']['local_dir']

    if config.user_input.user_metadata_location:
        metadata_path = config.user_input.user_metadata_location

    metadata_file: str = ''

    if (
        not config.user_input.metadata
        or config.user_input.metadata == pathlib.Path('').resolve()):

            # Support for specialized DATs like Redump conversions from https://dats.site
            if (
                'GameCube' in input_dat.search_name
                and (
                    'NKit GCZ' in input_dat.search_name
                    or 'NKit ISO' in input_dat.search_name
                    or 'NKit RVZ' in input_dat.search_name
                    or 'NASOS' in input_dat.search_name
                )):
                    metadata_file = f'{metadata_path}/Nintendo - GameCube (Redump).json'
            elif (
                'Wii' in input_dat.search_name
                and (
                    'NKit GCZ' in input_dat.search_name
                    or 'NKit ISO' in input_dat.search_name
                    or 'NKit RVZ' in input_dat.search_name
                    or 'NASOS' in input_dat.search_name
                )):
                    metadata_file = f'{metadata_path}/Nintendo - Wii (Redump).json'
            elif (
                'Wii U' in input_dat.search_name
                and 'WUX' in input_dat.search_name):
                    metadata_file = f'{metadata_path}/Nintendo - Wii U (Redump).json'
            else:
                # Support for other DATs
                    metadata_file = f'{metadata_path}/{input_dat.search_name}.json'
    else:
        metadata_file = config.user_input.metadata

    metadata: dict[str, Any] = load_data(metadata_file, 'metadata file', config)

    if pathlib.Path(metadata_file).is_file():
        try:
            with open(pathlib.Path(metadata_file), 'r', encoding='utf-8') as input_file:
                metadata =  json.load(input_file)
        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

    return metadata


# TODO: I guess this will eventually import system settings as a whole.
def import_system_filters(
    config: Config,
    search_name: str,
    user_language_key: str,
    user_region_order_key: str,
    user_video_order_key: str,
    user_list_prefix_key: str,
    user_list_suffix_key: str,
    user_gui_settings_key: str) -> None:
    """ Imports the system user filters from the relevant file.

    Args:
        `config (Config)`: The Retool config object.
        `search_name (str)`: The name of the system file, based on the DAT's system.
        `user_language_key (str)`: The key in user-config.yaml that specifies the
        language order as defined by the user.
        `user_region_order_key (str)`: The key in user-config.yaml that specifies the
        region order as defined by the user.
        `user_video_order_key (str)`: The key in user-config.yaml that specifies the
        order for video standards like MPAL, NTSC, PAL, and SECAM as defined by the
        user.
        `user_list_prefix_key (str)`: The key in user-config.yaml that specifies the
        prefix used when the user specifies `--listnames`.
        `user_list_suffix_key (str)`: The key in user-config.yaml that specifies the
        suffix used when the user specifies `--listnames`.
        `user_gui_settings_key (str)`: They key in user-config.yaml that specifies
        settings used by the GUI.
    """

    if pathlib.Path(f'{config.user_filters_path}/{search_name}.yaml').is_file():
        try:
            schema = Map(
                {
                    'clone list': Seq(Str())|Str(),
                    'metadata file': Seq(Str())|Str(),
                    user_language_key: Seq(Str()|MapPattern(Str(), Str()))|Str(),
                    user_region_order_key: Seq(Str()|MapPattern(Str(), Str()))|Str(),
                    user_video_order_key: Seq(Str()|MapPattern(Str(), Str()))|Str(),
                    user_list_prefix_key: Seq(Str()|MapPattern(Str(), Str()))|Str(),
                    user_list_suffix_key: Seq(Str()|MapPattern(Str(), Str()))|Str(),
                    'exclude': Seq(Str())|Str(),
                    'include': Seq(Str())|Str(),
                    user_gui_settings_key: Seq(Str()|MapPattern(Str(), Str()))|Str()})

            with open(pathlib.Path(f'{config.user_filters_path}/{search_name}.yaml'), encoding='utf-8') as user_filter_import:
                system_user_filters: Any = load(str(user_filter_import.read()), schema)


        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

        except YAMLError as e:
            eprint(f'\n{Font.error_bold}* YAML error: {Font.end}{str(e)}\n')
            raise

        config.system_exclude = system_user_filters.data['exclude']
        config.system_include = system_user_filters.data['include']


def load_data(data_file: str, file_type: str, config: Config) -> dict[str, Any]:
    """ Opens clone list or metadata files, and gives the user the option to redownload
    them if the JSON is invalid.

    Args:
        `data_file (str)`: The file to open.
        `file_type (str)`: The file type, either `'clone list'` or `'metadata file'`.
        `config (Config)`: The Retool config object.

    Returns:
        `dict[str, Any]`: The JSON representation of the file.
    """

    data_content: dict[str, Any] = {}

    if pathlib.Path(data_file).is_file():
        try:
            with open(pathlib.Path(data_file), 'r', encoding='utf-8') as input_file:
                data_content = json.load(input_file)

        except ValueError as e:
            download_data_file: str = ''

            while (
                not download_data_file
                or not (
                    download_data_file == 'y'
                    or download_data_file == 'n')):
                        printwrap(
                            f'{Font.warning_bold}* Warning: {Font.warning}The {Font.bold}'
                            f'{data_file}{Font.warning} {file_type} contains invalid JSON. Retool won\'t '
                            f'be able to detect clones as accurately. Would you like to redownload the '
                            f'{file_type} to fix this? (y/n)'
                            f'{Font.end}', 'error')

                        eprint('\n  > ')
                        download_data_file = input()

            if download_data_file == 'y':
                eprint(f'\n* Downloading {Font.bold}{data_file}{Font.end}... ', sep=' ', end='', flush=True)
                download(f'{config.clone_list_metadata_download_location}/{data_file}', pathlib.Path(f'{data_file}'))
                eprint('done.')
                data_content = load_data(data_file, file_type, config)

        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

    return data_content