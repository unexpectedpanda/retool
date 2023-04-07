#!/usr/bin/env python

"""
Filters DATs from [Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org) to remove titles
you don't want.

https://github.com/unexpectedpanda/retool
"""

import pathlib
import sys
import time
import traceback

from modules.utils import eprint

# Require at least Python 3.10
try:
    assert sys.version_info >= (3, 10)
except:
    eprint('\nYou need Python 3.10 or higher to run Retool.')
    sys.exit()

from copy import deepcopy
from typing import Any

from modules.constants import *
from modules.chooseparent import ParentTools
from modules.clonelists import CloneListTools
from modules.dats import Dat, DatNode
from modules.config import Config
from modules.dats import process_dat
from modules.input import check_input, UserInput
from modules.output import WriteFiles
from modules.stats import get_parent_clone_stats, report_stats, Stats
from modules.titletools import IncludeExcludeTools, Removes
from modules.utils import ExitRetool, Font, old_windows, printwrap
# from modules.perftest import perf_test

__version__: str = str(f'{VERSION_MAJOR}.{VERSION_MINOR}')

def main(gui_input: UserInput|None = None) -> None:
    """ The main Retool function.

    Args:
        `gui_input` (UserInput, optional): Indicates that the main function has been
        called from Retool GUI. Defaults to `None`.
    """

    # Start a timer from when the process started
    start_time: float = time.time()

    # Enable VT100 escape sequence for Windows 10+
    if (
        not old_windows()
        and sys.platform.startswith('win')):
            from modules.utils import enable_vt_mode
            enable_vt_mode()

    # Splash screen
    retool_name: str = f'Retool {__version__}'
    eprint(f'\n\n{Font.bold}{retool_name}{Font.end}')
    eprint('-'*len(retool_name))

    if (
        len(sys.argv) == 1
        and not gui_input):
            printwrap(
                f'Filters DATs from Redump ({Font.underline}http://redump.org/{Font.end}) '
                f'and No-Intro '
                f'({Font.underline}https://www.no-intro.org/{Font.end}) to remove titles '
                'you don\'t want. A new DAT file is automatically generated, the '
                'original file isn\'t altered.',
                'no_indent')

            eprint(
                f'\nUsage: {pathlib.Path(sys.argv[0]).name} <input DAT/folder> <options>'
                '\n\nOR to download updated clone lists:'
                f'\n\n{pathlib.Path(sys.argv[0]).name} --update'
                f'\n\nType {Font.bold}{pathlib.Path(sys.argv[0]).name} -h{Font.end} for all '
                'options\n')
            if gui_input:
                raise ExitRetool
            else:
                sys.exit()

    # Get user input
    if not gui_input:
        user_input: Any = check_input()
    else:
        user_input = gui_input

    # Create the config object
    config: Config = Config(
                    CLONE_LIST_METADATA_DOWNLOAD_LOCATION,
                    CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY,
                    PROGRAM_DOWNLOAD_LOCATION,
                    PROGRAM_DOWNLOAD_LOCATION_KEY,
                    CONFIG_FILE,
                    IGNORE_TAGS_KEY,
                    DISC_RENAME_KEY,
                    PROMOTE_EDITIONS_KEY,
                    DEMOTE_EDITIONS_KEY,
                    MODERN_EDITIONS_KEY,
                    LANGUAGES_KEY,
                    REGION_ORDER_KEY,
                    VIDEO_ORDER_KEY,
                    CLONE_LISTS_KEY,
                    METADATA_KEY,
                    USER_CONFIG_KEY,
                    USER_LANGUAGE_ORDER_KEY,
                    USER_REGION_ORDER_KEY,
                    USER_VIDEO_ORDER_KEY,
                    USER_LIST_PREFIX_KEY,
                    USER_LIST_SUFFIX_KEY,
                    USER_GUI_SETTINGS_KEY,
                    USER_FILTERS_PATH,
                    SANITIZED_CHARACTERS,
                    RESERVED_FILENAMES,
                    VERSION_MAJOR,
                    VERSION_MINOR,
                    user_input)

    # Run an update if requested, or if folders are missing
    if config.user_input.update:
        CloneListTools.update_clonelists_metadata(config, gui_input)

    if not (
        pathlib.Path(config.path_clone_list).is_dir()
        and pathlib.Path(config.path_metadata).is_dir()):
            download_updates: str = ''

            while not (
                download_updates == 'y'
                or download_updates == 'n'
            ):
                printwrap(
                    f'{Font.warning_bold}Warning:{Font.warning} Clone lists or metadata '
                    'files are missing, Retool is more accurate with them. Do you want '
                    f'to download them? (y/n) > {Font.end}', 'no_indent')

                download_updates = input()

            if download_updates.lower() == 'y':
                CloneListTools.update_clonelists_metadata(config, gui_input, no_exit=True)

    # Get the input file or folder
    input_type: str
    dat_files: tuple[str, ...]

    if pathlib.Path(config.user_input.input_file_name).is_dir():
        dat_files = tuple([str(x) for x in pathlib.Path(config.user_input.input_file_name).glob('*.dat')])
        input_type = 'folder'
        eprint('Processing folder...')
    elif '*' in str(config.user_input.input_file_name):
        dat_files = tuple([str(x) for x in pathlib.Path(config.user_input.input_file_name).parent.glob(pathlib.Path(config.user_input.input_file_name).name)])
        input_type = 'wildcard'
    else:
        dat_files = tuple([str(pathlib.Path(config.user_input.input_file_name).resolve())])
        input_type = 'file'

    # Verify that file/folder the user specified exists
    if input_type != 'wildcard':
        if not pathlib.Path(config.user_input.input_file_name).is_file() and not pathlib.Path(config.user_input.input_file_name).is_dir():
            eprint(
                f'\n{Font.warning}Can\'t find the specified input DAT or folder '
                f'{Font.warning_bold}"{config.user_input.input_file_name}".{Font.end}\n')
            if gui_input:
                raise ExitRetool
            else:
                sys.exit()

    dat_file_count: int = len(dat_files)

    # Process the DAT file/s
    if dat_file_count >= 1:
        removes: Removes = Removes()

        for i, dat_file in enumerate(dat_files):
            if dat_file_count > 1:
                eprint(f'\n{Font.underline}Processing file {i+1}/{len(dat_files)}{Font.end}\n')

            input_dat: Dat = process_dat(dat_file, input_type, gui_input, config)

            if not input_dat.end:
                processed_titles: dict[str, set[DatNode]] = deepcopy(input_dat.contents_dict)

                # Record the original title count in the DAT
                config.stats.original_count = len([val for lst in processed_titles.values() for val in lst])

                # Process the clone lists
                if not config.user_input.no_1g1r:
                    processed_titles = CloneListTools.mias(processed_titles, config, input_dat)
                    processed_titles = CloneListTools.removes(processed_titles, config, input_dat, removes)
                    processed_titles = CloneListTools.categories(processed_titles, config, input_dat)
                    processed_titles = CloneListTools.overrides(processed_titles, config, input_dat)
                    processed_titles = CloneListTools.variants(processed_titles, config, input_dat, is_includes=False)

                # Process user excludes
                processed_titles = IncludeExcludeTools.excludes(processed_titles, config, removes)

                # Filter languages
                if config.user_input.filter_languages:
                    processed_titles = IncludeExcludeTools.filter_languages(processed_titles, config, removes)

                # Filter regions
                processed_titles = IncludeExcludeTools.filter_regions(processed_titles, config, removes)

                # Select a parent
                if not config.user_input.no_1g1r:
                    processed_titles = ParentTools.choose_parent(processed_titles, config)

                # Detect parent/clone clashes
                processed_titles = ParentTools.detect_parent_clone_clash(processed_titles, config)

                # Process user includes
                if not config.user_input.no_filters:
                    if config.global_include or config.system_include:
                        original_titles_with_clonelist: dict[str, set[DatNode]] = CloneListTools.variants(input_dat.contents_dict, config, input_dat, is_includes=True)
                        processed_titles = IncludeExcludeTools.includes(processed_titles, input_dat.contents_dict, original_titles_with_clonelist, config, removes)

                if not config.user_input.trace:
                    # Grab the parent/clone stats, but also get the return of parent/clone relationships
                    # in case the user has set --log
                    log: tuple[dict[str, set[str]], set[DatNode]] = get_parent_clone_stats(processed_titles, config)

                    # Write the final results to file/s
                    if config.stats.final_count != 0:
                        WriteFiles.output(processed_titles, log, config, input_dat, removes)

                        # Report the stats, and reset them for when Retool is processing a directory of DATs
                        report_stats(config)
                        stats_final_count: int = config.stats.final_count
                        config.stats = Stats()
                    else:
                        printwrap(f'{Font.warning}* No titles in the input DAT match your preferences. No DAT file has been created.{Font.end}', 'error')
                        if input_type == 'file':
                            if gui_input:
                                raise ExitRetool
                            else:
                                sys.exit()
                else:
                    eprint('* Trace complete.')

                # Clear some memory
                input_dat.contents_dict.clear()
            else:
                continue

        if not config.user_input.trace:
            # Stop the timer
            stop_time = time.time()
            total_time_elapsed = str('{0:.2f}'.format(round(stop_time - start_time, 2)))

            # Print the success message
            eprint('')

            if dat_file_count == 1:
                if (
                    config.user_input.output_region_split
                    or config.user_input.output_remove_dat):
                        printwrap(
                        f'{Font.success}* Finished processing '
                        f'"{Font.bold}{pathlib.Path(user_input.input_file_name).resolve()}{Font.success}"'
                        f'in {total_time_elapsed}s. DATs have been created in the '
                        f'{Font.bold}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.success} folder.{Font.end}'
                        )
                else:
                    printwrap(
                        f'{Font.success}* Finished adding '
                        f'{str("{:,}".format(stats_final_count))} '
                        f'titles to "{Font.bold}{pathlib.Path(input_dat.output_filename).resolve()}" '
                        f'{Font.success}in {total_time_elapsed}s.{Font.end}'
                    )
            elif dat_file_count > 1 and input_type == 'folder':
                printwrap(
                    f'{Font.success}* Finished processing {dat_file_count} files in the '
                    f'{Font.bold}"{pathlib.Path(user_input.input_file_name).resolve()}{Font.success}" folder in '
                    f'{total_time_elapsed}s. DATs have been created in the '
                    f'{Font.bold}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.success} folder.{Font.end}'
                    )
            elif dat_file_count > 1 and input_type == 'wildcard':
                printwrap(
                    f'{Font.success}* Finished processing {dat_file_count} files in the '
                    f'{Font.bold}"{pathlib.Path(pathlib.Path(user_input.input_file_name).parent).resolve()}{Font.success}" folder in '
                    f'{total_time_elapsed}s. DATs have been created in the '
                    f'{Font.bold}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.success} folder.{Font.end}'
                    )

    else:
        eprint(f'\n{Font.warning}No DAT files found. Exiting...{Font.end}\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        eprint(f'{Font.error_bold}\n\n* Unexpected error:\n\n{Font.end}')
        traceback.print_exc()
        input(f'{Font.error_bold}\n\nPress any key to quit Retool{Font.end}')