import os
import pathlib
import re
import sys

from typing import Any

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from modules.config import Config
from modules.dats import format_system_name
from modules.titletools import TitleTools
from modules.utils import pattern2string


def add_list_items(list_widget: qtw.QListWidget, dat_details: dict[str, dict[str, str]], config: Config, main_window: Any, input_type: str = 'files', recursive: bool = False) -> None:
    """ Adds items to the passed in list widget.

    Args:
        - `list_widget (qtw.QListWidget)` The list widget to add the items to.

        - `dat_details (dict[str, dict[str, str]])` The dictionary that carries DAT file
          details like its system name and filepath.

        - `config (Config)` The Retool config object.

        - `main_window (Any)` The MainWindow widget.

        - `input_type (str, optional)` Whether the input as a folder or files. Defaults to
          `files`.

        - `recursive (bool, optional)` Whether to treat adding a folder as recursive. Must
          be used in combination with `input_type='folder'`. Defaults to `False`.
    """
    response: list[Any] = []

    # Get the current list contents
    file_list: list[str] = [list_widget.item(x).text() for x in range(list_widget.count())]

    if input_type == 'files':
        response = list(qtw.QFileDialog.getOpenFileNames(main_window, filter="DAT files (*.dat)"))

        for file in response[0]:
            if pathlib.Path(file).name not in file_list:
                file_list.append(pathlib.Path(file).name)
                dat_details[pathlib.Path(file).name] = {'system_name': get_system_name(str(pathlib.Path(file)), config), 'filepath': str(pathlib.Path(file))}
                list_widget.addItem(pathlib.Path(file).name)

    elif input_type == 'folder':
        response = [qtw.QFileDialog.getExistingDirectory()]
        files: list[pathlib.Path]

        if recursive:
            files = list(pathlib.Path(response[0]).glob('**/*.dat'))
        else:
            files = list(pathlib.Path(response[0]).glob('*.dat'))

        if response[0]:
            for file in [x for x in files]:
                if pathlib.Path(file).name not in file_list:
                    dat_details[pathlib.Path(file).name] = {'system_name': get_system_name(str(pathlib.Path(file)), config), 'filepath': str(pathlib.Path(file))}
                    list_widget.addItem(file.name)

    elif input_type == 'dropped':
        response = list(list_widget.dropped_files) # type: ignore

        for file in response:
            if pathlib.Path(file).name not in file_list:
                file_list.append(pathlib.Path(file).name)
                dat_details[pathlib.Path(file).name] = {'system_name': get_system_name(str(pathlib.Path(file)), config), 'filepath': str(pathlib.Path(file))}
                list_widget.addItem(pathlib.Path(file).name)


    # Remove placeholder text from the list widget
    if response[0]:
        try:
            placeholder_present: qtw.QListWidgetItem = list_widget.findItems('No DAT files added yet', qtc.Qt.MatchExactly)[0] # type: ignore
            placeholder_row: int = list_widget.row(placeholder_present)
            list_widget.takeItem(placeholder_row)
            enable_go_button(main_window)
        except:
            pass


def disable_incompatible_checkbox(checkbox_select: qtw.QCheckBox, checkbox_disable: tuple[qtw.QCheckBox, ...], checkbox_check: tuple[qtw.QCheckBox, ...] = ()) -> None:
    """ When a checkbox is selected that's incompatible with other checkboxes,
    disable those other checkboxes. Reenable them when it's cleared.

    Args:
        - `checkbox_select (qtw.QCheckBox)` The checkbox widget the user has interacted
          with.

        - `checkbox_disable (tuple[qtw.QCheckBox, ...])` The checkboxes that should be
          disabled/enabled based on whether or not `checkbox_select` is selected.

        - `checkbox_check (tuple[qtw.QCheckBox, ...], optional)` If these other checkboxes
          are selected, don't enable the `checkbox_disable` checkboxes, even if
          `checkbox_select` is cleared. Useful for three way relationships. For example:
          checkbox C must be disabled if checkbox A or B are checked. Defaults to `()`.
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

def enable_go_button(main_window: Any) -> None:
    """ Checks certain conditions to see if the "Process DAT files" button should be
    enabled or not.

    Args:
        - `main_window (Any)` The MainWindow widget.
    """

    disabled: bool = False
    message: str = ''

    # Check if there's at least one DAT file added
    if not [main_window.ui.listWidgetOpenFiles.item(x) for x in range(main_window.ui.listWidgetOpenFiles.count())]:
        disabled = True

        message = 'You need to add DAT files to the list'
    else:
        if 'No DAT files added yet' in [main_window.ui.listWidgetOpenFiles.item(x) for x in range(main_window.ui.listWidgetOpenFiles.count())][0].text():
            disabled = True

            message = 'You need to add DAT files to the list'

    # TODO: This gets a little more complicated with the system settings
    # Check if there's at least one region added
    if not [main_window.ui.listWidgetGlobalSelectedRegions.item(x).text() for x in range(main_window.ui.listWidgetGlobalSelectedRegions.count())]:
        disabled = True

        if message:
            message = f'{message},\nand add at least one region before you can process DATs'
        else:
            message = 'You need to add at least one region before you can process DATs'

    if message == 'You need to add DAT files to the list':
        message = f'{message} before you can process them'

    main_window.ui.buttonGo.setDisabled(disabled)

    # Set the tooltip
    if not disabled:
        main_window.ui.buttonGo.setToolTip('')
    else:
        main_window.ui.buttonGo.setToolTip(qtc.QCoreApplication.translate('MainWindow', f'{message}', None))


def get_system_name(dat_file_path: str, config: Config) -> str:
    """ Given a DAT file path, opens the file and returns its system name with the DAT
    release group appended to it.

    Args:
        - `dat_file_path (str)` The location of the DAT file.

        - `config (Config)` The Retool config object.

    Returns:
        `str` The system name stored in the DAT file.
    """

    with open(pathlib.Path(dat_file_path), 'rb') as file:
        pos: int = 0

        first_line: bytes = file.readline()
        header: bytes = b''
        system_name: str = ''
        regex_search_str: str = ''

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

                regex_search_str = pattern2string(re.compile('<name>(.*?)</name>'), str(header), group_number=1)
                system_name = regex_search_str.strip()
        elif b'clrmamepro' in first_line:
            while file.read(2) != b'\n)':
                pos += 1
                file.seek(pos, os.SEEK_SET)

            file.seek(0)
            header = file.read(pos - 2)

            regex_search_str = pattern2string(re.compile('name (.*)[\r\n]'), header.decode("utf-8"), group_number=1)
            system_name = regex_search_str.replace('"','').strip()

        # Clean up the name
        system_name = TitleTools.replace_invalid_characters(re.sub(' \\(Retool.*?\\)', '', system_name).replace('&amp;', '&'), config, is_header_detail=True)

        # Sanitize the system name to make referencing support files like clone lists and
        # system configurations easier
        system_url: str = ''
        system_homepage: str = ''
        system_comment: str = ''
        system_author: str = ''

        if b'<url>' in header:
            system_url = pattern2string(re.compile('<url>(.*?)</url>'), str(header), group_number=1).strip()

        if b'<homepage>' in header:
            system_homepage = pattern2string(re.compile('<homepage>(.*?)</homepage>'), str(header), group_number=1).strip()

        if b'<comment>' in header:
            system_comment = pattern2string(re.compile('<comment>(.*?)</comment>'), str(header), group_number=1).strip()

        if b'author' in header:
            system_author = pattern2string(re.compile('author.*([rR]edump.org)'), str(header), group_number=1).strip()

        system_name = format_system_name(system_name, system_url, system_homepage, system_comment, system_author)

    return f'{system_name}'


def move_list_items(origin_list_widget: qtw.QListWidget, destination_list_widget: qtw.QListWidget, all_items: bool = False) -> None:
    """ Moves an item from a list widget to another

    Args:
        - `origin_list_widget (qtw.QListWidget)` The source widget of the move.

        - `destination_list (qtw.QListWidget)` The destination widget of the move.

        - `all_items (bool, optional)` Whether the user has hit the "move all" button.
          Defaults to `False`.
    """

    item_list: list[qtw.QListWidgetItem]

    if all_items:
        item_list = [origin_list_widget.item(x) for x in range(origin_list_widget.count())]
    else:
        item_list = origin_list_widget.selectedItems()

    for item in item_list:
        destination_list_widget.addItem(item.text())
        origin_list_widget.takeItem(origin_list_widget.row(item))


def order_list_items(list_widget: qtw.QListWidget, direction: str) -> None:
    """ Moves an item up or down in a list widget.

    Args:
        - `list_widget(qtw.QListWidget)` The widget to move the item in.

        - `direction (str)` Either `up` or `down`.
    """

    # Get the selected items in row order
    selected_items_dict: dict[int, qtw.QListWidgetItem] = {}

    for item in list_widget.selectedItems():
        selected_items_dict[list_widget.row(item)] = item

    selected_items: list[qtw.QListWidgetItem] = [x for x in dict(sorted(selected_items_dict.items())).values()]

    all_items: list[qtw.QListWidgetItem] = [list_widget.item(x) for x in range(list_widget.count())]
    remainder_items: list[qtw.QListWidgetItem] = [x for x in all_items if x not in selected_items]

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
        for selected_item in selected_items_text:
            list_widget.findItems(selected_item, qtc.Qt.MatchFlag.MatchExactly)[0].setSelected(True)

        # Scroll the list widget to keep the selected items in view
        if direction == 'up':
            list_widget.scrollToItem(list_widget.item(top_row - 2))
        elif direction == 'down':
            list_widget.scrollToItem(list_widget.item(bottom_row + 2))


def remove_list_items(list_widget: qtw.QListWidget, dat_details: dict[str, dict[str, str]], system_settings_widget: Any, main_window: Any, remove_all: bool = True) -> None:
    """ Removes items from the passed in list.

    Args:
        - `list_widget (qtw.QListWidget)` The list widget to remove the items from

        - `dat_details (dict[str, dict[str, str]])` The dictionary that carries DAT file
          details like its system name and filepath.

        - `system_settings_widget (Any)` The widget that holds the system settings. This is
          updated if there's nothing left in the list widget.

        - `main_window (Any)` The MainWindow widget.

        - `remove_all (bool, optional)` Whether the user has hit the remove all button, all
          has individually removed an item. Defaults to `True`.
    """

    if remove_all:
        dat_details.clear()
        list_widget.clear()
    else:
        item_list: list[qtw.QListWidgetItem] = list_widget.selectedItems()

        for item in item_list:
            if item.text() != 'No DAT files added yet':
                dat_details.pop(item.text())
                list_widget.takeItem(list_widget.row(item))

    if not [list_widget.item(x) for x in range(list_widget.count())]:
        enable_go_button(main_window)
        list_widget.addItem('No DAT files added yet')
        system_settings_widget.setText('Add a DAT file, then select it in the list to enable system-specific settings.')
        main_window.ui.tabWidgetSystemSettings.setCurrentIndex(0)
        main_window.ui.tabWidgetSystemSettings.setEnabled(False)


def set_fonts(parent: Any) -> None:
    """ Sets the fonts on a widget, based on the OS that Retool is running on.

    Args:
        - `parent (Any)` The parent widget.
    """

    fonts: str = ''

    if sys.platform.startswith('win'):
        fonts = 'Segoe UI, Tahoma, Arial'
    elif 'linux' in sys.platform:
        fonts = 'Ubuntu, DejaVu Sans, FreeSans'

        all_widgets = []

        # Since Ubuntu fonts are really wide, find all widgets and decrease their font size
        try:
            all_widgets.extend(parent.findChildren(qtw.QPushButton))
            all_widgets.extend(parent.findChildren(qtw.QCheckBox))
            all_widgets.extend(parent.findChildren(qtw.QLabel))
            all_widgets.extend(parent.findChildren(qtw.QLineEdit))
            all_widgets.extend(parent.findChildren(qtw.QListWidget))
            all_widgets.extend(parent.findChildren(qtw.QTabWidget))
            all_widgets.extend(parent.findChildren(qtw.QTextEdit))
            all_widgets.extend(parent.findChildren(qtw.QToolTip))
        except:
            pass

        font: qtg.QFont

        for widget in all_widgets:
            try:
                font = widget.font()
                font.setPointSize(10)
                widget.setFont(font)
            except:
                pass

        # Pick up some straggling elements that don't update the font size
        try:
            font = parent.ui.labelGlobalSettings.font()
            font.setPointSize(10)
            parent.ui.menubar.setFont(font)
            parent.ui.menuFile.setFont(font)
            parent.ui.menuHelp.setFont(font)
        except:
            pass

        # Address other elements that need a different font size
        # Main window
        try:
            font = parent.ui.labelSelectOutput.font()
            font.setPointSize(8)
            parent.ui.labelSelectOutput.setFont(font)

            font = parent.ui.labelOutputFolder.font()
            font.setPointSize(8)
            parent.ui.labelOutputFolder.setFont(font)

            font = parent.ui.buttonGlobalDefaultRegionOrder.font()
            font.setPointSize(8)
            parent.ui.buttonGlobalDefaultRegionOrder.setFont(font)
        except:
            pass

    parent.setStyleSheet(f'font-family: {fonts}')


def set_path(parent: Any, current_path: str, label: qtw.QLabel, parent_attr: str, input_type: str = 'folder') -> None:
    """ Sets a path for a particular setting.

    Args:
        - `parent (Any)` The parent widget.

        - `current_folder (str)` What the folder is currently set to.

        - `label (qtw.QLabel)` The widget label to update with the new path.

        - `parent_attr (str)` The attribute on the parent that stores the path.
    """

    new_path: str = '.'

    if input_type == 'folder':
        new_path = str(pathlib.Path(qtw.QFileDialog.getExistingDirectory()))
    elif input_type == 'yaml':
        new_path = str(pathlib.Path(qtw.QFileDialog.getOpenFileName(parent, filter="User config file (*.yaml)")[0]))
    elif input_type == 'clone':
        new_path = str(pathlib.Path(qtw.QFileDialog.getOpenFileName(parent, filter="Clone list (*.json)")[0]))
    elif input_type == 'metadata':
        new_path = str(pathlib.Path(qtw.QFileDialog.getOpenFileName(parent, filter="Metadata file (*.json)")[0]))

    if new_path != '.':
        label.setText(new_path)
    else:
        if (
            current_path
            and current_path != '.'):
                new_path = current_path
                label.setText(new_path)

    setattr(parent, parent_attr, new_path)


def select_checkboxes(checkboxes: list[qtw.QCheckBox], set_checked: bool) -> None:
    """ Given a list of checkbox widgets, either checks or unchecks them all.

    Args:
        - `checkboxes (list[qtw.QCheckBox])` The list of checkbox widgets.
        - `set_checked (bool)` Whether to check or uncheck the checkboxes.
    """

    for checkbox in checkboxes:
        checkbox.setChecked(set_checked)


def show_hide(checkbox: qtw.QCheckBox, widget_to_change: Any) -> None:
    """ When a checkbox is selected, show a part of the UI. When it's cleared, hide that
    part of the UI.

    Args:
        - `checkbox (qtw.QCheckBox)` The checkbox widget the user has selected.

        - `widget_to_change (Any)` The element that should be shown or hidden.
    """

    if checkbox.isChecked():
        widget_to_change.show()
    else:
        widget_to_change.hide()


def system_enable(checkbox: qtw.QCheckBox, widgets: list[Any]) -> None:
    """ Enables or disables a set of widgets based on whether a checkbox is selected or
    not.

    Args:
        - `checkbox (qtw.QCheckBox)` The checkbox that controls if a widget is enabled
          or disabled.
        - `widgets (list[Any])` A list of widgets to enable or disable.
    """

    for widget in widgets:
        widget.setEnabled(checkbox.isChecked())
