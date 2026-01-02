import html
import pathlib
import sys
from typing import Any

import darkdetect  # type: ignore
import validators
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

import modules.constants as const
from modules.config.config import Config
from modules.gui.gui_config import write_config
from modules.gui.gui_utils import set_fonts, set_path
from modules.gui.gui_widgets import ElisionLabel
from modules.gui.retool_about import Ui_AboutWindow  # type: ignore
from modules.gui.retool_clone_list_name import Ui_CloneListNameTool  # type: ignore
from modules.gui.retool_settings import Ui_Settings  # type: ignore
from modules.titletools import TitleTools


class AboutWindow(qtw.QDialog):
    def __init__(self, parent: Any = None) -> None:
        """
        The "About" window for Retool.

        Args:
            parent (Any): The parent window that called this one. Important so the modal
                doesn't turn up on the taskbar, and makes the parent inaccessible while
                the modal is open. Defaults to `None`.
        """
        super().__init__(parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)

        # Change link colors if dark mode is detected
        if darkdetect.isDark():
            self.ui.labelName.setText(
                self.ui.labelName.text().replace('color:#0000ff', 'color:#47aae9')
            )
            self.ui.labelCreditIcons8.setText(
                self.ui.labelCreditIcons8.text().replace(
                    'color:#0000ff',
                    'color:#47aae9',
                )
            )

        # Fix the fonts
        set_fonts(self)

        # Set Retool versions
        self.ui.labelVersion.setText(f'Version: {const.__version__}')


class SettingsWindow(qtw.QDialog):
    def __init__(
        self, dat_details: dict[str, dict[str, str]], config: Config, parent: Any = None
    ) -> None:
        """
        The "Settings" window for Retool.

        Args:
            dat_details (dict[str, dict[str, str]]): The dictionary that carries DAT file
                details like its system name and filepath.

            config (Config): The Retool config object.

            parent (Any): The parent window that called this one. Important so the modal
                doesn't turn up on the taskbar, and makes the parent inaccessible while
                the modal is open. Defaults to `None`.
        """
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        # Hide the error label
        self.ui.labelURLError.hide()

        # The folder location labels don't want to render with promoted subclasses (likely
        # the parent is wrong), so we have to do it manually
        self.ui.labelCloneListsLocation.hide()
        self.ui.labelCloneListsLocation.deleteLater()
        self.ui.labelCloneListsLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameCloneListsLocation)  # type: ignore
        self.ui.labelCloneListsLocation.setText(
            qtc.QCoreApplication.translate('Settings', 'No clone list folder selected', None)
        )
        self.ui.labelCloneListsLocation.setObjectName('labelCloneListsLocation')
        self.ui.labelCloneListsLocation.setGeometry(qtc.QRect(56, 20, 520, 20))
        self.ui.labelCloneListsLocation.setStyleSheet('color: #777')

        self.ui.labelMetadataLocation.hide()
        self.ui.labelMetadataLocation.deleteLater()
        self.ui.labelMetadataLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameMetadataLocation)  # type: ignore
        self.ui.labelMetadataLocation.setText(
            qtc.QCoreApplication.translate('Settings', 'No metadata folder selected', None)
        )
        self.ui.labelMetadataLocation.setObjectName('labelMetadataLocation')
        self.ui.labelMetadataLocation.setGeometry(qtc.QRect(56, 20, 520, 20))
        self.ui.labelMetadataLocation.setStyleSheet('color: #777')

        self.ui.labelMIALocation.hide()
        self.ui.labelMIALocation.deleteLater()
        self.ui.labelMIALocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameMIALocation)  # type: ignore
        self.ui.labelMIALocation.setText(
            qtc.QCoreApplication.translate('Settings', 'No MIA folder selected', None)
        )
        self.ui.labelMIALocation.setObjectName('labelMIALocation')
        self.ui.labelMIALocation.setGeometry(qtc.QRect(56, 20, 520, 20))
        self.ui.labelMIALocation.setStyleSheet('color: #777')

        self.ui.labelRALocation.hide()
        self.ui.labelRALocation.deleteLater()
        self.ui.labelRALocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameRALocation)  # type: ignore
        self.ui.labelRALocation.setText(
            qtc.QCoreApplication.translate('Settings', 'No RetroAchievements folder selected', None)
        )
        self.ui.labelRALocation.setObjectName('labelRALocation')
        self.ui.labelRALocation.setGeometry(qtc.QRect(56, 20, 520, 20))
        self.ui.labelRALocation.setStyleSheet('color: #777')

        self.ui.labelQuickImportLocation.hide()
        self.ui.labelQuickImportLocation.deleteLater()
        self.ui.labelQuickImportLocation = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=self.ui.frameQuickImportLocation)  # type: ignore
        self.ui.labelQuickImportLocation.setText(
            qtc.QCoreApplication.translate('Settings', 'No quick import folder selected', None)
        )
        self.ui.labelQuickImportLocation.setObjectName('labelQuickImportLocation')
        self.ui.labelQuickImportLocation.setGeometry(qtc.QRect(56, 20, 520, 20))
        self.ui.labelQuickImportLocation.setStyleSheet('color: #777')

        # Fix the fonts
        set_fonts(self)

        # Get the values from the user config
        self.ui.labelCloneListsLocation.setText(
            str(pathlib.Path(parent.clone_lists_folder).resolve())
        )
        self.ui.labelMetadataLocation.setText(str(pathlib.Path(parent.metadata_folder).resolve()))
        self.ui.labelMIALocation.setText(str(pathlib.Path(parent.mia_folder).resolve()))
        self.ui.labelRALocation.setText(str(pathlib.Path(parent.ra_folder).resolve()))
        if parent.quick_import_folder:
            self.ui.labelQuickImportLocation.setText(
                str(pathlib.Path(parent.quick_import_folder).resolve())
            )
        self.ui.lineEditCloneListDownloadLocation.setText(parent.clone_list_metadata_url)

        # Set up the interactions
        self.ui.buttonChooseCloneListsLocation.clicked.connect(
            lambda: set_path(
                parent,
                parent.clone_lists_folder,
                self.ui.labelCloneListsLocation,
                'clone_lists_folder',
                input_type='folder',
            )
        )
        self.ui.buttonChooseMetadataLocation.clicked.connect(
            lambda: set_path(
                parent,
                parent.metadata_folder,
                self.ui.labelMetadataLocation,
                'metadata_folder',
                input_type='folder',
            )
        )
        self.ui.buttonChooseMIALocation.clicked.connect(
            lambda: set_path(
                parent,
                parent.mia_folder,
                self.ui.labelMIALocation,
                'mia_folder',
                input_type='folder',
            )
        )
        self.ui.buttonChooseRALocation.clicked.connect(
            lambda: set_path(
                parent,
                parent.ra_folder,
                self.ui.labelRALocation,
                'ra_folder',
                input_type='folder',
            )
        )
        self.ui.buttonChooseQuickImportLocation.clicked.connect(
            lambda: set_path(
                parent,
                parent.quick_import_folder,
                self.ui.labelQuickImportLocation,
                'quick_import_folder',
                input_type='folder',
            )
        )

        def url_entry(url: str) -> None:
            """
            Validates a URL, writes to config accordingly.

            Args:
                url (str): The URL to validate.
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

        self.ui.lineEditCloneListDownloadLocation.keyPressed.connect(
            lambda: url_entry(self.ui.lineEditCloneListDownloadLocation.text())
        )

        # Set up config writing
        self.ui.buttonChooseCloneListsLocation.clicked.connect(
            lambda: write_config(parent, dat_details, config, self)
        )
        self.ui.buttonChooseMetadataLocation.clicked.connect(
            lambda: write_config(parent, dat_details, config, self)
        )
        self.ui.buttonChooseMIALocation.clicked.connect(
            lambda: write_config(parent, dat_details, config, self)
        )
        self.ui.buttonChooseRALocation.clicked.connect(
            lambda: write_config(parent, dat_details, config, self)
        )
        self.ui.buttonChooseQuickImportLocation.clicked.connect(
            lambda: write_config(parent, dat_details, config, self)
        )

        def reset_config() -> None:
            """Resets the settings window when the reset button is clicked."""
            self.ui.labelCloneListsLocation.setText(
                str(pathlib.Path(config.path_clone_list).resolve())
            )
            self.ui.labelMetadataLocation.setText(str(pathlib.Path(config.path_metadata).resolve()))
            self.ui.labelMIALocation.setText(str(pathlib.Path(config.path_mia).resolve()))
            self.ui.labelRALocation.setText(str(pathlib.Path(config.path_ra).resolve()))
            self.ui.labelQuickImportLocation.setText(
                qtc.QCoreApplication.translate('Settings', 'No quick import folder selected', None)
            )
            self.ui.lineEditCloneListDownloadLocation.setText(
                config.clone_list_metadata_download_location
            )
            parent.clone_lists_folder = config.path_clone_list
            parent.metadata_folder = config.path_metadata
            parent.mia_folder = config.path_mia
            parent.ra_folder = config.path_ra
            parent.quick_import_folder = config.path_quick_import
            parent.clone_list_metadata_url = config.clone_list_metadata_download_location
            self.ui.labelURLError.hide()
            write_config(parent, dat_details, config, self)

        self.ui.pushButtonReset.clicked.connect(lambda: reset_config())


class TitleToolWindow(qtw.QMainWindow):
    def __init__(self, config: Config) -> None:
        """
        The title tool window in Retool. When a user enter's a title's full name, it shows
        the short name, group name, tag-free name, and region-free name.

        Args:
            config (Config): The Retool config object.
        """
        super().__init__()
        self.ui = Ui_CloneListNameTool()
        self.ui.setupUi(self)

        # Change link and field colors if dark mode is detected
        if darkdetect.isDark():
            self.ui.labelContribute.setText(
                self.ui.labelContribute.text().replace('color:#0000ff', 'color:#47aae9')
            )
            dark_mode_disabled_line_edit = '''
                QLineEdit{
                    background-color: #4a4a4a;
                }
                '''
            self.ui.lineEditShortName.setStyleSheet(dark_mode_disabled_line_edit)
            self.ui.lineEditGroupName.setStyleSheet(dark_mode_disabled_line_edit)
            self.ui.lineEditRegionFreeName.setStyleSheet(dark_mode_disabled_line_edit)

        # Fix the fonts
        set_fonts(self)

        # Fix checkboxes, which have a weird hover effect on Windows 4k monitors on hover if
        # you don't set a size that's divisible by 4. Also add custom SVGs to fix
        # check mark scaling.
        if sys.platform != 'darwin':
            checkbox_style = '''
                            QCheckBox::indicator {width: 16px; height: 16px;}
                            QCheckBox::indicator:unchecked {image: url(:/checkboxes/images/checkbox.svg);}
                            QCheckBox::indicator:unchecked:disabled {image: url(:/checkboxes/images/checkbox-disabled.svg);}
                            QCheckBox::indicator:unchecked:hover {image: url(:/checkboxes/images/checkbox-hover.svg);}
                            QCheckBox::indicator:unchecked:pressed {image: url(:/checkboxes/images/checkbox-pressed.svg);}
                            QCheckBox::indicator:checked {image: url(:/checkboxes/images/checkbox-checked.svg);}
                            QCheckBox::indicator:checked:disabled {image: url(:/checkboxes/images/checkbox-checked-disabled.svg);}
                            QCheckBox::indicator:checked:hover {image: url(:/checkboxes/images/checkbox-checked-hover.svg);}
                            QCheckBox::indicator:checked:pressed {image: url(:/checkboxes/images/checkbox-checked-pressed.svg);}
                            QCheckBox::indicator:checked:pressed {image: url(:/checkboxes/images/checkbox-checked-pressed.svg);}
                            '''

            checkboxes = self.ui.centralwidget.findChildren(
                qtw.QCheckBox, qtc.QRegularExpression('(checkBox.*)')
            )
            for checkbox in checkboxes:
                checkbox.setStyleSheet(checkbox_style)

        def update_names() -> None:
            """
            Grabs the different name variants of the title the user entered and populates
            the fields.
            """
            tags: set[str] = set(
                [f'({x}' for x in html.unescape(self.ui.lineEditEnterName.text()).split(' (')][
                    1:None
                ]
            )

            self.ui.lineEditShortName.setText(
                f'{TitleTools.get_short_name(html.unescape(self.ui.lineEditEnterName.text()), tags, config)}'
            )
            self.ui.lineEditGroupName.setText(
                TitleTools.get_group_name(html.unescape(self.ui.lineEditEnterName.text()), config)
            )
            self.ui.lineEditRegionFreeName.setText(
                f'{TitleTools.get_region_free_name(html.unescape(self.ui.lineEditEnterName.text()), tags, config)}'
            )

        self.ui.lineEditEnterName.keyPressed.connect(update_names)
