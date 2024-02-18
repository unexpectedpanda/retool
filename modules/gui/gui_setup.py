import darkdetect # type: ignore
import pathlib
import webbrowser

from typing import Any

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from modules.constants import *
from modules.config import Config
from modules.gui.gui_config import write_config
from modules.gui.gui_utils import add_list_items, disable_incompatible_checkbox, move_list_items, order_list_items, remove_list_items, set_path, select_checkboxes, system_enable, show_hide
from modules.gui.windows import AboutWindow, SettingsWindow, TitleToolWindow
from modules.input import get_config_value, import_system_settings
from modules.utils import eprint, Font


def default_english_order(main_window: Any, region_order_default: list[str], regions_list: str) -> None:
    """ Sets the specified regions list to the default English order.

    Args:
        - `main_window (Any)` The MainWindow widget.

        - `region_order_default (list[str])` The default region order.

        - `regions_list (str)` The regions list to modify. Valid values are `global` and
          `system`.
    """

    if regions_list == 'global':
        main_window.ui.listWidgetGlobalAvailableRegions.clear()
        main_window.ui.listWidgetGlobalSelectedRegions.clear()
        main_window.ui.listWidgetGlobalSelectedRegions.addItems(region_order_default)
    elif regions_list == 'system':
        main_window.ui.listWidgetSystemAvailableRegions.clear()
        main_window.ui.listWidgetSystemSelectedRegions.clear()
        main_window.ui.listWidgetSystemSelectedRegions.addItems(region_order_default)


def setup_gui_global(main_window: Any, dat_details: dict[str, dict[str, str]], config: Config) -> None:
    """ Populates the global GUI with data from config files, and sets up interactions.

    Args:
        - `main_window (Any)` The MainWindow widget.

        - `dat_details (dict[str, dict[str, str]])` The dictionary that carries DAT file
          details like its system name and filepath.

        - `config (Config)` The Retool config object.
    """

    # Reset the window size and splitter widths if they're available in user-config.yaml
    window_width: int = 0
    window_height: int = 0

    try:
        window_width = int(get_config_value(config.user_gui_settings, 'gui width', '0', False))
    except:
        pass

    try:
        window_height = int(get_config_value(config.user_gui_settings, 'gui height', '0', False))
    except:
        pass

    if window_width and window_height:
        main_window.resize(window_width, window_height)

    gui_split_left: int = 0
    gui_split_right: int = 0

    try:
        gui_split_left = int(get_config_value(config.user_gui_settings, 'gui split left', '0', False))
    except:
        pass

    try:
        gui_split_right = int(get_config_value(config.user_gui_settings, 'gui split right', '0', False))
    except:
        pass

    if gui_split_left and gui_split_right:
        main_window.ui.splitter.setSizes([gui_split_left, gui_split_right])

    # Change link colors if dark mode is detected
    if darkdetect.isDark():
        main_window.ui.labelGlobalOverride.setText(main_window.ui.labelGlobalOverride.text().replace('color:#0000ff', 'color:#47aae9'))
        main_window.ui.labelGlobalFilters.setText(main_window.ui.labelGlobalFilters.text().replace('color:#0000ff', 'color:#47aae9'))
        main_window.ui.labelGlobalLocalizeNames.setText(main_window.ui.labelGlobalLocalizeNames.text().replace('color:#0000ff', 'color:#47aae9'))
        main_window.ui.labelSystemOverride.setText(main_window.ui.labelSystemOverride.text().replace('color:#0000ff', 'color:#47aae9'))
        main_window.ui.labelSystemFilters.setText(main_window.ui.labelSystemFilters.text().replace('color:#0000ff', 'color:#47aae9'))
        main_window.ui.labelSystemLocalizeNames.setText(main_window.ui.labelSystemLocalizeNames.text().replace('color:#0000ff', 'color:#47aae9'))

    # Remove United Kingdom from the region lists, as UK is already in there.
    region_order_user: list[str] = [x for x in config.region_order_user if x != 'United Kingdom']
    region_order_default: list[str] = [x for x in config.region_order_default if x != 'United Kingdom']

    # Populate the global regions
    main_window.ui.listWidgetGlobalSelectedRegions.addItems(region_order_user)
    main_window.ui.listWidgetGlobalAvailableRegions.addItems(sorted([x for x in region_order_default if x not in region_order_user]))

    # Add languages to the language lists
    languages_user: list[str] = []

    if config.languages_user_found:
        for language in config.language_order_user:
            for key, value in config.languages.items():
                if language == value:
                    languages_user.append(key)

    main_window.ui.listWidgetGlobalSelectedLanguages.addItems(languages_user)
    main_window.ui.listWidgetGlobalAvailableLanguages.addItems(sorted([x for x in config.languages if x not in languages_user]))

    # Add languages to the localization lists
    localization_user: list[str] = []

    for language in config.localization_order_user:
        for key, value in config.languages.items():
            if language == value:
                localization_user.append(key)

    main_window.ui.listWidgetGlobalLocalizationSelectedLanguages.addItems(localization_user)
    main_window.ui.listWidgetGlobalLocalizationAvailableLanguages.addItems(sorted([x for x in config.languages if x not in localization_user]))

    # Add video standards to the video list
    if config.video_order_user:
        main_window.ui.listWidgetGlobalVideoStandards.addItems([x for x in config.video_order_user])
    else:
        main_window.ui.listWidgetGlobalVideoStandards.addItems([x for x in config.video_order_default])

    # Apply other settings from user-config.yaml
    if config.global_exclude: main_window.ui.textEditGlobalExclude.setText('\n'.join(config.global_exclude))
    if config.global_include: main_window.ui.textEditGlobalInclude.setText('\n'.join(config.global_include))
    if config.global_filter: main_window.ui.textEditGlobalFilterInclude.setText('\n'.join(config.global_filter))
    if config.user_prefix: main_window.ui.lineEditGlobalOptions1G1RPrefix.setText(config.user_prefix)
    if config.user_suffix: main_window.ui.lineEditGlobalOptions1G1RSuffix.setText(config.user_suffix)

    # Set attributes on the main window so they can be carried to other functions.
    main_window.output_folder = str(pathlib.Path.cwd())

    main_window.clone_lists_folder = get_config_value(config.user_gui_settings, 'clone lists folder', config.path_clone_list)
    main_window.metadata_folder = get_config_value(config.user_gui_settings, 'metadata folder', config.path_metadata)
    main_window.clone_list_metadata_url = get_config_value(config.user_gui_settings, 'clone list metadata url', config.clone_list_metadata_download_location, is_path=False)

    if config.user_gui_settings:
        if 'r' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsPreferRegions.setChecked(True)
        if 'e' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsIncludeHashless.setChecked(True)
        if 'z' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsModernPlatforms.setChecked(True)
        if 'y' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsDemoteUnlicensed.setChecked(True)
        if 'nooverrides' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsDisableOverrides.setChecked(True)
        if 'removesdat' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsRemovesDat.setChecked(True)
        if 'log' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsKeepRemove.setChecked(True)
        if 'machine' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsUseMachine.setChecked(True)
        if 'originalheader' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsOriginalHeader.setChecked(True)
        if 'warnings' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsReportWarnings.setChecked(True)
        if 'warningpause' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsPauseWarnings.setChecked(True)
        if 'nodtd' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsBypassDTD.setChecked(True)
        if 'singlecpu' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptionsDisableMultiCPU.setChecked(True)
        # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
        if 'listnames' in config.user_gui_settings: main_window.ui.checkBoxGlobalOptions1G1RNames.setChecked(True)
        if 'd' in config.user_gui_settings:
            main_window.ui.checkBoxGlobalOptionsDisable1G1R.setChecked(True)
            main_window.ui.checkBoxGlobalOptionsLegacy.setChecked(False)
            main_window.ui.checkBoxGlobalOptionsLegacy.setEnabled(False)
        if 'legacy' in config.user_gui_settings:
            main_window.ui.checkBoxGlobalOptionsLegacy.setChecked(True)
            main_window.ui.checkBoxGlobalOptionsSplitRegions.setChecked(False)
            main_window.ui.checkBoxGlobalOptionsSplitRegions.setEnabled(False)
            main_window.ui.checkBoxGlobalOptionsDisable1G1R.setChecked(False)
            main_window.ui.checkBoxGlobalOptionsDisable1G1R.setEnabled(False)
        if 'regionsplit' in config.user_gui_settings:
            main_window.ui.checkBoxGlobalOptionsSplitRegions.setChecked(True)
            main_window.ui.checkBoxGlobalOptionsLegacy.setChecked(False)
            main_window.ui.checkBoxGlobalOptionsLegacy.setEnabled(False)

    output: list[dict[str, str]] = [x for x in config.user_gui_settings if 'output' in x and x != {'output': ''}]

    if output:
        main_window.ui.labelOutputFolder.setText(output[0]['output'])
        main_window.output_folder = output[0]['output']

    excludes: list[dict[str, str]] = [x for x in config.user_gui_settings if 'exclude' in x and x != {'exclude': ''}]

    if excludes:
        exclude = excludes[0]['exclude']
        if 'a' in exclude: main_window.ui.checkBoxGlobalExcludeApplications.setChecked(True)
        if 'A' in exclude: main_window.ui.checkBoxGlobalExcludeAudio.setChecked(True)
        if 'b' in exclude: main_window.ui.checkBoxGlobalExcludeBadDumps.setChecked(True)
        if 'B' in exclude: main_window.ui.checkBoxGlobalExcludeBIOS.setChecked(True)
        if 'c' in exclude: main_window.ui.checkBoxGlobalExcludeCoverdiscs.setChecked(True)
        if 'D' in exclude: main_window.ui.checkBoxGlobalExcludeAddOns.setChecked(True)
        if 'd' in exclude: main_window.ui.checkBoxGlobalExcludeDemos.setChecked(True)
        if 'e' in exclude: main_window.ui.checkBoxGlobalExcludeEducational.setChecked(True)
        if 'g' in exclude: main_window.ui.checkBoxGlobalExcludeGames.setChecked(True)
        if 'k' in exclude: main_window.ui.checkBoxGlobalExcludeMIA.setChecked(True)
        if 'm' in exclude: main_window.ui.checkBoxGlobalExcludeManuals.setChecked(True)
        if 'M' in exclude: main_window.ui.checkBoxGlobalExcludeMultimedia.setChecked(True)
        if 'o' in exclude: main_window.ui.checkBoxGlobalExcludeBonusDiscs.setChecked(True)
        if 'p' in exclude: main_window.ui.checkBoxGlobalExcludePirate.setChecked(True)
        if 'P' in exclude: main_window.ui.checkBoxGlobalExcludePreproduction.setChecked(True)
        if 'r' in exclude: main_window.ui.checkBoxGlobalExcludePromotional.setChecked(True)
        if 'u' in exclude: main_window.ui.checkBoxGlobalExcludeUnlicensed.setChecked(True)
        if 'v' in exclude: main_window.ui.checkBoxGlobalExcludeVideo.setChecked(True)

    trace: list[dict[str, str]] = [x for x in config.user_gui_settings if 'trace' in x]

    if trace:
        # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
        trace_str = trace[0]['trace']
        main_window.ui.checkBoxGlobalOptionsTrace.setChecked(True)
        main_window.ui.lineEditGlobalOptionsTrace.setText(trace_str)

    # Set up the regions/languages/localizations interactivity
    main_window.ui.buttonGlobalLanguageAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalSelectedLanguages, main_window.ui.listWidgetGlobalAvailableLanguages, all_items=True))
    main_window.ui.buttonGlobalLanguageAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalAvailableLanguages, main_window.ui.listWidgetGlobalSelectedLanguages, all_items=True))
    main_window.ui.buttonGlobalLanguageDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalSelectedLanguages, 'down'))
    main_window.ui.buttonGlobalLanguageLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalSelectedLanguages, main_window.ui.listWidgetGlobalAvailableLanguages))
    main_window.ui.buttonGlobalLanguageRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalAvailableLanguages, main_window.ui.listWidgetGlobalSelectedLanguages))
    main_window.ui.buttonGlobalLanguageUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalSelectedLanguages, 'up'))

    main_window.ui.buttonGlobalRegionAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalSelectedRegions, main_window.ui.listWidgetGlobalAvailableRegions, all_items=True))
    main_window.ui.buttonGlobalRegionAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalAvailableRegions, main_window.ui.listWidgetGlobalSelectedRegions, all_items=True))
    main_window.ui.buttonGlobalRegionDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalSelectedRegions, 'down'))
    main_window.ui.buttonGlobalRegionLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalSelectedRegions, main_window.ui.listWidgetGlobalAvailableRegions))
    main_window.ui.buttonGlobalRegionRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalAvailableRegions, main_window.ui.listWidgetGlobalSelectedRegions))
    main_window.ui.buttonGlobalRegionUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalSelectedRegions, 'up'))

    main_window.ui.buttonGlobalLocalizationAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, main_window.ui.listWidgetGlobalLocalizationAvailableLanguages, all_items=True))
    main_window.ui.buttonGlobalLocalizationAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalLocalizationAvailableLanguages, main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, all_items=True))
    main_window.ui.buttonGlobalLocalizationDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, 'down'))
    main_window.ui.buttonGlobalLocalizationLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, main_window.ui.listWidgetGlobalLocalizationAvailableLanguages))
    main_window.ui.buttonGlobalLocalizationRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetGlobalLocalizationAvailableLanguages, main_window.ui.listWidgetGlobalLocalizationSelectedLanguages))
    main_window.ui.buttonGlobalLocalizationUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, 'up'))

    main_window.ui.buttonGlobalDefaultRegionOrder.clicked.connect(lambda: default_english_order(main_window, region_order_default, 'global'))

    # Set up the video order interactivity
    main_window.ui.buttonGlobalVideoStandardDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalVideoStandards, 'down'))
    main_window.ui.buttonGlobalVideoStandardUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetGlobalVideoStandards, 'up'))

    # Set up the excludes interactivity
    global_exclude_checkboxes = main_window.ui.tabGlobalExclusions.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxGlobalExclude.*'))

    main_window.ui.buttonGlobalDeselectAllExclude.clicked.connect(lambda: select_checkboxes(global_exclude_checkboxes, False))
    main_window.ui.buttonGlobalSelectAllExclude.clicked.connect(lambda: select_checkboxes(global_exclude_checkboxes, True))

    # Set up the options interactivity
    main_window.ui.checkBoxGlobalOptionsDisable1G1R.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxGlobalOptionsDisable1G1R, (main_window.ui.checkBoxGlobalOptionsLegacy,), (main_window.ui.checkBoxGlobalOptionsSplitRegions,)))
    main_window.ui.checkBoxGlobalOptionsLegacy.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxGlobalOptionsLegacy, (main_window.ui.checkBoxGlobalOptionsDisable1G1R, main_window.ui.checkBoxGlobalOptionsSplitRegions)))
    main_window.ui.checkBoxGlobalOptionsSplitRegions.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxGlobalOptionsSplitRegions, (main_window.ui.checkBoxGlobalOptionsLegacy,), (main_window.ui.checkBoxGlobalOptionsDisable1G1R,)))
    main_window.ui.frameGlobalOptions1G1RPrefix.hide()
    main_window.ui.frameGlobalOptionsTrace.hide()
    main_window.ui.checkBoxGlobalOptions1G1RNames.clicked.connect(lambda: show_hide(main_window.ui.checkBoxGlobalOptions1G1RNames, main_window.ui.frameGlobalOptions1G1RPrefix))
    main_window.ui.checkBoxGlobalOptionsTrace.clicked.connect(lambda: show_hide(main_window.ui.checkBoxGlobalOptionsTrace, main_window.ui.frameGlobalOptionsTrace))


    def CloneListNameToolWindow() -> None:
            """ Opens the clone list name tool window. Trying to just show the window
            directly with .show() means it opens and closes instantly, whereas formatting
            it like this keeps it on screen as intended.
            """

            main_window.new_window.show()

    main_window.ui.actionCloneListNameTool.triggered.connect(lambda: CloneListNameToolWindow())
    main_window.new_window = TitleToolWindow(config)
    main_window.ui.actionDocs.triggered.connect(lambda: webbrowser.open('https://unexpectedpanda.github.io/retool/'))
    main_window.ui.actionGitHub.triggered.connect(lambda: webbrowser.open('https://github.com/unexpectedpanda/retool/issues'))

    # Set up the menu items
    main_window.ui.actionCloneListUpdates.triggered.connect(lambda: write_config(main_window, dat_details, config, settings_window=None, run_retool=True, update_clone_list=True))
    main_window.ui.actionSettings.triggered.connect(lambda: SettingsWindow(dat_details, config, main_window).exec())
    main_window.ui.actionExit.triggered.connect(main_window.close)
    main_window.ui.actionAbout.triggered.connect(lambda: AboutWindow(main_window).exec())

    # Set up the file area
    main_window.ui.buttonAddDats.clicked.connect(lambda: add_list_items(main_window.ui.listWidgetOpenFiles, dat_details, config, main_window, 'files'))
    main_window.ui.buttonAddFolder.clicked.connect(lambda: add_list_items(main_window.ui.listWidgetOpenFiles, dat_details, config, main_window, 'folder'))
    main_window.ui.buttonAddFolderRecursive.clicked.connect(lambda: add_list_items(main_window.ui.listWidgetOpenFiles, dat_details, config, main_window, 'folder', recursive=True))
    main_window.ui.buttonClearDats.clicked.connect(lambda: remove_list_items(main_window.ui.listWidgetOpenFiles, dat_details, main_window.ui.labelSystemSettings, main_window))
    main_window.ui.buttonDeleteDats.clicked.connect(lambda: remove_list_items(main_window.ui.listWidgetOpenFiles, dat_details, main_window.ui.labelSystemSettings, main_window, remove_all=False))
    main_window.ui.buttonChooseOutput.clicked.connect(lambda: set_path(main_window, main_window.output_folder, main_window.ui.labelOutputFolder, 'output_folder'))

    main_window.ui.listWidgetOpenFiles.dropped.connect(lambda: add_list_items(main_window.ui.listWidgetOpenFiles, dat_details, config, main_window, 'dropped'))

    # Set up the "Process DAT files" button
    main_window.ui.buttonGo.clicked.connect(lambda: write_config(main_window, dat_details, config, settings_window=None, run_retool=True))

    def stop_threads() -> None:
        """ Stops the DAT processing after the current DAT file has finished. """

        main_window.threadpool.clear()

        main_window.ui.buttonStop.setEnabled(False)
        main_window.ui.buttonStop.setText(qtc.QCoreApplication.translate('MainWindow', u'Stopping...', None))

    main_window.ui.buttonStop.clicked.connect(lambda: stop_threads())


def setup_gui_system(main_window: Any, dat_details: dict[str, dict[str, str]], config: Config) -> None:
    """ Populates the system GUI with data from config files, and sets up interactions.

    Args:
        - `main_window (Any)` The MainWindow widget.

        - `dat_details (dict[str, dict[str, str]])` The dictionary that carries DAT file
          details like its system name and filepath.

        - `config (Config)` The Retool config object.
    """

    config.system_name = ''

    # Remove United Kingdom from the region lists, as UK is already in there.
    region_order_default: list[str] = [x for x in config.region_order_default if x != 'United Kingdom']

    # Add languages to the languages lists
    languages_user: list[str] = []

    if config.languages_user_found:
        for languages in config.language_order_user:
            for key, value in config.languages.items():
                if languages == value:
                    languages_user.append(key)

    # Set up attributes on the main window for system-specific settings
    main_window.system_output_folder = ''
    main_window.system_clone_list = ''
    main_window.system_metadata_file = ''

    # Set up variables for paths system settings
    output_not_found: str = 'No output folder selected, using global settings'
    clone_list_not_found: str = 'No custom clone list selected, using default clone list location'
    metadata_file_not_found: str = 'No custom metadata file selected, using default metadata file location'

    # Reset the path labels
    main_window.ui.labelSystemOutputFolder.setText(qtc.QCoreApplication.translate('MainWindow', output_not_found, None))
    main_window.ui.labelSystemCloneList.setText(qtc.QCoreApplication.translate('MainWindow', clone_list_not_found, None))
    main_window.ui.labelSystemMetadataFile.setText(qtc.QCoreApplication.translate('MainWindow', metadata_file_not_found, None))

    # Get the system exclude checkboxes
    system_exclude_checkboxes = main_window.ui.tabSystemExclusions.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxSystemExclude.*'))

    # Get the system options checkboxes
    system_options_checkboxes = main_window.ui.tabSystemOptions.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxSystemOptions.*'))

    # Set up system-specific settings to react to changes in the open files list
    def system_settings(open_files_list: Any, config: Config) -> None:
        """ Populates the system settings tab.

        Args:
            - `open_files_list (Any)` The widget containing the added DAT files.
            - `config (Config)` The Retool config object.
        """

        try:
            if open_files_list.selectedItems()[0].text() != 'No DAT files added yet':
                config.system_name = dat_details[open_files_list.selectedItems()[0].text()]['system_name']
                main_window.ui.labelSystemSettings.setText(f'These settings are only for <b>{config.system_name}</b>.')
            else:
                return
        except:
            return

        main_window.ui.listWidgetSystemAvailableLanguages.clear()
        main_window.ui.listWidgetSystemSelectedLanguages.clear()
        main_window.ui.listWidgetSystemAvailableRegions.clear()
        main_window.ui.listWidgetSystemSelectedRegions.clear()
        main_window.ui.listWidgetSystemLocalizationAvailableLanguages.clear()
        main_window.ui.listWidgetSystemLocalizationSelectedLanguages.clear()
        main_window.ui.listWidgetSystemVideoStandards.clear()

        select_checkboxes(system_exclude_checkboxes, False)
        select_checkboxes(system_options_checkboxes, False)

        main_window.ui.lineEditSystemOptions1G1RPrefix.clear()
        main_window.ui.lineEditSystemOptions1G1RSuffix.clear()
        main_window.ui.lineEditSystemOptionsTrace.clear()

        main_window.ui.frameSystemOptions1G1RPrefix.hide()
        main_window.ui.frameSystemOptionsTrace.hide()

        # Enable the system settings
        main_window.ui.tabWidgetSystemSettings.setEnabled(True)

        # Create the system config file if it's missing
        if not pathlib.Path(f'{config.system_settings_path}/{config.system_name}.yaml').is_file():
            try:
                with open(pathlib.Path(f'{config.system_settings_path}/template.yaml'), 'r', encoding='utf-8') as template_file:
                    template_str: list[str] = template_file.readlines()
                with open(pathlib.Path(f'{config.system_settings_path}/{config.system_name}.yaml'), 'w', encoding='utf-8') as system_config_file:
                    system_config_file.writelines(template_str)
            except OSError as e:
                eprint(f'\n{Font.error_bold}* Error: {Font.end}{str(e)}\n')
                raise

        # Pull the system settings
        import_system_settings(
            config,
            config.system_name,
            SYSTEM_LANGUAGE_ORDER_KEY,
            SYSTEM_REGION_ORDER_KEY,
            SYSTEM_LOCALIZATION_ORDER_KEY,
            SYSTEM_VIDEO_ORDER_KEY,
            SYSTEM_LIST_PREFIX_KEY,
            SYSTEM_LIST_SUFFIX_KEY,
            SYSTEM_OVERRIDE_EXCLUDE_KEY,
            SYSTEM_OVERRIDE_INCLUDE_KEY,
            SYSTEM_FILTER_KEY,
            SYSTEM_EXCLUSIONS_OPTIONS_KEY)

        # Set the system paths UI enabled/disabled depending on override state
        if {'override': 'true'} in config.system_user_path_settings:
            main_window.ui.checkBoxSystemOverridePaths.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverridePaths.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverridePaths,
            [
                main_window.ui.buttonChooseSystemOutput,
                main_window.ui.labelSelectSystemOutput,
                main_window.ui.labelSystemOutputFolder,
                main_window.ui.buttonChooseSystemCloneList,
                main_window.ui.labelSelectSystemCloneList,
                main_window.ui.labelSystemCloneList,
                main_window.ui.buttonChooseSystemMetadataFile,
                main_window.ui.labelSelectSystemMetadataFile,
                main_window.ui.labelSystemMetadataFile,
                main_window.ui.buttonClearSystemCloneList,
                main_window.ui.buttonClearSystemMetadataFile,
                main_window.ui.buttonClearSystemOutput
            ]
        )

        # Populate the paths
        if config.system_output:
            main_window.ui.labelSystemOutputFolder.setText(config.system_output)
            main_window.system_output_folder = str(config.system_output)
        else:
            main_window.ui.labelSystemOutputFolder.setText(qtc.QCoreApplication.translate('MainWindow', output_not_found, None))
            main_window.system_output_folder = ''

        if config.system_clone_list:
            main_window.ui.labelSystemCloneList.setText(config.system_clone_list)
            main_window.system_clone_list = str(config.system_clone_list)
        else:
            main_window.ui.labelSystemCloneList.setText(qtc.QCoreApplication.translate('MainWindow', clone_list_not_found, None))
            main_window.system_clone_list = ''

        if config.system_metadata_file:
            main_window.ui.labelSystemMetadataFile.setText(config.system_metadata_file)
            main_window.system_metadata_file = str(config.system_metadata_file)
        else:
            main_window.ui.labelSystemMetadataFile.setText(qtc.QCoreApplication.translate('MainWindow', metadata_file_not_found, None))
            main_window.system_metadata_file = ''

        # Set the system regions UI enabled/disabled depending on override state
        if {'override': 'true'} in config.system_region_order_user:
            main_window.ui.checkBoxSystemOverrideRegions.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideRegions.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideRegions,
            [
                main_window.ui.buttonSystemRegionAllLeft,
                main_window.ui.buttonSystemRegionAllRight,
                main_window.ui.buttonSystemRegionDown,
                main_window.ui.buttonSystemRegionLeft,
                main_window.ui.buttonSystemRegionRight,
                main_window.ui.buttonSystemRegionUp,
                main_window.ui.listWidgetSystemAvailableRegions,
                main_window.ui.listWidgetSystemSelectedRegions,
                main_window.ui.buttonSystemDefaultRegionOrder
            ])

        # Populate the system regions
        region_order_user: list[str] = [x for x in config.region_order_user if x != 'United Kingdom']
        region_order_default: list[str] = [x for x in config.region_order_default if x != 'United Kingdom']
        config.system_region_order_user = [x for x in config.system_region_order_user if x != 'United Kingdom']

        if config.system_region_order_user:
            main_window.ui.listWidgetSystemSelectedRegions.addItems([str(x) for x in config.system_region_order_user if x != {'override': 'true'} and x != {'override': 'false'}])
            main_window.ui.listWidgetSystemAvailableRegions.addItems([x for x in region_order_default if x not in config.system_region_order_user])
        else:
            main_window.ui.checkBoxSystemOverrideRegions.setChecked(False)
            main_window.ui.listWidgetSystemSelectedRegions.addItems([x for x in region_order_user])
            main_window.ui.listWidgetSystemAvailableRegions.addItems([x for x in region_order_default if x not in region_order_user])

        # Populate the system languages
        system_languages_user: list[str] = []

        # Add languages to the languages lists
        if config.system_languages_user_found:
            for languages in config.system_language_order_user:
                for key, value in config.languages.items():
                    if languages == value:
                        system_languages_user.append(key)

            main_window.ui.listWidgetSystemSelectedLanguages.addItems(system_languages_user)
            main_window.ui.listWidgetSystemAvailableLanguages.addItems(sorted([x for x in config.languages if x not in system_languages_user]))
        else:
            main_window.ui.checkBoxSystemOverrideLanguages.setChecked(False)

            main_window.ui.listWidgetSystemAvailableLanguages.addItems(sorted([x for x in config.languages]))

        # Add languages to the localization lists
        system_localization_user: list[str] = []

        for language in config.system_localization_order_user:
            for key, value in config.languages.items():
                if language == value:
                    system_localization_user.append(key)

        if config.system_localization_order_user:
            main_window.ui.listWidgetSystemLocalizationSelectedLanguages.addItems(system_localization_user)
            main_window.ui.listWidgetSystemLocalizationAvailableLanguages.addItems(sorted([x for x in config.languages if x not in system_localization_user]))
        else:
            main_window.ui.checkBoxSystemOverrideLocalization.setChecked(False)

            main_window.ui.listWidgetSystemLocalizationAvailableLanguages.addItems(sorted([x for x in config.languages]))

        # Set the system languages UI enabled/disabled depending on override state
        if {'override': 'true'} in config.system_language_order_user:
            main_window.ui.checkBoxSystemOverrideLanguages.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideLanguages.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideLanguages,
            [
                main_window.ui.buttonSystemLanguageAllLeft,
                main_window.ui.buttonSystemLanguageAllRight,
                main_window.ui.buttonSystemLanguageDown,
                main_window.ui.buttonSystemLanguageLeft,
                main_window.ui.buttonSystemLanguageRight,
                main_window.ui.buttonSystemLanguageUp,
                main_window.ui.listWidgetSystemAvailableLanguages,
                main_window.ui.listWidgetSystemSelectedLanguages,
            ])

        # Set the system localization UI enabled/disabled depending on override state
        if {'override': 'true'} in config.system_localization_order_user:
            main_window.ui.checkBoxSystemOverrideLocalization.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideLocalization.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideLocalization,
            [
                main_window.ui.buttonSystemLocalizationAllLeft,
                main_window.ui.buttonSystemLocalizationAllRight,
                main_window.ui.buttonSystemLocalizationDown,
                main_window.ui.buttonSystemLocalizationLeft,
                main_window.ui.buttonSystemLocalizationRight,
                main_window.ui.buttonSystemLocalizationUp,
                main_window.ui.listWidgetSystemLocalizationAvailableLanguages,
                main_window.ui.listWidgetSystemLocalizationSelectedLanguages,
            ])

        # Set the system video standards UI enabled/disabled depending on override state
        if {'override': 'true'} in config.system_video_order_user:
            main_window.ui.checkBoxSystemOverrideVideo.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideVideo.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideVideo,
            [
                main_window.ui.buttonSystemVideoStandardDown,
                main_window.ui.buttonSystemVideoStandardUp,
                main_window.ui.listWidgetSystemVideoStandards
            ])

        # Populate the system video standards
        if config.system_video_order_user:
            main_window.ui.listWidgetSystemVideoStandards.addItems([str(x) for x in config.system_video_order_user if x != {'override': 'true'} and x != {'override': 'false'}])
        else:
            main_window.ui.listWidgetSystemVideoStandards.setEnabled(False)
            main_window.ui.listWidgetSystemVideoStandards.addItems([x for x in config.video_order_default])

        # Set the system exclusions and options UI enabled/disabled depending on override state
        if {'override exclusions': 'true'} in config.system_exclusions_options:
            main_window.ui.checkBoxSystemOverrideExclusions.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideExclusions.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideExclusions,
            system_exclude_checkboxes
            + [
                main_window.ui.buttonSystemDeselectAllExclude,
                main_window.ui.buttonSystemSelectAllExclude
                ]
        )

        if {'override options': 'true'} in config.system_exclusions_options:
            main_window.ui.checkBoxSystemOverrideOptions.setChecked(True)
        else:
            main_window.ui.checkBoxSystemOverrideOptions.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverrideOptions,
            [main_window.ui.scrollAreaSystemOptions]
        )

        # Populate exclusions and options
        if config.system_exclusions_options:
            if 'r' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsPreferRegions.setChecked(True)
            if 'e' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsIncludeHashless.setChecked(True)
            if 'z' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsModernPlatforms.setChecked(True)
            if 'y' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsDemoteUnlicensed.setChecked(True)
            if 'nooverrides' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsDisableOverrides.setChecked(True)
            if 'removesdat' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsRemovesDat.setChecked(True)
            if 'log' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsKeepRemove.setChecked(True)
            if 'machine' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsUseMachine.setChecked(True)
            if 'originalheader' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsOriginalHeader.setChecked(True)
            if 'warnings' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsReportWarnings.setChecked(True)
            if 'warningpause' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsPauseWarnings.setChecked(True)
            if 'nodtd' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsBypassDTD.setChecked(True)
            if 'singlecpu' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptionsDisableMultiCPU.setChecked(True)
            # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
            if 'listnames' in config.system_exclusions_options: main_window.ui.checkBoxSystemOptions1G1RNames.setChecked(True)
            if 'd' in config.system_exclusions_options:
                main_window.ui.checkBoxSystemOptionsDisable1G1R.setChecked(True)
                main_window.ui.checkBoxSystemOptionsLegacy.setChecked(False)
                main_window.ui.checkBoxSystemOptionsLegacy.setEnabled(False)
            if 'legacy' in config.system_exclusions_options:
                main_window.ui.checkBoxSystemOptionsLegacy.setChecked(True)
                main_window.ui.checkBoxSystemOptionsSplitRegions.setChecked(False)
                main_window.ui.checkBoxSystemOptionsSplitRegions.setEnabled(False)
                main_window.ui.checkBoxSystemOptionsDisable1G1R.setChecked(False)
                main_window.ui.checkBoxSystemOptionsDisable1G1R.setEnabled(False)
            if 'regionsplit' in config.system_exclusions_options:
                main_window.ui.checkBoxSystemOptionsSplitRegions.setChecked(True)
                main_window.ui.checkBoxSystemOptionsLegacy.setChecked(False)
                main_window.ui.checkBoxSystemOptionsLegacy.setEnabled(False)

        system_excludes = [x for x in config.system_exclusions_options if 'exclude' in x and x != {'exclude': ''}]

        if system_excludes:
            system_exclude = system_excludes[0]['exclude']
            if 'a' in system_exclude: main_window.ui.checkBoxSystemExcludeApplications.setChecked(True)
            if 'A' in system_exclude: main_window.ui.checkBoxSystemExcludeAudio.setChecked(True)
            if 'b' in system_exclude: main_window.ui.checkBoxSystemExcludeBadDumps.setChecked(True)
            if 'B' in system_exclude: main_window.ui.checkBoxSystemExcludeBIOS.setChecked(True)
            if 'c' in system_exclude: main_window.ui.checkBoxSystemExcludeCoverdiscs.setChecked(True)
            if 'D' in system_exclude: main_window.ui.checkBoxSystemExcludeAddOns.setChecked(True)
            if 'd' in system_exclude: main_window.ui.checkBoxSystemExcludeDemos.setChecked(True)
            if 'e' in system_exclude: main_window.ui.checkBoxSystemExcludeEducational.setChecked(True)
            if 'g' in system_exclude: main_window.ui.checkBoxSystemExcludeGames.setChecked(True)
            if 'k' in system_exclude: main_window.ui.checkBoxSystemExcludeMIA.setChecked(True)
            if 'm' in system_exclude: main_window.ui.checkBoxSystemExcludeManuals.setChecked(True)
            if 'M' in system_exclude: main_window.ui.checkBoxSystemExcludeMultimedia.setChecked(True)
            if 'o' in system_exclude: main_window.ui.checkBoxSystemExcludeBonusDiscs.setChecked(True)
            if 'p' in system_exclude: main_window.ui.checkBoxSystemExcludePirate.setChecked(True)
            if 'P' in system_exclude: main_window.ui.checkBoxSystemExcludePreproduction.setChecked(True)
            if 'r' in system_exclude: main_window.ui.checkBoxSystemExcludePromotional.setChecked(True)
            if 'u' in system_exclude: main_window.ui.checkBoxSystemExcludeUnlicensed.setChecked(True)
            if 'v' in system_exclude: main_window.ui.checkBoxSystemExcludeVideo.setChecked(True)

        if config.system_user_prefix: main_window.ui.lineEditSystemOptions1G1RPrefix.setText(config.system_user_prefix)
        if config.system_user_suffix: main_window.ui.lineEditSystemOptions1G1RSuffix.setText(config.system_user_suffix)

        system_trace = [x for x in config.system_exclusions_options if 'trace' in x]

        if system_trace:
            # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
            system_trace_str = system_trace[0]['trace']
            main_window.ui.checkBoxSystemOptionsTrace.setChecked(True)
            main_window.ui.lineEditSystemOptionsTrace.setText(system_trace_str)

        if config.system_exclude:
            main_window.ui.textEditSystemExclude.setText('\n'.join(config.system_exclude))
        else:
            main_window.ui.textEditSystemExclude.clear()

        if config.system_include:
            main_window.ui.textEditSystemInclude.setText('\n'.join(config.system_include))
        else:
            main_window.ui.textEditSystemInclude.clear()

        if config.system_filter:
            main_window.ui.textEditSystemFilterInclude.setText('\n'.join([str(x) for x in config.system_filter if x != {'override': 'true'} and x != {'override': 'false'}]))
        else:
            main_window.ui.textEditSystemFilterInclude.clear()

        # Show lineEdits for certain options if checked
        show_hide(main_window.ui.checkBoxSystemOptions1G1RNames, main_window.ui.frameSystemOptions1G1RPrefix)
        show_hide(main_window.ui.checkBoxSystemOptionsTrace, main_window.ui.frameSystemOptionsTrace)

        # Set the post filters UI enabled/disabled depending on override state
        if config.system_filter:
            if {'override': 'true'} in config.system_filter:
                main_window.ui.checkBoxSystemOverridePostFilter.setChecked(True)
            else:
                main_window.ui.checkBoxSystemOverridePostFilter.setChecked(False)

        system_enable(
            main_window.ui.checkBoxSystemOverridePostFilter,
            [
                main_window.ui.textEditSystemFilterInclude
            ])

        # Populate the post filters
        if config.system_filter:
            main_window.ui.textEditSystemFilterInclude.setText('\n'.join([str(x) for x in config.system_filter if x != {'override': 'true'} and x != {'override': 'false'}]))
        else:
            main_window.ui.textEditSystemFilterInclude.clear()

    # Set up the tab refresh when the user clicks on a system
    main_window.ui.listWidgetOpenFiles.clicked.connect(lambda: system_settings(main_window.ui.listWidgetOpenFiles, config))
    main_window.ui.listWidgetOpenFiles.keyPressed.connect(lambda: system_settings(main_window.ui.listWidgetOpenFiles, config))

    # Set up the delete key for various lists
    def on_key(key: int, listWidget: qtw.QListWidget) -> None:
        if key == 16777223:
            if listWidget == main_window.ui.listWidgetOpenFiles:
                remove_list_items(listWidget, dat_details, main_window.ui.labelSystemSettings, main_window, remove_all=False)
            elif listWidget == main_window.ui.listWidgetGlobalSelectedRegions:
                move_list_items(main_window.ui.listWidgetGlobalSelectedRegions, main_window.ui.listWidgetGlobalAvailableRegions)
            elif listWidget == main_window.ui.listWidgetGlobalSelectedLanguages:
                move_list_items(main_window.ui.listWidgetGlobalSelectedLanguages, main_window.ui.listWidgetGlobalAvailableLanguages)
            elif listWidget == main_window.ui.listWidgetGlobalLocalizationSelectedLanguages:
                move_list_items(main_window.ui.listWidgetGlobalLocalizationSelectedLanguages, main_window.ui.listWidgetGlobalLocalizationAvailableLanguages)
            elif listWidget == main_window.ui.listWidgetSystemSelectedRegions:
                move_list_items(main_window.ui.listWidgetSystemSelectedRegions, main_window.ui.listWidgetSystemAvailableRegions)
            elif listWidget == main_window.ui.listWidgetSystemSelectedLanguages:
                move_list_items(main_window.ui.listWidgetSystemSelectedLanguages, main_window.ui.listWidgetSystemAvailableLanguages)
            elif listWidget == main_window.ui.listWidgetSystemLocalizationSelectedLanguages:
                move_list_items(main_window.ui.listWidgetSystemLocalizationSelectedLanguages, main_window.ui.listWidgetSystemLocalizationAvailableLanguages)

    main_window.ui.listWidgetOpenFiles.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetOpenFiles))
    main_window.ui.listWidgetGlobalSelectedRegions.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetGlobalSelectedRegions))
    main_window.ui.listWidgetGlobalSelectedLanguages.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetGlobalSelectedLanguages))
    main_window.ui.listWidgetGlobalLocalizationSelectedLanguages.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetGlobalLocalizationSelectedLanguages))
    main_window.ui.listWidgetSystemSelectedRegions.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetSystemSelectedRegions))
    main_window.ui.listWidgetSystemSelectedLanguages.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetSystemSelectedLanguages))
    main_window.ui.listWidgetSystemLocalizationSelectedLanguages.keyPressed.connect(lambda e: on_key(e, main_window.ui.listWidgetSystemLocalizationSelectedLanguages))

    # Set up the buttons for the system paths
    main_window.ui.checkBoxSystemOverridePaths.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverridePaths,
        [
            main_window.ui.buttonChooseSystemOutput,
            main_window.ui.labelSelectSystemOutput,
            main_window.ui.labelSystemOutputFolder,
            main_window.ui.buttonChooseSystemCloneList,
            main_window.ui.labelSelectSystemCloneList,
            main_window.ui.labelSystemCloneList,
            main_window.ui.buttonChooseSystemMetadataFile,
            main_window.ui.labelSelectSystemMetadataFile,
            main_window.ui.labelSystemMetadataFile,
            main_window.ui.buttonClearSystemCloneList,
            main_window.ui.buttonClearSystemMetadataFile,
            main_window.ui.buttonClearSystemOutput
        ]
    ))

    def clear_system_paths(clear_button: qtw.QPushButton) -> None:
        """ Clear labels associated with clear buttons.

        Args:
            - `clear_button (qtw.QPushButton)` The clear button that was pressed.
        """

        if clear_button == main_window.ui.buttonClearSystemOutput:
            main_window.ui.labelSystemOutputFolder.setText(output_not_found)
            main_window.system_output_folder = ''
            config.system_output = ''
        elif clear_button == main_window.ui.buttonClearSystemCloneList:
            main_window.ui.labelSystemCloneList.setText(clone_list_not_found)
            main_window.system_clone_list = ''
            config.system_clone_list = ''
        elif clear_button == main_window.ui.buttonClearSystemMetadataFile:
            main_window.ui.labelSystemMetadataFile.setText(metadata_file_not_found)
            main_window.system_metadata_file = ''
            config.system_metadata_file = ''

    main_window.ui.buttonChooseSystemOutput.clicked.connect(lambda: set_path(main_window, main_window.system_output_folder, main_window.ui.labelSystemOutputFolder, 'system_output_folder'))
    main_window.ui.buttonChooseSystemCloneList.clicked.connect(lambda: set_path(main_window, main_window.system_clone_list, main_window.ui.labelSystemCloneList, 'system_clone_list', input_type='clone'))
    main_window.ui.buttonChooseSystemMetadataFile.clicked.connect(lambda: set_path(main_window, main_window.system_metadata_file, main_window.ui.labelSystemMetadataFile, 'system_metadata_file', input_type='metadata'))
    main_window.ui.buttonClearSystemOutput.clicked.connect(lambda: clear_system_paths(main_window.ui.buttonClearSystemOutput))
    main_window.ui.buttonClearSystemCloneList.clicked.connect(lambda: clear_system_paths(main_window.ui.buttonClearSystemCloneList))
    main_window.ui.buttonClearSystemMetadataFile.clicked.connect(lambda: clear_system_paths(main_window.ui.buttonClearSystemMetadataFile))

    # Set up the regions/languages/localizations interactivity
    main_window.ui.checkBoxSystemOverrideLanguages.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideLanguages,
        [
            main_window.ui.buttonSystemLanguageAllLeft,
            main_window.ui.buttonSystemLanguageAllRight,
            main_window.ui.buttonSystemLanguageDown,
            main_window.ui.buttonSystemLanguageLeft,
            main_window.ui.buttonSystemLanguageRight,
            main_window.ui.buttonSystemLanguageUp,
            main_window.ui.listWidgetSystemAvailableLanguages,
            main_window.ui.listWidgetSystemSelectedLanguages,
        ]
    ))

    main_window.ui.checkBoxSystemOverrideRegions.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideRegions,
        [
            main_window.ui.buttonSystemRegionAllLeft,
            main_window.ui.buttonSystemRegionAllRight,
            main_window.ui.buttonSystemRegionDown,
            main_window.ui.buttonSystemRegionLeft,
            main_window.ui.buttonSystemRegionRight,
            main_window.ui.buttonSystemRegionUp,
            main_window.ui.listWidgetSystemAvailableRegions,
            main_window.ui.listWidgetSystemSelectedRegions,
            main_window.ui.buttonSystemDefaultRegionOrder
        ]
    ))

    main_window.ui.checkBoxSystemOverrideLocalization.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideLocalization,
        [
            main_window.ui.buttonSystemLocalizationAllLeft,
            main_window.ui.buttonSystemLocalizationAllRight,
            main_window.ui.buttonSystemLocalizationDown,
            main_window.ui.buttonSystemLocalizationLeft,
            main_window.ui.buttonSystemLocalizationRight,
            main_window.ui.buttonSystemLocalizationUp,
            main_window.ui.listWidgetSystemLocalizationAvailableLanguages,
            main_window.ui.listWidgetSystemLocalizationSelectedLanguages
        ]
    ))

    main_window.ui.buttonSystemLanguageAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemSelectedLanguages, main_window.ui.listWidgetSystemAvailableLanguages, all_items=True))
    main_window.ui.buttonSystemLanguageAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemAvailableLanguages, main_window.ui.listWidgetSystemSelectedLanguages, all_items=True))
    main_window.ui.buttonSystemLanguageDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemSelectedLanguages, 'down'))
    main_window.ui.buttonSystemLanguageLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemSelectedLanguages, main_window.ui.listWidgetSystemAvailableLanguages))
    main_window.ui.buttonSystemLanguageRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemAvailableLanguages, main_window.ui.listWidgetSystemSelectedLanguages))
    main_window.ui.buttonSystemLanguageUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemSelectedLanguages, 'up'))

    main_window.ui.buttonSystemRegionAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemSelectedRegions, main_window.ui.listWidgetSystemAvailableRegions, all_items=True))
    main_window.ui.buttonSystemRegionAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemAvailableRegions, main_window.ui.listWidgetSystemSelectedRegions, all_items=True))
    main_window.ui.buttonSystemRegionDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemSelectedRegions, 'down'))
    main_window.ui.buttonSystemRegionLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemSelectedRegions, main_window.ui.listWidgetSystemAvailableRegions))
    main_window.ui.buttonSystemRegionRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemAvailableRegions, main_window.ui.listWidgetSystemSelectedRegions))
    main_window.ui.buttonSystemRegionUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemSelectedRegions, 'up'))

    main_window.ui.buttonSystemLocalizationAllLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemLocalizationSelectedLanguages, main_window.ui.listWidgetSystemLocalizationAvailableLanguages, all_items=True))
    main_window.ui.buttonSystemLocalizationAllRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemLocalizationAvailableLanguages, main_window.ui.listWidgetSystemLocalizationSelectedLanguages, all_items=True))
    main_window.ui.buttonSystemLocalizationDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemLocalizationSelectedLanguages, 'down'))
    main_window.ui.buttonSystemLocalizationLeft.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemLocalizationSelectedLanguages, main_window.ui.listWidgetSystemLocalizationAvailableLanguages))
    main_window.ui.buttonSystemLocalizationRight.clicked.connect(lambda: move_list_items(main_window.ui.listWidgetSystemLocalizationAvailableLanguages, main_window.ui.listWidgetSystemLocalizationSelectedLanguages))
    main_window.ui.buttonSystemLocalizationUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemLocalizationSelectedLanguages, 'up'))

    main_window.ui.buttonSystemDefaultRegionOrder.clicked.connect(lambda: default_english_order(main_window, region_order_default, 'system'))

    # Set up the video order interactivity
    main_window.ui.checkBoxSystemOverrideVideo.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideVideo,
        [
            main_window.ui.buttonSystemVideoStandardDown,
            main_window.ui.buttonSystemVideoStandardUp,
            main_window.ui.listWidgetSystemVideoStandards
        ]))

    main_window.ui.buttonSystemVideoStandardDown.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemVideoStandards, 'down'))
    main_window.ui.buttonSystemVideoStandardUp.clicked.connect(lambda: order_list_items(main_window.ui.listWidgetSystemVideoStandards, 'up'))

    # Set up the excludes interactivity
    main_window.ui.checkBoxSystemOverrideExclusions.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideExclusions,
        system_exclude_checkboxes
        + [
            main_window.ui.buttonSystemDeselectAllExclude,
            main_window.ui.buttonSystemSelectAllExclude
            ]
        ))

    main_window.ui.buttonSystemDeselectAllExclude.clicked.connect(lambda: select_checkboxes(system_exclude_checkboxes, False))
    main_window.ui.buttonSystemSelectAllExclude.clicked.connect(lambda: select_checkboxes(system_exclude_checkboxes, True))

    # Set up the options interactivity
    main_window.ui.checkBoxSystemOverrideOptions.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverrideOptions,
        [main_window.ui.scrollAreaSystemOptions]
        ))

    main_window.ui.checkBoxSystemOptionsDisable1G1R.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxSystemOptionsDisable1G1R, (main_window.ui.checkBoxSystemOptionsLegacy,), (main_window.ui.checkBoxSystemOptionsSplitRegions,)))
    main_window.ui.checkBoxSystemOptionsLegacy.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxSystemOptionsLegacy, (main_window.ui.checkBoxSystemOptionsDisable1G1R, main_window.ui.checkBoxSystemOptionsSplitRegions)))
    main_window.ui.checkBoxSystemOptionsSplitRegions.clicked.connect(lambda: disable_incompatible_checkbox(main_window.ui.checkBoxSystemOptionsSplitRegions, (main_window.ui.checkBoxSystemOptionsLegacy,), (main_window.ui.checkBoxSystemOptionsDisable1G1R,)))
    main_window.ui.checkBoxSystemOptions1G1RNames.clicked.connect(lambda: show_hide(main_window.ui.checkBoxSystemOptions1G1RNames, main_window.ui.frameSystemOptions1G1RPrefix))
    main_window.ui.checkBoxSystemOptionsTrace.clicked.connect(lambda: show_hide(main_window.ui.checkBoxSystemOptionsTrace, main_window.ui.frameSystemOptionsTrace))

    # Set up the post filter interactivity
    main_window.ui.checkBoxSystemOverridePostFilter.clicked.connect(lambda: system_enable(
        main_window.ui.checkBoxSystemOverridePostFilter,
        [
            main_window.ui.textEditSystemFilterInclude
        ]))
