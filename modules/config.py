from __future__ import annotations

import json
import pathlib
import re
import sys

from functools import reduce
from itertools import product
from strictyaml import load, Map, MapPattern, Str, Seq, YAML, YAMLError, YAMLValidationError
from typing import Any, Pattern

from modules.input import UserInput
from modules.stats import Stats
from modules.titletools import Regex
from modules.utils import download, eprint, Font, printwrap


class Config:
    def __init__(self,
                 clone_list_metadata_download_location: str,
                 clone_list_metadata_download_location_key: str,
                 program_download_location: str,
                 program_download_location_key: str,
                 config_file: str,
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
                 version_major: str,
                 version_minor: str,
                 user_input: Any,
                 first_run_gui: bool = False) -> None:
        """ Creates an object that contains internal and user config data. Interactively
        browsable if you `print()` the object.

        Args:
            - `clone_list_metadata_download_location (str)` A URL that points to a folder
              containing clone lists and metadata files, so local copies can be updated.
              Only used if internal-config.json is missing.

            - `clone_list_metadata_download_location_key (str)` The key in
              internal-config.json that contains the URL that hosts clone lists and
              metadata files, so local copies can be updated.

            - `program_download_location (str)` A URL that points to where the Retool
              program can be downloaded. Not used, but if it was, it would only be used if
              internal-config.json was missing.

            - `program_download_location_key (str)` The key in internal-config.json that
              contains the URL that hosts the Retool program. Not used.

            - `config_file (str)` The location of internal-config.json.

            - `ignore_tags_key (str)` The key to look up in internal-config.json that
              contains tags that should be ignored so like titles can be grouped together.

            - `disc_rename_key (str)` The key in internal-config.json that specifies how
              multiple '(Disc)' tags should be renamed so they can be normalized and
              compared.

            - `promote_editions_key (str)` The key in internal-config.json that specifies
              which tags indicate a title should be promoted over another.

            - `demote_editions_key (str)` The key in internal-config.json that specifies
              which tags indicate a title should be demoted below another.

            - `modern_editions_key (str)` The key in internal-config.json that specifies
              which tags indicate a title is ripped from a modern release of a game, like
              those from Virtual Console.

            - `languages_key (str)` The key in internal-config.json that specifies the
              available languages and their associated language codes.

            - `region_order_key (str)` The key in internal-config.json that specifies the
              default region order and the implied language for each region.

            - `video_order_key (str)` The key in internal-config.json that specifies the
              default order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM.

            - `clone_lists_key (str)` The key in internal-config.json that specifies where
              the local clone lists are located.

            - `metadata_key (str)` The key in internal-config.json that specifies where the
              local metadata files are located.

            - `user_config_key (str)` The key in internal-config.json that specifies where
              user-config.yaml is located.

            - `user_language_key (str)` The key in user-config.yaml that specifies the
              language order as defined by the user.

            - `user_region_order_key (str)` The key in user-config.yaml that specifies the
              region order as defined by the user.

            - `user_video_order_key (str)` The key in user-config.yaml that specifies the
              order for video standards like MPAL, NTSC, PAL, PAL 60Hz, and SECAM as defined
              by the user.

            - `user_list_prefix_key (str)` The key in user-config.yaml that specifies the
              prefix used when the user specifies `--listnames`.

            - `user_list_suffix_key (str)` The key in user-config.yaml that specifies the
              suffix used when the user specifies `--listnames`.

            - `user_gui_settings_key (str)` They key in user-config.yaml that specifies
              settings used by the GUI.

            - `system_settings_path (str)` The location of the system config files.

            - `sanitized_characters (tuple[str, ...])` Characters that can't be used in
              filenames.

            - `reserved_filenames (tuple[str, ...])` Filenames that can't be used in
              certain operating systems.

            - `version_major (str)` The major version of Retool. Combined with the minor
              version to make up the full version string.

            - `version_minor (str)` The minor version of Retool. Combined with the major
              version to make up the full version string.

            - `user_input (Any)` In the CLI version, all the arguments passed in by the user.
              In the GUI version, constructed from UI elements the user has enabled or
              interacted with.

            - `first_run_gui (bool, optional)` When using the GUI, is set to `True` to
              prevent Retool from prompting the user through the CLI to generate
              user-config.yaml, as this happens automatically through GUI use anyway.
              Defaults to `False`.
        """

        # Determine if STDOUT is being redirected or not
        self.stdout = False

        if not sys.stdout.isatty():
            self.stdout = True

        # Create the stats object
        self.stats = Stats()

        # Download the internal config file if it's missing
        def download_required_files(download_files: tuple[str, str]) -> None:
            """ Downloads the files Retool requires to operate.

            Args:
                - `download_files (tuple[str])` A tuple of the files to download.
            """

            required_files: str = ''.join([f'\n* {Font.bold}{x}{Font.warning}' for x in download_files])
            download_config: str = ''
            missing_file: bool = False

            for download_file in download_files:
                if not pathlib.Path(download_file).is_file():
                    missing_file = True

            if missing_file:
                while (
                    not download_config
                    or not (
                        download_config == 'y'
                        or download_config == 'n')):
                            printwrap(
                                f'{Font.warning_bold}Warning: {Font.warning} One or more '
                                'of the following files are missing, which Retool needs '
                                'to operate:', 'no_indent')
                            eprint(f'{required_files}')

                            eprint(f'\nWould you like to download them? (y/n) > {Font.end}')

                            download_config = input()

                if download_config.lower() == 'y':
                    eprint('')
                    for download_file in download_files:
                        eprint(f'* Downloading {Font.bold}{download_file}{Font.end}... ', sep=' ', end='', flush=True)
                        failed = download(f'{clone_list_metadata_download_location}/{download_file}', str(pathlib.Path(download_file)))

                        if not failed:
                            eprint('done.')

                    eprint('\n')
                else:
                    eprint('\nExiting...\n')
                    sys.exit()

                # Check that the files are there now for Retool to start
                download_required_files((config_file, 'datafile.dtd'))

        self.config_file: str = config_file

        download_required_files((config_file, 'datafile.dtd'))

        # Import the contents of the internal config file
        self.clone_list_metadata_download_location: str = clone_list_metadata_download_location
        self.program_download_location: str = program_download_location
        self.languages: dict[str, str] = {}
        self.languages_implied: dict[str, tuple[str, ...]] = {}
        self.languages_filter: dict[str, list[str]] = {}
        self.region_order_default: list[str] = []
        self.video_order_default: list[str] = []
        self.tags_ignore: list[str] = []
        self.tags_disc_rename: dict[str, str] = {}
        self.tags_promote_editions: tuple[Pattern[str]]
        self.tags_demote_editions: tuple[Pattern[str]]
        self.tags_modern_editions: tuple[Pattern[str]]
        self.user_config_file: str = ''

        try:
            with open(pathlib.Path(config_file), 'r', encoding='utf-8') as input_file:
                self.config_file_content: dict[str, Any] = json.load(input_file)
        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise


        def import_key(key_name: str, dict_key_name: str, iter_type: str = '', tags_ignore: bool = False) -> None:
            """ Takes the data from a specific key in internal-config.json, then assigns
            it to a self.attribute.

            Args:
                - `key_name (str)` The key to find in internal-config.json.

                - `dict_key_name (str)` The attribute to assign to the Retool config
                  object.
                - `iter_type (str, optional)` Whether the resulting attribute value should
                  be a `list`, `tuple`, or neither. Defaults to `''`.

                - `tags_ignore (bool, optional)` Whether the values in the attribute should
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
        import_key(ignore_tags_key, 'tags_ignore', 'list', tags_ignore=True)
        import_key(promote_editions_key, 'tags_promote_editions', 'tuple', tags_ignore=True)
        import_key(demote_editions_key, 'tags_demote_editions', 'tuple', tags_ignore=True)
        import_key(modern_editions_key, 'tags_modern_editions', 'tuple', tags_ignore=True)
        import_key(user_config_key, 'user_config_file')

        if clone_list_metadata_download_location_key in self.config_file_content:
            self.clone_list_metadata_download_location = self.config_file_content[clone_list_metadata_download_location_key]

        if program_download_location_key in self.config_file_content:
            self.program_download_location = self.config_file_content[program_download_location_key]

        if region_order_key in self.config_file_content:
            self.region_order_default = [region for region in self.config_file_content[region_order_key]]

            # Set up the implied languages
            for key, values in self.config_file_content[region_order_key].items():
                language_filter_list: list[str] = []

                if values['impliedLanguage']:
                    if values['impliedLanguage'] in self.languages:
                        language_filter_list.append(self.languages[values['impliedLanguage']])
                        self.languages_implied[key] = (self.languages[values['impliedLanguage']][:2],)

                self.languages_filter[key] = language_filter_list

        if video_order_key in self.config_file_content:
            self.video_order_default = self.config_file_content[video_order_key]

        if 'localDir' in self.config_file_content[clone_lists_key]:
            self.path_clone_list = self.config_file_content[clone_lists_key]['localDir']

        if 'localDir' in self.config_file_content[metadata_key]:
            self.path_metadata = self.config_file_content[metadata_key]['localDir']


        def key_missing(section_key: str) -> None:
            """ Generates a warning if a specific key is missing from
            internal-config.json.

            Args:
                - `section_key (str)` The section to check for in internal-config.json.
            """

            if section_key not in self.config_file_content:
                printwrap(
                            f'{Font.warning}* The {Font.bold}{section_key}{Font.warning}'
                            f' key is missing from {Font.bold}{config_file}'
                            f'{Font.warning}. Clone matching won\'t be accurate.'
                            f'{Font.end}')

        set(map(lambda s: key_missing(s), [languages_key,
                                            region_order_key,
                                            ignore_tags_key,
                                            disc_rename_key,
                                            promote_editions_key,
                                            demote_editions_key,
                                            modern_editions_key]))

        # No-Intro uses a + sign for 2- and 3-in-1 compilations in their GBA DAT
        # to delineate languages between the first and subsequent titles. For
        # example: (En+En,Fr,De). We need to take this into account when
        # detecting languages in titles. Here we use a Cartesian product of all
        # languages to find these combinations. Thankfully there's only one
        # triple language title so far, so we manually add (En+En+En) instead of
        # searching for all triple language combinations and slowing things
        # down.

        no_intro_languages: list[str] = [x for x in self.languages.values()]
        compilation_languages: list[str] = []

        for language_combo in product(no_intro_languages, repeat=2):
            compilation_languages.append('\+'.join(language_combo))

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

        generate_config(user_config_file,
                        tuple(map(lambda s: s, self.languages)),
                        tuple(self.region_order_default),
                        tuple(self.video_order_default),
                        system_settings_path,
                        first_run_gui=first_run_gui)

        # Import the user config file
        self.region_order_languages_user: list[str] = []
        self.language_order_user: list[str] = []
        self.languages_user_found: bool = False
        self.region_order_user: list[str] = []
        self.video_order_user: list[str] = []
        self.user_prefix: str = ''
        self.user_suffix: str = ''
        self.user_gui_settings: tuple[Any, ...] = ()

        schema = Map(
                {user_language_order_key: Seq(Str())|Str(),
                 user_region_order_key: Seq(Str())|Str(),
                 user_video_order_key: Seq(Str())|Str(),
                 user_list_prefix_key: Seq(Str())|Str(),
                 user_list_suffix_key: Seq(Str())|Str(),
                 user_override_exclude_key: Seq(Str())|Str(),
                 user_override_include_key: Seq(Str())|Str(),
                 user_filter_key: Seq(Str())|Str(),
                 user_gui_settings_key: Seq(Str()|MapPattern(Str(), Str()))|Str()})

        user_config: YAML

        try:
            with open(pathlib.Path(user_config_file), 'r', encoding='utf-8') as user_config_import:
                user_config = load(str(user_config_import.read()), schema)

        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

        except YAMLValidationError as e:
            # Check for the filters key that was added in v2.01.0, and add it if not found
            if '\'filters\' not found' in str(e):
                try:
                    with open(pathlib.Path(user_config_file), 'r', encoding='utf-8') as user_config_import:
                        add_filters_key: list[str] = user_config_import.readlines()
                        add_filters_key.append('\n\nfilters:')

                    with open(pathlib.Path(user_config_file), 'w', encoding='utf-8') as user_config_import:
                        user_config_import.writelines(add_filters_key)
                except Exception as e2:
                    eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e2)}\n')
                    raise

                try:
                    with open(pathlib.Path(user_config_file), 'r', encoding='utf-8') as user_config_import:
                        user_config = load(str(user_config_import.read()), schema)
                except Exception as e2:
                    eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e2)}\n')
                    raise
            else:
                eprint(f'\n{Font.error_bold}* YAML validation error: {Font.end}{str(e)}\n')
                raise

        except YAMLError as e:
            eprint(f'\n{Font.error_bold}* YAML error: {Font.end}{str(e)}\n')
            raise

        self.language_order_user = list(user_config.data[user_language_order_key])
        self.region_order_user = list(user_config.data[user_region_order_key])
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
        self.region_order_languages_user = reduce(lambda x,y: x + [y] if not y in x else x, self.region_order_languages_user, [])

        language_list: list[str] = []

        if not self.language_order_user:
            language_list = self.region_order_languages_user
        else:
            self.languages_user_found = True

            for language in self.language_order_user:
                if language in self.languages:
                    language_list.append(self.languages[language])

        self.language_order_user = language_list

        # Compensate for No-Intro using "United Kingdom", and Redump using "UK"
        if 'UK' in self.region_order_user:
            uk_index: int = self.region_order_user.index('UK')
            self.region_order_user[uk_index + 1:uk_index + 1] = ['United Kingdom']

        uk_index = self.region_order_default.index('UK')
        self.region_order_default[uk_index + 1:uk_index + 1] = ['United Kingdom']

        # Add "Export" to the default region order regex as a pseudo-region, which is reinterpreted as "World" later
        self.regex.region_order_default = re.compile('\\s\\((?:\\w*,\\s)*(?:' + '|'.join(self.region_order_default + ['Export']) + ')(?:,\\s\\w*)*\\)')

        if 'UK' in self.languages_implied:
            self.languages_implied['United Kingdom'] = self.languages_implied['UK']
            self.languages_filter['United Kingdom'] = self.languages_filter['UK']

        # Import global overrides
        self.system_settings_path = system_settings_path

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
        self.system_language_order_user: list[str|dict[str,str]] = []
        self.system_region_order_user: list[str|dict[str,str]] = []
        self.system_video_order_user: list[str|dict[str,str]] = []
        self.system_exclude: list[str] = []
        self.system_include: list[str] = []
        self.system_filter: list[str|dict[str,str]] = []
        self.system_user_prefix: str = ''
        self.system_user_suffix: str = ''
        self.system_user_path_settings: tuple[Any, ...] = ()
        self.system_exclusions_options: tuple[Any, ...] = ()

        # Store the Retool version
        self.version_major: str = version_major
        self.version_minor: str = version_minor

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
                    return_attributes.append([f'  ├ .{attribute}:', f'(...) {format_value(str(type(getattr(self, attribute)).__name__))}'])
                else:
                    return_attributes.append([f'  ├ .{attribute}:', format_value(getattr(self, attribute))])

        final_item: list[str] = return_attributes[-1].copy()

        for i, s in enumerate(final_item):
            return_attributes[-1][i] = s.replace('├', '└')

        # Column alignment
        def class_output() -> None:
            eprint(f'\n  ○ Config object')
            col_width: int = max(len(word) for row in return_attributes for word in row) - 20
            for row in return_attributes:
                eprint(''.join(str(word).ljust(col_width) for word in row))

        key: str = 'blank'

        class_output()

        while key != 'q':
            eprint('\nEnter a dictionary key to expand (e.g. tags_disc_rename), q to continue, or hit enter to list: ')
            key = input()

            eprint(key)

            if hasattr(self, key):
                if (
                    isinstance(getattr(self, key), Regex)
                    or isinstance(getattr(self, key), UserInput)):
                        eprint(f'\n{vars(getattr(self, key))}')
                else:
                    eprint(f'\n{format_value(getattr(self, key))}')
            elif key == '':
                class_output()
            else:
                if key != 'q':
                    eprint(f'\nUnknown key "{key}".')
                else:
                    break

        return ''


class UserOverrides():
    """ Creates an object for overrides """

    def __init__(self, exclude: list[str] = [], include: list[str] = []):
        self.exclude: list[str] = exclude
        self.include: list[str] = include
        self.file = ''


def generate_config(
    user_config_file: str,
    languages: tuple[str, ...],
    regions: tuple[str, ...],
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
    system_paths: dict[str, str]  = {},
    override_status: dict[str, bool] = {},
    first_run_gui: bool = False
    ) -> None:
    """ When run from the CLI, creates required config files if they're missing. When run
    from the GUI, additionally manages the editing of those files.

    Args:
        - `user_config_file (str)` The location of user-config.yaml.

        - `languages (tuple[str, ...])` All languages Retool is processing.

        - `regions (tuple[str, ...])` All regions Retool is processing.

        - `video_standards (tuple[str, ...])` All video standards Retool is processing.

        - `overrides_path (str)` Where the overrides are stored for individual systems.

        - `global_overrides (dict[str, list[str]], optional)` Include and exclude overrides
          applied at the global level. Defaults to `{}`.

        - `system_overrides (dict[str, list[str]], optional)` Include and exclude overrides
          applied at the system level. Defaults to `{}`.

        - `list_prefix (str, optional)` A prefix to add to each title that's exported
          using `--listnames`. Defaults to `''`.

        - `list_suffix (str, optional)` A suffix to add to each title that's exported
          using `--listnames`. Defaults to `''`.

        - `gui_settings (set[str], optional)` Settings only written and used by Retool's
          GUI. Defaults to `set()`.

        - `overwrite (bool, optional)` Whether or not to overwrite an existing
          user-config.yaml. Only used when the GUI is writing the file. Defaults to `False`.

        - `system_config (bool)` Whether a system config is in play. Defaults to `False`.

        - `system_paths (dict[str, str])` The paths the user has set for the system config,
          including the output folder, clone list file, and metadata file.

        - `overide_status (dict[str, bool])` Which system settings tabs have the "Override
          global settings" checkbox enabled.

        - `first_run_gui (bool, optional)` When using the GUI, is set to `True` to prevent
          Retool from prompting the user through the CLI to generate user-config.yaml, as
          this happens automatically through GUI use anyway. Defaults to `False`.
    """

    new_user_config: bool = False

    if not pathlib.Path(user_config_file).exists() or overwrite:
        try:
            def add_entry(string: str, is_comment: bool = False) -> None:
                    """ Adds an entry to a YAML object.

                    Args:
                        - `string (str)` The entry to add to the list.

                        - `is_comment (bool, optional)` Whether or not the entry
                          should be commented out. Defaults to `False`.
                    """

                    if is_comment:
                        output_file.writelines(f'\n# - {string}')
                    else:
                        output_file.writelines(f'\n- {string}')

            with open(pathlib.Path(user_config_file), 'w', encoding='utf-8') as output_file:
                output_file.writelines(
                    '---')

                if system_config:
                    clone_list_path: str = '# clonelists\your-clone-list.json'
                    metadata_file_path: str = '# metadata/your-metadata-file.json'
                    output_path: str = '# C:\path'

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
                    '\nregion order:')

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
                    '\n\n# ==========='
                    '\n# VIDEO ORDER'
                    '\n# ==========='
                    '\n# Priority for titles with a video tag in their name. Do not comment out any'
                    '\n# lines.'
                    '\nvideo order:'
                )

                if system_config:
                    output_file.writelines(
                        f'\n- override: {str(override_status["video"]).lower()}'
                    )

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
                    '\nlist prefix:')

                if list_prefix != '':
                    add_entry(f'"{list_prefix}"')
                else:
                    output_file.writelines('\n# - "This text will be at the start of each line"')

                output_file.writelines(f'\n\nlist suffix:')

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
                    '\nexclude:')

                if system_config:
                    if (
                        system_overrides == UserOverrides()
                        or system_overrides.exclude == []):
                        output_file.writelines('\n# - "[b]"')
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), system_overrides.exclude))

                    output_file.writelines('\n\ninclude:')

                    if (
                        system_overrides == UserOverrides()
                        or system_overrides.include == []):
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), system_overrides.include))
                else:
                    if (
                        global_overrides == UserOverrides()
                        or global_overrides.exclude == []):
                        output_file.writelines('\n# - "[b]"')
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), global_overrides.exclude))

                    output_file.writelines('\n\ninclude:')

                    if (
                        global_overrides == UserOverrides()
                        or global_overrides.include == []):
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), global_overrides.include))

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
                    '\nfilters:')

                if system_config:
                    output_file.writelines(f'\n- override: {str(override_status["post_filters"]).lower()}')

                    if not system_filters:
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), system_filters))

                else:
                    if not global_filters:
                        output_file.writelines('\n# - "/.*?\\(Virtual*"')
                        output_file.writelines('\n# - "|My favorite title (Japan)"')
                    else:
                        list(map(lambda s: output_file.writelines(f'\n- "{s}"'), global_filters))

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
                        f'\n- override options: {str(override_status["options"]).lower()}')
                else:
                    output_file.writelines(
                    '\n\n# ============'
                    '\n# GUI SETTINGS'
                    '\n# ============'
                    '\n# GUI settings only, not used by the CLI.'
                    '\ngui settings:')

                if gui_settings != set():
                    for setting in sorted(gui_settings):
                        add_entry(setting)

                new_user_config = True

        except OSError as e:
            eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
            raise

    pathlib.Path(overrides_path).mkdir(parents=True, exist_ok=True)

    if (
        overwrite == False
        and not first_run_gui):

        if new_user_config:
            file_list: list[str]= []

            if new_user_config:
                file_list.append(f'* {Font.warning_bold}config/user-config.yaml{Font.warning}')

            file_list_str: str = '\n'.join(file_list)

            printwrap(f'{Font.warning}It\'s likely this is the first time '
                      'you\'ve run Retool. The following system files were '
                      f'missing and have been created:', 'no_indent')

            eprint(f'\n{file_list_str}\n')

            if new_user_config:
                printwrap(f'You might want to edit {Font.warning_bold}'
                          f'config/user-config.yaml{Font.warning} to define a custom '
                          f'region order, or to filter specific languages.{Font.end}',
                          'no_indent')
                eprint('')


            printwrap(f'{Font.success}You can now run Retool normally.{Font.end}', 'no_indent')

            sys.exit()
