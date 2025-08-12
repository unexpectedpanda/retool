from __future__ import annotations

import json
import os
import pathlib
import re
import sys
from functools import reduce
from itertools import product
from re import Pattern
from typing import Any

from strictyaml import YAML, Map, MapPattern, Seq, Str # type: ignore

from modules.input import UserInput
from modules.config.read_write_config import generate_config, read_config
from modules.stats import Stats
from modules.titletools import Regex
from modules.utils import Font, download, eprint


class Config:
    def __init__(
        self,
        clone_list_metadata_download_location: str,
        clone_list_metadata_download_location_key: str,
        program_download_location: str,
        program_download_location_key: str,
        config_file: str,
        dat_file_tags_key: str,
        ignore_tags_key: str,
        disc_rename_key: str,
        version_ignore_key: str,
        budget_editions_key: str,
        promote_editions_key: str,
        demote_editions_key: str,
        modern_editions_key: str,
        languages_key: str,
        region_order_key: str,
        video_order_key: str,
        clone_lists_key: str,
        metadata_key: str,
        mias_key: str,
        ra_key: str,
        user_config_key: str,
        user_language_order_key: str,
        user_region_order_key: str,
        user_localization_order_key: str,
        user_video_order_key: str,
        user_list_prefix_key: str,
        user_list_suffix_key: str,
        user_override_exclude_key: str,
        user_override_include_key: str,
        user_filter_key: str,
        user_gui_settings_key: str,
        system_settings_path: str,
        sanitized_characters: tuple[str, ...],
        reserved_filenames: tuple[str, ...],
        user_input: Any,
        first_run_gui: bool = False,
    ) -> None:
        """
        Creates an object that contains internal and user config data. Interactively
        browsable if you `print()` the object.

        Args:
            clone_list_metadata_download_location (str): A URL that points to a folder
                containing clone lists and metadata files, so local copies can be updated.
                Only used if `internal-config.json` is missing.

            clone_list_metadata_download_location_key (str): The key in
                `internal-config.json` that contains the URL that hosts clone lists and
                metadata files, so local copies can be updated.

            program_download_location (str): A URL that points to where the Retool program
                can be downloaded. Not used, but if it was, it would only be used if
                `internal-config.json` was missing.

            program_download_location_key (str): The key in `internal-config.json` that
                contains the URL that hosts the Retool program. Not used.

            config_file (str): The location of `internal-config.json`.

            dat_file_tags_key (str): The key to look up in `internal-config.json` that
                contains tags that should be ignored so DAT filenames can be matched to
                clone lists.

            ignore_tags_key (str): The key to look up in `internal-config.json` that
                contains tags that should be ignored so like titles can be grouped
                together.

            disc_rename_key (str): The key in `internal-config.json` that specifies how
                multiple '(Disc)' tags should be renamed so they can be normalized and
                compared.

            version_ignore_key (str): The key in `internal-config.json` that specifies a
               list of titles that should be ignored when using regex to try and isolate
               title versions.

            budget_editions_key (str): The key in `internal-config.json` that specifies
                which tags indicate a budget title that should be promoted over a
                non-budget title.

            promote_editions_key (str): The key in `internal-config.json` that specifies
                which tags indicate a title should be promoted over another.

            demote_editions_key (str): The key in `internal-config.json` that specifies
                which tags indicate a title should be demoted below another.

            modern_editions_key (str): The key in `internal-config.json` that specifies
                which tags indicate a title is ripped from a modern release of a game,
                like those from Virtual Console.

            languages_key (str): The key in `internal-config.json` that specifies the
                available languages and their associated language codes.

            region_order_key (str): The key in `internal-config.json` that specifies the
                default region order and the implied language for each region.

            video_order_key (str): The key in `internal-config.json` that specifies the
                default order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and
                SECAM.

            clone_lists_key (str): The key in `internal-config.json` that specifies where
                the local clone lists are located.

            metadata_key (str): The key in `internal-config.json` that specifies where the
                local metadata files are located.

            mias_key (str): The key in `internal-config.json` that specifies where the
                local MIA files are located.

            ra_key (str): The key in `internal-config.json` that specifies where the local
                RetroAchievements files are located.

            user_config_key (str): The key in `internal-config.json` that specifies where
                `user-config.yaml` is located.

            user_language_order_key (str): The key in `user-config.yaml` that specifies
                the language order as defined by the user.

            user_region_order_key (str): The key in `user-config.yaml` that specifies the
                region order as defined by the user.

            user_localization_order_key (str): The key in `user-config.yaml` that
                specifies localization order as defined by the user.

            user_video_order_key (str): The key in `user-config.yaml` that specifies the
                order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM as
                defined by the user.

            user_list_prefix_key (str): The key in `user-config.yaml` that specifies the
                prefix used when the user specifies `--listnames`.

            user_list_suffix_key (str): The key in `user-config.yaml` that specifies the
                suffix used when the user specifies `--listnames`.

            user_override_exclude_key (str): The key in `user-config.yaml` that specifies
                the override excludes.

            user_override_include_key (str): The key in `user-config.yaml` that specifies
                the override includes.

            user_filter_key (str): The key in `user-config.yaml` that specifies the post
                filters.

            user_gui_settings_key (str): They key in `user-config.yaml` that specifies
                settings used by the GUI.

            system_settings_path (str): The location of the system config files.

            sanitized_characters (tuple[str, ...]): Characters that can't be used in
                filenames.

            reserved_filenames (tuple[str, ...]): Filenames that can't be used in certain
                operating systems.

            user_input (Any): In the CLI version, all the arguments passed in by the user.
                In the GUI version, constructed from UI elements the user has enabled or
                interacted with.

            first_run_gui (bool, optional): When using the GUI, is set to `True` to
                prevent Retool from prompting the user through the CLI to generate
                `user-config.yaml`, as this happens automatically through GUI use anyway.
                Defaults to `False`.
        """
        # Store the Retool version
        self.retool_location: pathlib.Path = pathlib.Path(sys.argv[0]).resolve().parent

        # Determine if STDOUT is being redirected or not
        self.stdout = False

        if not sys.stdout.isatty():
            self.stdout = True

        # Create the stats object
        self.stats = Stats()

        # Download the internal config file if it's missing
        def download_required_files(download_files: tuple[str, ...]) -> None:
            """
            Downloads the files Retool requires to operate.

            Args:
                download_files (tuple[str]): A tuple of the files to download.
            """
            required_files: str = ''.join(
                [f'\n• {Font.b}{x}{Font.warning}' for x in download_files]
            )
            download_config: str = ''
            missing_file: bool = False

            for download_file in download_files:
                if not pathlib.Path(self.retool_location).joinpath(download_file).is_file():
                    missing_file = True

            if missing_file:
                while not download_config or not (download_config == 'y' or download_config == 'n'):
                    eprint(
                        f'{Font.warning_bold}Warning:{Font.warning} One or more '
                        'of the following files are missing, which Retool needs '
                        'to operate:',
                        level='warning',
                        indent=0,
                    )
                    eprint(f'{required_files}', level='warning', wrap=False)

                    eprint('\nWould you like to download them? (y/n) > ', level='warning')

                    download_config = input()

                if download_config.lower() == 'y':
                    eprint('')
                    for download_file in download_files:
                        eprint(
                            f'• Downloading {Font.b}{download_file}{Font.be}... ',
                            sep=' ',
                            end='',
                            flush=True,
                        )
                        failed = download(
                            (
                                f'{clone_list_metadata_download_location}/{download_file}',
                                str(pathlib.Path(self.retool_location).joinpath(download_file)),
                            ),
                            False,
                        )

                        if not failed:
                            eprint('done.')

                    eprint('\n')
                else:
                    eprint('\nExiting...\n')
                    sys.exit(1)

                # Check that the files are there now for Retool to start
                download_required_files(download_files)

        download_required_files((config_file,))

        # Make sure the config file is relative to wherever Retool is located
        self.config_file = pathlib.Path(self.retool_location).joinpath(config_file)

        # Initialize variables
        self.clone_list_metadata_download_location: str = clone_list_metadata_download_location
        self.program_download_location: str = program_download_location
        self.cpu_count: int = os.cpu_count() if os.cpu_count() is not None else 1  # type: ignore
        self.dat_file_tags: list[str]
        self.languages: dict[str, str] = {}
        self.languages_implied: dict[str, tuple[str, ...]] = {}
        self.languages_filter: dict[str, list[str]] = {}
        self.region_order_default: list[str] = []
        self.video_order_default: list[str] = []
        self.tags_ignore: list[str] = []
        self.tags_disc_rename: dict[str, str] = {}
        self.tags_promote_editions: tuple[list[Pattern[str]]]
        self.tags_demote_editions: tuple[list[Pattern[str]]]
        self.tags_budget_editions: tuple[list[Pattern[str]]]
        self.tags_modern_editions: tuple[list[Pattern[str]]]
        self.user_config_file: str = ''
        self.version_ignore: dict[str, str] = {}

        # Import the contents of the internal config file
        try:
            with open(self.config_file, encoding='utf-8') as input_file:
                config_file_content: dict[str, Any] = json.load(input_file)

                def import_key(
                    config_file_content: dict[str, Any],
                    key_name: str,
                    dict_key_name: str,
                    iter_type: str = '',
                    tags_ignore: bool = False,
                ) -> None:
                    """
                    Takes the data from a specific key in `internal-config.json`, then
                    assigns it to a self.attribute.

                    Args:
                        config_file_content (dict[str, Any]): The read in contents of the
                            `internal-config.json` file, in dictionary format.

                        key_name (str): The key to find in `internal-config.json`.

                        dict_key_name (str): The attribute to assign to the Retool config
                            object.

                        iter_type (str, optional): Whether the resulting attribute value
                            should be a `list`, `tuple`, or neither. Defaults to `''`.

                        tags_ignore (bool, optional): Whether the values in the attribute
                            should be added to Retool's ignored tags list. Defaults to
                            `False`.
                    """
                    if key_name in config_file_content:
                        if iter_type == 'tuple':
                            setattr(self, dict_key_name, tuple(config_file_content[key_name]))
                        elif iter_type == 'list':
                            setattr(self, dict_key_name, list(config_file_content[key_name]))
                        else:
                            setattr(self, dict_key_name, config_file_content[key_name])

                        if tags_ignore and iter_type != 'list':
                            list(map(self.tags_ignore.append, config_file_content[key_name]))

                import_key(config_file_content, languages_key, 'languages')
                import_key(config_file_content, disc_rename_key, 'tags_disc_rename')
                import_key(config_file_content, version_ignore_key, 'version_ignore')
                import_key(
                    config_file_content,
                    dat_file_tags_key,
                    'dat_file_tags',
                    'list',
                    tags_ignore=False,
                )
                import_key(
                    config_file_content, ignore_tags_key, 'tags_ignore', 'list', tags_ignore=True
                )
                import_key(
                    config_file_content,
                    budget_editions_key,
                    'tags_budget_editions',
                    'tuple',
                    tags_ignore=True,
                )
                import_key(
                    config_file_content,
                    promote_editions_key,
                    'tags_promote_editions',
                    'tuple',
                    tags_ignore=True,
                )
                import_key(
                    config_file_content,
                    demote_editions_key,
                    'tags_demote_editions',
                    'tuple',
                    tags_ignore=True,
                )
                import_key(
                    config_file_content,
                    modern_editions_key,
                    'tags_modern_editions',
                    'tuple',
                    tags_ignore=True,
                )
                import_key(config_file_content, user_config_key, 'user_config_file')

                # Get the minimum version of Retool required to take the most advantage of
                # the available internal-config.json file.

                self.minimum_version: str = ''

                if 'description' in config_file_content:
                    if 'minimumVersion' in config_file_content['description']:
                        self.minimum_version = config_file_content['description']['minimumVersion']

                if clone_list_metadata_download_location_key in config_file_content:
                    self.clone_list_metadata_download_location = config_file_content[
                        clone_list_metadata_download_location_key
                    ]

                if program_download_location_key in config_file_content:
                    self.program_download_location = config_file_content[
                        program_download_location_key
                    ]

                if region_order_key in config_file_content:
                    self.region_order_default = list(config_file_content[region_order_key])

                    # Set up the implied languages
                    for key, values in config_file_content[region_order_key].items():
                        language_filter_list: list[str] = []

                        if values['impliedLanguage']:
                            if values['impliedLanguage'] in self.languages:
                                language_filter_list.append(
                                    self.languages[values['impliedLanguage']]
                                )
                                self.languages_implied[key] = (
                                    re.sub(
                                        '[^-\\w].*', '', self.languages[values['impliedLanguage']]
                                    ),
                                )

                        self.languages_filter[key] = language_filter_list

                if video_order_key in config_file_content:
                    self.video_order_default = config_file_content[video_order_key]

                # Set up the default clone list, metadata, and MIA paths
                if 'localDir' in config_file_content[clone_lists_key]:
                    self.path_clone_list = pathlib.Path(self.retool_location).joinpath(
                        config_file_content[clone_lists_key]['localDir']
                    )

                if 'localDir' in config_file_content[metadata_key]:
                    self.path_metadata = pathlib.Path(self.retool_location).joinpath(
                        config_file_content[metadata_key]['localDir']
                    )

                if 'localDir' in config_file_content[mias_key]:
                    self.path_mia = pathlib.Path(self.retool_location).joinpath(
                        config_file_content[mias_key]['localDir']
                    )

                if 'localDir' in config_file_content[ra_key]:
                    self.path_ra = pathlib.Path(self.retool_location).joinpath(
                        config_file_content[ra_key]['localDir']
                    )

                self.path_quick_import: str = ''

                # Check for missing keys in internal-config.json
                def key_missing(section_key: str) -> None:
                    """
                    Generates a warning if a specific key is missing from
                    `internal-config.json`.

                    Args:
                        section_key (str): The section to check for in
                            `internal-config.json`.
                    """
                    if section_key not in config_file_content:
                        eprint(
                            f'• The {Font.b}{section_key}{Font.be} key is missing from '
                            f'{Font.b}{config_file}{Font.be}. Clone matching won\'t be accurate.',
                            level='warning',
                        )

                config_keys = [
                    languages_key,
                    region_order_key,
                    dat_file_tags_key,
                    ignore_tags_key,
                    disc_rename_key,
                    version_ignore_key,
                    budget_editions_key,
                    promote_editions_key,
                    demote_editions_key,
                    modern_editions_key,
                ]

                for s in config_keys:
                    key_missing(s)

        except OSError as e:
            eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
            raise

        # Generate the language lists.
        #
        # No-Intro uses a + sign for 2- and 3-in-1 compilations in their GBA DAT
        # to delineate languages between the first and subsequent titles. For
        # example: (En+En,Fr,De). We need to take this into account when
        # detecting languages in titles. Here we use a Cartesian product of all
        # languages to find these combinations. Thankfully there's only one
        # triple language title so far, so we manually add (En+En+En) instead of
        # searching for all triple language combinations and slowing things
        # down.

        no_intro_languages: list[str] = list(self.languages.values())
        compilation_languages: list[str] = []

        for language_combo in product(no_intro_languages, repeat=2):
            compilation_languages.append('\\+'.join(language_combo))

        no_intro_languages.extend(compilation_languages)
        no_intro_languages.append('En\\+En\\+En')

        LANGUAGES = '|'.join(no_intro_languages)

        # Build out required regular expressions
        self.regex = Regex(LANGUAGES)

        # Generate required files if they're missing
        if user_input.user_config:
            user_config_file = user_input.user_config
        else:
            user_config_file = self.user_config_file

        self.user_config_file = str(pathlib.Path(self.retool_location).joinpath(user_config_file))
        self.system_settings_path = str(
            pathlib.Path(self.retool_location).joinpath(system_settings_path)
        )

        generate_config(
            self.user_config_file,
            languages=tuple(self.languages),
            regions=tuple(self.region_order_default),
            localizations=(),
            video_standards=tuple(self.video_order_default),
            system_config_path=self.system_settings_path,
            first_run_gui=first_run_gui,
        )

        # Import the user config file
        self.region_order_languages_user: list[str] = []
        self.language_order_user: list[str] = []
        self.languages_user_found: bool = False
        self.localization_order_user: list[str] = []
        self.region_order_user: list[str] = []
        self.video_order_user: list[str] = []
        self.user_prefix: str = ''
        self.user_suffix: str = ''
        self.user_gui_settings: tuple[Any, ...] = ()

        schema = Map(
            {
                'config version': Str(),
                user_language_order_key: Seq(Str()) | Str(),
                user_region_order_key: Seq(Str()) | Str(),
                user_localization_order_key: Seq(Str()) | Str(),
                user_video_order_key: Seq(Str()) | Str(),
                user_list_prefix_key: Seq(Str()) | Str(),
                user_list_suffix_key: Seq(Str()) | Str(),
                user_override_exclude_key: Seq(Str()) | Str(),
                user_override_include_key: Seq(Str()) | Str(),
                user_filter_key: Seq(Str()) | Str(),
                user_gui_settings_key: Seq(Str() | MapPattern(Str(), Str())) | Str(),
            }
        )

        user_config: YAML = read_config(schema, self.user_config_file, self)

        self.language_order_user = list(user_config.data[user_language_order_key])
        self.region_order_user = list(user_config.data[user_region_order_key])
        self.localization_order_user = list(user_config.data[user_localization_order_key])
        self.video_order_user = list(user_config.data[user_video_order_key])
        self.user_prefix = ''.join(user_config.data[user_list_prefix_key])
        self.user_suffix = ''.join(user_config.data[user_list_suffix_key])

        if user_config.data[user_gui_settings_key]:
            self.user_gui_settings = user_config.data[user_gui_settings_key]

        # Get the language order as determined by user regions and user languages, change
        # the user languages list to be regex strings instead of language names
        for region in self.region_order_user:
            self.region_order_languages_user.extend(self.languages_filter[region])

        # Make sure language entries are unique
        self.region_order_languages_user = reduce(
            lambda x, y: [*x, y] if y not in x else x, self.region_order_languages_user, []
        )

        language_list: list[str] = []

        if not self.language_order_user:
            language_list = self.region_order_languages_user
        else:
            self.languages_user_found = True

            for language in self.language_order_user:
                if language in self.languages:
                    language_list.append(self.languages[language])

        self.language_order_user = language_list

        # Change the user localization list to be regex strings instead of language names
        localization_list: list[str] = []

        for language in self.localization_order_user:
            if language in self.languages:
                localization_list.append(self.languages[language])

        self.localization_order_user = localization_list

        # Compensate for No-Intro using "United Kingdom", and Redump using "UK"
        if 'UK' in self.region_order_user:
            uk_index: int = self.region_order_user.index('UK')
            self.region_order_user[uk_index + 1 : uk_index + 1] = ['United Kingdom']

        uk_index = self.region_order_default.index('UK')
        self.region_order_default[uk_index + 1 : uk_index + 1] = ['United Kingdom']

        # Add "Export" to the default region order regex as a pseudo-region, which is reinterpreted as "World" later
        self.regex.region_order_default = re.compile(
            '\\((?:\\w*,\\s)*(?:'
            + '|'.join([*self.region_order_default, 'Export'])
            + ')(?:,\\s\\w*)*\\)'
        )

        if 'UK' in self.languages_implied:
            self.languages_implied['United Kingdom'] = self.languages_implied['UK']
            self.languages_filter['United Kingdom'] = self.languages_filter['UK']

        # Import global overrides
        self.global_exclude: list[str] = user_config.data[user_override_exclude_key]
        self.global_include: list[str] = user_config.data[user_override_include_key]

        # Import global post filters
        self.global_filter: list[str] = user_config.data[user_filter_key]

        # Populate system settings later when the DAT file has been loaded
        self.system_clone_list: str = ''
        self.system_metadata_file: str = ''
        self.system_mia_file: str = ''
        self.system_ra_file: str = ''
        self.system_name: str = ''
        self.system_output: str = ''
        self.system_languages_user_found: bool = False
        self.system_language_order_user: list[str | dict[str, str]] = []
        self.system_localization_order_user: list[str | dict[str, str]] = []
        self.system_region_order_user: list[str | dict[str, str]] = []
        self.system_video_order_user: list[str | dict[str, str]] = []
        self.system_exclude: list[str] = []
        self.system_include: list[str] = []
        self.system_filter: list[str | dict[str, str]] = []
        self.system_user_prefix: str = ''
        self.system_user_suffix: str = ''
        self.system_user_path_settings: tuple[Any, ...] = ()
        self.system_exclusions_options: tuple[Any, ...] = ()

        # Store invalid input
        self.sanitized_characters: tuple[str, ...] = sanitized_characters
        self.reserved_filenames: tuple[str, ...] = reserved_filenames

        # Store the user input object
        self.user_input: Any = user_input

    def __str__(self) -> str:
        from modules.utils import format_value

        return_attributes: list[list[str]] = []

        for attribute in dir(self):
            if not attribute.startswith('__'):
                if len(str(getattr(self, attribute))) > 80:
                    return_attributes.append(
                        [
                            f'  ├ .{attribute}:',
                            f'(...) {format_value(str(type(getattr(self, attribute)).__name__))}',
                        ]
                    )
                else:
                    return_attributes.append(
                        [f'  ├ .{attribute}:', format_value(getattr(self, attribute))]
                    )

        final_item: list[str] = return_attributes[-1].copy()

        for i, s in enumerate(final_item):
            return_attributes[-1][i] = s.replace('├', '└')

        # Column alignment
        def class_output() -> None:
            eprint('\n  ○ Config object')
            col_width: int = max(len(word) for row in return_attributes for word in row) - 20
            for row in return_attributes:
                eprint(''.join(str(word).ljust(col_width) for word in row), wrap=False)

        key: str = 'blank'

        class_output()

        while key != 'q':
            eprint(
                '\nEnter a dictionary key to expand (e.g. tags_disc_rename), q to continue, or hit enter to list: ',
                indent=0,
            )
            key = input()

            if hasattr(self, key):
                if isinstance(getattr(self, key), Regex | UserInput):
                    eprint(f'\n{vars(getattr(self, key))}', wrap=False)
                else:
                    eprint(f'\n{format_value(getattr(self, key))}', wrap=False)
            elif key == '':
                class_output()
            else:
                if key != 'q':
                    eprint(f'\nUnknown key "{key}".', wrap=False)
                else:
                    break

        return ''
