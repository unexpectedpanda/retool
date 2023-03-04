"""
Filters DATs from [Redump](http://redump.org/) and
[No-Intro](https://www.no-intro.org) to remove titles
you don't want.

https://github.com/unexpectedpanda/retool
"""

import multiprocessing
import os
import sys
import traceback

import retool

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from modules.constants import *
from modules.config import Config
from modules.gui.retool_ui import Ui_MainWindow # type: ignore
from modules.gui.custom_widgets import custom_widgets, CustomList
from modules.gui.gui_config import import_config, write_config
from modules.gui.gui_setup import setup_gui_global, setup_gui_system
from modules.gui.gui_utils import show_hide
from modules.input import UserInput
from modules.utils import eprint, Font

# Require at least Python 3.10
assert sys.version_info >= (3, 10)

class MainWindow(qtw.QMainWindow):
    """ The main window for RetoolGUI """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = {}
        self.threadpool: qtc.QThreadPool = qtc.QThreadPool()

        # Limit the number of CLI threads that can run to 1. Potentially if we get
        # out of the CLI in the future and into full GUI this can be increased.
        self.threadpool.setMaxThreadCount(1)

        # Fix the taskbar icon not loading on Windows
        if sys.platform.startswith('win'):
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'retool')

        # Replace default QT widgets with customized versions
        self = custom_widgets(self)

        # Set the window size
        self.setFixedSize(957, 610)

        # Set the tab order
        # TODO: Set the tab order for replaced elements... shouldn't be so bad I think?

        # Disable the system settings for first launch
        self.ui.tabWidgetSystemSettings.setEnabled(False)

        # Import the user config
        config: Config = import_config()

        # Populate the global settings with data and set up user interactions
        setup_gui_global(self, dat_details, config)

        # Populate the system settings with data and set up user interactions
        setup_gui_system(self, dat_details, config)

        # Add all widgets to a list that should trigger a config write if interacted with
        interactive_widgets = []
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QPushButton, qtc.QRegularExpression('buttonGlobal(Language|Region|Video|Deselect|Select|Default).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QPushButton, qtc.QRegularExpression('buttonSystem(Language|Region|Video|Deselect|Select|Default).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QPushButton, qtc.QRegularExpression('button(Choose|Clear)System.*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxGlobal(Exclude|Options).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QCheckBox, qtc.QRegularExpression('checkBoxSystem(Exclude|Options|Override).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QTextEdit, qtc.QRegularExpression('textEditGlobal(Exclude|Include).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QTextEdit, qtc.QRegularExpression('textEditSystem(Exclude|Include).*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QLineEdit, qtc.QRegularExpression('lineEditGlobalOptions.*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QLineEdit, qtc.QRegularExpression('lineEditSystemOptions.*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QListWidget, qtc.QRegularExpression('listWidgetGlobal.*')))
        interactive_widgets.extend(self.ui.centralwidget.findChildren(qtw.QListWidget, qtc.QRegularExpression('listWidgetSystem.*')))
        interactive_widgets.extend([self.ui.buttonChooseOutput])

        # Track all meaningful interactions, write the config file if one happens
        for interactive_widget in interactive_widgets:
            try:
                if type(interactive_widget) is not CustomList:
                    interactive_widget.clicked.connect(lambda: write_config(self, dat_details, config, settings_window=None))
            except:
                pass
            try:
                interactive_widget.keyPressed.connect(lambda: write_config(self, dat_details, config, settings_window=None))
            except:
                pass
            try:
                interactive_widget.dropped.connect(lambda: write_config(self, dat_details, config, settings_window=None))
            except:
                pass


    def start_retool_thread(self, data: UserInput = None) -> None:
        """
        Start the thread that calls Retool CLI.

        Args:
            `data (UserInput)`: The Retool user input object. Defaults to `None`.
        """

        self.data = {}  # reset
        self.new_thread = RunThread('Retool', data)

        # Check to see if we can enable the interface
        self.new_thread.signals.finished.connect(self.enable_app)

        self.threadpool.start(self.new_thread)


    def enable_app(self):
        """ If all the threads have finished, re-enable the interface """
        if (self.threadpool.activeThreadCount() == 0):
            self.ui.buttonGo.setEnabled(True)
            self.ui.buttonStop.hide()
            self.ui.buttonStop.setText(qtc.QCoreApplication.translate("MainWindow", u"Stop", None))
            self.ui.buttonStop.setEnabled(True)
            self.ui.mainProgram.setEnabled(True)


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
            eprint(f'\n{Font.error}Retool has had an unexpected error. Please raise an issue at\nhttps://github.com/unexpectedpanda/retool/issues, attaching\nthe DAT file that caused the problem and the following trace:{Font.end}\n')
            traceback.print_exc()
            eprint(f'\n{Font.error}The error occurred on this file:\n{self.argument.input_file_name}{Font.end}\n')
            self.signals.finished.emit(self.data)

        self.signals.finished.emit(self.data)

class RunThread(ThreadTask):
    signals: Signals = Signals()


if __name__ == "__main__":
    multiprocessing.freeze_support()

    # Make sure everything scales as expected across multiple PPI settings
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

    # Encourage the user not to close the CLI
    eprint('Don\'t close this window, Retool uses it for processing.')

    # Set variables
    app: qtw.QApplication = qtw.QApplication(sys.argv)
    dat_details: dict[str, dict[str, str]] = {}
    window: MainWindow = MainWindow()

    # Show any line edits we need to if an associated checkbox is selected in
    # user-config.yaml. This has to be delayed, or they don't show.
    show_hide(window.ui.checkBoxGlobalOptions1G1RNames, window.ui.frameGlobalOptions1G1RPrefix)
    show_hide(window.ui.checkBoxGlobalOptionsTrace, window.ui.frameGlobalOptionsTrace)

    # Show the main window
    window.show()

    sys.exit(app.exec())