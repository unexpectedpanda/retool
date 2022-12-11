import multiprocessing
import os
import pathlib
import re
import sys
import threading
import traceback
import validators
import webbrowser

import retool

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

from modules.constants import *
from modules.config import Config, generate_config
from modules.dats import Dat
from modules.gui.retool_ui import Ui_MainWindow
from modules.gui.retool_about import Ui_AboutWindow
from modules.gui.retool_settings import Ui_Settings
from modules.gui.retool_clone_list_name import Ui_CloneListNameTool
from modules.input import UserInput
from modules.titletools import TitleTools
from modules.utils import Font

# Require at least Python 3.9
assert sys.version_info >= (3, 9)

__version__: str = str(f'{GUI_VERSION_MAJOR}.{GUI_VERSION_MINOR}')

class MainWindow(qtw.QMainWindow):
    """ The main window for Retool """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = {}
        self.threadpool = qtc.QThreadPool()

        # Limit the number of CLI threads that can run to 1. Potentially if we get
        # out of the CLI in the future and into full GUI this can be increased.
        self.threadpool.setMaxThreadCount(1)

        # Fix the taskbar icon not loading on Windows
        if sys.platform.startswith('win'):
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'retool')

        # Update list widgets with custom behavior
        self.ui.listWidgetGlobalAvailableRegions.deleteLater()
        self.ui.listWidgetGlobalAvailableLanguages.deleteLater()
        self.ui.listWidgetGlobalAvailableRegions = CustomList(self.ui.tabGlobalRegions, is_drag_drop=True)
        self.ui.listWidgetGlobalAvailableRegions.setObjectName(u"listWidgetGlobalAvailableRegions")
        self.ui.listWidgetGlobalAvailableRegions.setGeometry(qtc.QRect(10, 70, 221, 251))
        self.ui.listWidgetGlobalAvailableLanguages = CustomList(self.ui.tabGlobalLanguages, is_drag_drop=True)
        self.ui.listWidgetGlobalAvailableLanguages.setObjectName(u"listWidgetGlobalAvailableLanguages")
        self.ui.listWidgetGlobalAvailableLanguages.setGeometry(qtc.QRect(10, 70, 221, 291))

        self.ui.listWidgetGlobalSelectedRegions.deleteLater()
        self.ui.listWidgetGlobalSelectedRegions = CustomList(self.ui.tabGlobalRegions, is_drag_drop=True, self_drag=True)
        self.ui.listWidgetGlobalSelectedRegions.setObjectName(u"listWidgetGlobalSelectedRegions")
        self.ui.listWidgetGlobalSelectedRegions.setGeometry(qtc.QRect(300, 70, 221, 251))
        self.ui.listWidgetGlobalSelectedLanguages.deleteLater()
        self.ui.listWidgetGlobalSelectedLanguages = CustomList(self.ui.tabGlobalLanguages, is_drag_drop=True, self_drag=True)
        self.ui.listWidgetGlobalSelectedLanguages.setObjectName(u"listWidgetGlobalSelectedLanguages")
        self.ui.listWidgetGlobalSelectedLanguages.setGeometry(qtc.QRect(300, 70, 221, 291))

        self.ui.listWidgetGlobalVideoStandards.deleteLater()
        self.ui.listWidgetGlobalVideoStandards = CustomList(self.ui.tabGlobalVideo, is_drag_drop=True, self_drag=True)
        self.ui.listWidgetGlobalVideoStandards.setObjectName(u"listWidgetGlobalVideoStandards")
        self.ui.listWidgetGlobalVideoStandards.setGeometry(qtc.QRect(10, 70, 221, 291))

        self.ui.listWidgetOpenFiles.deleteLater()
        self.ui.listWidgetOpenFiles = CustomList(self.ui.mainProgram, is_drag_drop=False)
        self.ui.listWidgetOpenFiles.setGeometry(qtc.QRect(60, 40, 251, 411))
        self.ui.listWidgetOpenFiles.setObjectName(u"listWidgetOpenFiles")
        self.ui.listWidgetOpenFiles.addItem(qtc.QCoreApplication.translate("MainWindow", u"No DAT files added yet", None))

        # Update the output folder label with custom behavior
        self.ui.labelOutputFolder.deleteLater()
        self.ui.labelOutputFolder = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.mainProgram)
        self.ui.labelOutputFolder.setObjectName(u"labelOutputFolder")
        self.ui.labelOutputFolder.setText(str(pathlib.Path.cwd()))
        self.ui.labelOutputFolder.setGeometry(qtc.QRect(60, 500, 251, 16))
        self.ui.labelOutputFolder.setStyleSheet('color: #777')

        # Update line edits with custom behavior
        self.ui.lineEditGlobalOptions1G1RPrefix.deleteLater()
        self.ui.lineEditGlobalOptions1G1RPrefix = CustomLineEdit(self.ui.frameGlobalOptions1G1RPrefix)
        self.ui.lineEditGlobalOptions1G1RPrefix.setObjectName(u"lineEditGlobalOptions1G1RPrefix")
        self.ui.lineEditGlobalOptions1G1RPrefix.setGeometry(qtc.QRect(20, 30, 521, 24))
        self.ui.lineEditGlobalOptions1G1RPrefix.setMinimumSize(qtc.QSize(0, 24))
        self.ui.lineEditGlobalOptions1G1RSuffix.deleteLater()
        self.ui.lineEditGlobalOptions1G1RSuffix = CustomLineEdit(self.ui.frameGlobalOptions1G1RPrefix)
        self.ui.lineEditGlobalOptions1G1RSuffix.setObjectName(u"lineEditGlobalOptions1G1RSuffix")
        self.ui.lineEditGlobalOptions1G1RSuffix.setGeometry(qtc.QRect(20, 83, 521, 24))
        self.ui.lineEditGlobalOptions1G1RSuffix.setMinimumSize(qtc.QSize(0, 24))
        self.ui.lineEditGlobalOptionsTrace.deleteLater()
        self.ui.lineEditGlobalOptionsTrace = CustomLineEdit(self.ui.frameGlobalOptionsTrace)
        self.ui.lineEditGlobalOptionsTrace.setObjectName(u"lineEditGlobalOptionsTrace")
        self.ui.lineEditGlobalOptionsTrace.setGeometry(qtc.QRect(20, 30, 521, 24))
        self.ui.lineEditGlobalOptionsTrace.setMinimumSize(qtc.QSize(0, 24))

        # Update text edits with custom behavior
        self.ui.textEditGlobalInclude.deleteLater()
        self.ui.textEditGlobalInclude = CustomTextEdit(self.ui.scrollAreaWidgetContentsGlobalUserFilters)
        self.ui.textEditGlobalInclude.setObjectName(u"textEditGlobalInclude")
        self.ui.textEditGlobalInclude.setMinimumSize(qtc.QSize(0, 100))
        self.ui.textEditGlobalInclude.setMaximumSize(qtc.QSize(16777215, 100))
        self.ui.textEditGlobalInclude.setTabChangesFocus(True)
        self.ui.textEditGlobalInclude.setAcceptRichText(False)
        self.ui.textEditGlobalExclude.deleteLater()
        self.ui.textEditGlobalExclude = CustomTextEdit(self.ui.scrollAreaWidgetContentsGlobalUserFilters)
        self.ui.textEditGlobalExclude.setObjectName(u"textEditGlobalExclude")
        self.ui.textEditGlobalExclude.setMinimumSize(qtc.QSize(0, 100))
        self.ui.textEditGlobalExclude.setMaximumSize(qtc.QSize(16777215, 100))
        self.ui.textEditGlobalExclude.setTabChangesFocus(True)
        self.ui.textEditGlobalExclude.setAcceptRichText(False)

        self.ui.verticalLayout_2.insertWidget(8, self.ui.textEditGlobalInclude)
        self.ui.verticalLayout_2.insertWidget(11, self.ui.textEditGlobalExclude)

        # Set the tab order
        # TODO: Set the tab order for replaced elements... shouldn't be so bad I think?

        # Set the window size
        self.setFixedSize(957, 610)

        # Fix the fonts
        set_fonts(self)

        # Fix the scrollArea background color,which for some reason is altered
        # by setting the font previously
        self.ui.scrollAreaGlobalOptions.setStyleSheet('''
                                         QWidget{ background-color: #00000000 }
                                         QWidget:focus{ outline: 1px dotted #000000 }
                                         QScrollBar{ background-color: none }
                                         ''')

        self.ui.scrollAreaGlobalUserFilters.setStyleSheet('''
                                         QWidget{ background-color: #00000000 }
                                         QWidget:focus{ outline: 1px dotted #000000 }
                                         QScrollBar{ background-color: none }
                                         ''')

        self.ui.buttonGo.deleteLater()
        self.ui.buttonGo = CustomPushButton(self.ui.centralwidget)
        self.ui.buttonGo.setText(qtc.QCoreApplication.translate("MainWindow", u"Process DAT files", None))
        self.ui.buttonGo.setObjectName(u"buttonGo")
        self.ui.buttonGo.setGeometry(qtc.QRect(801, 530, 140, 45))
        self.ui.buttonGo.setDisabled(True)
        self.ui.buttonGo.setToolTip(qtc.QCoreApplication.translate("MainWindow", u"You need to add DAT files to the list before you can process them", None))

        # Build an early config object
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
            USER_LANGUAGE_KEY,
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

        # Remove United Kingdom from the region lists, as UK is already in there.
        # TODO: Check this doesn't impact actual processing
        region_order_user: list[str] = [x for x in config.region_order_user if x != 'United Kingdom']
        region_order_default: list[str] = [x for x in config.region_order_default if x != 'United Kingdom']

        # Add regions to the regions lists
        self.ui.listWidgetGlobalSelectedRegions.addItems(region_order_user)
        self.ui.listWidgetGlobalAvailableRegions.addItems(sorted([x for x in region_order_default if x not in region_order_user]))

        # Add languages to the languages lists
        languages_user: list[str] = []

        if config.languages_user_found:
            for languages in config.languages_user:
                for key, value in config.languages.items():
                    if languages == value:
                        languages_user.append(key)

        self.ui.listWidgetGlobalSelectedLanguages.addItems(languages_user)
        self.ui.listWidgetGlobalAvailableLanguages.addItems(sorted([x for x in config.languages if x not in languages_user]))

        # Add video standards to the video list
        if config.video_order_user:
            self.ui.listWidgetGlobalVideoStandards.addItems([x for x in config.video_order_user])
        else:
            self.ui.listWidgetGlobalVideoStandards.addItems([x for x in config.video_order_default])

        # Apply other settings from user-config.yaml
        if config.global_exclude: self.ui.textEditGlobalExclude.setText('\n'.join(config.global_exclude))
        if config.global_include: self.ui.textEditGlobalInclude.setText('\n'.join(config.global_include))
        if config.user_prefix: self.ui.lineEditGlobalOptions1G1RPrefix.setText(config.user_prefix)
        if config.user_suffix: self.ui.lineEditGlobalOptions1G1RSuffix.setText(config.user_suffix)

        self.output_folder = str(pathlib.Path.cwd())

        self.clone_lists_folder: str = get_gui_settings_value('clone lists folder', config.path_clone_list, config)
        self.metadata_folder: str = get_gui_settings_value('metadata folder', config.path_metadata, config)
        self.clone_list_metadata_url: str = get_gui_settings_value('clone list metadata url', config.clone_list_metadata_download_location, config, path=False)

        if config.user_gui_settings:
            if 'r' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsPreferRegions.setChecked(True)
            if 'e' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsIncludeHashless.setChecked(True)
            if 'z' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsModernPlatforms.setChecked(True)
            if 'y' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsDemoteUnlicensed.setChecked(True)
            if 'nofilters' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsDisableFilters.setChecked(True)
            if 'removesdat' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsRemovesDat.setChecked(True)
            if 'log' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsKeepRemove.setChecked(True)
            if 'warnings' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsReportWarnings.setChecked(True)
            if 'warningpause' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsPauseWarnings.setChecked(True)
            if 'nodtd' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsBypassDTD.setChecked(True)
            if 'singlecpu' in config.user_gui_settings: self.ui.checkBoxGlobalOptionsDisableMultiCPU.setChecked(True)
            # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
            if 'listnames' in config.user_gui_settings: self.ui.checkBoxGlobalOptions1G1RNames.setChecked(True)
            if 'd' in config.user_gui_settings:
                self.ui.checkBoxGlobalOptionsDisable1G1R.setChecked(True)
                self.ui.checkBoxGlobalOptionsLegacy.setChecked(False)
                self.ui.checkBoxGlobalOptionsLegacy.setDisabled(True)
            if 'legacy' in config.user_gui_settings:
                self.ui.checkBoxGlobalOptionsLegacy.setChecked(True)
                self.ui.checkBoxGlobalOptionsSplitRegions.setChecked(False)
                self.ui.checkBoxGlobalOptionsSplitRegions.setDisabled(True)
                self.ui.checkBoxGlobalOptionsDisable1G1R.setChecked(False)
                self.ui.checkBoxGlobalOptionsDisable1G1R.setDisabled(True)
            if 'regionsplit' in config.user_gui_settings:
                self.ui.checkBoxGlobalOptionsSplitRegions.setChecked(True)
                self.ui.checkBoxGlobalOptionsLegacy.setChecked(False)
                self.ui.checkBoxGlobalOptionsLegacy.setDisabled(True)

            output = [x for x in config.user_gui_settings if 'output' in x and x != {'output': ''}]

            if output:
                self.ui.labelOutputFolder.setText(output[0]['output'])
                self.output_folder: str = output[0]['output']

            excludes = [x for x in config.user_gui_settings if 'exclude' in x and x != {'exclude': ''}]

            if excludes:
                exclude = excludes[0]['exclude']
                if 'a' in exclude: self.ui.checkBoxGlobalExcludeApplications.setChecked(True)
                if 'A' in exclude: self.ui.checkBoxGlobalExcludeAudio.setChecked(True)
                if 'b' in exclude: self.ui.checkBoxGlobalExcludeBadDumps.setChecked(True)
                if 'B' in exclude: self.ui.checkBoxGlobalExcludeBIOS.setChecked(True)
                if 'c' in exclude: self.ui.checkBoxGlobalExcludeCoverdiscs.setChecked(True)
                if 'D' in exclude: self.ui.checkBoxGlobalExcludeAddOns.setChecked(True)
                if 'd' in exclude: self.ui.checkBoxGlobalExcludeDemos.setChecked(True)
                if 'e' in exclude: self.ui.checkBoxGlobalExcludeEducational.setChecked(True)
                if 'k' in exclude: self.ui.checkBoxGlobalExcludeMIA.setChecked(True)
                if 'm' in exclude: self.ui.checkBoxGlobalExcludeManuals.setChecked(True)
                if 'M' in exclude: self.ui.checkBoxGlobalExcludeMultimedia.setChecked(True)
                if 'o' in exclude: self.ui.checkBoxGlobalExcludeBonusDiscs.setChecked(True)
                if 'p' in exclude: self.ui.checkBoxGlobalExcludePirate.setChecked(True)
                if 'P' in exclude: self.ui.checkBoxGlobalExcludePreproduction.setChecked(True)
                if 'r' in exclude: self.ui.checkBoxGlobalExcludePromotional.setChecked(True)
                if 'u' in exclude: self.ui.checkBoxGlobalExcludeUnlicensed.setChecked(True)
                if 'v' in exclude: self.ui.checkBoxGlobalExcludeVideo.setChecked(True)

            trace = [x for x in config.user_gui_settings if 'trace' in x]

            if trace:
                # Show the associated lineEdit later, as it takes a while for the checkbox to be enabled
                trace_str = trace[0]['trace']
                self.ui.checkBoxGlobalOptionsTrace.setChecked(True)
                self.ui.lineEditGlobalOptionsTrace.setText(trace_str)

        # Set up the menu items
        self.ui.actionCloneListUpdates.triggered.connect(lambda: write_config(self, config, settings=None, run_retool=True, update_clone_list=True))
        self.ui.actionSettings.triggered.connect(lambda: SettingsWindow(config, self).exec())
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(lambda: AboutWindow(self).exec())

        def CloneListNameToolWindow() -> None:
            """
            Opens the clone list name tool window. Trying to just show the
            window directly with .show() means it opens and closes instantly,
            whereas formatting it like this keeps it on screen as intended. I
            have no idea why things work this way.
            """
            self.new_window.show()

        self.ui.actionCloneListNameTool.triggered.connect(lambda: CloneListNameToolWindow())
        self.new_window = TitleToolWindow(config)

        self.ui.actionGitHub.triggered.connect(lambda: webbrowser.open('https://github.com/unexpectedpanda/retool/issues'))

        # Set up the file area
        self.ui.buttonAddDats.clicked.connect(lambda: add_list_items(self.ui.listWidgetOpenFiles, dat_details, self.ui.buttonGo, config, 'files'))
        self.ui.buttonAddFolder.clicked.connect(lambda: add_list_items(self.ui.listWidgetOpenFiles, dat_details, self.ui.buttonGo, config, 'folder'))
        self.ui.buttonAddFolderRecursive.clicked.connect(lambda: add_list_items(self.ui.listWidgetOpenFiles, dat_details, self.ui.buttonGo, config, 'folder', recursive=True))
        self.ui.buttonClearDats.clicked.connect(lambda: remove_list_items(self.ui.listWidgetOpenFiles, dat_details, self.ui.labelSystemSettings, self.ui.buttonGo))
        self.ui.buttonDeleteDats.clicked.connect(lambda: remove_list_items(self.ui.listWidgetOpenFiles, dat_details, self.ui.labelSystemSettings, self.ui.buttonGo, remove_all=False))
        self.ui.buttonChooseOutput.clicked.connect(lambda: set_path(self, self.output_folder, self.ui.labelOutputFolder, 'output_folder'))

        # Set up system-specific settings to react to changes in the open files list
        def system_settings(open_files_list) -> None:
            """ Populates the system settings tab """
            try:
                if open_files_list.selectedItems()[0].text() != 'No DAT files added yet':
                    self.ui.labelSystemSettings.setText(f'These settings are only for <b>{dat_details[open_files_list.selectedItems()[0].text()]["system_name"]}</b>.')
            except:
                pass

        self.ui.listWidgetOpenFiles.clicked.connect(lambda: system_settings(self.ui.listWidgetOpenFiles))
        self.ui.listWidgetOpenFiles.keyPressed.connect(lambda: system_settings(self.ui.listWidgetOpenFiles))

        # Set up the buttons for the global regions/languages
        self.ui.buttonGlobalRegionLeft.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalSelectedRegions, self.ui.listWidgetGlobalAvailableRegions))
        self.ui.buttonGlobalRegionRight.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalAvailableRegions, self.ui.listWidgetGlobalSelectedRegions))
        self.ui.buttonGlobalLanguageLeft.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalSelectedLanguages, self.ui.listWidgetGlobalAvailableLanguages))
        self.ui.buttonGlobalLanguageRight.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalAvailableLanguages, self.ui.listWidgetGlobalSelectedLanguages))
        self.ui.buttonGlobalRegionAllLeft.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalSelectedRegions, self.ui.listWidgetGlobalAvailableRegions, all_items=True))
        self.ui.buttonGlobalRegionAllRight.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalAvailableRegions, self.ui.listWidgetGlobalSelectedRegions, all_items=True))
        self.ui.buttonGlobalLanguageAllLeft.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalSelectedLanguages, self.ui.listWidgetGlobalAvailableLanguages, all_items=True))
        self.ui.buttonGlobalLanguageAllRight.clicked.connect(lambda: move_list_items(self.ui.listWidgetGlobalAvailableLanguages, self.ui.listWidgetGlobalSelectedLanguages, all_items=True))
        self.ui.buttonGlobalRegionUp.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalSelectedRegions, 'up'))
        self.ui.buttonGlobalRegionDown.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalSelectedRegions, 'down'))
        self.ui.buttonGlobalLanguageUp.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalSelectedLanguages, 'up'))
        self.ui.buttonGlobalLanguageDown.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalSelectedLanguages, 'down'))

        def default_english_order() -> None:
            """ Sets the selected regions list to the default English order """
            self.ui.listWidgetGlobalSelectedRegions.clear()
            self.ui.listWidgetGlobalAvailableRegions.clear()
            self.ui.listWidgetGlobalSelectedRegions.addItems(region_order_default)

        self.ui.buttonGlobalDefaultRegionOrder.clicked.connect(lambda: default_english_order())

        # Set up the video order buttons
        self.ui.buttonGlobalVideoStandardUp.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalVideoStandards, 'up'))
        self.ui.buttonGlobalVideoStandardDown.clicked.connect(lambda: order_list_items(self.ui.listWidgetGlobalVideoStandards, 'down'))

        # Set up the global exclude buttons
        global_exclude_checkboxes = self.ui.tabGlobalExclusions.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxGlobalExclude.*'))

        self.ui.buttonGlobalSelectAllExclude.clicked.connect(lambda: select_checkboxes(global_exclude_checkboxes, True))
        self.ui.buttonGlobalDeselectAllExclude.clicked.connect(lambda: select_checkboxes(global_exclude_checkboxes, False))

        # Set up the global options
        self.ui.checkBoxGlobalOptionsDisable1G1R.clicked.connect(lambda: disable_incompatible_checkbox(self.ui.checkBoxGlobalOptionsDisable1G1R, (self.ui.checkBoxGlobalOptionsLegacy,), (self.ui.checkBoxGlobalOptionsSplitRegions,)))
        self.ui.checkBoxGlobalOptionsLegacy.clicked.connect(lambda: disable_incompatible_checkbox(self.ui.checkBoxGlobalOptionsLegacy, (self.ui.checkBoxGlobalOptionsDisable1G1R, self.ui.checkBoxGlobalOptionsSplitRegions)))
        self.ui.checkBoxGlobalOptionsSplitRegions.clicked.connect(lambda: disable_incompatible_checkbox(self.ui.checkBoxGlobalOptionsSplitRegions, (self.ui.checkBoxGlobalOptionsLegacy,), (self.ui.checkBoxGlobalOptionsDisable1G1R,)))
        self.ui.frameGlobalOptions1G1RPrefix.hide()
        self.ui.frameGlobalOptionsTrace.hide()
        self.ui.checkBoxGlobalOptions1G1RNames.clicked.connect(lambda: show_hide(self.ui.checkBoxGlobalOptions1G1RNames, self.ui.frameGlobalOptions1G1RPrefix))
        self.ui.checkBoxGlobalOptionsTrace.clicked.connect(lambda: show_hide(self.ui.checkBoxGlobalOptionsTrace, self.ui.frameGlobalOptionsTrace))

        # Set up the "Process DAT files" button
        self.ui.buttonGo.clicked.connect(lambda: write_config(self, config, settings=None, run_retool=True))

        self.ui.buttonStop = CustomPushButton(self.ui.centralwidget)
        self.ui.buttonStop.setText(qtc.QCoreApplication.translate("MainWindow", u"Stop", None))
        self.ui.buttonStop.setObjectName(u"buttonStop")
        self.ui.buttonStop.setGeometry(qtc.QRect(801, 530, 140, 45))
        self.ui.buttonStop.hide()

        def stop_threads():
            self.threadpool.clear()

            self.ui.buttonStop.setDisabled(True)
            self.ui.buttonStop.setText(qtc.QCoreApplication.translate("MainWindow", u"Stopping...", None))

        self.ui.buttonStop.clicked.connect(lambda: stop_threads())

        # Write a config file on any meaningful change
        interactive_widgets = []
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QPushButton, qtc.QRegularExpression('buttonGlobal(Language|Region|Video|Deselect|Select|Default).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxGlobal(Exclude|Options).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QTextEdit, qtc.QRegularExpression('textEditGlobal(Exclude|Include).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QLineEdit, qtc.QRegularExpression('lineEditGlobalOptions.*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QListWidget, qtc.QRegularExpression('listWidgetGlobal.*')))
        interactive_widgets.extend([self.ui.buttonChooseOutput])

        # Track all meaningful interactions, write the config file if one happens
        for interactive_widget in interactive_widgets:
            try:
                if type(interactive_widget) is not CustomList:
                    interactive_widget.clicked.connect(lambda: write_config(self, config, settings=None))
            except:
                pass
            try:
                interactive_widget.keyPressed.connect(lambda: write_config(self, config, settings=None))
            except:
                pass
            try:
                interactive_widget.dropped.connect(lambda: write_config(self, config, settings=None))
            except:
                pass

    def start_retool_thread(self, data: UserInput = None) -> None:
        """

        Args:
            `data (UserInput)`: The Retool user input object. Defaults to `None`.
        """

        self.data = {}  # reset
        self.new_thread = RunThread('Retool', data)

        # Check to see if we can enable the interface
        self.new_thread.signals.finished.connect(self.enable_app)

        self.threadpool.start(self.new_thread)

    def enable_app(self):
         # If all the threads have finished, re-enable the interface
        if (self.threadpool.activeThreadCount() == 0):
            self.ui.buttonGo.setEnabled(True)
            self.ui.buttonStop.hide()
            self.ui.buttonStop.setText(qtc.QCoreApplication.translate("MainWindow", u"Stop", None))
            self.ui.buttonStop.setEnabled(True)
            self.ui.mainProgram.setEnabled(True)


class AboutWindow(qtw.QDialog):
    def __init__(self, parent=None) -> None:
        """ The "About" window for Retool.

        Args:
            `parent`: The parent window that called this one. Important so the
            modal doesn't turn up on the taskbar, and makes the parent
            inaccessible while the modal is open. Defaults to `None`.
        """

        super(AboutWindow, self).__init__(parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        # Fix the fonts
        set_fonts(self)

        # Set Retool versions
        self.ui.labelGUIVersion.setText(f'GUI version: {__version__}')
        self.ui.labelCLIVersion.setText(f'CLI version: {CLI_VERSION_MAJOR}.{CLI_VERSION_MINOR}')


class SettingsWindow(qtw.QDialog):
    def __init__(self, config: Config, parent=None) -> None:
        """ The "Settings" window for Retool.

        Args:
            `parent`: The parent window that called this one. Important so the
            modal doesn't turn up on the taskbar, and makes the parent
            inaccessible while the modal is open. Defaults to `None`.
        """

        super(SettingsWindow, self).__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        # Fix the fonts
        set_fonts(self)

        # Hide the error label
        self.ui.labelURLError.hide()

        # Replace widgets with custom versions
        self.ui.labelCloneListsLocation.hide()
        self.ui.labelCloneListsLocation.deleteLater()
        self.ui.labelCloneListsLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameCloneListsLocation)
        self.ui.labelCloneListsLocation.setText(qtc.QCoreApplication.translate("Settings", u"No clone list folder selected", None))
        self.ui.labelCloneListsLocation.setObjectName(u"labelCloneListsLocation")
        self.ui.labelCloneListsLocation.setGeometry(qtc.QRect(50, 20, 531, 20))
        self.ui.labelCloneListsLocation.setStyleSheet('color: #777')

        self.ui.labelMetadataLocation.hide()
        self.ui.labelMetadataLocation.deleteLater()
        self.ui.labelMetadataLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameMetadataLocation)
        self.ui.labelMetadataLocation.setText(qtc.QCoreApplication.translate("Settings", u"No metadata folder selected", None))
        self.ui.labelMetadataLocation.setObjectName(u"labelMetadataLocation")
        self.ui.labelMetadataLocation.setGeometry(qtc.QRect(50, 20, 531, 20))
        self.ui.labelMetadataLocation.setStyleSheet('color: #777')

        self.ui.lineEditCloneListDownloadLocation.deleteLater()
        self.ui.lineEditCloneListDownloadLocation = CustomLineEdit(self.ui.frameCloneListMetadataDownloadLocation)
        self.ui.lineEditCloneListDownloadLocation.setObjectName(u"lineEditCloneListDownloadLocation")
        self.ui.lineEditCloneListDownloadLocation.setGeometry(qtc.QRect(0, 0, 571, 24))
        self.ui.lineEditCloneListDownloadLocation.setMinimumSize(qtc.QSize(0, 24))
        self.ui.lineEditCloneListDownloadLocation.setMaximumSize(qtc.QSize(16777215, 24))

        # Get the values from the user config
        self.ui.labelCloneListsLocation.setText(str(pathlib.Path(parent.clone_lists_folder).resolve()))
        self.ui.labelMetadataLocation.setText(str(pathlib.Path(parent.metadata_folder).resolve()))
        self.ui.lineEditCloneListDownloadLocation.setText(parent.clone_list_metadata_url)

        # Set up the interactions
        self.ui.buttonChooseCloneListsLocation.clicked.connect(lambda: set_path(parent, parent.clone_lists_folder, self.ui.labelCloneListsLocation, 'clone_lists_folder', input_type='folder'))
        self.ui.buttonChooseMetadataLocation.clicked.connect(lambda: set_path(parent, parent.metadata_folder, self.ui.labelMetadataLocation, 'metadata_folder', input_type='folder'))

        def url_entry(url: str) -> None:
            if not url:
                parent.clone_list_metadata_url = config.clone_list_metadata_download_location
                return
            else:
                if validators.url(url):
                    self.ui.labelURLError.hide()
                    parent.clone_list_metadata_url = url
                    write_config(parent, config, self)
                else:
                    # parent.clone_list_metadata_url = config.clone_list_metadata_download_location
                    self.ui.labelURLError.show()

        self.ui.lineEditCloneListDownloadLocation.keyPressed.connect(lambda: url_entry(self.ui.lineEditCloneListDownloadLocation.text()))

        # Set up config writing
        self.ui.buttonChooseCloneListsLocation.clicked.connect(lambda: write_config(parent, config, self))
        self.ui.buttonChooseMetadataLocation.clicked.connect(lambda: write_config(parent, config, self))

        def reset_config():
            self.ui.labelCloneListsLocation.setText(str(pathlib.Path(config.path_clone_list).resolve()))
            self.ui.labelMetadataLocation.setText(str(pathlib.Path(config.path_metadata).resolve()))
            self.ui.lineEditCloneListDownloadLocation.setText(config.clone_list_metadata_download_location)
            parent.clone_lists_folder = config.path_clone_list
            parent.metadata_folder = config.path_metadata
            parent.clone_list_metadata_url = config.clone_list_metadata_download_location
            write_config(parent, config, self)

        self.ui.pushButtonReset.clicked.connect(lambda: reset_config())


class TitleToolWindow(qtw.QMainWindow):
    def __init__(self, config: Config) -> None:
        """
        The title tool window in Retool. When a user enter's a title's full
        name, it shows the short name, group name, tag-free name, and
        region-free name.
        """

        super(TitleToolWindow, self).__init__()
        self.ui = Ui_CloneListNameTool()
        self.ui.setupUi(self)

        # Fix the fonts
        set_fonts(self)

        self.ui.lineEditEnterName.deleteLater()
        self.ui.lineEditEnterName = CustomLineEdit(self.ui.centralwidget)
        self.ui.lineEditEnterName.setObjectName(u"lineEditEnterName")
        self.ui.lineEditEnterName.setMinimumSize(qtc.QSize(320, 24))
        self.ui.verticalLayout.insertWidget(3, self.ui.lineEditEnterName)

        def update_names():
            self.ui.lineEditShortName.setText(TitleTools.get_short_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditGroupName.setText(TitleTools.get_group_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditTagFreeName.setText(TitleTools.get_tag_free_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditRegionFreeName.setText(TitleTools.get_region_free_name(self.ui.lineEditEnterName.text(), config))

        self.ui.lineEditEnterName.keyPressed.connect(update_names)


class CustomLineEdit(qtw.QLineEdit):
    """
    A subclassed line edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent=None) -> None:
        super(CustomLineEdit, self).__init__(parent)

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event) -> None:
        super(CustomLineEdit, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())


class CustomTextEdit(qtw.QTextEdit):
    """
    A subclassed text edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent=None) -> None:
        super(CustomTextEdit, self).__init__(parent)

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event) -> None:
        super(CustomTextEdit, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())


class CustomList(qtw.QListWidget):
    """
    A subclassed list widget that doesn't allow an item to be dragged and dropped within
    itself, and also emits keyboard and drop signals.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent=None, is_drag_drop: bool = True, self_drag: bool = False) -> None:
        super(CustomList, self).__init__(parent)

        self.drag = self_drag
        self.is_drag_drop = is_drag_drop

        if is_drag_drop:
            self.setAcceptDrops(True)
            self.setDragDropMode(qtw.QAbstractItemView.DragDrop)
            self.setDefaultDropAction(qtc.Qt.MoveAction)
        else:
            self.setDefaultDropAction(qtc.Qt.IgnoreAction)

        self.setTabKeyNavigation(True)
        self.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection)

        if not self_drag:
            self.setSortingEnabled(True)


    def dragEnterEvent(self, event) -> None:
        super().dragEnterEvent(event)
        event.accept()


    def dragMoveEvent(self, event) -> None:
        super().dragMoveEvent(event)
        if not self.drag:
            item = event.source()
            if item.isAncestorOf(self):
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

    # Handle drag and drop events
    dropped = qtc.Signal(int)

    def dropEvent(self, event) -> None:
        super().dropEvent(event)

        item = event.source()

        if not self.drag:
            if item.isAncestorOf(self):
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

        if event.isAccepted():
            # Make sure all the list items have been removed from the source before sending a signal
            def check_remove():
                while True:
                    try:
                        event.source()
                    except:
                        self.dropped.emit(event)
                        break

            t = threading.Thread(target=check_remove)
            t.start()

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event) -> None:
        super(CustomList, self).keyPressEvent(event)
        if not self.is_drag_drop:
            self.keyPressed.emit(event.key())


class CustomPushButton(qtw.QPushButton):
    def __init__(self, parent=None):
        """ Animates a button's background color.
        Modified from https://stackoverflow.com/questions/60443811/button-hover-transition-duration#answer-60446633

        Args:
            parent: The parent widget. Defaults to `None`.
        """
        super().__init__(parent)
        self._animation = qtc.QVariantAnimation()
        self._animation.setStartValue(qtg.QColor("#c3f1d6"))
        self._animation.setEndValue(qtg.QColor("lightgrey"))
        self._animation.setDuration(300)
        self._animation.valueChanged.connect(self._on_value_changed)
        self._update_stylesheet(qtg.QColor("lightgrey"), qtg.QColor("black"))

    def _on_value_changed(self, color):
            foreground = (
                qtg.QColor("black")
                if self._animation.direction() == qtc.QAbstractAnimation.Forward
                else qtg.QColor("black")
            )
            self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
            self.setStyleSheet(
                '''
                QPushButton{
                    background-color: %s;
                    color: %s;
                    text-align: center;
                    font-size: 13px;
                    margin: 4px 2px;
                    border: 1px solid #999;
                }
                QPushButton:disabled {
                    background-color: #ccc;
                    color: #777;
                    border: 1px solid #bfbfbf;
                }
                '''
                % (background.name(), foreground.name())
            )

    def enterEvent(self, event):
        self._animation.setDirection(qtc.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def focusInEvent(self, event):
        self._animation.setDirection(qtc.QAbstractAnimation.Backward)
        self._animation.start()
        super().focusInEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(qtc.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

    def focusOutEvent(self, event):
        self._animation.setDirection(qtc.QAbstractAnimation.Forward)
        self._animation.start()
        super().focusOutEvent(event)


class ElisionLabel(qtw.QLabel):
    """ Elides a label. Courtesy of
    https://stackoverflow.com/questions/11446478/pyside-pyqt-truncate-text-in-qlabel-based-on-minimumsize#answer-67628976

    Args:
        text: The label text.
        mode: Specifies where the elipsis in the label should go. Options include:
            * qtc.Qt.ElideLeft
            * qtc.Qt.ElideMiddle
            * qtc.Qt.ElideRight
        parent: The QWidget parent.
        f : Qt.WindowFlags(), as defined at
            https://doc-snapshots.qt.io/qtforpython-6.40/PySide6/QtCore/Qt.html#qtc.qtc.Qt.WindowType
    """

    elision_changed = qtc.Signal(bool)

    def __init__(self, text='', mode=qtc.Qt.ElideMiddle, **kwargs):
        super().__init__(**kwargs)

        self._mode = mode
        self.is_elided = False
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Preferred)
        self.setText(text)

    def setText(self, text):
        self._contents = text

        # This line set for testing.  Its value is the return value of
        # QFontMetrics.elidedText, set in paintEvent.  The variable
        # must be initialized for testing.  The value should always be
        # the same as contents when not elided.
        self._elided_line = text

        self.update()

    def text(self):
        return self._contents

    def paintEvent(self, event):
        super().paintEvent(event)

        did_elide = False

        painter = qtg.QPainter(self)
        font_metrics = painter.fontMetrics()
        text_width = font_metrics.horizontalAdvance(self.text())

        # layout phase
        text_layout = qtg.QTextLayout(self._contents, painter.font())
        text_layout.beginLayout()

        while True:
            line = text_layout.createLine()

            if not line.isValid():
                break

            line.setLineWidth(self.width())

            if text_width >= self.width():
                self._elided_line = font_metrics.elidedText(self._contents, self._mode, self.width())
                painter.drawText(qtc.QPoint(0, font_metrics.ascent()), self._elided_line)
                did_elide = line.isValid()
                break
            else:
                line.draw(painter, qtc.QPoint(0, 0))

        text_layout.endLayout()

        if did_elide != self.is_elided:
            self.is_elided = did_elide
            self.elision_changed.emit(did_elide)


class Filters():
    """ Creates an object for user filters """
    # TODO: This won't work with the new system config settings I don't think
    # TODO: As it would need to be referenced in each run

    def __init__(self, global_exclude:list[str]=[], global_include:list[str]=[]):
        self.exclude = global_exclude
        self.include = global_include
        self.file = ''


def add_list_items(list_widget, dat_details: dict[str, dict[str, str]], go_button, config: Config, input_type='files', recursive=False) -> None:
    """ Adds items to the passed in list widget

    Args:
        list_widget: The list widget to add the items to.
        dat_details (dict[str, dict[str, str]]): The dictionary that carries all the file details.
        config (Config): The Retool config object.
        input_type (str, optional): Whether the input as a folder or files. Defaults to
            'files'.
        recursive (bool, optional): Whether to treat adding a folder as recursive. Must be
            used in combination with input_type='folder'. Defaults to `False`.
    """
    response = None

    # Get the current list contents
    file_list: list[str] = [list_widget.item(x).text() for x in range(list_widget.count())]

    if input_type=='files':
        response = qtw.QFileDialog.getOpenFileNames(filter="DAT files (*.dat)")

        for i, file in enumerate(response[0], start=1):
            if pathlib.Path(file).name not in file_list:
                file_list.append(pathlib.Path(file).name)
                dat_details[pathlib.Path(file).name] = {'system_name': get_system_name(pathlib.Path(file), config), 'filepath': pathlib.Path(file)}
                list_widget.addItem(pathlib.Path(file).name)

    elif input_type=='folder':
        response = [qtw.QFileDialog.getExistingDirectory()]
        if recursive:
            files = list(pathlib.Path(response[0]).glob('**/*.dat'))
        else:
            files = list(pathlib.Path(response[0]).glob('*.dat'))

        if response[0]:
            for file in [x for x in files]:
                if pathlib.Path(file).name not in file_list:
                    dat_details[pathlib.Path(file).name] = {'system_name': get_system_name(pathlib.Path(file), config), 'filepath': pathlib.Path(file)}
                    list_widget.addItem(file.name)

    # Remove placeholder text from the list widget
    if response[0]:
        try:
            go_button.setEnabled(True)
            go_button.setToolTip('')
            placeholder_present = list_widget.findItems('No DAT files added yet',qtc.Qt.MatchExactly)[0]
            placeholder_text = list_widget.row(placeholder_present)
            list_widget.takeItem(placeholder_text)
        except:
            pass


def disable_incompatible_checkbox(checkbox_select, checkbox_disable, checkbox_check = ()) -> None:
    """
    When a checkbox is selected that's incompatible with other checkboxes,
    disable the other checkboxes. Reenable them when it's deselected.

    Args:
        checkbox_select: The checkbox widget the user has selected.
        checkbox_disable (tuple): The checkboxes that should be disabled as a
            result.
    """

    if checkbox_select.isChecked():
        for checkbox in checkbox_disable:
            checkbox.setChecked(False)
            checkbox.setEnabled(False)
    else:
        dont_enable: bool = False

        if checkbox_check:
            for checkbox in checkbox_check:
                if checkbox.isChecked():
                    dont_enable = True

        for checkbox in checkbox_disable:
            if not dont_enable:
                checkbox.setEnabled(True)


def get_gui_settings_value(key: str, default_value: str, config: Config, path: bool = True) -> str:
    """ Gets a value for a specific key out of the gui settings object in
    user-config.yaml.

    Args:
        key (str): The key in the gui settings object.
        default_value (str): The equivalent default value as found in
            internal-config.json
    """

    key_and_value: list[str] = [x for x in config.user_gui_settings if key in x and x != {f'"{key}": ""'}]

    value: str = ''

    if path:
        if key_and_value:
            if key_and_value[0][key] != str(pathlib.Path(default_value).resolve()):
                value = key_and_value[0][key]
        else:
            value = str(pathlib.Path(default_value).resolve())
    else:
        if key_and_value:
            if key_and_value[0][key] != default_value:
                value = key_and_value[0][key]
        else:
            value = default_value

    return value


def get_system_name(dat_file_path: str, config: Config) -> Dat:
    """ Given a DAT file path, opens the file and returns its system name
    with the DAT release group appended to it.

    Args:
        dat_file_path (str): The location of the DAT file.
        config (Config): The Retool config object.

    Returns:
        Dat: The system name stored in the DAT file.
    """

    with open(pathlib.Path(dat_file_path), 'rb') as file:
        pos: int = 0

        first_line = file.readline()
        header: bytes = b''
        system_name: str = ''

        file.seek(0)

        if (
            b'<?xml version' in first_line
            or b'<!DOCTYPE datafile' in first_line
            or b'<datafile>"' in first_line):
                while file.read(9) != b'</header>':
                    pos += 1
                    file.seek(pos, os.SEEK_SET)

                file.seek(0)
                header = file.read(pos + 9)
                system_name = re.search('<name>(.*?)</name>', str(header)).group(1).strip()
        elif b'clrmamepro' in first_line:
            while file.read(2) != b'\n)':
                pos += 1
                file.seek(pos, os.SEEK_SET)

            file.seek(0)
            header = file.read(pos - 2)
            system_name = re.search('name (.*)[\r\n]', header.decode("utf-8")).group(1).replace('"','').strip()

        # Clean up the name
        system_name = TitleTools.replace_invalid_characters(re.sub(' \\(Retool.*?\\)', '', system_name).replace('&amp;', '&'), config, is_header_detail=True)

        # Get the release group
        dat_group: str = ''

        if b'<url>' in header:
            search = re.search('<url>(.*?)</url>', str(header)).group(1).strip()
            if 'redump' in search:
                dat_group = ' (Redump)'
            elif 'no-intro' in search:
                dat_group = ' (No-Intro)'
            elif 'tosecdev.org' in search:
                dat_group = ' (TOSEC)'

        if re.search('author.*redump.org', str(header)):
            dat_group = ' (Redump)'

        if b'<homepage>' in header:
            search = re.search('<homepage>(.*?)</homepage>', str(header)).group(1).strip()

            if 'TOSEC' in search:
                dat_group = ' (TOSEC)'

        # Deal with https://dats.site DATs
        if 'GameCube' in system_name:
            if (
                'NKit GCZ' in system_name
                or 'NKit ISO' in system_name
                or 'NKit RVZ' in system_name
                or 'NASOS' in system_name):
                    system_name = 'Nintendo - GameCube (Redump)'

        if 'Wii' in system_name:
            if (
                'NKit GCZ' in system_name
                or 'NKit ISO' in system_name
                or 'NKit RVZ' in system_name
                or 'NASOS' in system_name):
                    system_name = 'Nintendo - Wii (Redump)'

        if (
            'Wii U' in system_name
            and 'WUX' in system_name):
                system_name = 'Nintendo - Wii U (Redump)'

    return f'{system_name}{dat_group}'


def move_list_items(origin_list_widget, destination_list_widget, all_items: bool = False) -> None:
    """ Moves an item from a list widget to another

    Args:
        origin_list_widget (_type_): The source widget of the move.
        destination_list (_type_): The destination widget of the move.
        all_items (bool, optional): Whether the user has hit the "move all" button.
            Defaults to `False`.
    """

    if all_items:
        item_list = [origin_list_widget.item(x) for x in range(origin_list_widget.count())]
    else:
        item_list = origin_list_widget.selectedItems()

    for item in item_list:
        destination_list_widget.addItem(item.text())
        origin_list_widget.takeItem(origin_list_widget.row(item))


def order_list_items(list_widget, direction: str = '') -> None:
    """ Moves an item up or down in a list widget

    Args:
        list_widget: The widget to move the item in.
        direction (str): Either 'up' or 'down'.

    """

    # Get the selected items in row order
    selected_items_dict = {}

    for item in list_widget.selectedItems():
        selected_items_dict[list_widget.row(item)] = item

    selected_items = [x for x in dict(sorted(selected_items_dict.items())).values()]

    all_items = [list_widget.item(x) for x in range(list_widget.count())]
    remainder_items = [x for x in all_items if x not in selected_items]

    if selected_items:
        if direction == 'up':
            # Get the top row number in the selected list
            top_row: int = list_widget.row(selected_items[0])

            if top_row <= 1:
                all_items = selected_items + remainder_items
            else:
                all_items = remainder_items[:top_row - 1] + selected_items + remainder_items[top_row - 1:]
        elif direction == 'down':
            # Get the bottom row number in the selected list
            bottom_row: int = list_widget.row(selected_items[-1])

            if bottom_row >= len(all_items) -2:
                all_items = remainder_items + selected_items
            else:
                all_items = (
                    remainder_items[:-len(all_items[bottom_row + 2:])]
                    + selected_items
                    + all_items[bottom_row + 2:]
                )

        # Convert the items to text, or QT can't retain the values if we clear the list later
        selected_items_text: list[str] = [x.text() for x in selected_items]
        all_items_text: list[str] = [x.text() for x in all_items]

        # Empty the list, then add the new entries
        list_widget.clear()
        list_widget.addItems(all_items_text)

        # Select the items the user previously had selected
        for item in selected_items_text:
            list_widget.findItems(item, qtc.Qt.MatchFlag.MatchExactly)[0].setSelected(True)

        # Scroll the list widget to keep the selected items in view
        if direction == 'up':
            list_widget.scrollToItem(list_widget.item(top_row - 2))
        elif direction == 'down':
            list_widget.scrollToItem(list_widget.item(bottom_row + 2))


def remove_list_items(list_widget, dat_details: dict[str, dict[str, str]], system_settings_widget, go_button, remove_all=True) -> None:
    """ Removes items from the passed in list

    Args:
        list_widget: The list widget to remove the items from
        dat_details (dict[str, dict[str, str]]): The dictionary that carries all the file
            details.
        system_settings_widget: The widget that holds the system settings. This is updated
            if there's nothing left in the list widget.
        remove_all (bool, optional): Whether the user has hit the remove all button, all
            has individually removed an item. Defaults to `True`.
    """

    if remove_all:
        dat_details.clear()
        list_widget.clear()
    else:
        item_list = list_widget.selectedItems()

        for item in item_list:
            dat_details.pop(item.text())
            list_widget.takeItem(list_widget.row(item))

    if not [list_widget.item(x) for x in range(list_widget.count())]:
        go_button.setDisabled(True)
        go_button.setToolTip(qtc.QCoreApplication.translate("MainWindow", u"You need to add DAT files to the list before you can process them", None))
        list_widget.addItem('No DAT files added yet')
        system_settings_widget.setText('Select a system from the filter list to enable system-specific settings.')


def select_checkboxes(checkboxes, set_checked: bool) -> None:
    """ Given a list of checkbox widgets, either checks or unchecks them all.

    Args:
        checkboxes: The list of checkbox widgets.
        set_checked (bool): Whether to check or uncheck the checkboxes.
    """
    for checkbox in checkboxes:
        checkbox.setChecked(set_checked)


def set_fonts(parent) -> None:
    """ Sets the fonts on a Window, based on the OS that Retool is running on.

    Args:
        parent: The parent window.
    """

    if sys.platform.startswith('win'):
        fonts: str = 'Segoe UI, Tahoma, Arial'
    elif 'linux' in sys.platform:
        fonts = 'Ubuntu, DejaVu Sans, FreeSans'

    parent.setStyleSheet(f'font-family: {fonts}')


def set_path(parent, current_path: str, label, parent_attr: str, input_type: str = 'folder') -> None:
    """ Sets a path for a particular setting.

    Args:
        parent: The parent widget.
        current_folder (str): What the folder is currently set to.
        label: The widget label to update with the new path.
        parent_attr (str): The attribute on the parent that stores the path.
    """
    if input_type == 'folder':
        new_path = str(pathlib.Path(qtw.QFileDialog.getExistingDirectory()))
    else:
        new_path = str(pathlib.Path(qtw.QFileDialog.getOpenFileName(filter="User config file (*.yaml)")[0]))

    if new_path != '.':
        label.setText(new_path)
    else:
        new_path = current_path
        label.setText(new_path)

    setattr(parent, parent_attr, new_path)


def show_hide(checkbox_select, widget_to_change) -> None:
    """
    When a checkbox is selected, show a part of the UI. When it's
    deselected, hide that part of the UI.

    Args:
        checkbox_select: The checkbox widget the user has selected.
        checkbox_disable (tuple): The checkboxes that should be disabled as a
            result.
    """

    if checkbox_select.isChecked():
        widget_to_change.show()
    else:
        widget_to_change.hide()


def write_config(parent, config: Config, settings=None, run_retool: bool = False, update_clone_list: bool = False):
    """ Gets widgets' state, then writes the user-config.yaml file """

    # Global list widgets
    available_languages: list[str] = [parent.ui.listWidgetGlobalAvailableLanguages.item(x).text() for x in range(parent.ui.listWidgetGlobalAvailableLanguages.count())]
    available_regions: list[str] = [parent.ui.listWidgetGlobalAvailableRegions.item(x).text() for x in range(parent.ui.listWidgetGlobalAvailableRegions.count())]
    selected_languages: list[str] = [parent.ui.listWidgetGlobalSelectedLanguages.item(x).text() for x in range(parent.ui.listWidgetGlobalSelectedLanguages.count())]
    selected_regions: list[str] = [parent.ui.listWidgetGlobalSelectedRegions.item(x).text() for x in range(parent.ui.listWidgetGlobalSelectedRegions.count())]
    video_standards: list[str] = [parent.ui.listWidgetGlobalVideoStandards.item(x).text() for x in range(parent.ui.listWidgetGlobalVideoStandards.count())]

    # If English isn't being processed, make sure it's commented out and at the top of the list
    if 'English' in available_languages: available_languages = ['English'] + [x for x in available_languages if x != 'English']

    # Global exclude options
    exclude_add_ons: bool = parent.ui.checkBoxGlobalExcludeAddOns.isChecked()
    exclude_applications: bool = parent.ui.checkBoxGlobalExcludeApplications.isChecked()
    exclude_audio: bool = parent.ui.checkBoxGlobalExcludeAudio.isChecked()
    exclude_bad_dumps: bool = parent.ui.checkBoxGlobalExcludeBadDumps.isChecked()
    exclude_bios: bool = parent.ui.checkBoxGlobalExcludeBIOS.isChecked()
    exclude_bonus_discs: bool = parent.ui.checkBoxGlobalExcludeBonusDiscs.isChecked()
    exclude_coverdiscs: bool = parent.ui.checkBoxGlobalExcludeCoverdiscs.isChecked()
    exclude_demos: bool = parent.ui.checkBoxGlobalExcludeDemos.isChecked()
    exclude_educational: bool = parent.ui.checkBoxGlobalExcludeEducational.isChecked()
    exclude_manuals: bool = parent.ui.checkBoxGlobalExcludeManuals.isChecked()
    exclude_mia: bool = parent.ui.checkBoxGlobalExcludeMIA.isChecked()
    exclude_multimedia: bool = parent.ui.checkBoxGlobalExcludeMultimedia.isChecked()
    exclude_pirate: bool = parent.ui.checkBoxGlobalExcludePirate.isChecked()
    exclude_preproduction: bool = parent.ui.checkBoxGlobalExcludePreproduction.isChecked()
    exclude_promotional: bool = parent.ui.checkBoxGlobalExcludePromotional.isChecked()
    exclude_unlicensed: bool = parent.ui.checkBoxGlobalExcludeUnlicensed.isChecked()
    exclude_video: bool = parent.ui.checkBoxGlobalExcludeVideo.isChecked()

    # Global options
    disable_1G1R: bool = parent.ui.checkBoxGlobalOptionsDisable1G1R.isChecked()
    prefer_regions: bool = parent.ui.checkBoxGlobalOptionsPreferRegions.isChecked()
    include_hashless: bool = parent.ui.checkBoxGlobalOptionsIncludeHashless.isChecked()
    modern_platforms: bool = parent.ui.checkBoxGlobalOptionsModernPlatforms.isChecked()
    demote_unlicensed: bool = parent.ui.checkBoxGlobalOptionsDemoteUnlicensed.isChecked()
    disable_filters: bool = parent.ui.checkBoxGlobalOptionsDisableFilters.isChecked()
    split_regions: bool = parent.ui.checkBoxGlobalOptionsSplitRegions.isChecked()
    removes_dat: bool = parent.ui.checkBoxGlobalOptionsRemovesDat.isChecked()
    keep_removes: bool = parent.ui.checkBoxGlobalOptionsKeepRemove.isChecked()
    list_1g1r_names: bool = parent.ui.checkBoxGlobalOptions1G1RNames.isChecked()
    report_warnings: bool = parent.ui.checkBoxGlobalOptionsReportWarnings.isChecked()
    pause_on_warnings: bool = parent.ui.checkBoxGlobalOptionsPauseWarnings.isChecked()
    legacy_dat: bool = parent.ui.checkBoxGlobalOptionsLegacy.isChecked()
    bypass_dtd: bool = parent.ui.checkBoxGlobalOptionsBypassDTD.isChecked()
    disable_multiprocessor: bool = parent.ui.checkBoxGlobalOptionsDisableMultiCPU.isChecked()
    trace: bool = parent.ui.checkBoxGlobalOptionsTrace.isChecked()

    prefix_1g1r: str = parent.ui.lineEditGlobalOptions1G1RPrefix.text().replace('\\', '\\\\').replace('"', '\\"')
    suffix_1g1r: str = parent.ui.lineEditGlobalOptions1G1RSuffix.text().replace('\\', '\\\\').replace('"', '\\"')

    trace_str: str = ''

    if trace:
        trace_str = parent.ui.lineEditGlobalOptionsTrace.text().replace('\\', '\\\\').replace('"', '\\"')

    # Global user filters
    global_exclude_filters: list[str] = []
    global_include_filters: list[str] = []

    if parent.ui.textEditGlobalExclude.toPlainText():
        global_exclude_filters: list[str] = parent.ui.textEditGlobalExclude.toPlainText().split('\n')
        global_exclude_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in global_exclude_filters if x]
    if parent.ui.textEditGlobalInclude.toPlainText():
        global_include_filters: list[str] = parent.ui.textEditGlobalInclude.toPlainText().split('\n')
        global_include_filters = [x.replace('\\', '\\\\').replace('"', '\\"') for x in global_include_filters if x]

    languages: tuple[str] = tuple([f'Comment|{x}' for x in available_languages] + selected_languages)
    regions: tuple[str] = tuple([f'Comment|{x}' for x in available_regions] + selected_regions)

    global_filters = Filters(global_exclude=global_exclude_filters, global_include=global_include_filters)
    # TODO: Figure out system filters
    system_filters = Filters()

    excludes: set[str] = set()

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
    if exclude_multimedia:  excludes.add('M')
    if exclude_pirate:  excludes.add('p')
    if exclude_preproduction:  excludes.add('P')
    if exclude_promotional:  excludes.add('r')
    if exclude_unlicensed:  excludes.add('u')
    if exclude_video:  excludes.add('v')

    gui_settings: list[str] = []

    if disable_1G1R: gui_settings.append('d')
    if prefer_regions: gui_settings.append('r')
    if include_hashless: gui_settings.append('e')
    if modern_platforms: gui_settings.append('z')
    if demote_unlicensed: gui_settings.append('y')
    if disable_filters: gui_settings.append('nofilters')
    if split_regions: gui_settings.append('regionsplit')
    if removes_dat: gui_settings.append('removesdat')
    if keep_removes: gui_settings.append('log')
    if list_1g1r_names: gui_settings.append('listnames')
    if report_warnings: gui_settings.append('warnings')
    if pause_on_warnings: gui_settings.append('warningpause')
    if legacy_dat: gui_settings.append('legacy')
    if bypass_dtd: gui_settings.append('nodtd')
    if disable_multiprocessor: gui_settings.append('singlecpu')
    if trace_str: gui_settings.append(f'trace: "{trace_str}"')

    # Add the excludes in
    gui_settings.sort()
    exclude_str: str = ''.join(sorted(excludes, key=str.casefold))

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

    if 'legacy' in gui_settings: user_options_list.append('x')

    user_options_str: str = ''

    if user_options_list:
        user_options_str = f' (-{"".join(sorted(user_options_list))})'

    gui_settings.append(f'exclude: {exclude_str}')
    gui_settings.append(f'output: {parent.output_folder}')

    # Grab settings from the settings dialog if it's open
    if settings:
        if (
            settings.ui.labelCloneListsLocation.text() != str(pathlib.Path(config.path_clone_list).resolve())
            and settings.ui.labelCloneListsLocation.text() != 'No clone list folder selected'):
                gui_settings.append(f'clone lists folder: {settings.ui.labelCloneListsLocation.text()}')

        if (
            settings.ui.labelMetadataLocation.text() != str(pathlib.Path(config.path_metadata).resolve())
            and settings.ui.labelMetadataLocation.text() != 'No metadata folder selected'):
                gui_settings.append(f'metadata folder: {settings.ui.labelMetadataLocation.text()}')

        if (
            settings.ui.lineEditCloneListDownloadLocation.text() != str(config.clone_list_metadata_download_location)
            and settings.ui.lineEditCloneListDownloadLocation.text() != ''):
                gui_settings.append(f'clone list metadata url: {settings.ui.lineEditCloneListDownloadLocation.text()}')
    else:
        # Compensate if we can't get the settings from the dialog itself
        clone_lists_folder: str = ''
        metadata_folder: str = ''
        clone_list_metadata_url: str = ''

        if parent.clone_lists_folder:
            clone_lists_folder = str(pathlib.Path(parent.clone_lists_folder).resolve())
        else:
            clone_lists_folder = get_gui_settings_value("clone lists folder", config.path_metadata, config)

        if parent.metadata_folder:
            metadata_folder = str(pathlib.Path(parent.metadata_folder).resolve())
        else:
            metadata_folder = get_gui_settings_value("metadata folder", config.path_metadata, config)

        if parent.clone_list_metadata_url:
            clone_list_metadata_url = parent.clone_list_metadata_url
        else:
            clone_list_metadata_url = get_gui_settings_value("clone list metadata url", config.clone_list_metadata_download_location, config, path=False)

        if (
            clone_lists_folder
            and clone_lists_folder != str(pathlib.Path(config.path_clone_list).resolve())):
                gui_settings.append(f'clone lists folder: {clone_lists_folder}')
        if (
            metadata_folder
            and metadata_folder != str(pathlib.Path(config.path_metadata).resolve())):
                gui_settings.append(f'metadata folder: {metadata_folder}')
        if (
            clone_list_metadata_url
            and clone_list_metadata_url != config.clone_list_metadata_download_location):
                gui_settings.append(f'clone list metadata url: {clone_list_metadata_url}')

    generate_config(config.user_config_file, languages, regions, video_standards, config.user_filters_path, global_filters, system_filters, prefix_1g1r, suffix_1g1r, gui_settings, overwrite=True)

    if run_retool:
        if dat_details:
            # Get a file list
            dat_files: list[pathlib.Path] = []
            for key in dat_details.keys():
                dat_files.append(dat_details[key]['filepath'])

            for dat_file in dat_files:

                # Build the gui_input instance
                filter_languages_enabled: bool = False

                if selected_languages:
                    filter_languages_enabled = True

                gui_input: UserInput = UserInput(
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
                    clone_list = '',  # TODO
                    user_config = '',
                    metadata = '', # TODO
                    no_filters = disable_filters,
                    list_names = list_1g1r_names,
                    log = keep_removes,
                    output_folder_name = parent.output_folder,
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

            parent.ui.buttonStop.show()
            parent.ui.mainProgram.setDisabled(True)
        else:
            gui_input: UserInput = UserInput(
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

        parent.start_retool_thread(gui_input)


# Run the Retool process in a separate thread. Needed so we can disable/enable
# bits of the Retool GUI as required, or cancel the process.

# Modified from
# https://www.pythonguis.com/faq/postpone-the-execution-of-sequential-processes-until-previous-thread-emit-the-result/

class Signals(qtc.QObject):
    finished = qtc.Signal(UserInput)

class ThreadTask(qtc.QRunnable):
    def __init__(self, data, argument):
        super().__init__()
        self.data = data
        self.argument = argument

    @qtc.Slot()
    def run(self):
        try:
            retool.main(self.argument)
        except retool.ExitRetool:
            # Quietly re-enable the GUI on this exception
            pass
        except Exception:
            print(f'\n{Font.error}Retool has had an unexpected error. Please raise an issue at\nhttps://github.com/unexpectedpanda/retool/issues, attaching\nthe DAT file that caused the problem and the following trace:{Font.end}\n')
            traceback.print_exc()
            print(f'\n{Font.error}The error occurred on this file:\n{self.argument.input_file_name}{Font.end}\n')

        self.signals.finished.emit(self.data)

class RunThread(ThreadTask):
    signals = Signals()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    # Make sure everything scales as expected across multiple PPI settings
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

    print('Don\'t close this window, Retool uses it for processing.')

    app = qtw.QApplication(sys.argv)
    dat_details: dict[str, dict[str, str]] = {}
    window = MainWindow()

    # Show any line edits we need to if an associated checkbox is selected in
    # user-config.yaml. This has to be delayed, or they don't show.
    show_hide(window.ui.checkBoxGlobalOptions1G1RNames, window.ui.frameGlobalOptions1G1RPrefix)
    show_hide(window.ui.checkBoxGlobalOptionsTrace, window.ui.frameGlobalOptionsTrace)

    window.show()

    sys.exit(app.exec())