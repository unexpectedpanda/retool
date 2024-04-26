from __future__ import annotations

import json
import pathlib
import re
import sys
from functools import reduce
from itertools import product
from re import Pattern
from typing import Any

from strictyaml import YAML, Map, MapPattern, Seq, Str, YAMLError, YAMLValidationError, load

from modules.input import UserInput
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
        promote_editions_key: str,
        demote_editions_key: str,
        modern_editions_key: str,
        languages_key: str,
        region_order_key: str,
        video_order_key: str,
        clone_lists_key: str,
        metadata_key: str,
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
            Only used if internal-config.json is missing.

            clone_list_metadata_download_location_key (str): The key in
            internal-config.json that contains the URL that hosts clone lists and
            metadata files, so local copies can be updated.

            program_download_location (str): A URL that points to where the Retool
            program can be downloaded. Not used, but if it was, it would only be used if
            internal-config.json was missing.

            program_download_location_key (str): The key in internal-config.json that
            contains the URL that hosts the Retool program. Not used.

            config_file (str): The location of internal-config.json.

            dat_file_tags_key (str): The key to look up in internal-config.json that
            contains tags that should be ignored so DAT filenames can be matched to
            clone lists.

            ignore_tags_key (str): The key to look up in internal-config.json that
            contains tags that should be ignored so like titles can be grouped together.

            disc_rename_key (str): The key in internal-config.json that specifies how
            multiple '(Disc)' tags should be renamed so they can be normalized and
            compared.

            promote_editions_key (str): The key in internal-config.json that specifies
            which tags indicate a title should be promoted over another.

            demote_editions_key (str): The key in internal-config.json that specifies
            which tags indicate a title should be demoted below another.

            modern_editions_key (str): The key in internal-config.json that specifies
            which tags indicate a title is ripped from a modern release of a game, like
            those from Virtual Console.

            languages_key (str): The key in internal-config.json that specifies the
            available languages and their associated language codes.

            region_order_key (str): The key in internal-config.json that specifies the
            default region order and the implied language for each region.

            video_order_key (str): The key in internal-config.json that specifies the
            default order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM.

            clone_lists_key (str): The key in internal-config.json that specifies where
            the local clone lists are located.

            metadata_key (str): The key in internal-config.json that specifies where the
            local metadata files are located.

            user_config_key (str): The key in internal-config.json that specifies where
            user-config.yaml is located.

            user_language_order_key (str): The key in user-config.yaml that specifies the
            language order as defined by the user.

            user_region_order_key (str): The key in user-config.yaml that specifies the
            region order as defined by the user.

            user_localization_order_key (str): The key in user-config.yaml that specifies
            localization order as defined by the user.

            user_video_order_key (str): The key in user-config.yaml that specifies the
            order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM as defined
            by the user.

            user_list_prefix_key (str): The key in user-config.yaml that specifies the
            prefix used when the user specifies `--listnames`.

            user_list_suffix_key (str): The key in user-config.yaml that specifies the
            suffix used when the user specifies `--listnames`.

            user_override_exclude_key (str): The key in user-config.yaml that specifies
            the override excludes.

            user_override_include_key (str): The key in user-config.yaml that specifies
            the override includes.

            user_filter_key (str): The key in user-config.yaml that specifies the post
            filters.

            user_gui_settings_key (str): They key in user-config.yaml that specifies
            settings used by the GUI.

            system_settings_path (str): The location of the system config files.

            sanitized_characters (tuple[str, ...]): Characters that can't be used in
            filenames.

            reserved_filenames (tuple[str, ...]): Filenames that can't be used in
            certain operating systems.

            user_input (Any): In the CLI version, all the arguments passed in by the user.
            In the GUI version, constructed from UI elements the user has enabled or
            interacted with.

            first_run_gui (bool, optional): When using the GUI, is set to `True` to
            prevent Retool from prompting the user through the CLI to generate
            user-config.yaml, as this happens automatically through GUI use anyway.
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
        def download_required_files(download_files: tuple[str, str]) -> None:
            """
            Downloads the files Retool requires to operate.

            Args:
                download_files (tuple[str]): A tuple of the files to download.
            """
            required_files: str = ''.join(
                [f'\n• {Font.bold}{x}{Font.warning}' for x in download_files]
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

        download_required_files((config_file, 'datafile.dtd'))

        # Make sure the config file is relative to wherever Retool is located
        self.config_file = pathlib.Path(self.retool_location).joinpath(config_file)

        # Import the contents of the internal config file
        self.clone_list_metadata_download_location: str = clone_list_metadata_download_location
        self.program_download_location: str = program_download_location
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
        self.tags_modern_editions: tuple[list[Pattern[str]]]
        self.user_config_file: str = ''

        try:
            with open(self.config_file, encoding='utf-8') as input_file:
                self.config_file_content: dict[str, Any] = json.load(input_file)
        except OSError as e:
            eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
            raise

        def import_key(
            key_name: str, dict_key_name: str, iter_type: str = '', tags_ignore: bool = False
        ) -> None:
            """
            Takes the data from a specific key in internal-config.json, then assigns
            it to a self.attribute.

            Args:
                key_name (str): The key to find in internal-config.json.

                dict_key_name (str): The attribute to assign to the Retool config object.

                iter_type (str, optional): Whether the resulting attribute value should
                be a `list`, `tuple`, or neither. Defaults to `''`.

                tags_ignore (bool, optional): Whether the values in the attribute should
                be added to Retool's ignored tags list. Defaults to `False`.
            """
            if key_name in self.config_file_content:
                if iter_type == 'tuple':
                    setattr(self, dict_key_name, tuple(self.config_file_content[key_name]))
                elif iter_type == 'list':
                    setattr(self, dict_key_name, list(self.config_file_content[key_name]))
                else:
                    setattr(self, dict_key_name, self.config_file_content[key_name])

                if tags_ignore and iter_type != 'list':
                    list(map(self.tags_ignore.append, self.config_file_content[key_name]))

        import_key(languages_key, 'languages')
        import_key(disc_rename_key, 'tags_disc_rename')
        import_key(dat_file_tags_key, 'dat_file_tags', 'list', tags_ignore=False)
        import_key(ignore_tags_key, 'tags_ignore', 'list', tags_ignore=True)
        import_key(promote_editions_key, 'tags_promote_editions', 'tuple', tags_ignore=True)
        import_key(demote_editions_key, 'tags_demote_editions', 'tuple', tags_ignore=True)
        import_key(modern_editions_key, 'tags_modern_editions', 'tuple', tags_ignore=True)
        import_key(user_config_key, 'user_config_file')

        if clone_list_metadata_download_location_key in self.config_file_content:
            self.clone_list_metadata_download_location = self.config_file_content[
                clone_list_metadata_download_location_key
            ]

        if program_download_location_key in self.config_file_content:
            self.program_download_location = self.config_file_content[program_download_location_key]

        if region_order_key in self.config_file_content:
            self.region_order_default = list(self.config_file_content[region_order_key])

            # Set up the implied languages
            for key, values in self.config_file_content[region_order_key].items():
                language_filter_list: list[str] = []

                if values['impliedLanguage']:
                    if values['impliedLanguage'] in self.languages:
                        language_filter_list.append(self.languages[values['impliedLanguage']])
                        self.languages_implied[key] = (
                            re.sub('[^-\\w].*', '', self.languages[values['impliedLanguage']]),
                        )

                self.languages_filter[key] = language_filter_list

        if video_order_key in self.config_file_content:
            self.video_order_default = self.config_file_content[video_order_key]

        # Set up the clone list and metadata folders to be tied to where Retool is located
        if 'localDir' in self.config_file_content[clone_lists_key]:
            self.path_clone_list = pathlib.Path(self.retool_location).joinpath(
                self.config_file_content[clone_lists_key]['localDir']
            )

        if 'localDir' in self.config_file_content[metadata_key]:
            self.path_metadata = pathlib.Path(self.retool_location).joinpath(
                self.config_file_content[metadata_key]['localDir']
            )

        self.path_quick_import: str = ''

        def key_missing(section_key: str) -> None:
            """
            Generates a warning if a specific key is missing from
            internal-config.json.

            Args:
                section_key (str): The section to check for in internal-config.json.
            """
            if section_key not in self.config_file_content:
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
            promote_editions_key,
            demote_editions_key,
            modern_editions_key,
        ]

        for s in config_keys:
            key_missing(s)

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
            tuple(self.languages),
            tuple(self.region_order_default),
            (),
            tuple(self.video_order_default),
            self.system_settings_path,
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

        user_config: YAML

        try:
            with open(pathlib.Path(self.user_config_file), encoding='utf-8') as user_config_import:
                user_config = load(str(user_config_import.read()), schema)

        except OSError as e:
            eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
            raise

        except YAMLValidationError as e:
            # For compatibility, check if the following filter keys are missing, and add
            # them if not found:
            #
            # * filters, added in v2.01.0
            # * localization order, added in v2.02.0

            if '\'filters\' not found' in str(e) or '\'localization order\' not found' in str(e):
                key_name: str = ''

                if '\'filters\' not found' in str(e):
                    key_name = 'filters'

                if '\'localization order\' not found' in str(e):
                    key_name = 'localization order'

                try:
                    with open(
                        pathlib.Path(self.user_config_file), encoding='utf-8'
                    ) as user_config_import:
                        add_filters_key: list[str] = user_config_import.readlines()
                        add_filters_key.append(f'\n\n{key_name}:')

                    with open(
                        pathlib.Path(self.user_config_file), 'w', encoding='utf-8'
                    ) as user_config_import:
                        user_config_import.writelines(add_filters_key)
                except Exception as e2:
                    eprint(f'• {Font.b}Error{Font.be}: {e2!s}\n', level='error')
                    raise

                try:
                    with open(
                        pathlib.Path(self.user_config_file), encoding='utf-8'
                    ) as user_config_import:
                        user_config = load(str(user_config_import.read()), schema)
                except Exception as e2:
                    eprint(f'• {Font.b}Error{Font.be}: {e2!s}\n', level='error')
                    raise
            else:
                eprint(f'• {Font.b}YAML validation error{Font.be}: {e!s}\n', level='error')
                raise

        except YAMLError as e:
            eprint(f'• {Font.b}YAML error{Font.be}:{e!s}\n', level='error')
            raise

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
                '\nEnter a dictionary key to expand (e.g. tags_disc_rename), q to continue, or hit enter to list: '
            )
            key = input()

            eprint(key)

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


class UserOverrides:
    """Creates an object for overrides."""

    def __init__(self, exclude: list[str] = [], include: list[str] = []):
        self.exclude: list[str] = exclude
        self.include: list[str] = include
        self.file = ''


def generate_config(
    user_config_file: str,
    languages: tuple[str, ...],
    regions: tuple[str, ...],
    localizations: tuple[str, ...],
    video_standards: tuple[str, ...],
    overrides_path: str,
    global_overrides: UserOverrides = UserOverrides(),
    system_overrides: UserOverrides = UserOverrides(),
    global_filters: list[str] = [],
    system_filters: list[str] = [],
    list_prefix: str = '',
    list_suffix: str = '',
    gui_settings: set[str] = set(),
    overwrite: bool = False,
    system_config: bool = False,
    system_paths: dict[str, str] = {},
    override_status: dict[str, bool] = {},
    first_run_gui: bool = False,
) -> None:
    """
    When run from the CLI, creates required config files if they're missing. When run
    from the GUI, additionally manages the editing of those files.

    Args:
        user_config_file (str): The location of user-config.yaml.

        languages (tuple[str, ...]): All languages Retool is processing.

        regions (tuple[str, ...]): All regions Retool is processing.

        localizations (tuple[str, ...]): All localization languages Retool is processing.

        video_standards (tuple[str, ...]): All video standards Retool is processing.

        overrides_path (str): Where the overrides are stored for individual systems.

        global_overrides (dict[str, list[str]], optional): Include and exclude overrides
        applied at the global level. Defaults to `{}`.

        system_overrides (dict[str, list[str]], optional): Include and exclude overrides
        applied at the system level. Defaults to `{}`.

        global_filters (list[str]): Global post filters applied at the global level.
        Defaults to [].

        system_filters (list[str]): System post filters applied at the global level.
        Defaults to [].

        list_prefix (str, optional): A prefix to add to each title that's exported
        using `--listnames`. Defaults to `''`.

        list_suffix (str, optional): A suffix to add to each title that's exported
        using `--listnames`. Defaults to `''`.

        gui_settings (set[str], optional): Settings only written and used by Retool's
        GUI. Defaults to `set()`.

        overwrite (bool, optional): Whether or not to overwrite an existing
        user-config.yaml. Only used when the GUI is writing the file. Defaults to `False`.

        system_config (bool): Whether a system config is in play. Defaults to `False`.

        system_paths (dict[str, str]): The paths the user has set for the system config,
        including the output folder, clone list file, and metadata file.

        override_status (dict[str, bool]): Which system settings tabs have the "Override
        global settings" checkbox enabled.

        first_run_gui (bool, optional): When using the GUI, is set to `True` to prevent
        Retool from prompting the user through the CLI to generate user-config.yaml, as
        this happens automatically through GUI use anyway. Defaults to `False`.
    """
    new_user_config: bool = False

    if not pathlib.Path(user_config_file).exists() or overwrite:
        try:

            def add_entry(string: str, is_comment: bool = False) -> None:
                """
                Adds an entry to a YAML object.

                Args:
                    string (str): The entry to add to the list.

                    is_comment (bool, optional): Whether or not the entry should be
                    commented out. Defaults to `False`.
                """
                if is_comment:
                    output_file.writelines(f'\n# - {string}')
                else:
                    output_file.writelines(f'\n- {string}')

            with open(pathlib.Path(user_config_file), 'w', encoding='utf-8') as output_file:
                output_file.writelines('---')

                if system_config:
                    clone_list_path: str = '# clonelists/your-clone-list.json'
                    metadata_file_path: str = '# metadata/your-metadata-file.json'
                    output_path: str = r'# C:\path'

                    if system_paths:
                        if system_paths['clone list']:
                            clone_list_path = system_paths['clone list']
                        if system_paths['metadata file']:
                            metadata_file_path = system_paths['metadata file']
                        if system_paths['output']:
                            output_path = system_paths['output']

                    output_file.writelines(
                        f'\n# This file contains the system settings for {pathlib.Path(user_config_file).stem}.'
                        '\n#'
                        '\n# It might override settings in config/user-config.yaml specifically for that'
                        '\n# DAT.'
                        '\n#'
                        '\n# =============================================='
                        '\n# CLONE LIST, METADATA FILE, AND OUTPUT LOCATION'
                        '\n# =============================================='
                        '\npaths:'
                        f'\n- override: {str(override_status["paths"]).lower()}'
                        f'\n- clone list: {clone_list_path}'
                        f'\n- metadata file: {metadata_file_path}'
                        f'\n- output: {output_path}'
                        '\n#'
                    )

                output_file.writelines(
                    '\n# =============='
                    '\n# LANGUAGE ORDER'
                    '\n# =============='
                    '\n# If the -l option is used, only include titles with the following languages.'
                    '\n# Comment out languages you don\'t want. Order is important.'
                    '\nlanguage order:'
                )

                if system_config:
                    output_file.writelines(
                        f'\n- override: {str(override_status["languages"]).lower()}'
                    )

                if not overwrite:
                    for language in languages:
                        add_entry(language, is_comment=True)
                else:
                    for language in languages:
                        if 'Comment|' in language:
                            add_entry(language[8:], is_comment=True)
                        else:
                            add_entry(language)

                output_file.writelines(
                    '\n\n# ============'
                    '\n# REGION ORDER'
                    '\n# ============'
                    '\n# Only include titles with the following regions. Comment out the regions you'
                    '\n# don\'t want. Order is important.'
                    '\nregion order:'
                )

                if system_config:
                    output_file.writelines(
                        f'\n- override: {str(override_status["regions"]).lower()}'
                    )

                for region in regions:
                    if not overwrite:
                        add_entry(region)
                    else:
                        if 'Comment|' in region:
                            add_entry(region[8:], is_comment=True)
                        else:
                            add_entry(region)

                output_file.writelines(
                    '\n\n# =================='
                    '\n# LOCALIZATION ORDER'
                    '\n# =================='
                    '\n# If the -n option is used, use local names where available for titles with the'
                    '\n# following languages. Comment out languages you don\'t want. Order is important.'
                    '\n# If all languages are commented out and -n is used, the language order is used'
                    '\n# instead.'
                    '\nlocalization order:'
                )

                if system_config:
                    output_file.writelines(
                        f'\n- override: {str(override_status["localizations"]).lower()}'
                    )

                if not overwrite:
                    for language in localizations:
                        add_entry(language, is_comment=True)
                else:
                    for language in localizations:
                        if 'Comment|' in language:
                            add_entry(language[8:], is_comment=True)
                        else:
                            add_entry(language)

                output_file.writelines(
                    '\n\n# ==========='
                    '\n# VIDEO ORDER'
                    '\n# ==========='
                    '\n# Priority for titles with a video tag in their name. Do not comment out any'
                    '\n# lines.'
                    '\nvideo order:'
                )

                if system_config:
                    output_file.writelines(f'\n- override: {str(override_status["video"]).lower()}')

                for video_standard in video_standards:
                    add_entry(video_standard)

                output_file.writelines(
                    '\n\n# ============================'
                    '\n# LIST NAMES PREFIX AND SUFFIX'
                    '\n# ============================'
                    '\n# If the --listnames option is used, you can optionally add a prefix and'
                    '\n# suffix to each title.'
                    '\n#'
                    '\n# If you start a prefix with http://, https://, or ftp://, each line in the'
                    '\n# list will be URL encoded.'
                    '\n#'
                    '\n# The text must be inside double quotes. You must escape other double quotes'
                    '\n# and backslashes inside the quotes like so: \\", \\\\'
                    '\nlist prefix:'
                )

                if list_prefix != '':
                    add_entry(f'"{list_prefix}"')
                else:
                    output_file.writelines('\n# - "This text will be at the start of each line"')

                output_file.writelines('\n\nlist suffix:')

                if list_suffix != '':
                    add_entry(f'"{list_suffix}"')
                else:
                    output_file.writelines('\n# - "This text will be at the end of each line"')

                output_file.writelines(
                    '\n\n# ===================================='
                    '\n# GLOBAL EXCLUDE AND INCLUDE OVERRIDES'
                    '\n# ===================================='
                    '\n# Override Retool and force exclude or include specific titles by adding your own'
                    '\n# text to match against. Items in the list are case sensitive. See the'
                    '\n# documentation for more information, and pay particular attention to how system'
                    '\n# overrides interact with global overrides.'
                    '\n#'
                    '\n# The formatting is as follows:'
                    '\n#'
                    '\n# * Plain text indicates a partial string match.'
                    '\n# * A prefix of / indicates a regular expression match.'
                    '\n# * A prefix of | indicates a full string match.'
                    '\n# * Additionally, wrap a string in <> to also remove any match\'s related clones.'
                    '\n#'
                    '\n# The text must be inside double quotes. You must escape double quotes and'
                    '\n# backslashes like so: \\", \\\\'
                    '\n#'
                    '\n# Comment out lines you don\'t want.'
                    '\nexclude:'
                )

                if system_config:
                    if system_overrides == UserOverrides() or system_overrides.exclude == []:
                        output_file.writelines('\n# - "[b]"')
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                    else:
                        for s in system_overrides.exclude:
                            output_file.writelines(f'\n- "{s}"')

                    output_file.writelines('\n\ninclude:')

                    if system_overrides == UserOverrides() or system_overrides.include == []:
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        for s in system_overrides.include:
                            output_file.writelines(f'\n- "{s}"')
                else:
                    if global_overrides == UserOverrides() or global_overrides.exclude == []:
                        output_file.writelines('\n# - "[b]"')
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                    else:
                        for s in global_overrides.exclude:
                            output_file.writelines(f'\n- "{s}"')

                    output_file.writelines('\n\ninclude:')

                    if global_overrides == UserOverrides() or global_overrides.include == []:
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        for s in global_overrides.include:
                            output_file.writelines(f'\n- "{s}"')

                output_file.writelines(
                    '\n\n# ============'
                    '\n# POST FILTERS'
                    '\n# ============'
                    '\n# After Retool has finished processing, remove all titles except the ones that'
                    '\n# match the text listed here. Items in the list are case sensitive. See the'
                    '\n# documentation for more information.'
                    '\n#'
                    '\n# The formatting is as follows:'
                    '\n#'
                    '\n# * Plain text indicates a partial string match.'
                    '\n# * A prefix of / indicates a regular expression match.'
                    '\n# * A prefix of | indicates a full string match.'
                    '\n#'
                    '\n# The text must be inside double quotes. You must escape double quotes and'
                    '\n# backslashes like so: \\", \\\\'
                    '\n#'
                    '\n# Comment out lines you don\'t want'
                    '\nfilters:'
                )

                if system_config:
                    output_file.writelines(
                        f'\n- override: {str(override_status["post_filters"]).lower()}'
                    )

                    if not system_filters:
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        for s in system_filters:
                            output_file.writelines(f'\n- "{s}"')

                else:
                    if not global_filters:
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        for s in global_filters:
                            output_file.writelines(f'\n- "{s}"')

                if system_config:
                    output_file.writelines(
                        '\n\n# ======================'
                        '\n# EXCLUSIONS AND OPTIONS'
                        '\n# ======================'
                        '\n# You should use the GUI to generate these options, even if you'
                        '\n# intend to use the CLI. Add a DAT, go the the System settings'
                        '\n# tab, and then change the exclusions and options to populate'
                        '\n# this section.'
                        '\nexclusions and options:'
                        f'\n- override exclusions: {str(override_status["exclusions"]).lower()}'
                        f'\n- override options: {str(override_status["options"]).lower()}'
                    )
                else:
                    output_file.writelines(
                        '\n\n# ============'
                        '\n# GUI SETTINGS'
                        '\n# ============'
                        '\n# GUI settings only, not used by the CLI.'
                        '\ngui settings:'
                    )

                if gui_settings != set():
                    for setting in sorted(gui_settings):
                        add_entry(setting)

                new_user_config = True

        except OSError as e:
            eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
            raise

    pathlib.Path(overrides_path).mkdir(parents=True, exist_ok=True)

    if not overwrite and not first_run_gui:

        if new_user_config:
            file_list: list[str] = []

            if new_user_config:
                file_list.append(f'• {Font.b}config/user-config.yaml{Font.be}')

            file_list_str: str = '\n'.join(file_list)

            eprint(
                'It\'s likely this is the first time you\'ve run Retool. The following '
                'system files were missing and have been created:',
                indent=0,
                level='warning',
            )

            eprint(f'\n{file_list_str}\n', wrap=False, level='warning')

            if new_user_config:
                eprint(
                    f'You might want to edit {Font.b}'
                    f'config/user-config.yaml{Font.be} to define a custom '
                    f'region order, or to filter specific languages.\n',
                    indent=0,
                    level='warning',
                )

            eprint('You can now run Retool normally.', indent=0, level='success')

            sys.exit(0)
