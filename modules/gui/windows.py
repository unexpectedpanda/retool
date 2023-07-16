import pathlib
import validators # type: ignore

from typing import Any

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from modules.constants import *
from modules.config import Config
from modules.gui.retool_about import Ui_AboutWindow # type: ignore
from modules.gui.retool_settings import Ui_Settings # type: ignore
from modules.gui.retool_clone_list_name import Ui_CloneListNameTool # type: ignore
from modules.gui.custom_widgets import ElisionLabel
from modules.gui.gui_config import write_config
from modules.gui.gui_utils import set_fonts, set_path
from modules.titletools import TitleTools


class AboutWindow(qtw.QDialog):
    def __init__(self, parent: Any = None) -> None:
        """ The "About" window for Retool.

        Args:
            - `parent (Any)` The parent window that called this one. Important so the
              modal doesn't turn up on the taskbar, and makes the parent
              inaccessible while the modal is open. Defaults to `None`.

            - `version (str)` The GUI version.
        """

        super(AboutWindow, self).__init__(parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        # Fix the fonts
        set_fonts(self)

        # Set Retool versions
        self.ui.labelVersion.setText(f'Version: {VERSION_MAJOR}.{VERSION_MINOR}')


class SettingsWindow(qtw.QDialog):
    def __init__(self, dat_details: dict[str, dict[str, str]], config: Config, parent: Any = None) -> None:
        """ The "Settings" window for Retool.

        Args:
            - `dat_details (dict[str, dict[str, str]])` The dictionary that carries DAT
              file details like its system name and filepath.

            - `config (Config)` The Retool config object.

            - `parent (Any)` The parent window that called this one. Important so the modal
              doesn't turn up on the taskbar, and makes the parent inaccessible while the
              modal is open. Defaults to `None`.
        """

        super(SettingsWindow, self).__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        # Hide the error label
        self.ui.labelURLError.hide()

        # The folder location labels don't want to render with promoted subclasses (likely
        # the parent is wrong), so we have to do it manually
        self.ui.labelCloneListsLocation.hide()
        self.ui.labelCloneListsLocation.deleteLater()
        self.ui.labelCloneListsLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameCloneListsLocation) # type: ignore
        self.ui.labelCloneListsLocation.setText(qtc.QCoreApplication.translate('Settings', u'No clone list folder selected', None)) # type: ignore
        self.ui.labelCloneListsLocation.setObjectName(u'labelCloneListsLocation')
        self.ui.labelCloneListsLocation.setGeometry(qtc.QRect(50, 20, 531, 20))
        self.ui.labelCloneListsLocation.setStyleSheet('color: #777')

        self.ui.labelMetadataLocation.hide()
        self.ui.labelMetadataLocation.deleteLater()
        self.ui.labelMetadataLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameMetadataLocation) # type: ignore
        self.ui.labelMetadataLocation.setText(qtc.QCoreApplication.translate('Settings', u'No metadata folder selected', None)) # type: ignore
        self.ui.labelMetadataLocation.setObjectName(u'labelMetadataLocation')
        self.ui.labelMetadataLocation.setGeometry(qtc.QRect(50, 20, 531, 20))
        self.ui.labelMetadataLocation.setStyleSheet('color: #777')

        # Fix the fonts
        set_fonts(self)

        # Get the values from the user config
        self.ui.labelCloneListsLocation.setText(str(pathlib.Path(parent.clone_lists_folder).resolve()))
        self.ui.labelMetadataLocation.setText(str(pathlib.Path(parent.metadata_folder).resolve()))
        self.ui.lineEditCloneListDownloadLocation.setText(parent.clone_list_metadata_url)

        # Set up the interactions
        self.ui.buttonChooseCloneListsLocation.clicked.connect(lambda: set_path(parent, parent.clone_lists_folder, self.ui.labelCloneListsLocation, 'clone_lists_folder', input_type='folder'))
        self.ui.buttonChooseMetadataLocation.clicked.connect(lambda: set_path(parent, parent.metadata_folder, self.ui.labelMetadataLocation, 'metadata_folder', input_type='folder'))

        def url_entry(url: str) -> None:
            """ Validates a URL, writes to config accordingly.

            Args:
                - `url (str)` The URL to validate.
            """
            if not url:
                parent.clone_list_metadata_url = config.clone_list_metadata_download_location
                return
            else:
                if validators.url(url):
                    self.ui.labelURLError.hide()
                    parent.clone_list_metadata_url = url
                    write_config(parent, dat_details, config, self)
                else:
                    self.ui.labelURLError.show()

        self.ui.lineEditCloneListDownloadLocation.keyPressed.connect(lambda: url_entry(self.ui.lineEditCloneListDownloadLocation.text()))

        # Set up config writing
        self.ui.buttonChooseCloneListsLocation.clicked.connect(lambda: write_config(parent, dat_details, config, self))
        self.ui.buttonChooseMetadataLocation.clicked.connect(lambda: write_config(parent, dat_details, config, self))

        def reset_config() -> None:
            """ Resets the settings window when the reset button is clicked. """
            self.ui.labelCloneListsLocation.setText(str(pathlib.Path(config.path_clone_list).resolve()))
            self.ui.labelMetadataLocation.setText(str(pathlib.Path(config.path_metadata).resolve()))
            self.ui.lineEditCloneListDownloadLocation.setText(config.clone_list_metadata_download_location)
            parent.clone_lists_folder = config.path_clone_list
            parent.metadata_folder = config.path_metadata
            parent.clone_list_metadata_url = config.clone_list_metadata_download_location
            write_config(parent, dat_details, config, self)

        self.ui.pushButtonReset.clicked.connect(lambda: reset_config())


class TitleToolWindow(qtw.QMainWindow):
    def __init__(self, config: Config) -> None:
        """
        The title tool window in Retool. When a user enter's a title's full
        name, it shows the short name, group name, tag-free name, and
        region-free name.

        Args:
            - `config (Config)` The Retool config object.
        """

        super(TitleToolWindow, self).__init__()
        self.ui = Ui_CloneListNameTool()
        self.ui.setupUi(self)

        # Fix the fonts
        set_fonts(self)

        def update_names() -> None:
            """ Grabs the different name variants of the title the user entered and
            populates the fields.
            """
            self.ui.lineEditShortName.setText(TitleTools.get_short_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditGroupName.setText(TitleTools.get_group_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditTagFreeName.setText(TitleTools.get_tag_free_name(self.ui.lineEditEnterName.text(), config))
            self.ui.lineEditRegionFreeName.setText(TitleTools.get_region_free_name(self.ui.lineEditEnterName.text(), config))

        self.ui.lineEditEnterName.keyPressed.connect(update_names)