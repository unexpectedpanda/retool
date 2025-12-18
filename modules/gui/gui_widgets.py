import sys
import threading
from typing import Any

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from modules.gui.gui_utils import set_fonts


class CustomComboBox(qtw.QComboBox):
    """
    A subclassed combo box widget that ignores mouse scrolling, and passes the
    event to the widget's parent instead.
    """

    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)
        self.setFocusPolicy(qtc.Qt.StrongFocus)  # type: ignore

    def wheelEvent(self, *args: Any, **kwargs: Any) -> Any:
        return self.parentWidget().wheelEvent(*args, **kwargs)  # type: ignore


class CustomLineEdit(qtw.QLineEdit):
    """
    A subclassed line edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)

        self.setStyleSheet(
            '''
                QLineEdit{
                    border: 1px solid #888;
                    border-collapse: collapse;
                }
                '''
        )

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())


class CustomList(qtw.QListWidget):
    """
    A subclassed list widget that doesn't allow an item to be dragged and dropped
    within itself, and also emits keyboard and drop signals.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(
        self, parent: Any = None, is_drag_drop: bool = True, self_drag: bool = False
    ) -> None:
        super().__init__(parent)

        self.setTabKeyNavigation(True)
        self.setSelectionMode(qtw.QAbstractItemView.ExtendedSelection)  # type: ignore

    def dragEnterEvent(self, event: qtg.QDragEnterEvent) -> None:
        super().dragEnterEvent(event)
        event.accept()

    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)
        item = event.source()

        if item:
            if item.isAncestorOf(self):  # type: ignore
                event.ignore()
            else:
                event.accept()

    # Handle drag and drop events
    dropped = qtc.Signal(qtg.QDropEvent)

    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

        item = event.source()

        if item:
            if item.isAncestorOf(self):  # type: ignore
                event.ignore()
            else:
                event.accept()

        if event.isAccepted():
            # Make sure all the list items have been removed from the source before sending a signal
            def check_remove() -> None:
                while True:
                    try:
                        event.source()
                    except Exception:
                        self.dropped.emit(event)
                        break

            t = threading.Thread(target=check_remove)
            t.start()

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())


class CustomListSelfDrag(CustomList):
    """
    A sub-subclassed list widget that does allow an item to be dragged and dropped
    within itself.
    """

    def __init__(self, parent: Any = None) -> None:
        super(CustomList, self).__init__(parent)

    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)
        item = event.source()

        if item:
            event.accept()
        else:
            event.ignore()

    # Handle drag and drop events
    dropped = qtc.Signal(qtg.QDropEvent)

    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

        item = event.source()

        if item:
            event.accept()
        else:
            event.ignore()

        if event.isAccepted():
            # Make sure all the list items have been removed from the source before sending a signal
            def check_remove() -> None:
                while True:
                    try:
                        event.source()
                    except Exception:
                        self.dropped.emit(event)
                        break

            t = threading.Thread(target=check_remove)
            t.start()


class CustomListDropFiles(CustomList):
    """
    A sub-subclassed list widget that allows a file to be dropped into it from a file
    explorer.
    """

    def __init__(self, parent: Any = None) -> None:
        super(CustomList, self).__init__(parent)

    def dragMoveEvent(self, event: qtg.QDragMoveEvent) -> None:
        super().dragMoveEvent(event)

        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # Handle drag and drop events
    dropped = qtc.Signal(qtg.QDropEvent)

    def dropEvent(self, event: qtg.QDropEvent) -> None:
        super().dropEvent(event)

        self.dropped_files = set()

        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

        if event.isAccepted():
            dropped_files: set[str] = set()

            for url in event.mimeData().urls():
                if url.toLocalFile().lower().endswith('.dat'):
                    dropped_files.add(url.toLocalFile())

            if dropped_files:
                self.dropped_files = dropped_files
                self.dropped.emit(event)


class CustomPushButton(qtw.QPushButton):
    """
    Animates a button's background color.

    Modified from https://stackoverflow.com/questions/60443811/button-hover-transition-duration#answer-60446633

    Args:
        parent (Any): The parent widget. Defaults to `None`.
    """

    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)
        self._animation = qtc.QVariantAnimation()
        self._animation.setStartValue(qtg.QColor("#c3f1d6"))
        self._animation.setEndValue(qtg.QColor("lightgrey"))
        self._animation.setDuration(300)
        self._animation.valueChanged.connect(self._on_value_changed)
        self._update_stylesheet(qtg.QColor("lightgrey"), qtg.QColor("black"))

    def _on_value_changed(self, color: Any) -> None:
        foreground = (
            qtg.QColor("black")
            if self._animation.direction() == qtc.QAbstractAnimation.Forward  # type: ignore
            else qtg.QColor("black")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background: Any, foreground: Any) -> None:
        self.setStyleSheet(
            f'''
                QPushButton{{
                    background-color: {background.name()};
                    color: {foreground.name()};
                    text-align: center;
                    font-size: 13px;
                    margin: 4px 2px;
                    border: 1px solid #999;
                }}
                QPushButton:disabled {{
                    background-color: #ccc;
                    color: #777;
                    border: 1px solid #bfbfbf;
                }}
                '''
        )

    def enterEvent(self, event: qtg.QEnterEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Backward)  # type: ignore
        self._animation.start()
        super().enterEvent(event)

    def focusInEvent(self, event: qtg.QFocusEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Backward)  # type: ignore
        self._animation.start()
        super().focusInEvent(event)

    def leaveEvent(self, event: qtc.QEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Forward)  # type: ignore
        self._animation.start()
        super().leaveEvent(event)

    def focusOutEvent(self, event: qtg.QFocusEvent) -> None:
        self._animation.setDirection(qtc.QAbstractAnimation.Forward)  # type: ignore
        self._animation.start()
        super().focusOutEvent(event)


class CustomTextEdit(qtw.QTextEdit):
    """
    A subclassed text edit widget that registers keyboard events.

    You can find the key that's pressed with something like:

    def on_key(key) -> None:
        print(key)

    And then calling:

    widget.keyPressed.connect(on_key)
    """

    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)

    # Handle keyboard events by creating a custom signal and emitting it from
    # an event handler
    keyPressed = qtc.Signal(int)

    def keyPressEvent(self, event: qtg.QKeyEvent) -> None:
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())


class ElisionLabel(qtw.QLabel):
    """
    Elides a label.

    Courtesy of
    https://stackoverflow.com/questions/11446478/pyside-pyqt-truncate-text-in-qlabel-based-on-minimumsize#answer-67628976

    Args:
        text (str): The label text.

        parent (Any): The QWidget main_window.

        f (Any): Qt.WindowFlags(), as defined at
            https://doc-snapshots.qt.io/qtforpython-6.40/PySide6/QtCore/Qt.html#qtc.qtc.Qt.WindowType
    """

    elision_changed = qtc.Signal(bool)

    def __init__(self, text: str = '', mode: Any = qtc.Qt.ElideMiddle, **kwargs: Any) -> None:  # type: ignore
        super().__init__(**kwargs)

        self._mode = qtc.Qt.ElideLeft  # type: ignore
        self.is_elided = False
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Preferred)  # type: ignore
        self.setText(text)

    def setText(self, text: Any) -> None:
        self._contents = text

        # This line set for testing. Its value is the return value of
        # QFontMetrics.elidedText, set in paintEvent. The variable must be initialized for
        # testing.  The value should always be the same as contents when not elided.
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
                self._elided_line = font_metrics.elidedText(
                    self._contents, self._mode, self.width()
                )
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
    """
    Adjusts properties of the widgets not covered by the promoted subclasses.

    Args:
        main_window (Any): The MainWindow widget.

    Returns:
        Any: MainWindow with the replaced widgets.
    """
    # DAT files list box
    main_window.ui.listWidgetOpenFiles.setDefaultDropAction(qtc.Qt.IgnoreAction)  # type: ignore

    # Fix checkboxes, which have a weird hover effect on Windows 4k monitors on hover if
    # you don't set a size that's divisible by 4. Also add a custom SVGs to fix check
    # mark scaling.
    if not sys.platform == 'darwin':
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

        checkboxes = main_window.ui.centralwidget.findChildren(
            qtw.QCheckBox, qtc.QRegularExpression('(checkBox.*)')
        )

        for checkbox in checkboxes:
            checkbox.setStyleSheet(checkbox_style)

    # Fix markers on dropdown boxes
    dropdown_style = '''
                    QComboBox::drop-down {
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        width: 16px;
                        border-top-right-radius: 3px; /* same radius as the QComboBox */
                        border-bottom-right-radius: 3px;
                    }
                    QComboBox::down-arrow {image: url(:/dropdowns/images/dropdown-arrow-down.svg);}
                    QComboBox::down-arrow:on {image: url(:/dropdowns/images/dropdown-arrow-up.svg);}
                    '''

    dropdowns = main_window.ui.centralwidget.findChildren(
        qtw.QComboBox, qtc.QRegularExpression('(comboBox)')
    )

    for dropdown in dropdowns:
        dropdown.setStyleSheet(dropdown_style)

    # Fix the scrollArea background color, which for some reason is altered by setting
    # the font previously
    scroll_area_style = '''
                        QScrollArea { background: transparent; }
                        QScrollArea > QWidget > QWidget { background: transparent; }
                        QScrollArea > QWidget > QScrollBar { background-color: none; }
                        '''

    scroll_widgets = main_window.findChildren(qtw.QScrollArea)

    for scroll_widget in scroll_widgets:
        scroll_widget.setStyleSheet(scroll_area_style)

    # Change the splitter drag handle
    drag_handle = '''
                    QSplitter::handle { image: url(:/arrows/images/vertical-grip.png); }
                  '''

    main_window.ui.splitter.setStyleSheet(drag_handle)

    # Adjust language and video moving button Y positions on macOS
    if sys.platform == 'darwin':
        main_window.ui.verticalSpacerGlobalLanguageLeftRightBottomBuffer.changeSize(20, 59)
        main_window.ui.verticalSpacerGlobalLanguageUpDownBottomBuffer.changeSize(20, 59)
        main_window.ui.verticalSpacerGlobalVideoUpDownBottomBuffer.changeSize(20, 59)
        main_window.ui.verticalSpacerSystemLanguageLeftRightBottomBuffer.changeSize(20, 59)
        main_window.ui.verticalSpacerSystemLanguageUpDownBottomBuffer.changeSize(20, 59)
        main_window.ui.verticalSpacerSystemVideoUpDownBottomBuffer.changeSize(20, 59)

    # Set macOS tabs to ElideRight so all tabs are visible in a constrained window
    if sys.platform == 'darwin':
        main_window.ui.tabWidgetGlobalSettings.setElideMode(qtc.Qt.ElideRight)
        main_window.ui.tabWidgetSystemSettings.setElideMode(qtc.Qt.ElideRight)

    # Create a "stop" button
    sizePolicy = qtw.QSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Fixed)  # type: ignore
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(main_window.ui.buttonGo.sizePolicy().hasHeightForWidth())

    main_window.ui.buttonStop = CustomPushButton(main_window.ui.centralwidget)
    main_window.ui.buttonStop.setText(qtc.QCoreApplication.translate('MainWindow', 'Stop', None))
    main_window.ui.buttonStop.setObjectName('buttonStop')
    main_window.ui.buttonStop.setGeometry(qtc.QRect(801, 530, 140, 45))
    main_window.ui.buttonStop.setSizePolicy(sizePolicy)
    main_window.ui.buttonStop.setMinimumSize(qtc.QSize(130, 41))

    main_window.ui.horizontalLayoutOutputGo.addWidget(main_window.ui.buttonStop)

    main_window.ui.buttonStop.hide()

    # Fix the fonts
    set_fonts(main_window)

    return main_window
