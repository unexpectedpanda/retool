import pathlib
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

        self.setTabKeyNavigation(True)
        self.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection) # type: ignore


    def dragEnterEvent(self, event: qtg.QDragEnterEvent) -> None:
        super().dragEnterEvent(event)
        event.accept()


    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)
        item = event.source()
        if item.isAncestorOf(self): # type: ignore
            event.ignore()
        else:
            event.accept()

    # Handle drag and drop events
    dropped = qtc.Signal(int)


    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

        item = event.source()


        if item.isAncestorOf(self): # type: ignore
            event.ignore()
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
        self.keyPressed.emit(event.key())


class CustomListSelfDrag(CustomList):
    """ A sub-subclassed list widget that does allow an item to be dragged and dropped
    within itself.
    """

    def __init__(self, parent: Any = None) -> None:
        super(CustomList, self).__init__(parent)

    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)
        event.accept()

    # Handle drag and drop events
    dropped = qtc.Signal(int)


    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

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
        `parent`: The QWidget main_window.
        `f`: Qt.WindowFlags(), as defined at
            https://doc-snapshots.qt.io/qtforpython-6.40/PySide6/QtCore/Qt.html#qtc.qtc.Qt.WindowType
    """

    elision_changed = qtc.Signal(bool)


    def __init__(self, text: str = '', mode: Any = qtc.Qt.ElideMiddle, **kwargs: Any) -> None:  # type: ignore
        super().__init__(**kwargs)

        self._mode = qtc.Qt.ElideLeft
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


def custom_widgets(main_window: Any) -> Any:
    """ Adjusts properties of the widgets not covered by the promoted subclasses.

    Args:
        `main_window (Any)`: The MainWindow widget.

    Returns:
        `Any`: MainWindow with the replaced widgets.
    """

    # DAT files list box
    main_window.ui.listWidgetOpenFiles.setDefaultDropAction(qtc.Qt.IgnoreAction) # type: ignore

    # The global output folder label doesn't want to render with promoted subclasses
    # (likely the parent is wrong), so we have to do it manually
    main_window.ui.labelOutputFolder.deleteLater()
    main_window.ui.labelOutputFolder = ElisionLabel('', mode=qtc.Qt.ElideLeft, parent=main_window.ui.mainProgram) # type: ignore
    main_window.ui.labelOutputFolder.setObjectName(u"labelOutputFolder")
    main_window.ui.labelOutputFolder.setText(str(pathlib.Path.cwd()))
    main_window.ui.labelOutputFolder.setGeometry(qtc.QRect(60, 31, 251, 20))
    main_window.ui.labelOutputFolder.setStyleSheet('color: #777')

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

    # Change the splitter drag handle
    drag_handle = '''
                    QSplitter::handle { image: url(:/Arrows/images/vertical-grip.png); }
                  '''

    main_window.ui.splitter.setStyleSheet(drag_handle)

    # Create a "stop" button
    sizePolicy = qtw.QSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main_window.ui.buttonGo.sizePolicy().hasHeightForWidth())

    main_window.ui.buttonStop = CustomPushButton(main_window.ui.centralwidget)
    main_window.ui.buttonStop.setText(qtc.QCoreApplication.translate('MainWindow', u'Stop', None)) # type: ignore
    main_window.ui.buttonStop.setObjectName(u'buttonStop')
    main_window.ui.buttonStop.setGeometry(qtc.QRect(801, 530, 140, 45))
    main_window.ui.buttonStop.setSizePolicy(sizePolicy)
    main_window.ui.buttonStop.setMinimumSize(qtc.QSize(130, 41))

    main_window.ui.horizontalLayoutOutputGo.addWidget(main_window.ui.buttonStop)

    main_window.ui.buttonStop.hide()

    # Fix the fonts
    set_fonts(main_window)

    return main_window