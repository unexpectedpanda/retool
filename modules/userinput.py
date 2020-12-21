import argparse
import os
import sys

from strictyaml import load, Map, MapPattern, Str, Seq, YAMLError

from modules.classes import SmartFormatter, UserInput
from modules.utils import Font

def check_input():
    """ Checks user input values"""

    parser = argparse.ArgumentParser(
        usage=f'%(prog)s <input dat/folder> <options>',
        allow_abbrev=False,
        formatter_class=SmartFormatter)

    dev_options = parser.add_argument_group('dev options')
    filter_options = parser.add_argument_group('filter options')

    parser.add_argument('Input',
                        metavar='<input dat>',
                        type=str,
                        help='R|the path to the dat file, or folder of dat files you want\nto process')

    parser.add_argument('-o',
                        metavar='<output folder>',
                        type=str,
                        help='R|set an output folder where the new 1G1R dat/s will be\ncreated')

    dev_options.add_argument('--log',
                        action='store_true',
                        help='R|also export a list of what titles have been kept and\nremoved/set as clones in the output dat/s')

    dev_options.add_argument('--errors',
                        action='store_true',
                        help=f'report clone list errors during processing')

    dev_options.add_argument('-x',
                        action='store_true',
                        help='export dat/s in legacy parent/clone format')

    filter_options.add_argument('-g',
                        action='store_true',
                        help='enable most filters (-bcdefirs)')

    filter_options.add_argument('-l',
                        action='store_true',
                        help=f'filter by languages using a list (see {Font.bold}user-config.yaml{Font.end})')

    filter_options.add_argument('-s',
                        action='store_true',
                        help='R|supersets (special editions, game of the year editions, and\ncollections) replace standard editions\n\n')

    filter_options.add_argument('-a',
                        action='store_true',
                        help='exclude applications')

    filter_options.add_argument('-b',
                        action='store_true',
                        help='exclude bad dumps')

    filter_options.add_argument('-c',
                        action='store_true',
                        help='exclude compilations with no unique titles')

    filter_options.add_argument('-d',
                        action='store_true',
                        help='exclude demos and samples')

    filter_options.add_argument('-e',
                        action='store_true',
                        help='exclude educational titles')

    filter_options.add_argument('-f',
                        action='store_true',
                        help='exclude coverdiscs (discs attached to the front of magazines)')

    filter_options.add_argument('-i',
                        action='store_true',
                        help='exclude audio titles (these might be used as soundtracks by games)')

    filter_options.add_argument('-j',
                        action='store_true',
                        help='exclude video titles')

    filter_options.add_argument('-k',
                        action='store_true',
                        help='exclude BIOS titles (No-Intro only)')

    filter_options.add_argument('-m',
                        action='store_true',
                        help='exclude multimedia titles (these might include games)')

    filter_options.add_argument('-n',
                        action='store_true',
                        help='exclude pirate titles')

    filter_options.add_argument('-p',
                        action='store_true',
                        help='exclude preproduction titles (alphas, betas, prototypes)')

    filter_options.add_argument('-q',
                        action='store_true',
                        help=argparse.SUPPRESS)

    filter_options.add_argument('-r',
                        action='store_true',
                        help='exclude promotional titles')

    filter_options.add_argument('-u',
                        action='store_true',
                        help='exclude unlicensed titles')

    if len(sys.argv) == 1:
        sys.exit(1)
    args = parser.parse_args()

    if not os.path.isfile(args.Input) and not os.path.isdir(args.Input):
        print(f'Can\'t find the specified input dat or folder {Font.bold}"{args.Input}"{Font.end}.')
        sys.exit()

    if args.o is not None:
        if os.path.isfile(args.o):
            print(f'Can\'t output to {Font.bold}"{args.o}"{Font.end}, as it\'s a file, not a folder.')
            sys.exit()
        elif not os.path.exists(args.o):
            print(f'* Creating folder "{Font.bold}{args.o}{Font.end}"')
            os.makedirs(args.o)
    else:
        args.o = ''

    # Set verbose and legacy to always be true if in dev environment
    if os.path.isfile('.dev') and args.q == False:
        setattr(args, 'x', True)
        setattr(args, 'errors', True)

    # Set -g options, and create user options string
    user_options = []
    hidden_options = ['Input', 'g', 'l', 'o', 'q', 'errors', 'log']
    non_g_options = ['a', 'm', 'n', 'p', 'u', 'x']

    if args.g == True:
        for arg in vars(args):
            if arg not in hidden_options and arg not in non_g_options:
                setattr(args, arg, True)

    for arg in vars(args):
        if arg not in hidden_options and getattr(args, arg) == True:
            user_options.append(arg)

    if user_options != []:
        user_options = f' (-{"".join(sorted(user_options))})'
    else:
        user_options = ''

    return UserInput(
            args.Input,
            args.o,
            args.a,
            args.b,
            args.c,
            args.d,
            args.e,
            args.f,
            args.i,
            args.j,
            args.k,
            args.m,
            args.n,
            args.p,
            args.r,
            args.u,
            args.s,
            args.l,
            args.x,
            user_options,
            args.errors,
            args.log)


def import_user_config(region_data, user_input):
    try:
        schema = Map({"language filter": Seq(Str())|Str(), "region order": Seq(Str())|Str(), "gui settings": Seq(Str()|MapPattern(Str(), Str()))|Str()})

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