from __future__ import annotations

import pathlib
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.config.config import Config

from strictyaml import YAML, Map, YAMLError, YAMLValidationError, load # type: ignore
from strictyaml.ruamel.comments import CommentedMap # type: ignore

from modules.utils import Font, eprint


class UserOverrides:
    """Creates an object for overrides."""

    def __init__(self, exclude: list[str] | None = None, include: list[str] | None = None):
        self.exclude: list[str] = exclude if exclude is not None else []
        self.include: list[str] = include if include is not None else []
        self.file = ''


def generate_config(
    config_path: str,
    languages: tuple[str, ...],
    regions: tuple[str, ...],
    localizations: tuple[str, ...],
    video_standards: tuple[str, ...],
    system_config_path: str,
    global_overrides: UserOverrides = UserOverrides(),
    system_overrides: UserOverrides = UserOverrides(),
    global_filters: list[str] | None = None,
    system_filters: list[str] | None = None,
    list_prefix: str = '',
    list_suffix: str = '',
    gui_settings: set[str] | None = None,
    overwrite: bool = False,
    system_config: bool = False,
    system_paths: dict[str, str] | None = None,
    override_status: dict[str, str] | None = None,
    first_run_gui: bool = False,
) -> None:
    """
    When run from the CLI, creates required config files if they're missing. When run
    from the GUI, additionally manages the editing of those files.

    Args:
        config_path (str): The path to either `user-config.yaml`, or the system config to
            write.

        languages (tuple[str, ...]): All languages Retool is processing.

        regions (tuple[str, ...]): All regions Retool is processing.

        localizations (tuple[str, ...]): All localization languages Retool is processing.

        video_standards (tuple[str, ...]): All video standards Retool is processing.

        system_config_path (str): Where the system configs are stored.

        global_overrides (dict[str, list[str]], optional): Include and exclude overrides
            applied at the global level. Defaults to `{}`.

        system_overrides (dict[str, list[str]], optional): Include and exclude overrides
            applied at the system level. Defaults to `{}`.

        global_filters (list[str]): Global post filters applied at the global level.
            Defaults to `None`.

        system_filters (list[str]): System post filters applied at the global level.
            Defaults to `None`.

        list_prefix (str, optional): A prefix to add to each title that's exported using
            `--listnames`. Defaults to `''`.

        list_suffix (str, optional): A suffix to add to each title that's exported using
            `--listnames`. Defaults to `''`.

        gui_settings (set[str], optional): Settings only written and used by Retool's GUI.
            Defaults to `None`.

        overwrite (bool, optional): Whether to overwrite an existing `user-config.yaml`.
            Only used when the GUI is writing the file, or if it needs to be rewritten due
            to changes between versions. Defaults to `False`.

        system_config (bool): Whether a system config is being generated. Defaults to
            `False`.

        system_paths (dict[str, str]): The paths the user has set for the system config,
            including the output folder, clone list file, metadata file, MIA file, and
            RetroAchievements file. Defaults to `None`.

        override_status (dict[str, str]): Which system settings tabs have the "Override
            global settings" checkbox enabled. Defaults to `None`.

        first_run_gui (bool, optional): When using the GUI, is set to `True` to prevent
            Retool from prompting the user through the CLI to generate `user-config.yaml`,
            as this happens automatically through GUI use anyway. Defaults to `False`.
    """
    new_user_config: bool = False
    global_filters = global_filters if global_filters is not None else []
    system_filters = system_filters if system_filters is not None else []
    system_paths = system_paths if system_paths is not None else {}
    override_status = override_status if override_status is not None else {}
    gui_settings = gui_settings if gui_settings is not None else set()

    if not pathlib.Path(config_path).exists() or overwrite:
        try:

            def add_entry(string: str, is_comment: bool = False) -> None:
                """
                Adds an entry to a YAML object.

                Args:
                    string (str): The entry to add to the list.

                    is_comment (bool, optional): Whether the entry should be commented
                        out. Defaults to `False`.
                """
                if is_comment:
                    output_file.writelines(f'\n# - {string}')
                else:
                    output_file.writelines(f'\n- {string}')

            with open(pathlib.Path(config_path), 'w', encoding='utf-8') as output_file:
                output_file.writelines('---\nconfig version: 2.4.0')

                if system_config:
                    clone_list_path: str = '# clonelists/your-clone-list.json'
                    metadata_file_path: str = '# metadata/your-metadata-file.json'
                    mia_file_path: str = '# mias/your-mia-file.json'
                    ra_file_path: str = '# retroachievements/your-retroachievements-file.json'
                    output_path: str = r'# C:\path'

                    if system_paths:
                        if system_paths['clone list']:
                            clone_list_path = system_paths['clone list']
                        if system_paths['metadata file']:
                            metadata_file_path = system_paths['metadata file']
                        if system_paths['mia file']:
                            mia_file_path = system_paths['mia file']
                        if system_paths['retroachievements file']:
                            ra_file_path = system_paths['retroachievements file']
                        if system_paths['output']:
                            output_path = system_paths['output']

                    output_file.writelines(
                        f'\n# This file contains the system settings for {pathlib.Path(config_path).stem}.'
                        '\n#'
                        '\n# It might override settings in config/user-config.yaml specifically for that'
                        '\n# DAT file.'
                        '\n#'
                        '\n# =============================================='
                        '\n# CLONE LIST, METADATA FILE, AND OUTPUT LOCATION'
                        '\n# =============================================='
                        '\npaths:'
                        f'\n- override: {override_status["paths"].lower()}'
                        f'\n- clone list: {clone_list_path}'
                        f'\n- metadata file: {metadata_file_path}'
                        f'\n- mia file: {mia_file_path}'
                        f'\n- retroachievements file: {ra_file_path}'
                        f'\n- output: {output_path}'
                        '\n'
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
                    output_file.writelines(f'\n- override: {override_status["languages"].lower()}')

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
                    output_file.writelines(f'\n- override: {override_status["regions"].lower()}')

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
                        f'\n- override: {override_status["localizations"].lower()}'
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
                    output_file.writelines(f'\n- override: {override_status["video"].lower()}')

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

                if system_config:
                    output_file.writelines(
                        '\n\n# ===================================='
                        '\n# SYSTEM EXCLUDE AND INCLUDE OVERRIDES'
                        '\n# ===================================='
                    )
                else:
                    output_file.writelines(
                        '\n\n# ===================================='
                        '\n# GLOBAL EXCLUDE AND INCLUDE OVERRIDES'
                        '\n# ===================================='
                    )

                output_file.writelines(
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
                    '\n# * Additionally, wrap a string in <> to also remove or include any match\'s '
                    '\n#   related clones.'
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
                        f'\n- override: {override_status["post_filters"].lower()}'
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
                        '\n# intend to use the CLI. Add a DAT file, go the the System'
                        '\n# settings tab, and then change the exclusions and options to'
                        '\n# populate this section.'
                        '\nexclusions and options:'
                        f'\n- override exclusions: {override_status["exclusions"].lower()}'
                        f'\n- override options: {override_status["options"].lower()}'
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

    if system_config_path:
        pathlib.Path(system_config_path).mkdir(parents=True, exist_ok=True)

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


def patch_config(
    config_yaml: YAML,
    config_file: str,
    config: Config,
) -> None:
    """
    Patches a config file for compatibility if changes have been made between Retool
    versions.

    Args:
        config_yaml (YAML): The config file as a YAML object.

        config_file (str): The path to the config file to write to.

        config (Config): The Retool config object.
    """
    # Get the data required from the config file
    languages: tuple[str, ...] = ()
    regions: tuple[str, ...] = ()
    localizations: tuple[str, ...] = ()
    video_standards: tuple[str, ...] = tuple(config.video_order_default)
    system_config_path: str = ''
    global_overrides: UserOverrides = UserOverrides()
    system_overrides: UserOverrides = UserOverrides()
    global_filters: list[str] = []
    system_filters: list[str] = []
    list_prefix: str = ''
    list_suffix: str = ''
    gui_settings: set[str] = set()
    overwrite: bool = True
    system_config: bool = False
    system_paths: dict[str, str] = {}
    override_status: dict[str, str] = {}

    if 'paths' in config_yaml:
        system_config = True

    def get_system_overrides(key: str) -> str:
        """
        Gets the override value from a specific key in a system config file.

        Args:
            key (str): The key to get the override setting in.

        Returns:
            str: The override value.
        """
        system_overrides = [x for x in config_yaml.as_marked_up()[key] if type(x) is CommentedMap]
        system_override: str = 'false'

        for system_override_setting in system_overrides:
            for value in system_override_setting.values():
                system_override = value

        return system_override

    # Language order
    language_override: str = 'false'
    if 'language order' in config_yaml:
        languages = tuple(
            x for x in config_yaml.as_marked_up()['language order'] if type(x) is not CommentedMap
        )
        available_languages = tuple(
            f'Comment|{x}' for x in sorted(config.languages) if x not in languages
        )

        languages += available_languages

        language_override = get_system_overrides('language order')

    # Region order
    region_override: str = 'false'
    if 'region order' in config_yaml:
        regions = tuple(
            x for x in config_yaml.as_marked_up()['region order'] if type(x) is not CommentedMap
        )
        available_regions = tuple(
            f'Comment|{x}'
            for x in sorted(config.region_order_default)
            if x not in regions and x != 'United Kingdom'
        )

        regions += available_regions

        region_override = get_system_overrides('region order')

    # Localization order
    localizations_override: str = 'false'
    if 'localization order' in config_yaml:
        localizations = tuple(
            x
            for x in config_yaml.as_marked_up()['localization order']
            if type(x) is not CommentedMap
        )
        available_localizations = tuple(
            f'Comment|{x}' for x in sorted(config.languages) if x not in localizations
        )

        localizations += available_localizations

        localizations_override = get_system_overrides('localization order')

    # Video order
    video_override: str = 'false'
    if 'video order' in config_yaml:
        video_override = get_system_overrides('video order')

    # Filters
    post_filters_override: str = 'false'
    if 'filters' in config_yaml:
        filters = [
            x.replace('\\', '\\\\')
            for x in config_yaml.as_marked_up()['filters']
            if type(x) is not CommentedMap
        ]

        if system_config:
            system_filters = filters
        else:
            global_filters = filters

        post_filters_override = get_system_overrides('filters')

    # List prefix and suffix
    if 'list prefix' in config_yaml:
        list_prefix = ''.join(
            [x.replace('\\', '\\\\') for x in config_yaml.as_marked_up()['list prefix']]
        )

    if 'list suffix' in config_yaml:
        list_suffix = ''.join(
            [x.replace('\\', '\\\\') for x in config_yaml.as_marked_up()['list suffix']]
        )

    # GUI settings
    if 'gui settings' in config_yaml:
        gui_settings_raw = [x.as_marked_up() for x in config_yaml['gui settings']]
        for item in gui_settings_raw:
            if type(item) is CommentedMap:
                for key, value in item.items():
                    gui_settings.add(f'{key}: {value}')
            else:
                gui_settings.add(item)

    # Paths
    if system_config:
        clone_list: str = ''
        metadata_file: str = ''
        mia_file: str = ''
        output: str = ''
        retroachievements_file: str = ''

        for item in config_yaml.as_marked_up()['paths']:
            if 'clone list' in item:
                clone_list = item['clone list']
            elif 'metadata file' in item:
                metadata_file = item['metadata file']
            elif 'mia file' in item:
                mia_file = item['mia file']
            elif 'output' in item:
                output = item['output']
            elif 'retroachievements file' in item:
                retroachievements_file = item['retroachievements file']
            elif 'override' in item:
                paths_override = item['override']

        system_paths = {
            'clone list': clone_list,
            'metadata file': metadata_file,
            'mia file': mia_file,
            'output': output,
            'retroachievements file': retroachievements_file,
        }

    # Global and system overrides
    overrides: UserOverrides = UserOverrides()

    if 'exclude' in config_yaml:
        overrides.exclude = [x.replace('\\', '\\\\') for x in config_yaml.as_marked_up()['exclude']]

    if 'include' in config_yaml:
        overrides.include = [x.replace('\\', '\\\\') for x in config_yaml.as_marked_up()['include']]

    if system_config:
        system_overrides = overrides
    else:
        global_overrides = overrides

    # System exclusions, options, and override statuses
    if system_config:
        if 'exclusions and options' in config_yaml:
            for item in list(config_yaml.as_marked_up()['exclusions and options']):
                if 'override exclusions' in item:
                    override_status['exclusions'] = item['override exclusions']
                elif 'override options' in item:
                    override_status['options'] = item['override options']
                else:
                    if type(item) is CommentedMap:
                        for key, value in item.items():
                            gui_settings.add(f'{key}: {value}')
                    else:
                        gui_settings.add(item)

        override_status['languages'] = language_override
        override_status['localizations'] = localizations_override
        override_status['paths'] = paths_override
        override_status['post_filters'] = post_filters_override
        override_status['regions'] = region_override
        override_status['video'] = video_override

    # Generate the new config file
    generate_config(
        config_file,
        languages,
        regions,
        localizations,
        video_standards,
        system_config_path,
        global_overrides,
        system_overrides,
        global_filters,
        system_filters,
        list_prefix,
        list_suffix,
        gui_settings,
        overwrite,
        system_config,
        system_paths,
        override_status,
    )


def read_config(schema: Map, config_file: str, config: Config) -> YAML:
    """
    Reads in a YAML config file for Retool.

    Args:
        schema (Map): The schema to use for the file.

        config_file (str): The path to the config file to read from.

        config (Config): The Retool config object.

    Returns:
        YAML: The config file as a YAML object.
    """
    try:
        # Load the YAML config file without a schema to retrieve data, and update the
        # config file if required keys are missing
        with open(pathlib.Path(config_file), encoding='utf-8') as config_import:
            config_yaml: YAML = load(str(config_import.read()))

        if 'config version' in config_yaml:
            config_version: tuple[int, ...] = tuple(
                int(x) for x in config_yaml.as_marked_up()['config version'].split('.')
            )
            if config_version < (2, 4, 0):
                patch_config(config_yaml, config_file, config)
        else:
            patch_config(config_yaml, config_file, config)

    except YAMLError as e:
        eprint(f'• {Font.b}YAML error{Font.be}: {e!s}\n', level='error')
        raise

    except Exception as e:
        eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
        raise

    # Read in the fixed config file with the appropriate schema
    try:
        with open(pathlib.Path(config_file), encoding='utf-8') as config_import:
            settings: YAML = load(str(config_import.read()), schema)

    except YAMLValidationError as e:
        eprint(f'• {Font.b}YAML validation error{Font.be}: {e!s}\n', level='error')
        raise

    except YAMLError as e:
        eprint(f'• {Font.b}YAML error{Font.be}: {e!s}\n', level='error')
        raise

    except Exception as e:
        eprint(f'• {Font.b}Error{Font.be}: {e!s}\n', level='error')
        raise

    return settings
