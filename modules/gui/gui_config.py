import pathlib
import re
from typing import Any

import modules.constants as const
from modules.config.config import Config
from modules.config.read_write_config import UserOverrides, generate_config
from modules.gui.gui_utils import enable_go_button
from modules.input import UserInput, get_config_value


def import_config() -> Config:
    """Builds a config object for the GUI that Retool understands."""
    config: Config = Config(
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION,
        const.CLONE_LIST_METADATA_DOWNLOAD_LOCATION_KEY,
        const.PROGRAM_DOWNLOAD_LOCATION,
        const.PROGRAM_DOWNLOAD_LOCATION_KEY,
        const.CONFIG_FILE,
        const.DAT_FILE_TAGS_KEY,
        const.IGNORE_TAGS_KEY,
        const.DISC_RENAME_KEY,
        const.VERSION_IGNORE_KEY,
        const.BUDGET_EDITIONS_KEY,
        const.PROMOTE_EDITIONS_KEY,
        const.DEMOTE_EDITIONS_KEY,
        const.MODERN_EDITIONS_KEY,
        const.LANGUAGES_KEY,
        const.REGION_ORDER_KEY,
        const.VIDEO_ORDER_KEY,
        const.CLONE_LISTS_KEY,
        const.METADATA_KEY,
        const.MIAS_KEY,
        const.RA_KEY,
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
        UserInput(),
        first_run_gui=True,
    )

    return config


def write_config(
    main_window: Any,
    dat_details: dict[str, dict[str, str]],
    config: Config,
    settings_window: Any = None,
    run_retool: bool = False,
    update_clone_list: bool = False,
) -> None:
    """
    Gets widgets' state, then writes the user-config.yaml file.

    Args:
        main_window (Any): The MainWindow widget.

        dat_details (dict[str, dict[str, str]]): The dictionary that carries DAT file
            details like its system name and filepath.

        config (Config): The Retool config object.

        settings_window (Any): The settings widget. Defaults to `None`.

        run_retool (bool, optional): Whether Retool should be run after a config write.
            Defaults to `False`.

        update_clone_list (bool, optional): Whether the user has requested a clone list
            update. Defaults to `False`.
    """
    # Check if the "Process DAT files" button should be enabled
    enable_go_button(main_window)

    # Global list widgets
    available_languages: list[str] = [
        main_window.ui.listWidgetGlobalAvailableLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalAvailableLanguages.count())
    ]
    available_regions: list[str] = [
        main_window.ui.listWidgetGlobalAvailableRegions.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalAvailableRegions.count())
    ]
    available_localizations: list[str] = [
        main_window.ui.listWidgetGlobalLocalizationAvailableLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalLocalizationAvailableLanguages.count())
    ]
    selected_languages: list[str] = [
        main_window.ui.listWidgetGlobalSelectedLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalSelectedLanguages.count())
    ]
    selected_regions: list[str] = [
        main_window.ui.listWidgetGlobalSelectedRegions.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalSelectedRegions.count())
    ]
    selected_localizations: list[str] = [
        main_window.ui.listWidgetGlobalLocalizationSelectedLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages.count())
    ]
    video_standards: list[str] = [
        main_window.ui.listWidgetGlobalVideoStandards.item(x).text()
        for x in range(main_window.ui.listWidgetGlobalVideoStandards.count())
    ]

    # System list widgets
    system_available_languages: list[str] = [
        main_window.ui.listWidgetSystemAvailableLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetSystemAvailableLanguages.count())
    ]
    system_available_regions: list[str] = [
        main_window.ui.listWidgetSystemAvailableRegions.item(x).text()
        for x in range(main_window.ui.listWidgetSystemAvailableRegions.count())
    ]
    system_available_localizations: list[str] = [
        main_window.ui.listWidgetSystemLocalizationAvailableLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetSystemLocalizationAvailableLanguages.count())
    ]
    system_selected_languages: list[str] = [
        main_window.ui.listWidgetSystemSelectedLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetSystemSelectedLanguages.count())
    ]
    system_selected_regions: list[str] = [
        main_window.ui.listWidgetSystemSelectedRegions.item(x).text()
        for x in range(main_window.ui.listWidgetSystemSelectedRegions.count())
    ]
    system_selected_localizations: list[str] = [
        main_window.ui.listWidgetSystemLocalizationSelectedLanguages.item(x).text()
        for x in range(main_window.ui.listWidgetSystemLocalizationSelectedLanguages.count())
    ]
    system_video_standards: list[str] = [
        main_window.ui.listWidgetSystemVideoStandards.item(x).text()
        for x in range(main_window.ui.listWidgetSystemVideoStandards.count())
    ]

    system_overrides_status = {
        'exclusions': str(main_window.ui.checkBoxSystemOverrideExclusions.isChecked()),
        'languages': str(main_window.ui.checkBoxSystemOverrideLanguages.isChecked()),
        'localizations': str(main_window.ui.checkBoxSystemOverrideLocalization.isChecked()),
        'options': str(main_window.ui.checkBoxSystemOverrideOptions.isChecked()),
        'paths': str(main_window.ui.checkBoxSystemOverridePaths.isChecked()),
        'post_filters': str(main_window.ui.checkBoxSystemOverridePostFilter.isChecked()),
        'regions': str(main_window.ui.checkBoxSystemOverrideRegions.isChecked()),
        'video': str(main_window.ui.checkBoxSystemOverrideVideo.isChecked()),
    }

    # System paths
    output_folder: str = ''
    clone_list: str = ''
    metadata_file: str = ''
    mia_file: str = ''
    ra_file: str = ''

    if main_window.system_output_folder != '.':
        output_folder = main_window.system_output_folder

    if main_window.system_clone_list != '.':
        clone_list = main_window.system_clone_list

    if main_window.system_metadata_file != '.':
        metadata_file = main_window.system_metadata_file

    if main_window.system_mia_file != '.':
        mia_file = main_window.system_mia_file

    if main_window.system_ra_file != '.':
        ra_file = main_window.system_ra_file

    system_override_paths: dict[str, str] = {
        'output': output_folder,
        'clone list': clone_list,
        'metadata file': metadata_file,
        'mia file': mia_file,
        'retroachievements file': ra_file,
    }

    # If English isn't being processed, make sure it's commented out and at the top of the list
    if 'English' in available_languages:
        available_languages = ['English'] + [x for x in available_languages if x != 'English']

    # Languages, regions, and localizations
    languages: tuple[str, ...] = tuple(
        [f'Comment|{x}' for x in available_languages] + selected_languages
    )
    regions: tuple[str, ...] = tuple([f'Comment|{x}' for x in available_regions] + selected_regions)
    localizations: tuple[str, ...] = tuple(
        [f'Comment|{x}' for x in available_localizations] + selected_localizations
    )

    system_languages: tuple[str, ...] = tuple(
        [f'Comment|{x}' for x in system_available_languages] + system_selected_languages
    )
    system_regions: tuple[str, ...] = tuple(
        [f'Comment|{x}' for x in system_available_regions] + system_selected_regions
    )
    system_localizations: tuple[str, ...] = tuple(
        [f'Comment|{x}' for x in system_available_localizations] + system_selected_localizations
    )

    # Global exclude options
    exclude_add_ons: bool = main_window.ui.checkBoxGlobalExcludeAddOns.isChecked()
    exclude_aftermarket: bool = main_window.ui.checkBoxGlobalExcludeAftermarket.isChecked()
    exclude_applications: bool = main_window.ui.checkBoxGlobalExcludeApplications.isChecked()
    exclude_audio: bool = main_window.ui.checkBoxGlobalExcludeAudio.isChecked()
    exclude_bad_dumps: bool = main_window.ui.checkBoxGlobalExcludeBadDumps.isChecked()
    exclude_bios: bool = main_window.ui.checkBoxGlobalExcludeBIOS.isChecked()
    exclude_bonus_discs: bool = main_window.ui.checkBoxGlobalExcludeBonusDiscs.isChecked()
    exclude_coverdiscs: bool = main_window.ui.checkBoxGlobalExcludeCoverdiscs.isChecked()
    exclude_demos: bool = main_window.ui.checkBoxGlobalExcludeDemos.isChecked()
    exclude_educational: bool = main_window.ui.checkBoxGlobalExcludeEducational.isChecked()
    exclude_games: bool = main_window.ui.checkBoxGlobalExcludeGames.isChecked()
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
    system_exclude_aftermarket: bool = main_window.ui.checkBoxSystemExcludeAftermarket.isChecked()
    system_exclude_applications: bool = main_window.ui.checkBoxSystemExcludeApplications.isChecked()
    system_exclude_audio: bool = main_window.ui.checkBoxSystemExcludeAudio.isChecked()
    system_exclude_bad_dumps: bool = main_window.ui.checkBoxSystemExcludeBadDumps.isChecked()
    system_exclude_bios: bool = main_window.ui.checkBoxSystemExcludeBIOS.isChecked()
    system_exclude_bonus_discs: bool = main_window.ui.checkBoxSystemExcludeBonusDiscs.isChecked()
    system_exclude_coverdiscs: bool = main_window.ui.checkBoxSystemExcludeCoverdiscs.isChecked()
    system_exclude_demos: bool = main_window.ui.checkBoxSystemExcludeDemos.isChecked()
    system_exclude_educational: bool = main_window.ui.checkBoxSystemExcludeEducational.isChecked()
    system_exclude_games: bool = main_window.ui.checkBoxSystemExcludeGames.isChecked()
    system_exclude_manuals: bool = main_window.ui.checkBoxSystemExcludeManuals.isChecked()
    system_exclude_mia: bool = main_window.ui.checkBoxSystemExcludeMIA.isChecked()
    system_exclude_multimedia: bool = main_window.ui.checkBoxSystemExcludeMultimedia.isChecked()
    system_exclude_pirate: bool = main_window.ui.checkBoxSystemExcludePirate.isChecked()
    system_exclude_preproduction: bool = (
        main_window.ui.checkBoxSystemExcludePreproduction.isChecked()
    )
    system_exclude_promotional: bool = main_window.ui.checkBoxSystemExcludePromotional.isChecked()
    system_exclude_unlicensed: bool = main_window.ui.checkBoxSystemExcludeUnlicensed.isChecked()
    system_exclude_video: bool = main_window.ui.checkBoxSystemExcludeVideo.isChecked()

    # Global options
    disable_1G1R: bool = main_window.ui.checkBoxGlobalOptionsDisable1G1R.isChecked()
    prefer_regions: bool = main_window.ui.checkBoxGlobalOptionsPreferRegions.isChecked()
    prefer_oldest: bool = main_window.ui.checkBoxGlobalOptionsPreferOldest.isChecked()
    prefer_retro: bool = main_window.ui.checkBoxGlobalOptionsPreferRetro.isChecked()
    modern_platforms: bool = main_window.ui.checkBoxGlobalOptionsModernPlatforms.isChecked()
    demote_unlicensed: bool = main_window.ui.checkBoxGlobalOptionsDemoteUnlicensed.isChecked()
    disable_overrides: bool = main_window.ui.checkBoxGlobalOptionsDisableOverrides.isChecked()

    compilations: str = ''

    if main_window.ui.comboBoxGlobalChooseCompilationsMode.currentIndex() == 0:
        compilations = ''
        main_window.ui.labelGlobalCompilationsExplanation.setText(const.COMPILATIONS_DEFAULT)
    elif main_window.ui.comboBoxGlobalChooseCompilationsMode.currentIndex() == 1:
        compilations = 'i'
        main_window.ui.labelGlobalCompilationsExplanation.setText(const.COMPILATIONS_INDIVIDUAL)
    elif main_window.ui.comboBoxGlobalChooseCompilationsMode.currentIndex() == 2:
        compilations = 'k'
        main_window.ui.labelGlobalCompilationsExplanation.setText(const.COMPILATIONS_KEEP)
    elif main_window.ui.comboBoxGlobalChooseCompilationsMode.currentIndex() == 3:
        compilations = 'o'
        main_window.ui.labelGlobalCompilationsExplanation.setText(const.COMPILATIONS_OPTIMIZE)

    split_regions: bool = main_window.ui.checkBoxGlobalOptionsSplitRegions.isChecked()
    removes_dat: bool = main_window.ui.checkBoxGlobalOptionsRemovesDat.isChecked()
    replace_dat: bool = main_window.ui.checkBoxGlobalReplaceInputDats.isChecked()
    reprocess: bool = main_window.ui.checkBoxGlobalOptionsAlreadyProcessed.isChecked()
    keep_removes: bool = main_window.ui.checkBoxGlobalOptionsKeepRemove.isChecked()
    use_machine: bool = main_window.ui.checkBoxGlobalOptionsUseMachine.isChecked()
    label_mia: bool = main_window.ui.checkBoxGlobalOptionsMIA.isChecked()
    label_retro: bool = main_window.ui.checkBoxGlobalOptionsRetroAchievements.isChecked()
    use_original_header: bool = main_window.ui.checkBoxGlobalOptionsOriginalHeader.isChecked()
    list_1g1r_names: bool = main_window.ui.checkBoxGlobalOptions1G1RNames.isChecked()
    report_warnings: bool = main_window.ui.checkBoxGlobalOptionsReportWarnings.isChecked()
    pause_on_warnings: bool = main_window.ui.checkBoxGlobalOptionsPauseWarnings.isChecked()
    legacy_dat: bool = main_window.ui.checkBoxGlobalOptionsLegacy.isChecked()
    disable_multiprocessor: bool = main_window.ui.checkBoxGlobalOptionsDisableMultiCPU.isChecked()
    trace: bool = main_window.ui.checkBoxGlobalOptionsTrace.isChecked()

    prefix_1g1r: str = (
        main_window.ui.lineEditGlobalOptions1G1RPrefix.text()
        .replace('\\', '\\\\')
        .replace('"', '\\"')
    )
    suffix_1g1r: str = (
        main_window.ui.lineEditGlobalOptions1G1RSuffix.text()
        .replace('\\', '\\\\')
        .replace('"', '\\"')
    )

    trace_str: str = ''

    if trace:
        trace_str = (
            main_window.ui.lineEditGlobalOptionsTrace.text()
            .replace('\\', '\\\\')
            .replace('"', '\\"')
        )

    # System options
    system_disable_1G1R: bool = main_window.ui.checkBoxSystemOptionsDisable1G1R.isChecked()
    system_prefer_regions: bool = main_window.ui.checkBoxSystemOptionsPreferRegions.isChecked()
    system_prefer_oldest: bool = main_window.ui.checkBoxSystemOptionsPreferOldest.isChecked()
    system_prefer_retro: bool = main_window.ui.checkBoxSystemOptionsPreferRetro.isChecked()
    system_modern_platforms: bool = main_window.ui.checkBoxSystemOptionsModernPlatforms.isChecked()
    system_demote_unlicensed: bool = (
        main_window.ui.checkBoxSystemOptionsDemoteUnlicensed.isChecked()
    )
    system_disable_overrides: bool = (
        main_window.ui.checkBoxSystemOptionsDisableOverrides.isChecked()
    )

    system_compilations: str = ''

    if main_window.ui.comboBoxSystemChooseCompilationsMode.currentIndex() == 0:
        system_compilations = ''
        main_window.ui.labelSystemCompilationsExplanation.setText(const.COMPILATIONS_DEFAULT)
    elif main_window.ui.comboBoxSystemChooseCompilationsMode.currentIndex() == 1:
        system_compilations = 'i'
        main_window.ui.labelSystemCompilationsExplanation.setText(const.COMPILATIONS_INDIVIDUAL)
    elif main_window.ui.comboBoxSystemChooseCompilationsMode.currentIndex() == 2:
        system_compilations = 'k'
        main_window.ui.labelSystemCompilationsExplanation.setText(const.COMPILATIONS_KEEP)
    elif main_window.ui.comboBoxSystemChooseCompilationsMode.currentIndex() == 3:
        system_compilations = 'o'
        main_window.ui.labelSystemCompilationsExplanation.setText(const.COMPILATIONS_OPTIMIZE)

    system_split_regions: bool = main_window.ui.checkBoxSystemOptionsSplitRegions.isChecked()
    system_removes_dat: bool = main_window.ui.checkBoxSystemOptionsRemovesDat.isChecked()
    system_replace_dat: bool = main_window.ui.checkBoxSystemReplaceInputDats.isChecked()
    system_reprocess: bool = main_window.ui.checkBoxSystemOptionsAlreadyProcessed.isChecked()
    system_keep_removes: bool = main_window.ui.checkBoxSystemOptionsKeepRemove.isChecked()
    system_use_machine: bool = main_window.ui.checkBoxSystemOptionsUseMachine.isChecked()
    system_label_mia: bool = main_window.ui.checkBoxSystemOptionsMIA.isChecked()
    system_label_retro: bool = main_window.ui.checkBoxSystemOptionsRetroAchievements.isChecked()
    system_use_original_header: bool = (
        main_window.ui.checkBoxSystemOptionsOriginalHeader.isChecked()
    )
    system_list_1g1r_names: bool = main_window.ui.checkBoxSystemOptions1G1RNames.isChecked()
    system_report_warnings: bool = main_window.ui.checkBoxSystemOptionsReportWarnings.isChecked()
    system_pause_on_warnings: bool = main_window.ui.checkBoxSystemOptionsPauseWarnings.isChecked()
    system_legacy_dat: bool = main_window.ui.checkBoxSystemOptionsLegacy.isChecked()
    system_disable_multiprocessor: bool = (
        main_window.ui.checkBoxSystemOptionsDisableMultiCPU.isChecked()
    )
    system_trace: bool = main_window.ui.checkBoxSystemOptionsTrace.isChecked()

    system_prefix_1g1r: str = (
        main_window.ui.lineEditSystemOptions1G1RPrefix.text()
        .replace('\\', '\\\\')
        .replace('"', '\\"')
    )
    system_suffix_1g1r: str = (
        main_window.ui.lineEditSystemOptions1G1RSuffix.text()
        .replace('\\', '\\\\')
        .replace('"', '\\"')
    )

    system_trace_str: str = ''

    if system_trace:
        system_trace_str = (
            main_window.ui.lineEditSystemOptionsTrace.text()
            .replace('\\', '\\\\')
            .replace('"', '\\"')
        )

    # Global overrides
    global_exclude_overrides: list[str] = []
    global_include_overrides: list[str] = []

    if main_window.ui.textEditGlobalExclude.toPlainText():
        global_exclude_overrides = main_window.ui.textEditGlobalExclude.toPlainText().split('\n')
        global_exclude_overrides = [
            x.replace('\\', '\\\\').replace('"', '\\"') for x in global_exclude_overrides if x
        ]
    if main_window.ui.textEditGlobalInclude.toPlainText():
        global_include_overrides = main_window.ui.textEditGlobalInclude.toPlainText().split('\n')
        global_include_overrides = [
            x.replace('\\', '\\\\').replace('"', '\\"') for x in global_include_overrides if x
        ]

    global_overrides: UserOverrides = UserOverrides(
        global_exclude_overrides, global_include_overrides
    )

    # System overrides
    system_exclude_overrides: list[str] = []
    system_include_overrides: list[str] = []

    if main_window.ui.textEditSystemExclude.toPlainText():
        system_exclude_overrides = main_window.ui.textEditSystemExclude.toPlainText().split('\n')
        system_exclude_overrides = [
            x.replace('\\', '\\\\').replace('"', '\\"') for x in system_exclude_overrides if x
        ]
    if main_window.ui.textEditSystemInclude.toPlainText():
        system_include_overrides = main_window.ui.textEditSystemInclude.toPlainText().split('\n')
        system_include_overrides = [
            x.replace('\\', '\\\\').replace('"', '\\"') for x in system_include_overrides if x
        ]

    system_overrides: UserOverrides = UserOverrides(
        system_exclude_overrides, system_include_overrides
    )

    # Global post filters
    global_filters: list[str] = []

    if main_window.ui.textEditGlobalFilterInclude.toPlainText():
        global_filters = main_window.ui.textEditGlobalFilterInclude.toPlainText().split('\n')
        global_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in global_filters if x]

    # System post filters
    system_filters: list[str] = []

    if main_window.ui.textEditSystemFilterInclude.toPlainText():
        system_filters = main_window.ui.textEditSystemFilterInclude.toPlainText().split('\n')
        system_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in system_filters if x]

    # Excludes
    excludes: set[str] = set()
    system_excludes: set[str] = set()

    if exclude_add_ons:
        excludes.add('D')
    if exclude_applications:
        excludes.add('a')
    if exclude_audio:
        excludes.add('A')
    if exclude_bad_dumps:
        excludes.add('b')
    if exclude_bios:
        excludes.add('B')
    if exclude_bonus_discs:
        excludes.add('o')
    if exclude_coverdiscs:
        excludes.add('c')
    if exclude_demos:
        excludes.add('d')
    if exclude_educational:
        excludes.add('e')
    if exclude_aftermarket:
        excludes.add('f')
    if exclude_games:
        excludes.add('g')
    if exclude_manuals:
        excludes.add('m')
    if exclude_mia:
        excludes.add('k')
    if exclude_multimedia:
        excludes.add('M')
    if exclude_pirate:
        excludes.add('p')
    if exclude_preproduction:
        excludes.add('P')
    if exclude_promotional:
        excludes.add('r')
    if exclude_unlicensed:
        excludes.add('u')
    if exclude_video:
        excludes.add('v')

    if system_exclude_add_ons:
        system_excludes.add('D')
    if system_exclude_applications:
        system_excludes.add('a')
    if system_exclude_audio:
        system_excludes.add('A')
    if system_exclude_bad_dumps:
        system_excludes.add('b')
    if system_exclude_bios:
        system_excludes.add('B')
    if system_exclude_bonus_discs:
        system_excludes.add('o')
    if system_exclude_coverdiscs:
        system_excludes.add('c')
    if system_exclude_demos:
        system_excludes.add('d')
    if system_exclude_educational:
        system_excludes.add('e')
    if system_exclude_aftermarket:
        system_excludes.add('f')
    if system_exclude_games:
        system_excludes.add('g')
    if system_exclude_manuals:
        system_excludes.add('m')
    if system_exclude_mia:
        system_excludes.add('k')
    if system_exclude_multimedia:
        system_excludes.add('M')
    if system_exclude_pirate:
        system_excludes.add('p')
    if system_exclude_preproduction:
        system_excludes.add('P')
    if system_exclude_promotional:
        system_excludes.add('r')
    if system_exclude_unlicensed:
        system_excludes.add('u')
    if system_exclude_video:
        system_excludes.add('v')

    gui_settings: set[str] = set()
    system_exclusions_options: set[str] = set()

    if disable_1G1R:
        gui_settings.add('d')
    if prefer_regions:
        gui_settings.add('r')
    if prefer_oldest:
        gui_settings.add('o')
    if prefer_retro:
        gui_settings.add('c')
    if modern_platforms:
        gui_settings.add('z')
    if demote_unlicensed:
        gui_settings.add('y')
    if disable_overrides:
        gui_settings.add('nooverrides')
    if compilations:
        gui_settings.add(f'compilations: {compilations}')
    if split_regions:
        gui_settings.add('regionsplit')
    if removes_dat:
        gui_settings.add('removesdat')
    if replace_dat:
        gui_settings.add('replace')
    if reprocess:
        gui_settings.add('reprocess')
    if keep_removes:
        gui_settings.add('report')
    if use_machine:
        gui_settings.add('machine')
    if label_mia:
        gui_settings.add('labelmia')
    if label_retro:
        gui_settings.add('labelretro')
    if use_original_header:
        gui_settings.add('originalheader')
    if list_1g1r_names:
        gui_settings.add('listnames')
    if report_warnings:
        gui_settings.add('warnings')
    if pause_on_warnings:
        gui_settings.add('warningpause')
    if legacy_dat:
        gui_settings.add('legacy')
    if disable_multiprocessor:
        gui_settings.add('singlecpu')
    if trace_str:
        gui_settings.add(f'trace: "{trace_str}"')

    if system_disable_1G1R:
        system_exclusions_options.add('d')
    if system_prefer_regions:
        system_exclusions_options.add('r')
    if system_prefer_oldest:
        system_exclusions_options.add('o')
    if system_prefer_retro:
        system_exclusions_options.add('c')
    if system_modern_platforms:
        system_exclusions_options.add('z')
    if system_demote_unlicensed:
        system_exclusions_options.add('y')
    if system_disable_overrides:
        system_exclusions_options.add('nooverrides')
    if system_compilations:
        system_exclusions_options.add(f'compilations: {system_compilations}')
    if system_split_regions:
        system_exclusions_options.add('regionsplit')
    if system_removes_dat:
        system_exclusions_options.add('removesdat')
    if system_replace_dat:
        system_exclusions_options.add('replace')
    if system_reprocess:
        system_exclusions_options.add('reprocess')
    if system_keep_removes:
        system_exclusions_options.add('report')
    if system_use_machine:
        system_exclusions_options.add('machine')
    if system_label_mia:
        system_exclusions_options.add('labelmia')
    if system_label_retro:
        system_exclusions_options.add('labelretro')
    if system_use_original_header:
        system_exclusions_options.add('originalheader')
    if system_list_1g1r_names:
        system_exclusions_options.add('listnames')
    if system_report_warnings:
        system_exclusions_options.add('warnings')
    if system_pause_on_warnings:
        system_exclusions_options.add('warningpause')
    if system_legacy_dat:
        system_exclusions_options.add('legacy')
    if system_disable_multiprocessor:
        system_exclusions_options.add('singlecpu')
    if system_trace_str:
        system_exclusions_options.add(f'trace: "{system_trace_str}"')

    # Add the global excludes in
    exclude_str: str = ''.join(sorted(excludes, key=lambda s: s.lower()))

    # Add the system excludes in
    system_exclude_str: str = ''.join(sorted(system_excludes, key=lambda s: s.lower()))

    hidden_options: tuple[str, ...] = (
        'Input',
        'output',
        'clonelist',
        'compilations',
        'config',
        'e',
        'exclude',
        'legacy',
        'labelmia',
        'labelretro',
        'listnames',
        'machine',
        'metadata',
        'mia',
        'mianooverrides',
        'originalheader',
        'q',
        'regionsplit',
        'removesdat',
        'replace',
        'report',
        'reprocess',
        'retroachievements',
        'singlecpu',
        'test',
        'trace',
        'warnings',
        'warningpause',
    )

    user_options_list: list[str] = sorted([x for x in gui_settings if x not in hidden_options])
    system_user_options_list: list[str] = sorted(
        [x for x in system_exclusions_options for x in hidden_options]
    )

    # Remove dynamic entries
    user_options_list = [
        x for x in user_options_list if not re.search('(compilations|trace):.*?', x)
    ]
    system_user_options_list = [
        x for x in system_user_options_list if not re.search('(compilations|trace):.*?', x)
    ]

    if 'legacy' in gui_settings:
        user_options_list.append('x')

    if 'legacy' in system_exclusions_options:
        system_user_options_list.append('x')

    if selected_localizations or (
        main_window.ui.checkBoxSystemOverrideLocalization.isChecked()
        and system_selected_localizations
    ):
        user_options_list.append('n')

    user_options_str: str = ''

    if user_options_list:
        user_options_str = f' (-{"".join(sorted(user_options_list))})'

    exclude_str_space: str = ''
    system_exclude_str_space: str = ''

    if exclude_str:
        exclude_str_space = ' '

    if system_exclude_str:
        system_exclude_str_space = ' '

    gui_settings.add(f'exclude:{exclude_str_space}{exclude_str}')
    system_exclusions_options.add(f'exclude:{system_exclude_str_space}{system_exclude_str}')

    gui_settings.add(f'output: {main_window.output_folder}')

    # Get the current window size
    gui_settings.add(f'gui width: {main_window.width()}\n- gui height: {main_window.height()}')

    # Get the current file list size
    gui_settings.add(
        f'gui split left: {main_window.ui.splitter.sizes()[0]}\n- gui split right: {main_window.ui.splitter.sizes()[1]}'
    )

    # Grab settings from the settings dialog if it's open
    if settings_window:
        if (
            settings_window.ui.labelCloneListsLocation.text()
            != str(pathlib.Path(config.path_clone_list).resolve())
            and settings_window.ui.labelCloneListsLocation.text() != 'No clone list folder selected'
        ):
            gui_settings.add(
                f'clone lists folder: {settings_window.ui.labelCloneListsLocation.text()}'
            )

        if (
            settings_window.ui.labelMetadataLocation.text()
            != str(pathlib.Path(config.path_metadata).resolve())
            and settings_window.ui.labelMetadataLocation.text() != 'No metadata folder selected'
        ):
            gui_settings.add(f'metadata folder: {settings_window.ui.labelMetadataLocation.text()}')

        if (
            settings_window.ui.labelMIALocation.text()
            != str(pathlib.Path(config.path_mia).resolve())
            and settings_window.ui.labelMIALocation.text() != 'No MIA folder selected'
        ):
            gui_settings.add(f'mia folder: {settings_window.ui.labelMIALocation.text()}')

        if (
            settings_window.ui.labelRALocation.text() != str(pathlib.Path(config.path_ra).resolve())
            and settings_window.ui.labelRALocation.text() != 'No RetroAchievements folder selected'
        ):
            gui_settings.add(
                f'retroachievements folder: {settings_window.ui.labelRALocation.text()}'
            )

        if (
            settings_window.ui.labelQuickImportLocation.text()
            != str(pathlib.Path(config.path_quick_import).resolve())
            and settings_window.ui.labelQuickImportLocation.text()
            != 'No quick import folder selected'
        ):
            gui_settings.add(
                f'quick import folder: {settings_window.ui.labelQuickImportLocation.text()}'
            )

        if (
            settings_window.ui.lineEditCloneListDownloadLocation.text()
            != str(config.clone_list_metadata_download_location)
            and settings_window.ui.lineEditCloneListDownloadLocation.text() != ''
        ):
            gui_settings.add(
                f'clone list metadata url: {settings_window.ui.lineEditCloneListDownloadLocation.text()}'
            )
    else:
        # Compensate if we can't get the settings from the dialog itself
        clone_lists_folder: str = ''
        metadata_folder: str = ''
        mia_folder: str = ''
        ra_folder: str = ''
        quick_import_folder: str = ''
        clone_list_metadata_url: str = ''

        if main_window.clone_lists_folder:
            clone_lists_folder = str(pathlib.Path(main_window.clone_lists_folder).resolve())
        else:
            clone_lists_folder = get_config_value(
                config.user_gui_settings, 'clone lists folder', str(config.path_clone_list)
            )

        if main_window.metadata_folder:
            metadata_folder = str(pathlib.Path(main_window.metadata_folder).resolve())
        else:
            metadata_folder = get_config_value(
                config.user_gui_settings, 'metadata folder', str(config.path_metadata)
            )

        if main_window.mia_folder:
            mia_folder = str(pathlib.Path(main_window.mia_folder).resolve())
        else:
            mia_folder = get_config_value(
                config.user_gui_settings, 'mia folder', str(config.path_mia)
            )

        if main_window.ra_folder:
            ra_folder = str(pathlib.Path(main_window.ra_folder).resolve())
        else:
            ra_folder = get_config_value(
                config.user_gui_settings, 'retroachievements folder', str(config.path_ra)
            )

        if main_window.quick_import_folder:
            quick_import_folder = str(pathlib.Path(main_window.quick_import_folder).resolve())
        else:
            quick_import_folder = get_config_value(
                config.user_gui_settings, 'quick import folder', config.path_quick_import
            )

        if main_window.clone_list_metadata_url:
            clone_list_metadata_url = main_window.clone_list_metadata_url
        else:
            clone_list_metadata_url = get_config_value(
                config.user_gui_settings,
                'clone list metadata url',
                config.clone_list_metadata_download_location,
                is_path=False,
            )

        if clone_lists_folder and clone_lists_folder != str(
            pathlib.Path(config.path_clone_list).resolve()
        ):
            gui_settings.add(f'clone lists folder: {clone_lists_folder}')

        if metadata_folder and metadata_folder != str(pathlib.Path(config.path_metadata).resolve()):
            gui_settings.add(f'metadata folder: {metadata_folder}')

        if mia_folder and mia_folder != str(pathlib.Path(config.path_mia).resolve()):
            gui_settings.add(f'mia folder: {mia_folder}')

        if ra_folder and ra_folder != str(pathlib.Path(config.path_ra).resolve()):
            gui_settings.add(f'retroachievements folder: {ra_folder}')

        if quick_import_folder and quick_import_folder != str(
            pathlib.Path(config.path_quick_import).resolve()
        ):
            gui_settings.add(f'quick import folder: {quick_import_folder}')

        if (
            clone_list_metadata_url
            and clone_list_metadata_url != config.clone_list_metadata_download_location
        ):
            gui_settings.add(f'clone list metadata url: {clone_list_metadata_url}')

    generate_config(
        config.user_config_file,
        languages,
        regions,
        localizations,
        tuple(video_standards),
        config.system_settings_path,
        global_overrides,
        system_overrides,
        global_filters,
        system_filters,
        prefix_1g1r,
        suffix_1g1r,
        gui_settings,
        overwrite=True,
    )
    if config.system_name:
        system_config_path: str = f'{config.system_settings_path}/{config.system_name}.yaml'
        system_config_path = str(
            f'{pathlib.Path(config.retool_location).joinpath(system_config_path)}'
        )
        generate_config(
            system_config_path,
            system_languages,
            system_regions,
            system_localizations,
            tuple(system_video_standards),
            config.system_settings_path,
            global_overrides,
            system_overrides,
            global_filters,
            system_filters,
            system_prefix_1g1r,
            system_suffix_1g1r,
            system_exclusions_options,
            overwrite=True,
            system_config=True,
            system_paths=system_override_paths,
            override_status=system_overrides_status,
        )

    if run_retool:
        if dat_details:
            # Get a file list
            dat_files: list[pathlib.Path] = []

            main_window.ui.buttonGo.hide()
            main_window.ui.buttonStop.show()
            main_window.ui.frame.setEnabled(False)

            for key in dat_details.keys():
                dat_files.append(pathlib.Path(dat_details[key]['filepath']))

            gui_input: UserInput

            # Manage escapes in the trace string
            trace_str = rf'{trace_str}'.replace('\\\\', '\\')

            for dat_file in dat_files:
                # Build the gui_input instance
                filter_languages_enabled: bool = False
                use_local_names: bool = False

                if selected_languages or (
                    main_window.ui.checkBoxSystemOverrideLanguages.isChecked()
                    and system_selected_languages
                ):
                    filter_languages_enabled = True

                if selected_localizations or (
                    main_window.ui.checkBoxSystemOverrideLocalization.isChecked()
                    and system_selected_localizations
                ):
                    use_local_names = True

                gui_input = UserInput(
                    input_file_name=str(dat_file),
                    update=update_clone_list,
                    no_1g1r=disable_1G1R,
                    filter_languages=filter_languages_enabled,
                    local_names=use_local_names,
                    oldest=prefer_oldest,
                    retroachievements=prefer_retro,
                    region_bias=prefer_regions,
                    legacy=legacy_dat,
                    demote_unl=demote_unlicensed,
                    modern=modern_platforms,
                    compilations=compilations,
                    no_applications=exclude_applications,
                    no_audio=exclude_audio,
                    no_bad_dumps=exclude_bad_dumps,
                    no_bios=exclude_bios,
                    no_coverdiscs=exclude_coverdiscs,
                    no_demos=exclude_demos,
                    no_add_ons=exclude_add_ons,
                    no_educational=exclude_educational,
                    no_aftermarket=exclude_aftermarket,
                    no_games=exclude_games,
                    no_mia=exclude_mia,
                    no_manuals=exclude_manuals,
                    no_multimedia=exclude_multimedia,
                    no_bonus_discs=exclude_bonus_discs,
                    no_pirate=exclude_pirate,
                    no_preproduction=exclude_preproduction,
                    no_promotional=exclude_promotional,
                    no_unlicensed=exclude_unlicensed,
                    no_video=exclude_video,
                    clone_list='',
                    user_config='',
                    metadata='',
                    mia='',
                    ra='',
                    no_overrides=disable_overrides,
                    list_names=list_1g1r_names,
                    report=keep_removes,
                    machine_not_game=use_machine,
                    label_mia=label_mia,
                    label_retro=label_retro,
                    original_header=use_original_header,
                    output_folder_name=main_window.output_folder,
                    output_region_split=split_regions,
                    output_remove_dat=removes_dat,
                    replace=replace_dat,
                    reprocess_dat=reprocess,
                    verbose=report_warnings,
                    warningpause=pause_on_warnings,
                    single_cpu=disable_multiprocessor,
                    trace=trace_str,
                    excludes=exclude_str,
                    dev_mode=False,
                    user_options=user_options_str,
                    user_clone_list_location=clone_lists_folder,
                    user_clone_list_metadata_download_location=clone_list_metadata_url,
                    user_metadata_location=metadata_folder,
                    user_mia_location=mia_folder,
                    user_ra_location=ra_folder,
                    test=False,
                )

                main_window.start_retool_thread(gui_input)
        else:
            gui_input = UserInput(
                input_file_name='',
                update=update_clone_list,
                no_1g1r=False,
                filter_languages=False,
                local_names=False,
                oldest=False,
                retroachievements=False,
                region_bias=False,
                legacy=False,
                demote_unl=False,
                modern=False,
                compilations='',
                no_applications=False,
                no_audio=False,
                no_bad_dumps=False,
                no_bios=False,
                no_coverdiscs=False,
                no_demos=False,
                no_add_ons=False,
                no_educational=False,
                no_aftermarket=False,
                no_games=False,
                no_mia=False,
                no_manuals=False,
                no_multimedia=False,
                no_bonus_discs=False,
                no_pirate=False,
                no_preproduction=False,
                no_promotional=False,
                no_unlicensed=False,
                no_video=False,
                clone_list='',
                user_config='',
                metadata='',
                mia='',
                ra='',
                no_overrides=False,
                list_names=False,
                report=False,
                machine_not_game=False,
                label_mia=False,
                label_retro=False,
                original_header=False,
                output_folder_name='',
                output_region_split=False,
                output_remove_dat=False,
                replace=False,
                reprocess_dat=False,
                verbose=False,
                warningpause=False,
                single_cpu=False,
                trace='',
                excludes='',
                dev_mode=False,
                user_options='',
                user_clone_list_location='',
                user_clone_list_metadata_download_location=clone_list_metadata_url,
                user_metadata_location='',
                user_mia_location='',
                user_ra_location='',
                test=False,
            )

            main_window.start_retool_thread(gui_input)
