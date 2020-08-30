import os
import re
import sys
import textwrap

from strictyaml import load

from modules.classes import UserInput
from modules.utils import Font


def usage():
    """ Generic error message, also shows when the user doesn't provide any options """

    print(f'USAGE: {Font.bold}{os.path.basename(sys.argv[0])} -i {Font.end}<input dat/folder> <options>')
    print(f'\nA new file is automatically generated, the original file isn\'t altered.'
            f'\nEdit the {Font.bold}user-config.yaml{Font.end} file to set region order and filter languages.\n')

    print('OPTIONS:')
    if os.path.isfile('.dev'):
        print(f'{Font.bold}-q{Font.end}                   Disable dev mode (delete .dev file to')
        print(f'                     disable permanently)')
    print(f'{Font.bold}-o{Font.end} <output folder>   Set an output folder')
    print(f'{Font.bold}-x{Font.end}                   Export dat in legacy parent/clone format')
    print('                     (for use with Clonerel, not dat managers)')
    print(f'{Font.bold}-y{Font.end}                   Export a list of what titles have been')
    print(f'                     kept and removed in the output dat')
    print(f'{Font.bold}-v{Font.end}                   Verbose mode: report clone list errors')
    print('\nFILTER OPTIONS:')
    print(f'{Font.bold}-l{Font.end}  Filter languages using a list (see {Font.bold}user-config.yaml{Font.end})')
    print(f'{Font.bold}-g{Font.end}  Enable most filters (-b -c -d -e -f -m -r -s)')
    print(f'{Font.bold}-s{Font.end}  Enable supersets: special editions, game of the year')
    print('    editions, and collections replace standard editions\n')
    print(f'{Font.bold}-a{Font.end}  Exclude applications        {Font.bold}-m{Font.end}  Exclude multimedia titles')
    print(f'{Font.bold}-b{Font.end}  Exclude bad dumps           {Font.bold}-n{Font.end}  Exclude pirate titles')
    print(f'{Font.bold}-c{Font.end}  Exclude compilations        {Font.bold}-p{Font.end}  Exclude preproduction titles')
    print('    with no unique titles           (alphas, betas, prototypes)')
    print(f'{Font.bold}-d{Font.end}  Exclude demos and samples   {Font.bold}-r{Font.end}  Exclude promotional titles')
    print(f'{Font.bold}-e{Font.end}  Exclude educational titles  {Font.bold}-u{Font.end}  Exclude unlicensed titles')
    print(f'{Font.bold}-f{Font.end}  Exclude coverdiscs')
    sys.exit()


def check_input():
    """ Checks user input values"""

    error_state = False
    user_options = []

    # Handle most user options
    options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'x', 'y', 'z', '?']

    # Remove these options from the output file name and other places
    hide_options = ['g', 'i', 'l', 'o', 'q', 'v', 'y', 'z', '?']
    non_g_options = ['a', 'n', 'p', 'u', 'x']

    for option in options:
        if (len([x for x in sys.argv if x == f'-{option}']) > 0):
            user_options.append(option)

    no_applications = True if 'a' in user_options else False
    no_bad_dumps = True if 'b' in user_options or 'g' in user_options else False
    no_compilations = True if 'c' in user_options or 'g' in user_options else False
    no_demos = True if 'd' in user_options or 'g' in user_options else False
    no_educational = True if 'e' in user_options or 'g' in user_options else False
    no_coverdiscs = True if 'f' in user_options or 'g' in user_options else False
    no_multimedia = True if 'm' in user_options or 'g' in user_options else False
    no_pirate = True if 'n' in user_options else False
    no_preproduction = True if 'p' in user_options else False
    no_promotional = True  if 'r' in user_options or 'g' in user_options else False
    no_unlicensed = True if 'u' in user_options else False
    supersets = True if 's' in user_options or 'g' in user_options else False
    filter_languages = True if 'l' in user_options else False
    legacy = True if 'x' in user_options else False
    verbose = True if 'v' in user_options else False
    undo_dev = True if 'q' in user_options else False
    keep_remove = True if 'y' in user_options else False
    use_cache = True if 'z' in user_options else False

    if user_options != []:
        # Set verbose and legacy to always be true if in dev environment
        if os.path.isfile('.dev') and undo_dev == False:
            verbose = True
            legacy = True
            user_options.append('x')

        user_options_temp = user_options.copy()

        # Remove hidden options and handle -g
        for option in user_options_temp:
            if option == 'g':
                g = [g_option for g_option in options if (g_option not in hide_options and g_option not in non_g_options)]
                user_options.extend(g)

            if option in hide_options:
                user_options.remove(option)

        # Create user options string
        if user_options != []:
            user_options = f' (-{"".join(sorted(user_options))})'
        else:
            user_options = ''
    else:
        user_options = ''

    # Handle input, output, and invalid options
    for i, x in enumerate(sys.argv):
        # Check that the options entered are valid
        if (x.startswith('-')
            and x[1:] not in options):
                print(f'{Font.error}* Invalid option {sys.argv[i]}{Font.end}')
                error_state = True

        # Handle -i
        if len([x for x in sys.argv if x=='-?']) <= 0:
            if x == '-i':
                # Handle invalid or empty input
                if i + 1 == len(sys.argv) or bool(re.search(f'^-([{"".join(options)}]$)', sys.argv[i+1])):
                    print(f'{Font.error}* No input file specified{Font.end}')
                    error_state = True
                else:
                    input_file_name = os.path.abspath(sys.argv[i+1])

                    if not os.path.exists(input_file_name):
                        print(textwrap.TextWrapper(width=80, subsequent_indent='  ').fill(
                            f'{Font.error}* Input file "{Font.bold}{input_file_name}'
                            f'{Font.error}" does not exist.{Font.end}'))
                        error_state = True

        # Handle -o
        if x == '-o':
                # Handle invalid or empty input
                if (
                    i+1 == len(sys.argv)
                    or bool(re.search(f'^-([{"".join(options)}]$)', sys.argv[i+1]))):
                    print(f'{Font.error}* No output folder specified{Font.end}')
                    error_state = True
                else:
                    output_folder_name = os.path.abspath(sys.argv[i+1])

                    # Check if the output is a folder, if it doesn't exist, create it
                    if (
                        os.path.isdir(output_folder_name) == False
                        and os.path.isfile(output_folder_name) == False):
                            print(f'* Creating folder "{Font.bold}{output_folder_name}{Font.end}"')
                            os.makedirs(output_folder_name)

    # Check if no options have been provided
    if len(sys.argv) == 1:
        error_state = True

    # Check if -i is missing
    if len([x for x in sys.argv if x=='-?']) <= 0:
        if len([x for x in sys.argv if x=='-i']) == 0 and len(sys.argv) != 1:
            print(f'{Font.error}* Missing -i, no input file specified{Font.end}')
            error_state = True

        # Check if the user has entered more than one -i
        if len([x for x in sys.argv if x=='-i']) > 1:
            print(f'{Font.error}* Can\'t have more than one -i{Font.end}')
            error_state = True

    # Check if the user has entered more than one -o
    if len([x for x in sys.argv if x=='-o']) > 1:
        print(f'{Font.error}* Can\'t have more than one -o{Font.end}')
        error_state = True

    # Set the ouput folder name if the user hasn't specified -o
    if len([x for x in sys.argv if x=='-o']) == 0:
            output_folder_name = os.path.abspath('.')

    # Check that both -y and -z haven't been set
    if len([x for x in sys.argv if x=='-y']) > 0 and len([x for x in sys.argv if x=='-x']) > 0:
        print(f'{Font.error}* Can\'t use -y with -x, no titles are removed in a legacy parent/clone dat{Font.end}')
        error_state = True

    # Check if the user has entered -?
    if len([x for x in sys.argv if x=='-?']) > 0:
        usage()

    # Exit if there was an error in user input
    if error_state == True:
        print(f'\nUSAGE: {Font.bold}{os.path.basename(sys.argv[0])} -i {Font.end}<input dat/folder> <options>'
            f'\n\nType {Font.bold}{os.path.basename(sys.argv[0])} -?{Font.end} to see all options.')
        sys.exit()

    return UserInput(
        input_file_name,
        output_folder_name,

        no_applications,
        no_bad_dumps,
        no_compilations,
        no_demos,
        no_educational,
        no_coverdiscs,
        no_multimedia,
        no_pirate,
        no_preproduction,
        no_promotional,
        no_unlicensed,
        supersets,
        filter_languages,
        legacy,
        user_options,
        verbose,
        keep_remove,
        use_cache)


def import_user_config(region_data, user_input):
    try:
        with open('user-config.yaml', encoding='utf-8') as user_config_import:
            user_config = load(str(user_config_import.read()))
    except OSError as e:
        print(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
        raise

    for i, entry in enumerate(user_config):
        if 'language filter' in entry:
            # Convert long languages to short
            user_input.user_languages = []

            for key, value in region_data.languages_key.items():
                for language in user_config[i]['language filter'].data:
                    if language == key:
                        user_input.user_languages.append(value)

        elif 'region order' in entry:
            user_input.user_region_order = user_config[i]['region order'].data

    return user_input