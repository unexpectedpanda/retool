import argparse
import os
import sys

from strictyaml import load, Map, MapPattern, Str, Seq, YAMLError

from modules.classes import SmartFormatter, UserInput
from modules.utils import Font, regex_test

def check_input():
    """ Checks user input values"""

    parser = argparse.ArgumentParser(
        usage=f'%(prog)s <input dat/folder> <options>',
        allow_abbrev=False,
        formatter_class=SmartFormatter)

    dev_options = parser.add_argument_group('dev options')
    modes = parser.add_argument_group('modes')
    exclusions = parser.add_argument_group('exclusions')

    parser.add_argument('Input',
                        metavar='<input dat>',
                        type=str,
                        help='R|the path to the dat file, or folder of dat files you want\nto process')

    parser.add_argument('--output',
                        metavar='<output folder>',
                        type=str,
                        help='R|set an output folder where the new 1G1R dat/s will be\ncreated')

    parser.add_argument('--emptytitles',
                        action='store_true',
                        help='R|include titles that don\'t have hashes, ROMs, or disks\nspecified')

    parser.add_argument('--nofilters',
                        action='store_true',
                        help='R|don\'t load custom global and system filters from the\nuser-filters folder')

    dev_options.add_argument('--errors',
                        action='store_true',
                        help='report clone list errors during processing')

    dev_options.add_argument('--list',
                        action='store_true',
                        help=f'R|also output a list of just the 1G1R title names (See\n{Font.bold}user-config.yaml{Font.end} to add a prefix and/or suffix to each line)')

    dev_options.add_argument('--log',
                        action='store_true',
                        help='R|also output lists of what titles have been kept,\nremoved, and set as clones')

    modes.add_argument('-l',
                        action='store_true',
                        help=f'filter by languages using a list (see {Font.bold}user-config.yaml{Font.end})')

    modes.add_argument('-x',
                        action='store_true',
                        help='output dat/s in legacy parent/clone format')

    modes.add_argument('-y',
                        action='store_true',
                        help='R|don\'t demote (Unl) titles if a production version is found in another region')

    modes.add_argument('-z',
                        action='store_true',
                        help='R|titles ripped from modern platform rereleases, such as those found\nin Virtual Console, replace standard editions (ripped titles might\nnot work in emulators)')

    exclusions.add_argument('--exclude',
                                action='extend',
                                metavar='FILTERS',
                                help='R|use with the following single letter filters to exclude these\ntypes of titles:\n'
                                '\na\tapplications'
                                '\nA\taudio (might include game soundtracks)'
                                '\nb\tbad dumps'
                                '\nB\tBIOS and other chips'
                                '\nc\tcoverdiscs (discs attached to the front of magazines)'
                                '\nd\tdemos, kiosks, and samples'
                                '\nD\tadd-ons (expansion packs and additional material)'
                                '\ne\teducational titles'
                                '\nm\tmanuals'
                                '\nM\tmultimedia titles (might include games)'
                                '\no\tbonus discs'
                                '\np\tpirate titles'
                                '\nP\tpreproduction titles (alphas, betas, prototypes)'
                                '\nr\tpromotional titles'
                                '\nu\tunlicensed titles'
                                '\nv\tvideo\n\n',
                                nargs='+')

    modes.add_argument('-q',
                        action='store_true',
                        help=argparse.SUPPRESS)

    modes.add_argument('--test',
                        action='store_true',
                        help=argparse.SUPPRESS)

    if len(sys.argv) == 1:
        sys.exit(1)
    args = parser.parse_args()

    if not os.path.isfile(args.Input) and not os.path.isdir(args.Input):
        print(f'Can\'t find the specified input dat or folder {Font.bold}"{args.Input}"{Font.end}.')
        sys.exit()

    if args.output is not None:
        if os.path.isfile(args.output):
            print(f'Can\'t output to {Font.bold}"{args.output}"{Font.end}, as it\'s a file, not a folder.')
            sys.exit()
        elif not os.path.exists(args.output):
            print(f'* Creating folder "{Font.bold}{args.output}{Font.end}"')
            os.makedirs(args.output)
    else:
        args.output = ''

    # Set errors and legacy to always be true if in dev environment
    if os.path.isfile('.dev') and args.q == False:
        setattr(args, 'x', True)
        setattr(args, 'errors', True)

    # Create user options string
    user_options = []
    hidden_options = ['Input', 'output', 'q', 'errors', 'log', 'nofilters', 'list', 'test', 'emptytitles']

    for arg in vars(args):
        if arg not in hidden_options and getattr(args, arg) == True:
            user_options.append(arg)

    if args.exclude != [] and args.exclude != None:
        for arg in args.exclude:
            user_options.append(arg)

    if user_options != []:
        user_options = f' (-{"".join(sorted([x for x in "".join(user_options)], key=str.casefold))})'
    else:
        user_options = ''

    return UserInput(
            args.Input,
            args.output,
            True if 'a' in user_options else False,
            True if 'A' in user_options else False,
            True if 'b' in user_options else False,
            True if 'B' in user_options else False,
            True if 'c' in user_options else False,
            True if 'd' in user_options else False,
            True if 'D' in user_options else False,
            True if 'e' in user_options else False,
            True if 'm' in user_options else False,
            True if 'M' in user_options else False,
            True if 'o' in user_options else False,
            True if 'p' in user_options else False,
            True if 'P' in user_options else False,
            True if 'r' in user_options else False,
            True if 'u' in user_options else False,
            True if 'v' in user_options else False,
            args.z,
            args.y,
            args.l,
            args.x,
            user_options,
            args.errors,
            args.nofilters,
            args.log,
            args.list,
            args.emptytitles,
            args.test)


def import_user_config(region_data, user_input):
    """ Import user config data for use in creating the output dat """

    # Import user-config.yaml settings
    try:
        schema = Map({"language filter": Seq(Str())|Str(), "region order": Seq(Str())|Str(), "list prefix": Seq(Str())|Str(), "list suffix": Seq(Str())|Str(), "gui settings": Seq(Str()|MapPattern(Str(), Str()))|Str()})

        with open('user-config.yaml', encoding='utf-8') as user_config_import:
            user_config = load(str(user_config_import.read()), schema)

    except OSError as e:
        print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
        raise

    except YAMLError as e:
        print(f'\n{Font.error_bold}* YAML error: {Font.end}{str(e)}\n')
        raise

    user_input.user_languages = []

    for key, value in region_data.languages_key.items():
        for language in user_config.data['language filter']:
            if language == key:
                user_input.user_languages.append(value)

    user_input.user_region_order = user_config.data['region order']

    user_input.user_config = user_config

    return user_input


def import_user_filters(filename, filter_type):
    """ Import user filters for excluding/including specific strings """

    try:
        schema = Map({"exclude": Seq(Str())|Str(), "include": Seq(Str())|Str()})

        with open(f'user-filters/{filename}.yaml', encoding='utf-8') as user_filter_import:
            user_filters = load(str(user_filter_import.read()), schema)

        # Check for valid regex
        user_filters.data['exclude'] = regex_test(user_filters.data['exclude'], filter_type)
        user_filters.data['include'] = regex_test(user_filters.data['include'], filter_type)

    except OSError as e:
        print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
        raise

    except YAMLError as e:
        print(f'\n{Font.error_bold}* YAML error: {Font.end}{str(e)}\n')
        raise

    return user_filters
