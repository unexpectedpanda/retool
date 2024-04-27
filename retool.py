#!/usr/bin/env python

"""
Filters DAT files from [Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org) to remove titles
you don't want.

https://github.com/unexpectedpanda/retool
"""

import pathlib
import sys
import time
import traceback

import modules.constants as const
from modules.utils import eprint

# Require at least Python 3.10
try:
    assert sys.version_info >= (3, 10)
except Exception:
    eprint('You need Python 3.10 or higher to run Retool.', level='error')
    sys.exit()

from copy import deepcopy
from typing import Any

from modules.clone_lists.mias import clone_list_mias
from modules.clone_lists.variants_orchestrator import clone_list_variants_orchestrator
from modules.config import Config
from modules.dats import Dat, DatNode, process_dat
from modules.input import UserInput, check_input
from modules.output import WriteFiles
from modules.stats import Stats, get_parent_clone_stats, report_stats
from modules.title_selection.choose_1g1r_orchestrator import choose_1g1r_orchestrator
from modules.title_selection.excludes import excludes
from modules.title_selection.filter_languages import filter_languages
from modules.title_selection.filter_regions import filter_regions
from modules.title_selection.includes import includes
from modules.title_selection.overrides_post_filters import post_filters
from modules.title_selection.resolve_parent_clone_clash import resolve_parent_clone_clash
from modules.titletools import Removes
from modules.update_clone_list_metadata import update_clonelists_metadata
from modules.utils import ExitRetool, Font, minimum_version, old_windows

# from modules.perftest import perf_test


def main(gui_input: UserInput | None = None) -> None:
    """
    The main Retool function.

    Args:
        gui_input (UserInput, optional): Indicates that the main function has been
        called from Retool GUI. Defaults to `None`.
    """
    # Start a timer from when the process started
    start_time: float = time.time()

    # Enable VT100 escape sequence for Windows 10+
    if not old_windows() and sys.platform.startswith('win'):
        from modules.utils import enable_vt_mode

        enable_vt_mode()

    # Splash screen
    retool_name: str = f'Retool {const.__version__}'
    eprint(f'\n\n{Font.b}{retool_name}{Font.be}')
    eprint('─' * len(retool_name))

    if len(sys.argv) == 1 and not gui_input:
        eprint(
            f'Filters DAT files from Redump ({Font.u}http://redump.org/{Font.ue}) and'
            f'No-Intro ({Font.u}https://www.no-intro.org/{Font.ue}) to remove titles '
            'you don\'t want. A new DAT file is automatically generated, the original'
            'file isn\'t altered.',
            indent=0,
        )

        eprint(
            f'\nUsage: {pathlib.Path(sys.argv[0]).name} <input DAT/folder> <options>'
            '\n\nOR to download updated clone lists:'
            f'\n\n{pathlib.Path(sys.argv[0]).name} --update'
            f'\n\nType {Font.b}{pathlib.Path(sys.argv[0]).name} -h{Font.be} for all '
            'options\n',
            indent=0,
            wrap=False,
        )
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
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION,
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY,
        const.PROGRAM_DOWNLOAD_LOCATION,
        const.PROGRAM_DOWNLOAD_LOCATION_KEY,
        const.CONFIG_FILE,
        const.DAT_FILE_TAGS_KEY,
        const.IGNORE_TAGS_KEY,
        const.DISC_RENAME_KEY,
        const.BUDGET_EDITIONS_KEY,
        const.PROMOTE_EDITIONS_KEY,
        const.DEMOTE_EDITIONS_KEY,
        const.MODERN_EDITIONS_KEY,
        const.LANGUAGES_KEY,
        const.REGION_ORDER_KEY,
        const.VIDEO_ORDER_KEY,
        const.CLONE_LISTS_KEY,
        const.METADATA_KEY,
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
        user_input,
    )

    # Check the minimum version required for internal-config.json
    if 'description' in config.config_file_content:
        if 'minimumVersion' in config.config_file_content['description']:
            min_version = config.config_file_content['description']['minimumVersion']
            minimum_version(min_version, const.CONFIG_FILE, gui_input)

    # Run an update if requested, or if folders are missing
    if config.user_input.update:
        update_clonelists_metadata(config, gui_input)

    if not (
        pathlib.Path(config.path_clone_list).is_dir()
        and pathlib.Path(config.path_metadata).is_dir()
    ):
        download_updates: str = ''

        while not (download_updates == 'y' or download_updates == 'n'):
            eprint(
                f'{Font.b}Warning:{Font.be} Clone lists or metadata '
                'files are missing, Retool is more accurate with them. Do you want '
                f'to download them? (y/n) >',
                level='warning',
                indent=0,
            )

            download_updates = input()

        if download_updates.lower() == 'y':
            update_clonelists_metadata(config, gui_input, no_exit=True)

    # Get the input file or folder
    input_type: str
    dat_files: tuple[str, ...]

    if pathlib.Path(config.user_input.input_file_name).is_dir():
        dat_files = tuple(
            [str(x) for x in pathlib.Path(config.user_input.input_file_name).glob('*.dat')]
        )
        input_type = 'folder'
        eprint('• Processing folder...')
    elif '*' in str(config.user_input.input_file_name):
        dat_files = tuple(
            [
                str(x)
                for x in pathlib.Path(config.user_input.input_file_name).parent.glob(
                    pathlib.Path(config.user_input.input_file_name).name
                )
            ]
        )
        input_type = 'wildcard'
    else:
        dat_files = (str(pathlib.Path(config.user_input.input_file_name).resolve()),)
        input_type = 'file'

    # Verify that file/folder the user specified exists
    if input_type != 'wildcard':
        if (
            not pathlib.Path(config.user_input.input_file_name).is_file()
            and not pathlib.Path(config.user_input.input_file_name).is_dir()
        ):
            eprint(
                f'Can\'t find the specified input DAT or folder '
                f'{Font.b}"{config.user_input.input_file_name}".{Font.be}',
                level='warning',
                indent=0,
            )
            if gui_input:
                raise ExitRetool
            else:
                sys.exit()

    dat_file_count: int = len(dat_files)

    # Process the DAT file/s
    if dat_file_count >= 1:
        removes: Removes = Removes()
        stats_final_count: int = 0

        for i, dat_file in enumerate(dat_files):
            if dat_file_count > 1:
                eprint(f'\n{Font.u}Processing file {i+1}/{len(dat_files)}{Font.ue}\n')

            input_dat: Dat = process_dat(dat_file, input_type, gui_input, config)

            if not input_dat.end:
                processed_titles: dict[str, set[DatNode]] = deepcopy(input_dat.contents_dict)

                # Record the original title count in the DAT
                config.stats.original_count = (
                    len([val for lst in processed_titles.values() for val in lst])
                    + config.stats.duplicate_titles_count
                )

                # Process the clone lists
                if not config.user_input.no_1g1r:
                    if not config.user_input.no_label_mia:
                        processed_titles = clone_list_mias(processed_titles, config, input_dat)

                    processed_titles = clone_list_variants_orchestrator(
                        processed_titles, config, input_dat, removes, is_includes=False
                    )

                # Process user excludes
                processed_titles = excludes(processed_titles, config, removes)

                # Filter languages
                if config.user_input.filter_languages:
                    processed_titles = filter_languages(processed_titles, config, removes)

                # Filter regions
                processed_titles = filter_regions(processed_titles, config, removes)

                # Select a parent
                if not config.user_input.no_1g1r:
                    processed_titles = choose_1g1r_orchestrator(processed_titles, config)

                # Detect parent/clone clashes
                processed_titles = resolve_parent_clone_clash(processed_titles, config)

                # Process user includes
                if not config.user_input.no_overrides:
                    if config.global_include or config.system_include:
                        original_titles_with_clonelist: dict[str, set[DatNode]] = (
                            clone_list_variants_orchestrator(
                                input_dat.contents_dict,
                                config,
                                input_dat,
                                removes,
                                is_includes=True,
                            )
                        )
                        processed_titles = includes(
                            processed_titles,
                            input_dat.contents_dict,
                            original_titles_with_clonelist,
                            config,
                            removes,
                        )

                # Process post filters
                if config.global_filter or config.system_filter:
                    processed_titles = post_filters(processed_titles, config, removes)

                if not config.user_input.trace:
                    # Grab the parent/clone stats, but also get the return of parent/clone relationships
                    # in case the user has set --log
                    log: tuple[dict[str, set[str]], set[DatNode]] = get_parent_clone_stats(
                        processed_titles, config
                    )

                    # Write the final results to file/s
                    if config.stats.final_count != 0:
                        WriteFiles.output(
                            processed_titles, log, config, input_dat, removes, dat_file
                        )

                        if config.user_input.replace and config.user_input.output_region_split:
                            pathlib.Path(dat_file).unlink()

                        # Report the stats, and reset them for when Retool is processing a directory of DATs
                        report_stats(config)
                        stats_final_count = config.stats.final_count
                        config.stats = Stats()
                    else:
                        eprint(
                            '• No titles in the input DAT match your preferences. No DAT file has been created.',
                            level='error',
                        )
                        if input_type == 'file':
                            if gui_input:
                                raise ExitRetool
                            else:
                                sys.exit()
                else:
                    eprint('• Trace complete.')

                # Clear some memory
                input_dat.contents_dict.clear()
            else:
                continue

        if not config.user_input.trace:
            # Stop the timer
            stop_time = time.time()
            total_time_elapsed = str(f'{round(stop_time - start_time, 2):.2f}')

            # Print the success message
            file_folder_details: str = ''

            if dat_file_count == 1:
                if config.user_input.output_region_split or config.user_input.output_remove_dat:
                    if config.stdout and not config.user_input.user_output_folder:
                        file_folder_details = f'{Font.end}'
                    else:
                        file_folder_details = f' DATs have been created in the {Font.b}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.be} folder.'

                    eprint(
                        f'\n• Finished processing '
                        f'"{Font.b}{pathlib.Path(user_input.input_file_name).resolve()}{Font.be}"'
                        f'in {total_time_elapsed}s.{file_folder_details}',
                        level='success',
                    )
                elif stats_final_count:
                    if config.stdout and not config.user_input.user_output_folder:
                        file_folder_details = ''
                    else:
                        file_folder_details = f' to {Font.b}{pathlib.Path(input_dat.output_filename).resolve()}"{Font.be}'

                    eprint(
                        f'\n• Finished adding '
                        f'{f"{stats_final_count:,}"!s} titles{file_folder_details} in {total_time_elapsed}s.',
                        level='success',
                    )
                elif input_type == 'folder':
                    if config.stdout and not config.user_input.user_output_folder:
                        file_folder_details = f'{Font.end}'
                    else:
                        file_folder_details = f' Any DATs that have been created are in the {Font.b}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.be} folder.'

                    eprint(
                        f'\n• Finished processing 1 file in the '
                        f'{Font.b}"{pathlib.Path(user_input.input_file_name).resolve()}{Font.be}" folder in '
                        f'{total_time_elapsed}s.{file_folder_details}',
                        level='success',
                    )
            elif dat_file_count > 1 and input_type == 'folder':
                if config.stdout and not config.user_input.user_output_folder:
                    file_folder_details = f'{Font.end}'
                else:
                    file_folder_details = f' Any DATs that have been created are in the {Font.b}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.be} folder.'

                eprint(
                    f'\n• Finished processing {dat_file_count} files in the '
                    f'{Font.b}"{pathlib.Path(user_input.input_file_name).resolve()}{Font.be}" folder in '
                    f'{total_time_elapsed}s.{file_folder_details}',
                    level='success',
                )
            elif dat_file_count > 1 and input_type == 'wildcard':
                if config.stdout and not config.user_input.user_output_folder:
                    file_folder_details = f'{Font.end}'
                else:
                    file_folder_details = f' Any DATs that have been created are in the {Font.b}"{pathlib.Path(user_input.output_folder_name).resolve()}"{Font.be} folder.'

                eprint(
                    f'\n• Finished processing {dat_file_count} files in the '
                    f'{Font.b}"{pathlib.Path(pathlib.Path(user_input.input_file_name).parent).resolve()}{Font.be}" folder in '
                    f'{total_time_elapsed}s.{file_folder_details}',
                    level='success',
                )

    else:
        eprint('No DAT files found. Exiting...', level='warning')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        eprint('\n• Unexpected error:\n\n', level='error')
        traceback.print_exc()
        input(f'{Font.error_bold}\n\nPress any key to quit Retool{Font.end}')
