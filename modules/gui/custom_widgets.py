import pathlib
import sys
import threading

from typing import Any

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

from modules.gui.gui_utils import set_fonts


class CustomLineEdit(qtw.QLineEdit):
    """ A subclassed line edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent: Any = None) -> None:
        super(CustomLineEdit, self).__init__(parent)

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super(CustomLineEdit, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())


class CustomList(qtw.QListWidget):
    """ A subclassed list widget that doesn't allow an item to be dragged and dropped
    within itself, and also emits keyboard and drop signals.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """


    def __init__(self, parent: Any = None, is_drag_drop: bool = True, self_drag: bool = False) -> None:
        super(CustomList, self).__init__(parent)

        self.drag = self_drag
        self.is_drag_drop = is_drag_drop

        if is_drag_drop:
            self.setAcceptDrops(True)
            self.setDragDropMode(qtw.QAbstractItemView.DragDrop) # type: ignore
            self.setDefaultDropAction(qtc.Qt.MoveAction) # type: ignore
        else:
            self.setDefaultDropAction(qtc.Qt.IgnoreAction) # type: ignore

        self.setTabKeyNavigation(True)
        self.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection) # type: ignore

        if not self_drag:
            self.setSortingEnabled(True)


    def dragEnterEvent(self, event: qtg.QDragEnterEvent) -> None:
        super().dragEnterEvent(event)
        event.accept()


    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)
        if not self.drag:
            item = event.source()
            if item.isAncestorOf(self): # type: ignore
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

    # Handle drag and drop events
    dropped = qtc.Signal(int)


    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

        item = event.source()

        if not self.drag:
            if item.isAncestorOf(self): # type: ignore
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

        if event.isAccepted():
            # Make sure all the list items have been removed from the source before sending a signal
            def check_remove() -> None:
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


    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super(CustomList, self).keyPressEvent(event)
        if not self.is_drag_drop:
            self.keyPressed.emit(event.key())


class CustomPushButton(qtw.QPushButton):
    """ Animates a button's background color.
    Modified from https://stackoverflow.com/questions/60443811/button-hover-transition-duration#answer-60446633

    Args:
        `parent`: The parent widget. Defaults to `None`.
    """


    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)
        self._animation = qtc.QVariantAnimation()
        self._animation.setStartValue(qtg.QColor("#c3f1d6"))
        self._animation.setEndValue(qtg.QColor("lightgrey"))
        self._animation.setDuration(300)
        self._animation.valueChanged.connect(self._on_value_changed) # type: ignore
        self._update_stylesheet(qtg.QColor("lightgrey"), qtg.QColor("black"))


    def _on_value_changed(self, color: Any) -> None:
            foreground = (
                qtg.QColor("black")
                if self._animation.direction() == qtc.QAbstractAnimation.Forward # type: ignore
                else qtg.QColor("black")
            )
            self._update_stylesheet(color, foreground)


    def _update_stylesheet(self, background: Any, foreground: Any) -> None:
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


    def enterEvent(self, event: qtg.QEnterEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Backward) # type: ignore
        self._animation.start()
        super().enterEvent(event)


    def focusInEvent(self, event: qtg.QFocusEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Backward) # type: ignore
        self._animation.start()
        super().focusInEvent(event)


    def leaveEvent(self, event: qtc.QEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Forward) # type: ignore
        self._animation.start()
        super().leaveEvent(event)


    def focusOutEvent(self, event: qtg.QFocusEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Forward) # type: ignore
        self._animation.start()
        super().focusOutEvent(event)


class CustomTextEdit(qtw.QTextEdit):
    """ A subclassed text edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """


    def __init__(self, parent: Any = None) -> None:
        super(CustomTextEdit, self).__init__(parent)

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)


    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super(CustomTextEdit, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())


class ElisionLabel(qtw.QLabel):
    """ Elides a label. Courtesy of
    https://stackoverflow.com/questions/11446478/pyside-pyqt-truncate-text-in-qlabel-based-on-minimumsize#answer-67628976

    Args:
        `text`: The label text.
        `mode`: Specifies where the elipsis in the label should go. Options include:
            * qtc.Qt.ElideLeft
            * qtc.Qt.ElideMiddle
            * qtc.Qt.ElideRight
        `parent`: The QWidget main_window.
        `f`: Qt.WindowFlags(), as defined at
            https://doc-snapshots.qt.io/qtforpython-6.40/PySide6/QtCore/Qt.html#qtc.qtc.Qt.WindowType
    """

    elision_changed = qtc.Signal(bool)


    def __init__(self, text: str = '', mode: Any = qtc.Qt.ElideMiddle, **kwargs: Any) -> None:  # type: ignore
        super().__init__(**kwargs)

        self._mode = mode
        self.is_elided = False
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Preferred) # type: ignore
        self.setText(text)


    def setText(self, text: Any) -> None:
        self._contents = text

        # This line set for testing. Its value is the return value of
        # QFontMetrics.elidedText, set in paintEvent. The variable
        # must be initialized for testing.  The value should always be
        # the same as contents when not elided.
        self._elided_line = text

        self.update()


    def text(self) -> Any:
        return self._contents


    def paintEvent(self, event: qtg.QPaintEvent) -> None:
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


def custom_line_edit(widget: qtw.QLineEdit, widget_name: str, parent: Any, x: int, y: int, w: int, h: int, min_w: int, min_h: int) -> Any:
        """ Deletes the existing line edit widget, and replaces it with a custom one.

        Args:
            `widget (qtw.QLineEdit)`: The original line edit widget.
            `widget_name (str)`: The line edit widget's name.
            `parent (Any)`: The parent widget that houses the line edit widget.
            `x (int)`: X coordinate of the line edit widget from the left.
            `y (int)`: Y coordinate of the line edit widget from the top.
            `w (int)`: Width of the line edit widget.
            `h (int)`: Height of the line edit widget.
            `min_w (int)`: Minimum width of the line edit widget.
            `min_h (int)`: Minimum height of the line edit widget.

        Returns:
            `Any`: The new line edit widget.
        """

        widget.deleteLater()
        new_widget = CustomLineEdit(parent)
        new_widget.setObjectName(widget_name)
        new_widget.setGeometry(qtc.QRect(x, y, w, h))
        new_widget.setMinimumSize(qtc.QSize(min_w, min_h))

        return new_widget


def custom_list(widget: qtw.QListWidget, widget_name: str, parent: Any, x: int, y: int, w: int, h: int, is_drag_drop: bool = False, self_drag: bool = False) -> Any:
    """ Deletes the existing list widget, and replaces it with a custom one.

    Args:
        `widget (qtw.QListWidget):` The original list widget.
        `widget_name (str)`: The list widget's name.
        `parent (any)`: The parent widget that houses the list widget.
        `x (int)`: X coordinate of the list widget from the left.
        `y (int)`: Y coordinate of the list widget from the top.
        `w (int)`: Width of the list widget.
        `h (int)`: Height of the list widget.
        `is_drag_drop (bool)`: Whether the list widget has drag and drop enabled.
        `self_drag (bool)`: Whether the widget allows drag and drop to itself.

    Returns:
        `Any`: The new list widget.
    """

    widget.deleteLater()
    new_widget = CustomList(parent, is_drag_drop, self_drag)
    new_widget.setObjectName(widget_name)
    new_widget.setGeometry(qtc.QRect(x, y, w, h))

    return new_widget


def custom_text_edit(widget: qtw.QTextEdit, widget_name: str, parent: Any) -> Any:
    """ Deletes the existing text edit widget, and replaces it with a custom one.

    Args:
        `widget (qtw.QTextEdit)`: The original text edit widget.
        `widget_name (str)`: The text edit widget's name.
        `parent (Any)`: The parent widget that houses the text edit widget.

    Returns:
        `Any`: The new text edit widget.
    """

    widget.deleteLater()
    new_widget = CustomTextEdit(parent)
    new_widget.setObjectName(widget_name)
    new_widget.setMinimumSize(qtc.QSize(0, 100))
    new_widget.setMaximumSize(qtc.QSize(16777215, 100))
    new_widget.setTabChangesFocus(True)
    new_widget.setAcceptRichText(False)

    return new_widget


def custom_widgets(main_window: Any) -> Any:
    """ Adds custom behavior to the default QT widgets.

    Args:
        `main_window (Any)`: The MainWindow widget.

    Returns:
        `Any`: MainWindow with the replaced widgets.
    """

    # Replace the list widgets with customized versions
    main_window.ui.listWidgetGlobalAvailableLanguages = custom_list(main_window.ui.listWidgetGlobalAvailableLanguages, 'listWidgetGlobalAvailableLanguages', main_window.ui.tabGlobalLanguages, 10, 70, 221, 291, is_drag_drop=True)
    main_window.ui.listWidgetGlobalAvailableRegions = custom_list(main_window.ui.listWidgetGlobalAvailableRegions, 'listWidgetGlobalAvailableRegions', main_window.ui.tabGlobalRegions, 10, 70, 221, 251, is_drag_drop=True)
    main_window.ui.listWidgetGlobalSelectedLanguages = custom_list(main_window.ui.listWidgetGlobalSelectedLanguages, 'listWidgetGlobalSelectedLanguages', main_window.ui.tabGlobalLanguages, 300, 70, 221, 291, is_drag_drop=True, self_drag=True)
    main_window.ui.listWidgetGlobalSelectedRegions = custom_list(main_window.ui.listWidgetGlobalSelectedRegions, 'listWidgetGlobalSelectedRegions', main_window.ui.tabGlobalRegions, 300, 70, 221, 251, is_drag_drop=True, self_drag=True)
    main_window.ui.listWidgetGlobalVideoStandards = custom_list(main_window.ui.listWidgetGlobalVideoStandards, 'listWidgetGlobalVideoStandards', main_window.ui.tabGlobalVideo, 10, 70, 221, 291, is_drag_drop=True, self_drag=True)

    main_window.ui.listWidgetSystemAvailableLanguages = custom_list(main_window.ui.listWidgetSystemAvailableLanguages, 'listWidgetSystemAvailableLanguages', main_window.ui.tabSystemLanguages, 10, 70, 221, 291, is_drag_drop=True)
    main_window.ui.listWidgetSystemAvailableRegions = custom_list(main_window.ui.listWidgetSystemAvailableRegions, 'listWidgetSystemAvailableRegions', main_window.ui.tabSystemRegions, 10, 70, 221, 251, is_drag_drop=True)
    main_window.ui.listWidgetSystemSelectedLanguages = custom_list(main_window.ui.listWidgetSystemSelectedLanguages, 'listWidgetSystemSelectedLanguages', main_window.ui.tabSystemLanguages, 300, 70, 221, 291, is_drag_drop=True, self_drag=True)
    main_window.ui.listWidgetSystemSelectedRegions = custom_list(main_window.ui.listWidgetSystemSelectedRegions, 'listWidgetSystemSelectedRegions', main_window.ui.tabSystemRegions, 300, 70, 221, 251, is_drag_drop=True, self_drag=True)
    main_window.ui.listWidgetSystemVideoStandards = custom_list(main_window.ui.listWidgetSystemVideoStandards, 'listWidgetSystemVideoStandards', main_window.ui.tabSystemVideo, 10, 70, 221, 291, is_drag_drop=True, self_drag=True)

    main_window.ui.listWidgetOpenFiles = custom_list(main_window.ui.listWidgetOpenFiles, 'listWidgetOpenFiles', main_window.ui.mainProgram, 60, 40, 251, 411, is_drag_drop=False)
    main_window.ui.listWidgetOpenFiles.addItem(qtc.QCoreApplication.translate('MainWindow', u'No DAT files added yet', None)) # type: ignore

    # Update the output folder label with custom behavior
    main_window.ui.labelOutputFolder.deleteLater()
    main_window.ui.labelOutputFolder = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=main_window.ui.mainProgram) # type: ignore
    main_window.ui.labelOutputFolder.setObjectName(u"labelOutputFolder")
    main_window.ui.labelOutputFolder.setText(str(pathlib.Path.cwd()))
    main_window.ui.labelOutputFolder.setGeometry(qtc.QRect(60, 500, 251, 16))
    main_window.ui.labelOutputFolder.setStyleSheet('color: #777')

    # Replace line edit widgets with customized versions
    main_window.ui.lineEditGlobalOptions1G1RPrefix = custom_line_edit(main_window.ui.lineEditGlobalOptions1G1RPrefix, 'lineEditGlobalOptions1G1RPrefix', main_window.ui.frameGlobalOptions1G1RPrefix, 20, 30, 521, 24, 0, 24)
    main_window.ui.lineEditGlobalOptions1G1RSuffix = custom_line_edit(main_window.ui.lineEditGlobalOptions1G1RSuffix, 'lineEditGlobalOptions1G1RSuffix', main_window.ui.frameGlobalOptions1G1RPrefix, 20, 83, 521, 24, 0, 24)
    main_window.ui.lineEditGlobalOptionsTrace = custom_line_edit(main_window.ui.lineEditGlobalOptionsTrace, 'lineEditGlobalOptionsTrace', main_window.ui.frameGlobalOptionsTrace, 20, 30, 521, 24, 0, 24)

    main_window.ui.lineEditSystemOptions1G1RPrefix = custom_line_edit(main_window.ui.lineEditSystemOptions1G1RPrefix, 'lineEditSystemOptions1G1RPrefix', main_window.ui.frameSystemOptions1G1RPrefix, 20, 30, 521, 24, 0, 24)
    main_window.ui.lineEditSystemOptions1G1RSuffix = custom_line_edit(main_window.ui.lineEditSystemOptions1G1RSuffix, 'lineEditSystemOptions1G1RSuffix,', main_window.ui.frameSystemOptions1G1RPrefix, 20, 83, 521, 24, 0, 24)
    main_window.ui.lineEditSystemOptionsTrace = custom_line_edit(main_window.ui.lineEditSystemOptionsTrace, 'lineEditSystemOptionsTrace', main_window.ui.frameSystemOptionsTrace, 20, 30, 521, 24, 0, 24)

    # Replace text edit widgets with customized versions
    main_window.ui.textEditGlobalExclude = custom_text_edit(main_window.ui.textEditGlobalExclude, 'textEditGlobalExclude', main_window.ui.scrollAreaWidgetContentsGlobalUserFilters)
    main_window.ui.textEditGlobalInclude = custom_text_edit(main_window.ui.textEditGlobalInclude, 'textEditGlobalInclude', main_window.ui.scrollAreaWidgetContentsGlobalUserFilters)

    main_window.ui.verticalLayout_2.insertWidget(8, main_window.ui.textEditGlobalInclude)
    main_window.ui.verticalLayout_2.insertWidget(12, main_window.ui.textEditGlobalExclude)

    main_window.ui.textEditSystemExclude = custom_text_edit(main_window.ui.textEditSystemExclude, 'textEditSystemExclude', main_window.ui.scrollAreaWidgetContentsSystemUserFilters)
    main_window.ui.textEditSystemInclude = custom_text_edit(main_window.ui.textEditSystemInclude, 'textEditSystemInclude', main_window.ui.scrollAreaWidgetContentsSystemUserFilters)

    main_window.ui.verticalLayout_4.insertWidget(8, main_window.ui.textEditSystemInclude)
    main_window.ui.verticalLayout_4.insertWidget(12, main_window.ui.textEditSystemExclude)

    # Fix the scrollArea background color,which for some reason is altered by setting
    # the font previously
    scroll_area_style = '''
                        QScrollArea { background: transparent; }
                        QScrollArea > QWidget > QWidget { background: transparent; }
                        QScrollArea > QWidget > QScrollBar { background-color: none; }
                        '''

    main_window.ui.scrollAreaGlobalOptions.setStyleSheet(scroll_area_style)
    main_window.ui.scrollAreaGlobalUserFilters.setStyleSheet(scroll_area_style)
    main_window.ui.scrollAreaSystemOptions.setStyleSheet(scroll_area_style)
    main_window.ui.scrollAreaSystemUserFilters.setStyleSheet(scroll_area_style)

    # Fix some line heights for Ubuntu
    if 'linux' in sys.platform:
        main_window.ui.verticalSpacerGlobalOptions.changeSize(20,3)
        main_window.ui.verticalSpacerGlobalUserFilters.changeSize(20,3)
        main_window.ui.verticalSpacerSystemUserFilters.changeSize(20,3)

    # Replace the "Process DAT files" button with a customized version
    main_window.ui.buttonGo.deleteLater()
    main_window.ui.buttonGo = CustomPushButton(main_window.ui.centralwidget)
    main_window.ui.buttonGo.setText(qtc.QCoreApplication.translate('MainWindow', u'Process DAT files', None)) # type: ignore
    main_window.ui.buttonGo.setObjectName(u'buttonGo')
    main_window.ui.buttonGo.setGeometry(qtc.QRect(801, 530, 140, 45))
    main_window.ui.buttonGo.setEnabled(False)
    main_window.ui.buttonGo.setToolTip(qtc.QCoreApplication.translate('MainWindow', u'You need to add DAT files to the list before you can process them', None)) # type: ignore

    main_window.ui.buttonStop = CustomPushButton(main_window.ui.centralwidget)
    main_window.ui.buttonStop.setText(qtc.QCoreApplication.translate('MainWindow', u'Stop', None)) # type: ignore
    main_window.ui.buttonStop.setObjectName(u'buttonStop')
    main_window.ui.buttonStop.setGeometry(qtc.QRect(801, 530, 140, 45))
    main_window.ui.buttonStop.hide()

    # Fix the fonts
    set_fonts(main_window)

    return main_window