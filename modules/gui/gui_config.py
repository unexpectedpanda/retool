import pathlib

from typing import Any

from modules.constants import *
from modules.config import Config, Filters, generate_config
from modules.gui.gui_utils import enable_go_button
from modules.input import get_config_value, UserInput


def import_config() -> Config:
    """ Builds a config object for the GUI that Retool understands """

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
        CLI_VERSION_MAJOR,
        CLI_VERSION_MINOR,
        UserInput(),
        first_run_gui=True)

    return config


def write_config(main_window: Any, dat_details: dict[str, dict[str, str]], config: Config, settings_window: Any = None, run_retool: bool = False, update_clone_list: bool = False) -> None:
    """
    Gets widgets' state, then writes the user-config.yaml file

    Args:
        `main_window (Any)`: The MainWindow widget.
        `dat_details (dict[str, dict[str, str]])`: The dictionary that carries DAT file
        details like its system name and filepath.
        `config (Config)`: The Retool config object.
        `settings_window (Any)`: The settings widget. Defaults to `None`.
        `run_retool (bool, optional): Whether Retool should be run after a config write.
        Defaults to `False`.
        `update_clone_list (bool, optional)`: Whether the user has requested a clone list
        update. Defaults to `False`.
    """

    # Check if the "Process DAT files" button should be enabled
    enable_go_button(main_window)

    # Global list widgets
    available_languages: list[str] = [main_window.ui.listWidgetGlobalAvailableLanguages.item(x).text() for x in range(main_window.ui.listWidgetGlobalAvailableLanguages.count())]
    available_regions: list[str] = [main_window.ui.listWidgetGlobalAvailableRegions.item(x).text() for x in range(main_window.ui.listWidgetGlobalAvailableRegions.count())]
    selected_languages: list[str] = [main_window.ui.listWidgetGlobalSelectedLanguages.item(x).text() for x in range(main_window.ui.listWidgetGlobalSelectedLanguages.count())]
    selected_regions: list[str] = [main_window.ui.listWidgetGlobalSelectedRegions.item(x).text() for x in range(main_window.ui.listWidgetGlobalSelectedRegions.count())]
    video_standards: list[str] = [main_window.ui.listWidgetGlobalVideoStandards.item(x).text() for x in range(main_window.ui.listWidgetGlobalVideoStandards.count())]

    # System list widgets
    system_available_languages: list[str] = [main_window.ui.listWidgetSystemAvailableLanguages.item(x).text() for x in range(main_window.ui.listWidgetSystemAvailableLanguages.count())]
    system_available_regions: list[str] = [main_window.ui.listWidgetSystemAvailableRegions.item(x).text() for x in range(main_window.ui.listWidgetSystemAvailableRegions.count())]
    system_selected_languages: list[str] = [main_window.ui.listWidgetSystemSelectedLanguages.item(x).text() for x in range(main_window.ui.listWidgetSystemSelectedLanguages.count())]
    system_selected_regions: list[str] = [main_window.ui.listWidgetSystemSelectedRegions.item(x).text() for x in range(main_window.ui.listWidgetSystemSelectedRegions.count())]
    system_video_standards: list[str] = [main_window.ui.listWidgetSystemVideoStandards.item(x).text() for x in range(main_window.ui.listWidgetSystemVideoStandards.count())]

    system_overrides = {
        'exclusions': main_window.ui.checkBoxSystemOverrideExclusions.isChecked(),
        'languages': main_window.ui.checkBoxSystemOverrideLanguages.isChecked(),
        'options': main_window.ui.checkBoxSystemOverrideOptions.isChecked(),
        'paths': main_window.ui.checkBoxSystemOverridePaths.isChecked(),
        'regions': main_window.ui.checkBoxSystemOverrideRegions.isChecked(),
        'video': main_window.ui.checkBoxSystemOverrideVideo.isChecked()
    }

    # System paths
    output_folder: str = ''
    clone_list: str = ''
    metadata_file: str = ''

    if main_window.system_output_folder != '.':
        output_folder = main_window.system_output_folder

    if main_window.system_clone_list != '.':
        clone_list = main_window.system_clone_list

    if main_window.system_metadata_file != '.':
        metadata_file = main_window.system_metadata_file

    system_override_paths: dict[str, str] = {
        'output': output_folder,
        'clone list': clone_list,
        'metadata file': metadata_file
    }

    # If English isn't being processed, make sure it's commented out and at the top of the list
    if 'English' in available_languages: available_languages = ['English'] + [x for x in available_languages if x != 'English']

    # Languages and regions
    languages: tuple[str, ...] = tuple([f'Comment|{x}' for x in available_languages] + selected_languages)
    regions: tuple[str, ...] = tuple([f'Comment|{x}' for x in available_regions] + selected_regions)

    system_languages: tuple[str, ...] = tuple([f'Comment|{x}' for x in system_available_languages] + system_selected_languages)
    system_regions: tuple[str, ...] = tuple([f'Comment|{x}' for x in system_available_regions] + system_selected_regions)

    # Global exclude options
    exclude_add_ons: bool = main_window.ui.checkBoxGlobalExcludeAddOns.isChecked()
    exclude_applications: bool = main_window.ui.checkBoxGlobalExcludeApplications.isChecked()
    exclude_audio: bool = main_window.ui.checkBoxGlobalExcludeAudio.isChecked()
    exclude_bad_dumps: bool = main_window.ui.checkBoxGlobalExcludeBadDumps.isChecked()
    exclude_bios: bool = main_window.ui.checkBoxGlobalExcludeBIOS.isChecked()
    exclude_bonus_discs: bool = main_window.ui.checkBoxGlobalExcludeBonusDiscs.isChecked()
    exclude_coverdiscs: bool = main_window.ui.checkBoxGlobalExcludeCoverdiscs.isChecked()
    exclude_demos: bool = main_window.ui.checkBoxGlobalExcludeDemos.isChecked()
    exclude_educational: bool = main_window.ui.checkBoxGlobalExcludeEducational.isChecked()
    exclude_manuals: bool = main_window.ui.checkBoxGlobalExcludeManuals.isChecked()
    exclude_mia: bool = main_window.ui.checkBoxGlobalExcludeMIA.isChecked()
    exclude_multimedia: bool = main_window.ui.checkBoxGlobalExcludeMultimedia.isChecked()
    exclude_pirate: bool = main_window.ui.checkBoxGlobalExcludePirate.isChecked()
    exclude_preproduction: bool = main_window.ui.checkBoxGlobalExcludePreproduction.isChecked()
    exclude_promotional: bool = main_window.ui.checkBoxGlobalExcludePromotional.isChecked()
    exclude_unlicensed: bool = main_window.ui.checkBoxGlobalExcludeUnlicensed.isChecked()
    exclude_video: bool = main_window.ui.checkBoxGlobalExcludeVideo.isChecked()

    # System exclude options
    system_exclude_add_ons: bool = main_window.ui.checkBoxSystemExcludeAddOns.isChecked()
    system_exclude_applications: bool = main_window.ui.checkBoxSystemExcludeApplications.isChecked()
    system_exclude_audio: bool = main_window.ui.checkBoxSystemExcludeAudio.isChecked()
    system_exclude_bad_dumps: bool = main_window.ui.checkBoxSystemExcludeBadDumps.isChecked()
    system_exclude_bios: bool = main_window.ui.checkBoxSystemExcludeBIOS.isChecked()
    system_exclude_bonus_discs: bool = main_window.ui.checkBoxSystemExcludeBonusDiscs.isChecked()
    system_exclude_coverdiscs: bool = main_window.ui.checkBoxSystemExcludeCoverdiscs.isChecked()
    system_exclude_demos: bool = main_window.ui.checkBoxSystemExcludeDemos.isChecked()
    system_exclude_educational: bool = main_window.ui.checkBoxSystemExcludeEducational.isChecked()
    system_exclude_manuals: bool = main_window.ui.checkBoxSystemExcludeManuals.isChecked()
    system_exclude_mia: bool = main_window.ui.checkBoxSystemExcludeMIA.isChecked()
    system_exclude_multimedia: bool = main_window.ui.checkBoxSystemExcludeMultimedia.isChecked()
    system_exclude_pirate: bool = main_window.ui.checkBoxSystemExcludePirate.isChecked()
    system_exclude_preproduction: bool = main_window.ui.checkBoxSystemExcludePreproduction.isChecked()
    system_exclude_promotional: bool = main_window.ui.checkBoxSystemExcludePromotional.isChecked()
    system_exclude_unlicensed: bool = main_window.ui.checkBoxSystemExcludeUnlicensed.isChecked()
    system_exclude_video: bool = main_window.ui.checkBoxSystemExcludeVideo.isChecked()

    # Global options
    disable_1G1R: bool = main_window.ui.checkBoxGlobalOptionsDisable1G1R.isChecked()
    prefer_regions: bool = main_window.ui.checkBoxGlobalOptionsPreferRegions.isChecked()
    include_hashless: bool = main_window.ui.checkBoxGlobalOptionsIncludeHashless.isChecked()
    modern_platforms: bool = main_window.ui.checkBoxGlobalOptionsModernPlatforms.isChecked()
    demote_unlicensed: bool = main_window.ui.checkBoxGlobalOptionsDemoteUnlicensed.isChecked()
    disable_filters: bool = main_window.ui.checkBoxGlobalOptionsDisableFilters.isChecked()
    split_regions: bool = main_window.ui.checkBoxGlobalOptionsSplitRegions.isChecked()
    removes_dat: bool = main_window.ui.checkBoxGlobalOptionsRemovesDat.isChecked()
    keep_removes: bool = main_window.ui.checkBoxGlobalOptionsKeepRemove.isChecked()
    list_1g1r_names: bool = main_window.ui.checkBoxGlobalOptions1G1RNames.isChecked()
    report_warnings: bool = main_window.ui.checkBoxGlobalOptionsReportWarnings.isChecked()
    pause_on_warnings: bool = main_window.ui.checkBoxGlobalOptionsPauseWarnings.isChecked()
    legacy_dat: bool = main_window.ui.checkBoxGlobalOptionsLegacy.isChecked()
    bypass_dtd: bool = main_window.ui.checkBoxGlobalOptionsBypassDTD.isChecked()
    disable_multiprocessor: bool = main_window.ui.checkBoxGlobalOptionsDisableMultiCPU.isChecked()
    trace: bool = main_window.ui.checkBoxGlobalOptionsTrace.isChecked()

    prefix_1g1r: str = main_window.ui.lineEditGlobalOptions1G1RPrefix.text().replace('\\', '\\\\').replace('"', '\\"')
    suffix_1g1r: str = main_window.ui.lineEditGlobalOptions1G1RSuffix.text().replace('\\', '\\\\').replace('"', '\\"')

    trace_str: str = ''

    if trace:
        trace_str = main_window.ui.lineEditGlobalOptionsTrace.text().replace('\\', '\\\\').replace('"', '\\"')

    # System options
    system_disable_1G1R: bool = main_window.ui.checkBoxSystemOptionsDisable1G1R.isChecked()
    system_prefer_regions: bool = main_window.ui.checkBoxSystemOptionsPreferRegions.isChecked()
    system_include_hashless: bool = main_window.ui.checkBoxSystemOptionsIncludeHashless.isChecked()
    system_modern_platforms: bool = main_window.ui.checkBoxSystemOptionsModernPlatforms.isChecked()
    system_demote_unlicensed: bool = main_window.ui.checkBoxSystemOptionsDemoteUnlicensed.isChecked()
    system_disable_filters: bool = main_window.ui.checkBoxSystemOptionsDisableFilters.isChecked()
    system_split_regions: bool = main_window.ui.checkBoxSystemOptionsSplitRegions.isChecked()
    system_removes_dat: bool = main_window.ui.checkBoxSystemOptionsRemovesDat.isChecked()
    system_keep_removes: bool = main_window.ui.checkBoxSystemOptionsKeepRemove.isChecked()
    system_list_1g1r_names: bool = main_window.ui.checkBoxSystemOptions1G1RNames.isChecked()
    system_report_warnings: bool = main_window.ui.checkBoxSystemOptionsReportWarnings.isChecked()
    system_pause_on_warnings: bool = main_window.ui.checkBoxSystemOptionsPauseWarnings.isChecked()
    system_legacy_dat: bool = main_window.ui.checkBoxSystemOptionsLegacy.isChecked()
    system_bypass_dtd: bool = main_window.ui.checkBoxSystemOptionsBypassDTD.isChecked()
    system_disable_multiprocessor: bool = main_window.ui.checkBoxSystemOptionsDisableMultiCPU.isChecked()
    system_trace: bool = main_window.ui.checkBoxSystemOptionsTrace.isChecked()

    system_prefix_1g1r: str = main_window.ui.lineEditSystemOptions1G1RPrefix.text().replace('\\', '\\\\').replace('"', '\\"')
    system_suffix_1g1r: str = main_window.ui.lineEditSystemOptions1G1RSuffix.text().replace('\\', '\\\\').replace('"', '\\"')

    system_trace_str: str = ''

    if system_trace:
        system_trace_str = main_window.ui.lineEditSystemOptionsTrace.text().replace('\\', '\\\\').replace('"', '\\"')

    # Global user filters
    global_exclude_filters: list[str] = []
    global_include_filters: list[str] = []

    if main_window.ui.textEditGlobalExclude.toPlainText():
        global_exclude_filters = main_window.ui.textEditGlobalExclude.toPlainText().split('\n')
        global_exclude_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in global_exclude_filters if x]
    if main_window.ui.textEditGlobalInclude.toPlainText():
        global_include_filters = main_window.ui.textEditGlobalInclude.toPlainText().split('\n')
        global_include_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in global_include_filters if x]

    global_filters: Filters = Filters(global_exclude_filters, global_include_filters)

    # System user filters
    system_exclude_filters: list[str] = []
    system_include_filters: list[str] = []

    if main_window.ui.textEditSystemExclude.toPlainText():
        system_exclude_filters = main_window.ui.textEditSystemExclude.toPlainText().split('\n')
        system_exclude_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in system_exclude_filters if x]
    if main_window.ui.textEditSystemInclude.toPlainText():
        system_include_filters = main_window.ui.textEditSystemInclude.toPlainText().split('\n')
        system_include_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in system_include_filters if x]

    system_filters: Filters = Filters(system_exclude_filters, system_include_filters)

    excludes: set[str] = set()
    system_excludes: set[str] = set()

    if exclude_add_ons: excludes.add('D')
    if exclude_applications: excludes.add('a')
    if exclude_audio: excludes.add('A')
    if exclude_bad_dumps: excludes.add('b')
    if exclude_bios: excludes.add('B')
    if exclude_bonus_discs: excludes.add('o')
    if exclude_coverdiscs: excludes.add('c')
    if exclude_demos: excludes.add('d')
    if exclude_educational: excludes.add('e')
    if exclude_manuals: excludes.add('m')
    if exclude_mia: excludes.add('k')
    if exclude_multimedia: excludes.add('M')
    if exclude_pirate: excludes.add('p')
    if exclude_preproduction: excludes.add('P')
    if exclude_promotional: excludes.add('r')
    if exclude_unlicensed: excludes.add('u')
    if exclude_video: excludes.add('v')

    if system_exclude_add_ons: system_excludes.add('D')
    if system_exclude_applications: system_excludes.add('a')
    if system_exclude_audio: system_excludes.add('A')
    if system_exclude_bad_dumps: system_excludes.add('b')
    if system_exclude_bios: system_excludes.add('B')
    if system_exclude_bonus_discs: system_excludes.add('o')
    if system_exclude_coverdiscs: system_excludes.add('c')
    if system_exclude_demos: system_excludes.add('d')
    if system_exclude_educational: system_excludes.add('e')
    if system_exclude_manuals: system_excludes.add('m')
    if system_exclude_mia: system_excludes.add('k')
    if system_exclude_multimedia: system_excludes.add('M')
    if system_exclude_pirate: system_excludes.add('p')
    if system_exclude_preproduction: system_excludes.add('P')
    if system_exclude_promotional: system_excludes.add('r')
    if system_exclude_unlicensed: system_excludes.add('u')
    if system_exclude_video: system_excludes.add('v')

    gui_settings: set[str] = set()
    system_exclusions_options: set[str] = set()

    if disable_1G1R: gui_settings.add('d')
    if prefer_regions: gui_settings.add('r')
    if include_hashless: gui_settings.add('e')
    if modern_platforms: gui_settings.add('z')
    if demote_unlicensed: gui_settings.add('y')
    if disable_filters: gui_settings.add('nofilters')
    if split_regions: gui_settings.add('regionsplit')
    if removes_dat: gui_settings.add('removesdat')
    if keep_removes: gui_settings.add('log')
    if list_1g1r_names: gui_settings.add('listnames')
    if report_warnings: gui_settings.add('warnings')
    if pause_on_warnings: gui_settings.add('warningpause')
    if legacy_dat: gui_settings.add('legacy')
    if bypass_dtd: gui_settings.add('nodtd')
    if disable_multiprocessor: gui_settings.add('singlecpu')
    if trace_str: gui_settings.add(f'trace: "{trace_str}"')

    if system_disable_1G1R: system_exclusions_options.add('d')
    if system_prefer_regions: system_exclusions_options.add('r')
    if system_include_hashless: system_exclusions_options.add('e')
    if system_modern_platforms: system_exclusions_options.add('z')
    if system_demote_unlicensed: system_exclusions_options.add('y')
    if system_disable_filters: system_exclusions_options.add('nofilters')
    if system_split_regions: system_exclusions_options.add('regionsplit')
    if system_removes_dat: system_exclusions_options.add('removesdat')
    if system_keep_removes: system_exclusions_options.add('log')
    if system_list_1g1r_names: system_exclusions_options.add('listnames')
    if system_report_warnings: system_exclusions_options.add('warnings')
    if system_pause_on_warnings: system_exclusions_options.add('warningpause')
    if system_legacy_dat: system_exclusions_options.add('legacy')
    if system_bypass_dtd: system_exclusions_options.add('nodtd')
    if system_disable_multiprocessor: system_exclusions_options.add('singlecpu')
    if system_trace_str: system_exclusions_options.add(f'trace: "{system_trace_str}"')

    # Add the global excludes in
    exclude_str: str = ''.join(sorted(excludes, key=str.casefold))

    # Add the system excludes in
    system_exclude_str: str = ''.join(sorted(system_excludes, key=str.casefold))

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

    user_options_list: list[str] = sorted([x for x in gui_settings if x not in hidden_options])
    system_user_options_list: list[str] = sorted([x for x in system_exclusions_options if x not in hidden_options])

    if 'legacy' in gui_settings: user_options_list.append('x')
    if 'legacy' in system_exclusions_options: system_user_options_list.append('x')

    user_options_str: str = ''

    if user_options_list:
        user_options_str = f' (-{"".join(sorted(user_options_list))})'

    gui_settings.add(f'exclude: {exclude_str}')
    system_exclusions_options.add(f'exclude: {system_exclude_str}')

    gui_settings.add(f'output: {main_window.output_folder}')

    # Grab settings from the settings dialog if it's open
    if settings_window:
        if (
            settings_window.ui.labelCloneListsLocation.text() != str(pathlib.Path(config.path_clone_list).resolve())
            and settings_window.ui.labelCloneListsLocation.text() != 'No clone list folder selected'):
                gui_settings.add(f'clone lists folder: {settings_window.ui.labelCloneListsLocation.text()}')

        if (
            settings_window.ui.labelMetadataLocation.text() != str(pathlib.Path(config.path_metadata).resolve())
            and settings_window.ui.labelMetadataLocation.text() != 'No metadata folder selected'):
                gui_settings.add(f'metadata folder: {settings_window.ui.labelMetadataLocation.text()}')

        if (
            settings_window.ui.lineEditCloneListDownloadLocation.text() != str(config.clone_list_metadata_download_location)
            and settings_window.ui.lineEditCloneListDownloadLocation.text() != ''):
                gui_settings.add(f'clone list metadata url: {settings_window.ui.lineEditCloneListDownloadLocation.text()}')
    else:
        # Compensate if we can't get the settings from the dialog itself
        clone_lists_folder: str = ''
        metadata_folder: str = ''
        clone_list_metadata_url: str = ''

        if main_window.clone_lists_folder:
            clone_lists_folder = str(pathlib.Path(main_window.clone_lists_folder).resolve())
        else:
            clone_lists_folder = get_config_value(config.user_gui_settings, 'clone lists folder', config.path_metadata)

        if main_window.metadata_folder:
            metadata_folder = str(pathlib.Path(main_window.metadata_folder).resolve())
        else:
            metadata_folder = get_config_value(config.user_gui_settings, 'metadata folder', config.path_metadata)

        if main_window.clone_list_metadata_url:
            clone_list_metadata_url = main_window.clone_list_metadata_url
        else:
            clone_list_metadata_url = get_config_value(config.user_gui_settings, 'clone list metadata url', config.clone_list_metadata_download_location, path=False)

        if (
            clone_lists_folder
            and clone_lists_folder != str(pathlib.Path(config.path_clone_list).resolve())):
                gui_settings.add(f'clone lists folder: {clone_lists_folder}')
        if (
            metadata_folder
            and metadata_folder != str(pathlib.Path(config.path_metadata).resolve())):
                gui_settings.add(f'metadata folder: {metadata_folder}')
        if (
            clone_list_metadata_url
            and clone_list_metadata_url != config.clone_list_metadata_download_location):
                gui_settings.add(f'clone list metadata url: {clone_list_metadata_url}')

    generate_config(config.user_config_file, languages, regions, tuple(video_standards), config.user_filters_path, global_filters, system_filters, prefix_1g1r, suffix_1g1r, gui_settings, overwrite=True)
    if config.system_name:
        generate_config(f'{config.user_filters_path}/{config.system_name}.yaml', system_languages, system_regions, tuple(system_video_standards), config.user_filters_path, global_filters, system_filters, system_prefix_1g1r, system_suffix_1g1r, system_exclusions_options, overwrite=True, system_config=True, system_paths=system_override_paths, overrides=system_overrides)

    if run_retool:
        if dat_details:
            # Get a file list
            dat_files: list[pathlib.Path] = []

            main_window.ui.buttonStop.show()
            main_window.ui.mainProgram.setEnabled(False)

            for key in dat_details.keys():
                dat_files.append(pathlib.Path(dat_details[key]['filepath']))

            gui_input: UserInput

            for dat_file in dat_files:
                # Build the gui_input instance
                filter_languages_enabled: bool = False

                if selected_languages or system_selected_languages:
                    filter_languages_enabled = True

                gui_input = UserInput(
                    input_file_name = str(dat_file),
                    update = update_clone_list,
                    no_1g1r = disable_1G1R,
                    empty_titles = include_hashless,
                    filter_languages = filter_languages_enabled,
                    region_bias = prefer_regions,
                    legacy = legacy_dat,
                    demote_unl = demote_unlicensed,
                    modern = modern_platforms,
                    no_applications = exclude_applications,
                    no_audio = exclude_audio,
                    no_bad_dumps = exclude_bad_dumps,
                    no_bios = exclude_bios,
                    no_coverdiscs = exclude_coverdiscs,
                    no_demos = exclude_demos,
                    no_add_ons = exclude_add_ons,
                    no_educational = exclude_educational,
                    no_mia = exclude_mia,
                    no_manuals = exclude_manuals,
                    no_multimedia = exclude_multimedia,
                    no_bonus_discs = exclude_bonus_discs,
                    no_pirate = exclude_pirate,
                    no_preproduction = exclude_preproduction,
                    no_promotional = exclude_promotional,
                    no_unlicensed = exclude_unlicensed,
                    no_video = exclude_video,
                    clone_list = '',
                    user_config = '',
                    metadata = '',
                    no_filters = disable_filters,
                    list_names = list_1g1r_names,
                    log = keep_removes,
                    output_folder_name = main_window.output_folder,
                    output_region_split = split_regions,
                    output_remove_dat = removes_dat,
                    verbose = report_warnings,
                    warningpause = pause_on_warnings,
                    single_cpu = disable_multiprocessor,
                    trace = trace_str,
                    no_dtd = bypass_dtd,
                    excludes = exclude_str,
                    dev_mode = False,
                    user_options = user_options_str,
                    user_clone_list_location = clone_lists_folder,
                    user_clone_list_metadata_download_location = clone_list_metadata_url,
                    user_metadata_location = metadata_folder,
                    test = False # TODO
                )

                main_window.start_retool_thread(gui_input)
        else:
            gui_input = UserInput(
                    input_file_name = '',
                    update = update_clone_list,
                    no_1g1r = False,
                    empty_titles = False,
                    filter_languages = False,
                    region_bias = False,
                    legacy = False,
                    demote_unl = False,
                    modern = False,
                    no_applications = False,
                    no_audio = False,
                    no_bad_dumps = False,
                    no_bios = False,
                    no_coverdiscs = False,
                    no_demos = False,
                    no_add_ons = False,
                    no_educational = False,
                    no_mia = False,
                    no_manuals = False,
                    no_multimedia = False,
                    no_bonus_discs = False,
                    no_pirate = False,
                    no_preproduction = False,
                    no_promotional = False,
                    no_unlicensed = False,
                    no_video = False,
                    clone_list = '',
                    user_config = '',
                    metadata = '',
                    no_filters = False,
                    list_names = False,
                    log = False,
                    output_folder_name = '',
                    output_region_split = False,
                    output_remove_dat = False,
                    verbose = False,
                    warningpause = False,
                    single_cpu = False,
                    trace = '',
                    no_dtd = False,
                    excludes = '',
                    dev_mode = False,
                    user_options = '',
                    user_clone_list_location = '',
                    user_clone_list_metadata_download_location = clone_list_metadata_url,
                    user_metadata_location = '',
                    test = False
                )

            main_window.start_retool_thread(gui_input)