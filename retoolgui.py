#!/usr/bin/env python

"""
Filters DATs from [Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org) to remove titles
you don't want.

https://github.com/unexpectedpanda/retool
"""

import multiprocessing
import os
import pathlib
import sys
import traceback
from typing import Any

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

import retool
from modules.config import Config
from modules.gui.custom_widgets import CustomList, custom_widgets
from modules.gui.gui_config import import_config, write_config
from modules.gui.gui_setup import setup_gui_global, setup_gui_system
from modules.gui.gui_utils import enable_go_button, show_hide
from modules.gui.retool_ui import Ui_MainWindow  # type: ignore
from modules.input import UserInput
from modules.utils import Font, eprint

# Require at least Python 3.10
assert sys.version_info >= (3, 10)

dat_details: dict[str, dict[str, str]] = {}


def main() -> None:
    multiprocessing.freeze_support()

    # Make sure everything scales as expected across multiple PPI settings
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

    # Encourage the user not to close the CLI
    eprint('Don\'t close this window, Retool uses it for processing.')

    # Set variables
    app: qtw.QApplication = qtw.QApplication(sys.argv)
    window: MainWindow = MainWindow()

    # Show any line edits we need to if an associated checkbox is selected in
    # user-config.yaml. This has to be delayed, or they don't show.
    show_hide(window.ui.checkBoxGlobalOptions1G1RNames, window.ui.frameGlobalOptions1G1RPrefix)
    show_hide(window.ui.checkBoxGlobalOptionsTrace, window.ui.frameGlobalOptionsTrace)

    # Check if the "Process DAT files" button should be enabled
    enable_go_button(window)

    # Show the main window
    window.show()

    # Prompt the user if clone lists or metadata are needed
    if window.clonelistmetadata_needed:
        msg = qtw.QMessageBox()
        msg.setText(
            'This might be the first time you\'ve run Retool, as its clone lists\n'
            'or metadata files are missing.\n\n'
            'Retool is more accurate with these files. Do you want to\n'
            'download them?'
        )
        msg.setWindowTitle('Clone lists or metadata needed')
        msg.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No)  # type: ignore
        icon = qtg.QIcon()
        icon.addFile(':/retoolIcon/images/retool.ico', qtc.QSize(), qtg.QIcon.Normal, qtg.QIcon.Off)  # type: ignore
        msg.setWindowIcon(icon)

        download_update: int = msg.exec()

        if download_update == qtw.QMessageBox.Yes:  # type: ignore
            config: Config = import_config()
            write_config(
                window,
                dat_details,
                config,
                settings_window=None,
                run_retool=True,
                update_clone_list=True,
            )

    sys.exit(app.exec())


class MainWindow(qtw.QMainWindow):
    """The main window for RetoolGUI."""

    # Import the user config
    config: Config = import_config()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data: dict[Any, Any] = {}
        self.threadpool: qtc.QThreadPool = qtc.QThreadPool()
        self.clonelistmetadata_needed: bool = False

        # Limit the number of CLI threads that can run to 1. Potentially if we get
        # out of the CLI in the future and into full GUI this can be increased.
        self.threadpool.setMaxThreadCount(1)

        # Fix the taskbar icon not loading on Windows
        if sys.platform.startswith('win'):
            import ctypes

            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('retool')

        # Replace default QT widgets with customized versions
        self = custom_widgets(self)

        # Disable the system settings for first launch
        self.ui.tabWidgetSystemSettings.setEnabled(False)

        # Populate the global settings with data and set up user interactions
        setup_gui_global(self, dat_details, self.config)

        # Populate the system settings with data and set up user interactions
        setup_gui_system(self, dat_details, self.config)

        # Check if clone lists or metadata files are required
        if not (
            pathlib.Path(self.config.path_clone_list).is_dir()
            and pathlib.Path(self.config.path_metadata).is_dir()
        ):
            self.clonelistmetadata_needed = True

        # Set up a timer on the splitter move before writing to config
        timer_splitter = qtc.QTimer(self)
        timer_splitter.setSingleShot(True)
        timer_splitter.timeout.connect(
            lambda: write_config(self, dat_details, self.config, settings_window=None)
        )

        self.ui.splitter.splitterMoved.connect(lambda: timer_splitter.start(500))

        # Set up a timer on the window resize move before writing to config
        self.timer_resize = qtc.QTimer(self)
        self.timer_resize.setSingleShot(True)
        self.timer_resize.timeout.connect(
            lambda: write_config(self, dat_details, self.config, settings_window=None)
        )

        # Add all widgets to a list that should trigger a config write if interacted with
        interactive_widgets = []
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QPushButton,
                qtc.QRegularExpression(
                    'buttonGlobal(Language|Region|Localization|Video|Deselect|Select|Default).*'
                ),
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QPushButton,
                qtc.QRegularExpression(
                    'buttonSystem(Language|Region|Localization|Video|Deselect|Select|Default).*'
                ),
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QPushButton, qtc.QRegularExpression('button(Choose|Clear)System.*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QCheckBox, qtc.QRegularExpression('checkBoxGlobal(Exclude|Options).*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QCheckBox, qtc.QRegularExpression('checkBoxSystem(Exclude|Options|Override).*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QTextEdit, qtc.QRegularExpression('textEditGlobal(Exclude|Include|Filter).*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QTextEdit, qtc.QRegularExpression('textEditSystem(Exclude|Include|Filter).*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QLineEdit, qtc.QRegularExpression('lineEditGlobalOptions.*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QLineEdit, qtc.QRegularExpression('lineEditSystemOptions.*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QListWidget, qtc.QRegularExpression('listWidgetGlobal.*')
            )
        )
        interactive_widgets.extend(
            self.ui.centralwidget.findChildren(
                qtw.QListWidget, qtc.QRegularExpression('listWidgetSystem.*')
            )
        )
        interactive_widgets.extend([self.ui.buttonChooseOutput])

        # Track all meaningful interactions, write the config file if one happens
        for interactive_widget in interactive_widgets:
            try:
                if type(interactive_widget) is not CustomList:
                    interactive_widget.clicked.connect(
                        lambda: write_config(self, dat_details, self.config, settings_window=None)
                    )
            except Exception:
                pass
            try:
                interactive_widget.keyPressed.connect(
                    lambda: write_config(self, dat_details, self.config, settings_window=None)
                )
            except Exception:
                pass
            try:
                interactive_widget.dropped.connect(
                    lambda: write_config(self, dat_details, self.config, settings_window=None)
                )
            except Exception:
                pass

    def closeEvent(self, event: Any) -> None:
        qtw.QApplication.closeAllWindows()
        event.accept()

    def enable_app(self) -> None:
        """If all the threads have finished, re-enable the interface."""
        if self.threadpool.activeThreadCount() == 0:
            self.ui.buttonGo.setEnabled(True)
            self.ui.buttonStop.hide()
            self.ui.buttonGo.show()
            self.ui.buttonStop.setText(qtc.QCoreApplication.translate("MainWindow", "Stop", None))
            self.ui.buttonStop.setEnabled(True)
            self.ui.mainProgram.setEnabled(True)

    def resizeEvent(self, event: Any) -> None:
        """Record the window size when the user resizes it."""
        # Set up a timer on the resize before writing to config

        self.timer_resize.start(500)

    def start_retool_thread(self, data: UserInput | None = None) -> None:
        """
        Start the thread that calls Retool CLI.

        Args:
            data (UserInput): The Retool user input object. Defaults to `None`.
        """
        self.data = {}  # reset
        self.new_thread = RunThread('Retool', data)

        # Check to see if we can enable the interface
        self.new_thread.signals.finished.connect(self.enable_app)

        self.threadpool.start(self.new_thread)


# Run the Retool process in a separate thread. Needed so we can disable/enable
# bits of the Retool GUI as required, or cancel the process.

# Modified from
# https://www.pythonguis.com/faq/postpone-the-execution-of-sequential-processes-until-previous-thread-emit-the-result/


class Signals(qtc.QObject):
    finished = qtc.Signal(UserInput)


class ThreadTask(qtc.QRunnable):
    def __init__(self, data: Any, argument: Any) -> None:
        super().__init__()
        self.data = data
        self.argument = argument

    @qtc.Slot()
    def run(self) -> None:
        try:
            retool.main(self.argument)
        except retool.ExitRetool:  # type: ignore
            # Quietly re-enable the GUI on this exception
            pass
        except Exception:
            eprint(
                f'\n{Font.error}Retool has had an unexpected error. Please raise an issue at\nhttps://github.com/unexpectedpanda/retool/issues, attaching\nthe DAT file that caused the problem and the following trace:{Font.end}\n'
            )
            traceback.print_exc()
            eprint(
                f'\n{Font.error}The error occurred on this file:\n{self.argument.input_file_name}{Font.end}\n'
            )
            if pathlib.Path('.dev').is_file():
                input(
                    f'\n{Font.disabled}Press enter to continue. This message is only shown in dev mode.{Font.end}'
                )
            self.signals.finished.emit(self.data)  # type: ignore

        self.signals.finished.emit(self.data)  # type: ignore


class RunThread(ThreadTask):
    signals: Signals = Signals()


if __name__ == '__main__':
    main()
