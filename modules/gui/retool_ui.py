# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from modules.gui.gui_widgets import (CustomComboBox, CustomLineEdit, CustomList, CustomListDropFiles,
    CustomListSelfDrag, CustomPushButton, CustomTextEdit, ElisionLabel)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(957, 650))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/retoolIcon/images/retool.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setIconSize(QSize(256, 256))
        MainWindow.setDocumentMode(False)
        self.actionGitHub = QAction(MainWindow)
        self.actionGitHub.setObjectName(u"actionGitHub")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionCloneListUpdates = QAction(MainWindow)
        self.actionCloneListUpdates.setObjectName(u"actionCloneListUpdates")
        self.actionCloneListUpdates.setVisible(True)
        self.actionCloneListUpdates.setIconVisibleInMenu(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setIconVisibleInMenu(False)
        self.actionCloneListNameTool = QAction(MainWindow)
        self.actionCloneListNameTool.setObjectName(u"actionCloneListNameTool")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMouseTracking(False)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 481))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(9)
        self.frameAddFiles = QFrame(self.frame)
        self.frameAddFiles.setObjectName(u"frameAddFiles")
        self.frameAddFiles.setMinimumSize(QSize(54, 0))
        self.frameAddFiles.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAddFiles.setFrameShadow(QFrame.Shadow.Plain)
        self.buttonAddDats = QPushButton(self.frameAddFiles)
        self.buttonAddDats.setObjectName(u"buttonAddDats")
        self.buttonAddDats.setGeometry(QRect(2, 0, 44, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.buttonAddDats.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/retoolFiles/images/icons8-add-list-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddDats.setIcon(icon1)
        self.buttonAddDats.setIconSize(QSize(32, 32))
        self.buttonAddFolder = QPushButton(self.frameAddFiles)
        self.buttonAddFolder.setObjectName(u"buttonAddFolder")
        self.buttonAddFolder.setGeometry(QRect(2, 50, 44, 40))
        self.buttonAddFolder.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/retoolFiles/images/icons8-add-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddFolder.setIcon(icon2)
        self.buttonAddFolder.setIconSize(QSize(32, 32))
        self.buttonAddFolderRecursive = QPushButton(self.frameAddFiles)
        self.buttonAddFolderRecursive.setObjectName(u"buttonAddFolderRecursive")
        self.buttonAddFolderRecursive.setGeometry(QRect(2, 100, 44, 40))
        self.buttonAddFolderRecursive.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/retoolFiles/images/icons8-recursive-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddFolderRecursive.setIcon(icon3)
        self.buttonAddFolderRecursive.setIconSize(QSize(32, 32))
        self.buttonDeleteDats = QPushButton(self.frameAddFiles)
        self.buttonDeleteDats.setObjectName(u"buttonDeleteDats")
        self.buttonDeleteDats.setGeometry(QRect(2, 209, 44, 40))
        self.buttonDeleteDats.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/retoolFiles/images/icons8-delete-file-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonDeleteDats.setIcon(icon4)
        self.buttonDeleteDats.setIconSize(QSize(32, 32))
        self.buttonClearDats = QPushButton(self.frameAddFiles)
        self.buttonClearDats.setObjectName(u"buttonClearDats")
        self.buttonClearDats.setGeometry(QRect(2, 259, 44, 40))
        self.buttonClearDats.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/retoolFiles/images/icons8-multiply-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonClearDats.setIcon(icon5)
        self.buttonClearDats.setIconSize(QSize(32, 32))
        self.buttonQuickImport = QPushButton(self.frameAddFiles)
        self.buttonQuickImport.setObjectName(u"buttonQuickImport")
        self.buttonQuickImport.setGeometry(QRect(2, 150, 44, 40))
        self.buttonQuickImport.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/retoolFiles/images/icons8-add-quick-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonQuickImport.setIcon(icon6)
        self.buttonQuickImport.setIconSize(QSize(32, 32))
        self.lineAddRemoveSeparator = QFrame(self.frameAddFiles)
        self.lineAddRemoveSeparator.setObjectName(u"lineAddRemoveSeparator")
        self.lineAddRemoveSeparator.setGeometry(QRect(8, 190, 31, 20))
        self.lineAddRemoveSeparator.setFrameShape(QFrame.Shape.HLine)
        self.lineAddRemoveSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frameAddFiles, 2, 0, 1, 1)

        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(80)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setMouseTracking(False)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.gridLayoutLeftFiles = QWidget(self.splitter)
        self.gridLayoutLeftFiles.setObjectName(u"gridLayoutLeftFiles")
        self.gridLayoutLeftFiles.setMouseTracking(False)
        self.gridLayoutLeft = QGridLayout(self.gridLayoutLeftFiles)
        self.gridLayoutLeft.setObjectName(u"gridLayoutLeft")
        self.gridLayoutLeft.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayoutLeft.setContentsMargins(6, 0, 3, 9)
        self.listWidgetOpenFiles = CustomListDropFiles(self.gridLayoutLeftFiles)
        QListWidgetItem(self.listWidgetOpenFiles)
        self.listWidgetOpenFiles.setObjectName(u"listWidgetOpenFiles")
        self.listWidgetOpenFiles.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidgetOpenFiles.sizePolicy().hasHeightForWidth())
        self.listWidgetOpenFiles.setSizePolicy(sizePolicy2)
        self.listWidgetOpenFiles.setMinimumSize(QSize(187, 392))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        self.listWidgetOpenFiles.setFont(font2)
        self.listWidgetOpenFiles.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.listWidgetOpenFiles.setFrameShape(QFrame.Shape.Box)
        self.listWidgetOpenFiles.setProperty(u"showDropIndicator", False)
        self.listWidgetOpenFiles.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.listWidgetOpenFiles.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetOpenFiles.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetOpenFiles.setSortingEnabled(True)

        self.gridLayoutLeft.addWidget(self.listWidgetOpenFiles, 1, 2, 1, 1)

        self.labelSelectInput = QLabel(self.gridLayoutLeftFiles)
        self.labelSelectInput.setObjectName(u"labelSelectInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelSelectInput.sizePolicy().hasHeightForWidth())
        self.labelSelectInput.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.labelSelectInput.setFont(font3)

        self.gridLayoutLeft.addWidget(self.labelSelectInput, 0, 2, 1, 1)

        self.splitter.addWidget(self.gridLayoutLeftFiles)
        self.gridLayoutRightSettings = QWidget(self.splitter)
        self.gridLayoutRightSettings.setObjectName(u"gridLayoutRightSettings")
        self.gridLayoutRightSettings.setMinimumSize(QSize(650, 0))
        self.gridLayoutRightSettings.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.gridLayoutRightSettings.setMouseTracking(False)
        self.gridLayoutRight = QGridLayout(self.gridLayoutRightSettings)
        self.gridLayoutRight.setObjectName(u"gridLayoutRight")
        self.gridLayoutRight.setContentsMargins(3, 0, -1, -1)
        self.tabWidgetSettings = QTabWidget(self.gridLayoutRightSettings)
        self.tabWidgetSettings.setObjectName(u"tabWidgetSettings")
        sizePolicy.setHeightForWidth(self.tabWidgetSettings.sizePolicy().hasHeightForWidth())
        self.tabWidgetSettings.setSizePolicy(sizePolicy)
        self.tabWidgetSettings.setMinimumSize(QSize(611, 481))
        self.tabWidgetSettings.setFont(font)
        self.tabGlobalSettings = QWidget()
        self.tabGlobalSettings.setObjectName(u"tabGlobalSettings")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(100)
        sizePolicy4.setHeightForWidth(self.tabGlobalSettings.sizePolicy().hasHeightForWidth())
        self.tabGlobalSettings.setSizePolicy(sizePolicy4)
        self.tabGlobalSettings.setMinimumSize(QSize(605, 452))
        self.verticalLayout_7 = QVBoxLayout(self.tabGlobalSettings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.labelGlobalSettings = QLabel(self.tabGlobalSettings)
        self.labelGlobalSettings.setObjectName(u"labelGlobalSettings")
        self.labelGlobalSettings.setFont(font)
        self.labelGlobalSettings.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.labelGlobalSettings)

        self.tabWidgetGlobalSettings = QTabWidget(self.tabGlobalSettings)
        self.tabWidgetGlobalSettings.setObjectName(u"tabWidgetGlobalSettings")
        self.tabWidgetGlobalSettings.setFont(font)
        self.tabGlobalPaths = QWidget()
        self.tabGlobalPaths.setObjectName(u"tabGlobalPaths")
        self.gridLayout_7 = QGridLayout(self.tabGlobalPaths)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacerGlobalPaths = QSpacerItem(20, 177, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacerGlobalPaths, 8, 3, 1, 1)

        self.horizontalSpacerGlobalPaths_2 = QSpacerItem(4, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacerGlobalPaths_2, 6, 2, 1, 1)

        self.labelGlobalSelectOutput = QLabel(self.tabGlobalPaths)
        self.labelGlobalSelectOutput.setObjectName(u"labelGlobalSelectOutput")
        self.labelGlobalSelectOutput.setMinimumSize(QSize(400, 0))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(8)
        font4.setBold(False)
        self.labelGlobalSelectOutput.setFont(font4)

        self.gridLayout_7.addWidget(self.labelGlobalSelectOutput, 2, 3, 1, 1)

        self.frameGlobalReplace = QFrame(self.tabGlobalPaths)
        self.frameGlobalReplace.setObjectName(u"frameGlobalReplace")
        self.frameGlobalReplace.setMinimumSize(QSize(0, 0))
        self.frameGlobalReplace.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalReplace.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_35 = QVBoxLayout(self.frameGlobalReplace)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 6, 0, 10)
        self.checkBoxGlobalReplaceInputDats = QCheckBox(self.frameGlobalReplace)
        self.checkBoxGlobalReplaceInputDats.setObjectName(u"checkBoxGlobalReplaceInputDats")
        self.checkBoxGlobalReplaceInputDats.setFont(font2)
        self.checkBoxGlobalReplaceInputDats.setIconSize(QSize(16, 16))
        self.checkBoxGlobalReplaceInputDats.setChecked(False)

        self.verticalLayout_35.addWidget(self.checkBoxGlobalReplaceInputDats)


        self.gridLayout_7.addWidget(self.frameGlobalReplace, 4, 0, 1, 4)

        self.lineGlobalCustomFilesAndFolders = QFrame(self.tabGlobalPaths)
        self.lineGlobalCustomFilesAndFolders.setObjectName(u"lineGlobalCustomFilesAndFolders")
        palette = QPalette()
        brush = QBrush(QColor(85, 85, 85, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalCustomFilesAndFolders.setPalette(palette)
        self.lineGlobalCustomFilesAndFolders.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalCustomFilesAndFolders.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_7.addWidget(self.lineGlobalCustomFilesAndFolders, 1, 0, 1, 5)

        self.labelGlobalOutputFolder = ElisionLabel(self.tabGlobalPaths)
        self.labelGlobalOutputFolder.setObjectName(u"labelGlobalOutputFolder")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelGlobalOutputFolder.sizePolicy().hasHeightForWidth())
        self.labelGlobalOutputFolder.setSizePolicy(sizePolicy5)
        self.labelGlobalOutputFolder.setMinimumSize(QSize(400, 0))
        palette1 = QPalette()
        brush2 = QBrush(QColor(119, 119, 119, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelGlobalOutputFolder.setPalette(palette1)
        self.labelGlobalOutputFolder.setFont(font2)

        self.gridLayout_7.addWidget(self.labelGlobalOutputFolder, 3, 3, 1, 1)

        self.frameGlobalPathsHeader = QFrame(self.tabGlobalPaths)
        self.frameGlobalPathsHeader.setObjectName(u"frameGlobalPathsHeader")
        sizePolicy3.setHeightForWidth(self.frameGlobalPathsHeader.sizePolicy().hasHeightForWidth())
        self.frameGlobalPathsHeader.setSizePolicy(sizePolicy3)
        self.frameGlobalPathsHeader.setMinimumSize(QSize(0, 20))
        self.frameGlobalPathsHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalPathsHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalPathsHeader.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frameGlobalPathsHeader)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalCustomFilesAndFolders = QLabel(self.frameGlobalPathsHeader)
        self.labelGlobalCustomFilesAndFolders.setObjectName(u"labelGlobalCustomFilesAndFolders")
        self.labelGlobalCustomFilesAndFolders.setFont(font3)
        self.labelGlobalCustomFilesAndFolders.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_9.addWidget(self.labelGlobalCustomFilesAndFolders)


        self.gridLayout_7.addWidget(self.frameGlobalPathsHeader, 0, 0, 1, 5)

        self.buttonGlobalChooseOutput = QPushButton(self.tabGlobalPaths)
        self.buttonGlobalChooseOutput.setObjectName(u"buttonGlobalChooseOutput")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonGlobalChooseOutput.sizePolicy().hasHeightForWidth())
        self.buttonGlobalChooseOutput.setSizePolicy(sizePolicy6)
        self.buttonGlobalChooseOutput.setFont(font1)
        self.buttonGlobalChooseOutput.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/retoolFiles/images/icons8-live-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalChooseOutput.setIcon(icon7)
        self.buttonGlobalChooseOutput.setIconSize(QSize(32, 32))
        self.buttonGlobalChooseOutput.setFlat(False)

        self.gridLayout_7.addWidget(self.buttonGlobalChooseOutput, 2, 0, 2, 2)

        self.horizontalSpacerGlobalPaths = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacerGlobalPaths, 7, 4, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalPaths, "")
        self.tabGlobalRegions = QWidget()
        self.tabGlobalRegions.setObjectName(u"tabGlobalRegions")
        self.verticalLayout_6 = QVBoxLayout(self.tabGlobalRegions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridGlobalRegions = QWidget(self.tabGlobalRegions)
        self.gridGlobalRegions.setObjectName(u"gridGlobalRegions")
        self.gridLayoutGlobalRegions = QGridLayout(self.gridGlobalRegions)
        self.gridLayoutGlobalRegions.setObjectName(u"gridLayoutGlobalRegions")
        self.gridLayoutGlobalRegions.setContentsMargins(1, 0, 0, 0)
        self.listWidgetGlobalSelectedRegions = CustomListSelfDrag(self.gridGlobalRegions)
        self.listWidgetGlobalSelectedRegions.setObjectName(u"listWidgetGlobalSelectedRegions")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedRegions.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalSelectedRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalSelectedRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalSelectedRegions.setTabKeyNavigation(True)
        self.listWidgetGlobalSelectedRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalSelectedRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalSelectedRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalSelectedRegions.setAlternatingRowColors(False)
        self.listWidgetGlobalSelectedRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalSelectedRegions.setProperty(u"self_drag", True)
        self.listWidgetGlobalSelectedRegions.setProperty(u"is_drag_drop", True)

        self.gridLayoutGlobalRegions.addWidget(self.listWidgetGlobalSelectedRegions, 3, 2, 1, 1)

        self.verticalSpacerGlobalRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalRegions.addItem(self.verticalSpacerGlobalRegionsEnglishButton, 4, 0, 1, 1)

        self.lineGlobalRegionSeparator = QFrame(self.gridGlobalRegions)
        self.lineGlobalRegionSeparator.setObjectName(u"lineGlobalRegionSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalRegionSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalRegionSeparator.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalRegionSeparator.setPalette(palette2)
        self.lineGlobalRegionSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalRegionSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalRegions.addWidget(self.lineGlobalRegionSeparator, 1, 0, 1, 5)

        self.labelGlobalFilterByRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalFilterByRegions.setObjectName(u"labelGlobalFilterByRegions")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.labelGlobalFilterByRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByRegions.setSizePolicy(sizePolicy8)
        self.labelGlobalFilterByRegions.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByRegions.setFont(font3)
        self.labelGlobalFilterByRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalFilterByRegions, 0, 0, 1, 5)

        self.labelGlobalSelectedRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalSelectedRegions.setObjectName(u"labelGlobalSelectedRegions")
        sizePolicy8.setHeightForWidth(self.labelGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedRegions.setSizePolicy(sizePolicy8)
        self.labelGlobalSelectedRegions.setFont(font)
        self.labelGlobalSelectedRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalSelectedRegions, 2, 2, 1, 1)

        self.labelGlobalAvailableRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalAvailableRegions.setObjectName(u"labelGlobalAvailableRegions")
        sizePolicy8.setHeightForWidth(self.labelGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableRegions.setSizePolicy(sizePolicy8)
        self.labelGlobalAvailableRegions.setFont(font)
        self.labelGlobalAvailableRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalAvailableRegions, 2, 0, 1, 1)

        self.listWidgetGlobalAvailableRegions = CustomList(self.gridGlobalRegions)
        self.listWidgetGlobalAvailableRegions.setObjectName(u"listWidgetGlobalAvailableRegions")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableRegions.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalAvailableRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalAvailableRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalAvailableRegions.setTabKeyNavigation(True)
        self.listWidgetGlobalAvailableRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalAvailableRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalAvailableRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalAvailableRegions.setAlternatingRowColors(False)
        self.listWidgetGlobalAvailableRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalAvailableRegions.setSortingEnabled(True)
        self.listWidgetGlobalAvailableRegions.setProperty(u"self_drag", False)
        self.listWidgetGlobalAvailableRegions.setProperty(u"is_drag_drop", True)

        self.gridLayoutGlobalRegions.addWidget(self.listWidgetGlobalAvailableRegions, 3, 0, 1, 1)

        self.buttonGlobalDefaultRegionOrder = QPushButton(self.gridGlobalRegions)
        self.buttonGlobalDefaultRegionOrder.setObjectName(u"buttonGlobalDefaultRegionOrder")
        sizePolicy6.setHeightForWidth(self.buttonGlobalDefaultRegionOrder.sizePolicy().hasHeightForWidth())
        self.buttonGlobalDefaultRegionOrder.setSizePolicy(sizePolicy6)
        self.buttonGlobalDefaultRegionOrder.setMinimumSize(QSize(286, 41))

        self.gridLayoutGlobalRegions.addWidget(self.buttonGlobalDefaultRegionOrder, 5, 0, 1, 2)

        self.horizontalSpacerGlobalRegions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalRegions.addItem(self.horizontalSpacerGlobalRegions, 3, 4, 1, 1)

        self.frameGlobalRegionLeftRight = QFrame(self.gridGlobalRegions)
        self.frameGlobalRegionLeftRight.setObjectName(u"frameGlobalRegionLeftRight")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frameGlobalRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionLeftRight.setSizePolicy(sizePolicy9)
        self.frameGlobalRegionLeftRight.setMinimumSize(QSize(60, 0))
        self.frameGlobalRegionLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalRegionLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.frameGlobalRegionLeftRight)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacerGlobalRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacerGlobalRegionLeftRightTop)

        self.buttonGlobalRegionAllRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllRight.setObjectName(u"buttonGlobalRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllRight.setMinimumSize(QSize(40, 41))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.buttonGlobalRegionAllRight.setFont(font5)
        icon8 = QIcon()
        icon8.addFile(u":/arrows/images/icons8-end-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionAllRight.setIcon(icon8)
        self.buttonGlobalRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionAllRight)

        self.buttonGlobalRegionRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionRight.setObjectName(u"buttonGlobalRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionRight.setFont(font5)
        icon9 = QIcon()
        icon9.addFile(u":/arrows/images/icons8-sort-right-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionRight.setIcon(icon9)
        self.buttonGlobalRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionRight)

        self.buttonGlobalRegionLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionLeft.setObjectName(u"buttonGlobalRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionLeft.setFont(font5)
        icon10 = QIcon()
        icon10.addFile(u":/arrows/images/icons8-sort-left-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionLeft.setIcon(icon10)

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionLeft)

        self.buttonGlobalRegionAllLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllLeft.setObjectName(u"buttonGlobalRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionAllLeft.setFont(font5)
        icon11 = QIcon()
        icon11.addFile(u":/arrows/images/icons8-skip-to-start-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionAllLeft.setIcon(icon11)
        self.buttonGlobalRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionAllLeft)

        self.verticalSpacerGlobalRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacerGlobalRegionLeftRightBottom)


        self.gridLayoutGlobalRegions.addWidget(self.frameGlobalRegionLeftRight, 3, 1, 1, 1)

        self.frameGlobalRegionUpDown = QFrame(self.gridGlobalRegions)
        self.frameGlobalRegionUpDown.setObjectName(u"frameGlobalRegionUpDown")
        sizePolicy9.setHeightForWidth(self.frameGlobalRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionUpDown.setSizePolicy(sizePolicy9)
        self.frameGlobalRegionUpDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalRegionUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalRegionUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frameGlobalRegionUpDown)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacerGlobalRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacerGlobalRegionUpDownTop)

        self.buttonGlobalRegionUp = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionUp.setObjectName(u"buttonGlobalRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionUp.setFont(font5)
        icon12 = QIcon()
        icon12.addFile(u":/arrows/images/icons8-sort-up-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionUp.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.buttonGlobalRegionUp)

        self.buttonGlobalRegionDown = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionDown.setObjectName(u"buttonGlobalRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionDown.setFont(font5)
        icon13 = QIcon()
        icon13.addFile(u":/arrows/images/icons8-sort-down-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionDown.setIcon(icon13)

        self.verticalLayout_13.addWidget(self.buttonGlobalRegionDown)

        self.verticalSpacerGlobalRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacerGlobalRegionUpDownBottom)


        self.gridLayoutGlobalRegions.addWidget(self.frameGlobalRegionUpDown, 3, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.gridGlobalRegions)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalRegions, "")
        self.tabGlobalLanguages = QWidget()
        self.tabGlobalLanguages.setObjectName(u"tabGlobalLanguages")
        self.verticalLayoutTabGlobalLanguages = QVBoxLayout(self.tabGlobalLanguages)
        self.verticalLayoutTabGlobalLanguages.setObjectName(u"verticalLayoutTabGlobalLanguages")
        self.gridGlobalLanguages = QWidget(self.tabGlobalLanguages)
        self.gridGlobalLanguages.setObjectName(u"gridGlobalLanguages")
        self.gridLayoutGlobalLanguages = QGridLayout(self.gridGlobalLanguages)
        self.gridLayoutGlobalLanguages.setObjectName(u"gridLayoutGlobalLanguages")
        self.gridLayoutGlobalLanguages.setContentsMargins(1, 0, 0, 0)
        self.labelGlobalSelectedLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalSelectedLanguages.setObjectName(u"labelGlobalSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalSelectedLanguages.setFont(font)
        self.labelGlobalSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages.addWidget(self.labelGlobalSelectedLanguages, 2, 2, 1, 1)

        self.frameGlobalLanguageUpDown = QFrame(self.gridGlobalLanguages)
        self.frameGlobalLanguageUpDown.setObjectName(u"frameGlobalLanguageUpDown")
        sizePolicy9.setHeightForWidth(self.frameGlobalLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageUpDown.setSizePolicy(sizePolicy9)
        self.frameGlobalLanguageUpDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalLanguageUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLanguageUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frameGlobalLanguageUpDown)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacerGlobalLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownTop)

        self.buttonGlobalLanguageUp = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageUp.setObjectName(u"buttonGlobalLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageUp.setFont(font5)
        self.buttonGlobalLanguageUp.setIcon(icon12)

        self.verticalLayout_24.addWidget(self.buttonGlobalLanguageUp)

        self.buttonGlobalLanguageDown = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageDown.setObjectName(u"buttonGlobalLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageDown.setFont(font5)
        self.buttonGlobalLanguageDown.setIcon(icon13)

        self.verticalLayout_24.addWidget(self.buttonGlobalLanguageDown)

        self.verticalSpacerGlobalLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownBottom)

        self.verticalSpacerGlobalLanguageUpDownBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownBuffer)


        self.gridLayoutGlobalLanguages.addWidget(self.frameGlobalLanguageUpDown, 3, 3, 1, 1)

        self.listWidgetGlobalAvailableLanguages = CustomList(self.gridGlobalLanguages)
        self.listWidgetGlobalAvailableLanguages.setObjectName(u"listWidgetGlobalAvailableLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalAvailableLanguages.setSortingEnabled(True)

        self.gridLayoutGlobalLanguages.addWidget(self.listWidgetGlobalAvailableLanguages, 3, 0, 1, 1)

        self.lineGlobalLanguageSeparator = QFrame(self.gridGlobalLanguages)
        self.lineGlobalLanguageSeparator.setObjectName(u"lineGlobalLanguageSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalLanguageSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalLanguageSeparator.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalLanguageSeparator.setPalette(palette3)
        self.lineGlobalLanguageSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalLanguageSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalLanguages.addWidget(self.lineGlobalLanguageSeparator, 1, 0, 1, 5)

        self.listWidgetGlobalSelectedLanguages = CustomListSelfDrag(self.gridGlobalLanguages)
        self.listWidgetGlobalSelectedLanguages.setObjectName(u"listWidgetGlobalSelectedLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutGlobalLanguages.addWidget(self.listWidgetGlobalSelectedLanguages, 3, 2, 1, 1)

        self.frameGlobalLanguageLeftRight = QFrame(self.gridGlobalLanguages)
        self.frameGlobalLanguageLeftRight.setObjectName(u"frameGlobalLanguageLeftRight")
        sizePolicy9.setHeightForWidth(self.frameGlobalLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageLeftRight.setSizePolicy(sizePolicy9)
        self.frameGlobalLanguageLeftRight.setMinimumSize(QSize(60, 0))
        self.frameGlobalLanguageLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLanguageLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_25 = QVBoxLayout(self.frameGlobalLanguageLeftRight)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacerGlobalLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightTop)

        self.buttonGlobalLanguageAllRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllRight.setObjectName(u"buttonGlobalLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllRight.setFont(font5)
        self.buttonGlobalLanguageAllRight.setIcon(icon8)
        self.buttonGlobalLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageAllRight)

        self.buttonGlobalLanguageRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageRight.setObjectName(u"buttonGlobalLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageRight.setFont(font5)
        self.buttonGlobalLanguageRight.setIcon(icon9)
        self.buttonGlobalLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageRight)

        self.buttonGlobalLanguageLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageLeft.setObjectName(u"buttonGlobalLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageLeft.setFont(font5)
        self.buttonGlobalLanguageLeft.setIcon(icon10)

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageLeft)

        self.buttonGlobalLanguageAllLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllLeft.setObjectName(u"buttonGlobalLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllLeft.setFont(font5)
        self.buttonGlobalLanguageAllLeft.setIcon(icon11)
        self.buttonGlobalLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageAllLeft)

        self.verticalSpacerGlobalLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightBottom)

        self.verticalSpacerGlobalLanguageLeftRightBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightBuffer)


        self.gridLayoutGlobalLanguages.addWidget(self.frameGlobalLanguageLeftRight, 3, 1, 1, 1)

        self.horizontalSpacerGlobalLanguages = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalLanguages.addItem(self.horizontalSpacerGlobalLanguages, 3, 4, 1, 1)

        self.labelGlobalAvailableLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalAvailableLanguages.setObjectName(u"labelGlobalAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalAvailableLanguages.setFont(font)
        self.labelGlobalAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages.addWidget(self.labelGlobalAvailableLanguages, 2, 0, 1, 1)

        self.labelGlobalFilterByLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalFilterByLanguages.setObjectName(u"labelGlobalFilterByLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalFilterByLanguages.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByLanguages.setFont(font3)
        self.labelGlobalFilterByLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages.addWidget(self.labelGlobalFilterByLanguages, 0, 0, 1, 5)


        self.verticalLayoutTabGlobalLanguages.addWidget(self.gridGlobalLanguages)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalLanguages, "")
        self.tabGlobalVideo = QWidget()
        self.tabGlobalVideo.setObjectName(u"tabGlobalVideo")
        self.verticalLayout_9 = QVBoxLayout(self.tabGlobalVideo)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridGlobalVideo = QWidget(self.tabGlobalVideo)
        self.gridGlobalVideo.setObjectName(u"gridGlobalVideo")
        self.gridLayoutGlobalVideo = QGridLayout(self.gridGlobalVideo)
        self.gridLayoutGlobalVideo.setSpacing(6)
        self.gridLayoutGlobalVideo.setObjectName(u"gridLayoutGlobalVideo")
        self.gridLayoutGlobalVideo.setContentsMargins(1, 0, 0, 0)
        self.frameGlobalVideoDown = QFrame(self.gridGlobalVideo)
        self.frameGlobalVideoDown.setObjectName(u"frameGlobalVideoDown")
        sizePolicy9.setHeightForWidth(self.frameGlobalVideoDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalVideoDown.setSizePolicy(sizePolicy9)
        self.frameGlobalVideoDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalVideoDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalVideoDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_27 = QVBoxLayout(self.frameGlobalVideoDown)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacerGlobalVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownTop)

        self.buttonGlobalVideoStandardUp = QPushButton(self.frameGlobalVideoDown)
        self.buttonGlobalVideoStandardUp.setObjectName(u"buttonGlobalVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardUp.setFont(font5)
        self.buttonGlobalVideoStandardUp.setIcon(icon12)

        self.verticalLayout_27.addWidget(self.buttonGlobalVideoStandardUp)

        self.buttonGlobalVideoStandardDown = QPushButton(self.frameGlobalVideoDown)
        self.buttonGlobalVideoStandardDown.setObjectName(u"buttonGlobalVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardDown.setFont(font5)
        self.buttonGlobalVideoStandardDown.setIcon(icon13)

        self.verticalLayout_27.addWidget(self.buttonGlobalVideoStandardDown)

        self.verticalSpacerGlobalVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownBottom)

        self.verticalSpacerGlobalVideoUpDownBuffer = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownBuffer)


        self.gridLayoutGlobalVideo.addWidget(self.frameGlobalVideoDown, 4, 1, 1, 1)

        self.horizontalSpacerGlobalVideo_1 = QSpacerItem(220, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_1, 4, 2, 1, 1)

        self.listWidgetGlobalVideoStandards = CustomListSelfDrag(self.gridGlobalVideo)
        self.listWidgetGlobalVideoStandards.setObjectName(u"listWidgetGlobalVideoStandards")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalVideoStandards.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalVideoStandards.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalVideoStandards.setTabKeyNavigation(True)
        self.listWidgetGlobalVideoStandards.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalVideoStandards.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalVideoStandards.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalVideoStandards.setAlternatingRowColors(False)
        self.listWidgetGlobalVideoStandards.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutGlobalVideo.addWidget(self.listWidgetGlobalVideoStandards, 4, 0, 1, 1)

        self.horizontalSpacerGlobalVideo_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_3, 4, 4, 1, 1)

        self.labelGlobalVideoStandardsOrder = QLabel(self.gridGlobalVideo)
        self.labelGlobalVideoStandardsOrder.setObjectName(u"labelGlobalVideoStandardsOrder")
        sizePolicy8.setHeightForWidth(self.labelGlobalVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelGlobalVideoStandardsOrder.setSizePolicy(sizePolicy8)
        self.labelGlobalVideoStandardsOrder.setFont(font)
        self.labelGlobalVideoStandardsOrder.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalVideo.addWidget(self.labelGlobalVideoStandardsOrder, 2, 0, 1, 1)

        self.horizontalSpacerGlobalVideo_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_2, 4, 3, 1, 1)

        self.lineGlobalVideoStandardsSeparator = QFrame(self.gridGlobalVideo)
        self.lineGlobalVideoStandardsSeparator.setObjectName(u"lineGlobalVideoStandardsSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalVideoStandardsSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalVideoStandardsSeparator.setSizePolicy(sizePolicy3)
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalVideoStandardsSeparator.setPalette(palette4)
        self.lineGlobalVideoStandardsSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalVideoStandardsSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalVideo.addWidget(self.lineGlobalVideoStandardsSeparator, 1, 0, 1, 5)

        self.labelGlobalFilterByVideo = QLabel(self.gridGlobalVideo)
        self.labelGlobalFilterByVideo.setObjectName(u"labelGlobalFilterByVideo")
        sizePolicy8.setHeightForWidth(self.labelGlobalFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByVideo.setSizePolicy(sizePolicy8)
        self.labelGlobalFilterByVideo.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByVideo.setFont(font3)
        self.labelGlobalFilterByVideo.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalVideo.addWidget(self.labelGlobalFilterByVideo, 0, 0, 1, 5)


        self.verticalLayout_9.addWidget(self.gridGlobalVideo)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalVideo, "")
        self.tabGlobalExclusions = QWidget()
        self.tabGlobalExclusions.setObjectName(u"tabGlobalExclusions")
        self.verticalLayout_10 = QVBoxLayout(self.tabGlobalExclusions)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayoutGlobalExclusions = QGridLayout()
        self.gridLayoutGlobalExclusions.setObjectName(u"gridLayoutGlobalExclusions")
        self.gridLayoutGlobalExclusions.setContentsMargins(1, -1, -1, -1)
        self.checkBoxGlobalExcludeDemos = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeDemos.setObjectName(u"checkBoxGlobalExcludeDemos")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeDemos, 10, 0, 1, 1)

        self.horizontalSpacerGlobalExclude_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_2, 6, 1, 1, 1)

        self.checkBoxGlobalExcludeUnlicensedAll = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeUnlicensedAll.setObjectName(u"checkBoxGlobalExcludeUnlicensedAll")
        self.checkBoxGlobalExcludeUnlicensedAll.setTristate(False)

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeUnlicensedAll, 7, 2, 1, 1)

        self.checkBoxGlobalExcludeApplications = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeApplications.setObjectName(u"checkBoxGlobalExcludeApplications")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeApplications, 3, 0, 1, 1)

        self.checkBoxGlobalExcludeManuals = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeManuals.setObjectName(u"checkBoxGlobalExcludeManuals")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeManuals, 2, 2, 1, 1)

        self.checkBoxGlobalExcludeBonusDiscs = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBonusDiscs.setObjectName(u"checkBoxGlobalExcludeBonusDiscs")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBonusDiscs, 7, 0, 1, 1)

        self.frameGlobalExcludeSelectButtons = QFrame(self.tabGlobalExclusions)
        self.frameGlobalExcludeSelectButtons.setObjectName(u"frameGlobalExcludeSelectButtons")
        sizePolicy7.setHeightForWidth(self.frameGlobalExcludeSelectButtons.sizePolicy().hasHeightForWidth())
        self.frameGlobalExcludeSelectButtons.setSizePolicy(sizePolicy7)
        self.frameGlobalExcludeSelectButtons.setMinimumSize(QSize(120, 80))
        self.frameGlobalExcludeSelectButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalExcludeSelectButtons.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalExcludeSelectButtons.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frameGlobalExcludeSelectButtons)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.buttonGlobalSelectAllExclude = QPushButton(self.frameGlobalExcludeSelectButtons)
        self.buttonGlobalSelectAllExclude.setObjectName(u"buttonGlobalSelectAllExclude")
        self.buttonGlobalSelectAllExclude.setMinimumSize(QSize(0, 30))

        self.verticalLayout_19.addWidget(self.buttonGlobalSelectAllExclude)

        self.buttonGlobalDeselectAllExclude = QPushButton(self.frameGlobalExcludeSelectButtons)
        self.buttonGlobalDeselectAllExclude.setObjectName(u"buttonGlobalDeselectAllExclude")
        self.buttonGlobalDeselectAllExclude.setMinimumSize(QSize(0, 30))

        self.verticalLayout_19.addWidget(self.buttonGlobalDeselectAllExclude)

        self.verticalSpacerGlobalExclude_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacerGlobalExclude_1)


        self.gridLayoutGlobalExclusions.addWidget(self.frameGlobalExcludeSelectButtons, 2, 4, 4, 1)

        self.checkBoxGlobalExcludePromotional = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePromotional.setObjectName(u"checkBoxGlobalExcludePromotional")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludePromotional, 6, 2, 1, 1)

        self.checkBoxGlobalExcludeBadDumps = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBadDumps.setObjectName(u"checkBoxGlobalExcludeBadDumps")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBadDumps, 5, 0, 1, 1)

        self.lineGlobalExclude = QFrame(self.tabGlobalExclusions)
        self.lineGlobalExclude.setObjectName(u"lineGlobalExclude")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalExclude.setPalette(palette5)
        self.lineGlobalExclude.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalExclude.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalExclusions.addWidget(self.lineGlobalExclude, 1, 0, 1, 6)

        self.labelGlobalExclude = QLabel(self.tabGlobalExclusions)
        self.labelGlobalExclude.setObjectName(u"labelGlobalExclude")
        self.labelGlobalExclude.setMinimumSize(QSize(0, 20))
        self.labelGlobalExclude.setFont(font3)
        self.labelGlobalExclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalExclusions.addWidget(self.labelGlobalExclude, 0, 0, 1, 6)

        self.checkBoxGlobalExcludeAudio = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeAudio.setObjectName(u"checkBoxGlobalExcludeAudio")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeAudio, 4, 0, 1, 1)

        self.horizontalSpacerGlobalExclude_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_1, 2, 5, 1, 1)

        self.checkBoxGlobalExcludeCoverdiscs = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeCoverdiscs.setObjectName(u"checkBoxGlobalExcludeCoverdiscs")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeCoverdiscs, 8, 0, 1, 1)

        self.checkBoxGlobalExcludeVideo = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeVideo.setObjectName(u"checkBoxGlobalExcludeVideo")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeVideo, 12, 2, 1, 1)

        self.frameGlobalUnlicensedSubOptionsPirate = QHBoxLayout()
        self.frameGlobalUnlicensedSubOptionsPirate.setObjectName(u"frameGlobalUnlicensedSubOptionsPirate")
        self.unlicensedGlobalSubOptionsSpacerPirate = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameGlobalUnlicensedSubOptionsPirate.addItem(self.unlicensedGlobalSubOptionsSpacerPirate)

        self.checkBoxGlobalExcludePirate = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePirate.setObjectName(u"checkBoxGlobalExcludePirate")

        self.frameGlobalUnlicensedSubOptionsPirate.addWidget(self.checkBoxGlobalExcludePirate)


        self.gridLayoutGlobalExclusions.addLayout(self.frameGlobalUnlicensedSubOptionsPirate, 10, 2, 1, 1)

        self.checkBoxGlobalExcludeEducational = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeEducational.setObjectName(u"checkBoxGlobalExcludeEducational")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeEducational, 11, 0, 1, 1)

        self.checkBoxGlobalExcludeGames = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeGames.setObjectName(u"checkBoxGlobalExcludeGames")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeGames, 12, 0, 1, 1)

        self.checkBoxGlobalExcludeAddOns = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeAddOns.setObjectName(u"checkBoxGlobalExcludeAddOns")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeAddOns, 2, 0, 1, 1)

        self.checkBoxGlobalExcludeMIA = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeMIA.setObjectName(u"checkBoxGlobalExcludeMIA")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeMIA, 3, 2, 1, 1)

        self.checkBoxGlobalExcludePreproduction = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePreproduction.setObjectName(u"checkBoxGlobalExcludePreproduction")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludePreproduction, 5, 2, 1, 1)

        self.horizontalSpacerGlobalExclude_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_3, 6, 3, 1, 1)

        self.checkBoxGlobalExcludeBIOS = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBIOS.setObjectName(u"checkBoxGlobalExcludeBIOS")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBIOS, 6, 0, 1, 1)

        self.checkBoxGlobalExcludeMultimedia = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeMultimedia.setObjectName(u"checkBoxGlobalExcludeMultimedia")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeMultimedia, 4, 2, 1, 1)

        self.verticalSpacerGlobalExclude_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutGlobalExclusions.addItem(self.verticalSpacerGlobalExclude_2, 14, 0, 1, 1)

        self.frameGlobalUnlicensedSubOptionsAftermarket = QHBoxLayout()
        self.frameGlobalUnlicensedSubOptionsAftermarket.setObjectName(u"frameGlobalUnlicensedSubOptionsAftermarket")
        self.unlicensedGlobalSubOptionsSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameGlobalUnlicensedSubOptionsAftermarket.addItem(self.unlicensedGlobalSubOptionsSpacer)

        self.checkBoxGlobalExcludeAftermarket = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeAftermarket.setObjectName(u"checkBoxGlobalExcludeAftermarket")

        self.frameGlobalUnlicensedSubOptionsAftermarket.addWidget(self.checkBoxGlobalExcludeAftermarket)


        self.gridLayoutGlobalExclusions.addLayout(self.frameGlobalUnlicensedSubOptionsAftermarket, 8, 2, 1, 1)

        self.frameGlobalUnlicensedSubOptionsUnlicensed = QHBoxLayout()
        self.frameGlobalUnlicensedSubOptionsUnlicensed.setObjectName(u"frameGlobalUnlicensedSubOptionsUnlicensed")
        self.unlicensedGlobalSubOptionsSpacerUnlicensed = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameGlobalUnlicensedSubOptionsUnlicensed.addItem(self.unlicensedGlobalSubOptionsSpacerUnlicensed)

        self.checkBoxGlobalExcludeUnlicensed = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeUnlicensed.setObjectName(u"checkBoxGlobalExcludeUnlicensed")

        self.frameGlobalUnlicensedSubOptionsUnlicensed.addWidget(self.checkBoxGlobalExcludeUnlicensed)


        self.gridLayoutGlobalExclusions.addLayout(self.frameGlobalUnlicensedSubOptionsUnlicensed, 11, 2, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayoutGlobalExclusions)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalExclusions, "")
        self.tabGlobalLocalization = QWidget()
        self.tabGlobalLocalization.setObjectName(u"tabGlobalLocalization")
        self.gridLayout_5 = QGridLayout(self.tabGlobalLocalization)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridGlobalLocalization = QWidget(self.tabGlobalLocalization)
        self.gridGlobalLocalization.setObjectName(u"gridGlobalLocalization")
        self.gridLayoutGlobalLanguages_2 = QGridLayout(self.gridGlobalLocalization)
        self.gridLayoutGlobalLanguages_2.setObjectName(u"gridLayoutGlobalLanguages_2")
        self.gridLayoutGlobalLanguages_2.setContentsMargins(1, 0, 0, 0)
        self.horizontalSpacerGlobalLocalization = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalLanguages_2.addItem(self.horizontalSpacerGlobalLocalization, 8, 4, 1, 1)

        self.listWidgetGlobalLocalizationAvailableLanguages = CustomList(self.gridGlobalLocalization)
        self.listWidgetGlobalLocalizationAvailableLanguages.setObjectName(u"listWidgetGlobalLocalizationAvailableLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalLocalizationAvailableLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalLocalizationAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalLocalizationAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalLocalizationAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalLocalizationAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalLocalizationAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalLocalizationAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalLocalizationAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalLocalizationAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalLocalizationAvailableLanguages.setSortingEnabled(True)

        self.gridLayoutGlobalLanguages_2.addWidget(self.listWidgetGlobalLocalizationAvailableLanguages, 8, 0, 1, 1)

        self.labelGlobalLocalizeNames = QLabel(self.gridGlobalLocalization)
        self.labelGlobalLocalizeNames.setObjectName(u"labelGlobalLocalizeNames")
        self.labelGlobalLocalizeNames.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalLocalizeNames.setWordWrap(True)
        self.labelGlobalLocalizeNames.setOpenExternalLinks(True)
        self.labelGlobalLocalizeNames.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutGlobalLanguages_2.addWidget(self.labelGlobalLocalizeNames, 2, 0, 1, 5)

        self.listWidgetGlobalLocalizationSelectedLanguages = CustomListSelfDrag(self.gridGlobalLocalization)
        self.listWidgetGlobalLocalizationSelectedLanguages.setObjectName(u"listWidgetGlobalLocalizationSelectedLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetGlobalLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalLocalizationSelectedLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetGlobalLocalizationSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalLocalizationSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalLocalizationSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalLocalizationSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalLocalizationSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalLocalizationSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalLocalizationSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalLocalizationSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutGlobalLanguages_2.addWidget(self.listWidgetGlobalLocalizationSelectedLanguages, 8, 2, 1, 1)

        self.labelGlobalLocalizationSelectedLanguages = QLabel(self.gridGlobalLocalization)
        self.labelGlobalLocalizationSelectedLanguages.setObjectName(u"labelGlobalLocalizationSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalLocalizationSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalLocalizationSelectedLanguages.setFont(font)
        self.labelGlobalLocalizationSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages_2.addWidget(self.labelGlobalLocalizationSelectedLanguages, 7, 2, 1, 1)

        self.frameGlobalLocalizationUpDown = QFrame(self.gridGlobalLocalization)
        self.frameGlobalLocalizationUpDown.setObjectName(u"frameGlobalLocalizationUpDown")
        sizePolicy9.setHeightForWidth(self.frameGlobalLocalizationUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalLocalizationUpDown.setSizePolicy(sizePolicy9)
        self.frameGlobalLocalizationUpDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalLocalizationUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLocalizationUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_32 = QVBoxLayout(self.frameGlobalLocalizationUpDown)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalSpacerGlobalLocalizationDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacerGlobalLocalizationDownTop)

        self.buttonGlobalLocalizationUp = QPushButton(self.frameGlobalLocalizationUpDown)
        self.buttonGlobalLocalizationUp.setObjectName(u"buttonGlobalLocalizationUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationUp.setFont(font5)
        self.buttonGlobalLocalizationUp.setIcon(icon12)

        self.verticalLayout_32.addWidget(self.buttonGlobalLocalizationUp)

        self.buttonGlobalLocalizationDown = QPushButton(self.frameGlobalLocalizationUpDown)
        self.buttonGlobalLocalizationDown.setObjectName(u"buttonGlobalLocalizationDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationDown.setFont(font5)
        self.buttonGlobalLocalizationDown.setIcon(icon13)

        self.verticalLayout_32.addWidget(self.buttonGlobalLocalizationDown)

        self.verticalSpacerGlobalLocalizationUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacerGlobalLocalizationUpDownBottom)


        self.gridLayoutGlobalLanguages_2.addWidget(self.frameGlobalLocalizationUpDown, 8, 3, 1, 1)

        self.verticalSpacerGlobalLocalizationList = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalLanguages_2.addItem(self.verticalSpacerGlobalLocalizationList, 4, 0, 1, 4)

        self.lineGlobalLocalizationSeparator = QFrame(self.gridGlobalLocalization)
        self.lineGlobalLocalizationSeparator.setObjectName(u"lineGlobalLocalizationSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalLocalizationSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalLocalizationSeparator.setSizePolicy(sizePolicy3)
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalLocalizationSeparator.setPalette(palette6)
        self.lineGlobalLocalizationSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalLocalizationSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalLanguages_2.addWidget(self.lineGlobalLocalizationSeparator, 1, 0, 1, 5)

        self.frameGlobalLocalizationLeftRight = QFrame(self.gridGlobalLocalization)
        self.frameGlobalLocalizationLeftRight.setObjectName(u"frameGlobalLocalizationLeftRight")
        sizePolicy9.setHeightForWidth(self.frameGlobalLocalizationLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalLocalizationLeftRight.setSizePolicy(sizePolicy9)
        self.frameGlobalLocalizationLeftRight.setMinimumSize(QSize(60, 0))
        self.frameGlobalLocalizationLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLocalizationLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_31 = QVBoxLayout(self.frameGlobalLocalizationLeftRight)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalSpacerGlobalLocalizationLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacerGlobalLocalizationLeftRightTop)

        self.buttonGlobalLocalizationAllRight = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationAllRight.setObjectName(u"buttonGlobalLocalizationAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllRight.setFont(font5)
        self.buttonGlobalLocalizationAllRight.setIcon(icon8)
        self.buttonGlobalLocalizationAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_31.addWidget(self.buttonGlobalLocalizationAllRight)

        self.buttonGlobalLocalizationRight = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationRight.setObjectName(u"buttonGlobalLocalizationRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationRight.setFont(font5)
        self.buttonGlobalLocalizationRight.setIcon(icon9)
        self.buttonGlobalLocalizationRight.setIconSize(QSize(16, 16))

        self.verticalLayout_31.addWidget(self.buttonGlobalLocalizationRight)

        self.buttonGlobalLocalizationLeft = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationLeft.setObjectName(u"buttonGlobalLocalizationLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationLeft.setFont(font5)
        self.buttonGlobalLocalizationLeft.setIcon(icon10)

        self.verticalLayout_31.addWidget(self.buttonGlobalLocalizationLeft)

        self.buttonGlobalLocalizationAllLeft = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationAllLeft.setObjectName(u"buttonGlobalLocalizationAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllLeft.setFont(font5)
        self.buttonGlobalLocalizationAllLeft.setIcon(icon11)
        self.buttonGlobalLocalizationAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_31.addWidget(self.buttonGlobalLocalizationAllLeft)

        self.verticalSpacerGlobalLocalizationLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacerGlobalLocalizationLeftRightBottom)


        self.gridLayoutGlobalLanguages_2.addWidget(self.frameGlobalLocalizationLeftRight, 8, 1, 1, 1)

        self.labelGlobalLocalizationAvailableLanguages = QLabel(self.gridGlobalLocalization)
        self.labelGlobalLocalizationAvailableLanguages.setObjectName(u"labelGlobalLocalizationAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalLocalizationAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalLocalizationAvailableLanguages.setFont(font)
        self.labelGlobalLocalizationAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages_2.addWidget(self.labelGlobalLocalizationAvailableLanguages, 7, 0, 1, 1)

        self.labelGlobalUseLocalNames = QLabel(self.gridGlobalLocalization)
        self.labelGlobalUseLocalNames.setObjectName(u"labelGlobalUseLocalNames")
        sizePolicy8.setHeightForWidth(self.labelGlobalUseLocalNames.sizePolicy().hasHeightForWidth())
        self.labelGlobalUseLocalNames.setSizePolicy(sizePolicy8)
        self.labelGlobalUseLocalNames.setMinimumSize(QSize(0, 20))
        self.labelGlobalUseLocalNames.setFont(font3)
        self.labelGlobalUseLocalNames.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages_2.addWidget(self.labelGlobalUseLocalNames, 0, 0, 1, 4)


        self.gridLayout_5.addWidget(self.gridGlobalLocalization, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalLocalization, "")
        self.tabGlobalOverrides = QWidget()
        self.tabGlobalOverrides.setObjectName(u"tabGlobalOverrides")
        self.verticalLayout_11 = QVBoxLayout(self.tabGlobalOverrides)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, -1, 9)
        self.scrollAreaGlobalOverrides = QScrollArea(self.tabGlobalOverrides)
        self.scrollAreaGlobalOverrides.setObjectName(u"scrollAreaGlobalOverrides")
        sizePolicy.setHeightForWidth(self.scrollAreaGlobalOverrides.sizePolicy().hasHeightForWidth())
        self.scrollAreaGlobalOverrides.setSizePolicy(sizePolicy)
        self.scrollAreaGlobalOverrides.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaGlobalOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalOverrides.setLineWidth(0)
        self.scrollAreaGlobalOverrides.setMidLineWidth(0)
        self.scrollAreaGlobalOverrides.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalOverrides.setWidgetResizable(True)
        self.scrollAreaGlobalOverrides.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsGlobalOverrides = QWidget()
        self.scrollAreaWidgetContentsGlobalOverrides.setObjectName(u"scrollAreaWidgetContentsGlobalOverrides")
        self.scrollAreaWidgetContentsGlobalOverrides.setGeometry(QRect(0, 0, 590, 396))
        self.gridLayoutGlobalUserFilters = QGridLayout(self.scrollAreaWidgetContentsGlobalOverrides)
        self.gridLayoutGlobalUserFilters.setObjectName(u"gridLayoutGlobalUserFilters")
        self.gridLayoutGlobalUserFilters.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayoutGlobalUserFilters.setContentsMargins(1, 0, 0, 0)
        self.labelGlobalOverride = QLabel(self.scrollAreaWidgetContentsGlobalOverrides)
        self.labelGlobalOverride.setObjectName(u"labelGlobalOverride")
        self.labelGlobalOverride.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalOverride.setWordWrap(True)
        self.labelGlobalOverride.setOpenExternalLinks(True)
        self.labelGlobalOverride.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalOverride, 2, 0, 1, 3)

        self.labelGlobalOverrideByText = QLabel(self.scrollAreaWidgetContentsGlobalOverrides)
        self.labelGlobalOverrideByText.setObjectName(u"labelGlobalOverrideByText")
        self.labelGlobalOverrideByText.setMinimumSize(QSize(0, 20))
        self.labelGlobalOverrideByText.setFont(font3)
        self.labelGlobalOverrideByText.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalOverrideByText, 0, 0, 1, 3)

        self.horizontalSpacerGlobalOverrides = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalUserFilters.addItem(self.horizontalSpacerGlobalOverrides, 5, 1, 1, 1)

        self.labelGlobalOverrideInclude = QLabel(self.scrollAreaWidgetContentsGlobalOverrides)
        self.labelGlobalOverrideInclude.setObjectName(u"labelGlobalOverrideInclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalOverrideInclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalOverrideInclude.setSizePolicy(sizePolicy8)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        self.labelGlobalOverrideInclude.setFont(font6)
        self.labelGlobalOverrideInclude.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelGlobalOverrideInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalOverrideInclude, 4, 0, 1, 1)

        self.lineGlobalOverrideByText = QFrame(self.scrollAreaWidgetContentsGlobalOverrides)
        self.lineGlobalOverrideByText.setObjectName(u"lineGlobalOverrideByText")
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalOverrideByText.setPalette(palette7)
        self.lineGlobalOverrideByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalOverrideByText.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalUserFilters.addWidget(self.lineGlobalOverrideByText, 1, 0, 1, 3)

        self.textEditGlobalExclude = CustomTextEdit(self.scrollAreaWidgetContentsGlobalOverrides)
        self.textEditGlobalExclude.setObjectName(u"textEditGlobalExclude")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.textEditGlobalExclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalExclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalExclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalExclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalExclude.setTabChangesFocus(True)
        self.textEditGlobalExclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters.addWidget(self.textEditGlobalExclude, 5, 2, 1, 1)

        self.labelGlobalOverrideExclude = QLabel(self.scrollAreaWidgetContentsGlobalOverrides)
        self.labelGlobalOverrideExclude.setObjectName(u"labelGlobalOverrideExclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalOverrideExclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalOverrideExclude.setSizePolicy(sizePolicy8)
        self.labelGlobalOverrideExclude.setMinimumSize(QSize(0, 0))
        self.labelGlobalOverrideExclude.setFont(font6)
        self.labelGlobalOverrideExclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalOverrideExclude, 4, 2, 1, 1)

        self.textEditGlobalInclude = CustomTextEdit(self.scrollAreaWidgetContentsGlobalOverrides)
        self.textEditGlobalInclude.setObjectName(u"textEditGlobalInclude")
        sizePolicy10.setHeightForWidth(self.textEditGlobalInclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalInclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalInclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalInclude.setTabChangesFocus(True)
        self.textEditGlobalInclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters.addWidget(self.textEditGlobalInclude, 5, 0, 1, 1)

        self.verticalSpacerGlobalOverrides = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalUserFilters.addItem(self.verticalSpacerGlobalOverrides, 3, 0, 1, 3)

        self.scrollAreaGlobalOverrides.setWidget(self.scrollAreaWidgetContentsGlobalOverrides)

        self.verticalLayout_11.addWidget(self.scrollAreaGlobalOverrides)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalOverrides, "")
        self.tabGlobalPostFilter = QWidget()
        self.tabGlobalPostFilter.setObjectName(u"tabGlobalPostFilter")
        self.verticalLayout_23 = QVBoxLayout(self.tabGlobalPostFilter)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_23.setContentsMargins(-1, -1, -1, 9)
        self.scrollAreaGlobalPostFilters = QScrollArea(self.tabGlobalPostFilter)
        self.scrollAreaGlobalPostFilters.setObjectName(u"scrollAreaGlobalPostFilters")
        self.scrollAreaGlobalPostFilters.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaGlobalPostFilters.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalPostFilters.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalPostFilters.setLineWidth(0)
        self.scrollAreaGlobalPostFilters.setMidLineWidth(0)
        self.scrollAreaGlobalPostFilters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalPostFilters.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollAreaGlobalPostFilters.setWidgetResizable(True)
        self.scrollAreaGlobalPostFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsGlobalPostFilters = QWidget()
        self.scrollAreaWidgetContentsGlobalPostFilters.setObjectName(u"scrollAreaWidgetContentsGlobalPostFilters")
        self.scrollAreaWidgetContentsGlobalPostFilters.setGeometry(QRect(0, 0, 590, 396))
        sizePolicy8.setHeightForWidth(self.scrollAreaWidgetContentsGlobalPostFilters.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalPostFilters.setSizePolicy(sizePolicy8)
        self.gridLayoutGlobalUserFilters_3 = QGridLayout(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.gridLayoutGlobalUserFilters_3.setObjectName(u"gridLayoutGlobalUserFilters_3")
        self.gridLayoutGlobalUserFilters_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayoutGlobalUserFilters_3.setContentsMargins(1, 0, 0, 0)
        self.lineGlobalFilterByText = QFrame(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.lineGlobalFilterByText.setObjectName(u"lineGlobalFilterByText")
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalFilterByText.setPalette(palette8)
        self.lineGlobalFilterByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalFilterByText.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalUserFilters_3.addWidget(self.lineGlobalFilterByText, 1, 0, 1, 2)

        self.labelGlobalFilterByText = QLabel(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.labelGlobalFilterByText.setObjectName(u"labelGlobalFilterByText")
        self.labelGlobalFilterByText.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByText.setFont(font3)
        self.labelGlobalFilterByText.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters_3.addWidget(self.labelGlobalFilterByText, 0, 0, 1, 2)

        self.labelGlobalFilterInclude = QLabel(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.labelGlobalFilterInclude.setObjectName(u"labelGlobalFilterInclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterInclude.setSizePolicy(sizePolicy8)
        self.labelGlobalFilterInclude.setFont(font6)
        self.labelGlobalFilterInclude.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelGlobalFilterInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters_3.addWidget(self.labelGlobalFilterInclude, 4, 0, 1, 1)

        self.labelGlobalFilters = QLabel(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.labelGlobalFilters.setObjectName(u"labelGlobalFilters")
        self.labelGlobalFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalFilters.setWordWrap(True)
        self.labelGlobalFilters.setOpenExternalLinks(True)
        self.labelGlobalFilters.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutGlobalUserFilters_3.addWidget(self.labelGlobalFilters, 2, 0, 1, 2)

        self.verticalSpacerGlobalFilters = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalUserFilters_3.addItem(self.verticalSpacerGlobalFilters, 3, 0, 1, 2)

        self.textEditGlobalFilterInclude = CustomTextEdit(self.scrollAreaWidgetContentsGlobalPostFilters)
        self.textEditGlobalFilterInclude.setObjectName(u"textEditGlobalFilterInclude")
        self.textEditGlobalFilterInclude.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.textEditGlobalFilterInclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalFilterInclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalFilterInclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalFilterInclude.setMaximumSize(QSize(16777211, 16777215))
        self.textEditGlobalFilterInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalFilterInclude.setTabChangesFocus(True)
        self.textEditGlobalFilterInclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters_3.addWidget(self.textEditGlobalFilterInclude, 5, 0, 1, 2)

        self.scrollAreaGlobalPostFilters.setWidget(self.scrollAreaWidgetContentsGlobalPostFilters)

        self.verticalLayout_23.addWidget(self.scrollAreaGlobalPostFilters)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalPostFilter, "")
        self.tabGlobalOptions = QWidget()
        self.tabGlobalOptions.setObjectName(u"tabGlobalOptions")
        self.verticalLayout_14 = QVBoxLayout(self.tabGlobalOptions)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 9, -1, 0)
        self.scrollAreaGlobalOptions = QScrollArea(self.tabGlobalOptions)
        self.scrollAreaGlobalOptions.setObjectName(u"scrollAreaGlobalOptions")
        sizePolicy8.setHeightForWidth(self.scrollAreaGlobalOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaGlobalOptions.setSizePolicy(sizePolicy8)
        self.scrollAreaGlobalOptions.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaGlobalOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalOptions.setLineWidth(0)
        self.scrollAreaGlobalOptions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollAreaGlobalOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalOptions.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollAreaGlobalOptions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalOptions = QWidget()
        self.scrollAreaWidgetContentsGlobalOptions.setObjectName(u"scrollAreaWidgetContentsGlobalOptions")
        self.scrollAreaWidgetContentsGlobalOptions.setGeometry(QRect(0, -570, 573, 1159))
        sizePolicy8.setHeightForWidth(self.scrollAreaWidgetContentsGlobalOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalOptions.setSizePolicy(sizePolicy8)
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalOptions)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 18, 18)
        self.labelGlobalOptions = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptions.setObjectName(u"labelGlobalOptions")
        self.labelGlobalOptions.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptions.setFont(font3)
        self.labelGlobalOptions.setScaledContents(False)
        self.labelGlobalOptions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptions)

        self.lineGlobalOptionsTitle = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.lineGlobalOptionsTitle.setObjectName(u"lineGlobalOptionsTitle")
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalOptionsTitle.setPalette(palette9)
        self.lineGlobalOptionsTitle.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalOptionsTitle.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_16.addWidget(self.lineGlobalOptionsTitle)

        self.labelGlobalOptionsTitle = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsTitle.setObjectName(u"labelGlobalOptionsTitle")
        self.labelGlobalOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsTitle.setFont(font3)
        self.labelGlobalOptionsTitle.setScaledContents(False)
        self.labelGlobalOptionsTitle.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsTitle)

        self.checkBoxGlobalOptionsDisable1G1R = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisable1G1R.setObjectName(u"checkBoxGlobalOptionsDisable1G1R")
        self.checkBoxGlobalOptionsDisable1G1R.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setKerning(True)
        self.checkBoxGlobalOptionsDisable1G1R.setFont(font7)
        self.checkBoxGlobalOptionsDisable1G1R.setStyleSheet(u"")
        self.checkBoxGlobalOptionsDisable1G1R.setTristate(False)

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisable1G1R)

        self.checkBoxGlobalOptionsPreferRegions = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferRegions.setObjectName(u"checkBoxGlobalOptionsPreferRegions")
        self.checkBoxGlobalOptionsPreferRegions.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferRegions.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsPreferRegions)

        self.checkBoxGlobalOptionsModernPlatforms = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsModernPlatforms.setObjectName(u"checkBoxGlobalOptionsModernPlatforms")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsModernPlatforms.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsModernPlatforms.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsModernPlatforms.setFont(font)
        self.checkBoxGlobalOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsModernPlatforms)

        self.checkBoxGlobalOptionsPreferOldest = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferOldest.setObjectName(u"checkBoxGlobalOptionsPreferOldest")
        self.checkBoxGlobalOptionsPreferOldest.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferOldest.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsPreferOldest)

        self.checkBoxGlobalOptionsDemoteUnlicensed = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setObjectName(u"checkBoxGlobalOptionsDemoteUnlicensed")
        self.checkBoxGlobalOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDemoteUnlicensed)

        self.checkBoxGlobalOptionsDisableOverrides = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableOverrides.setObjectName(u"checkBoxGlobalOptionsDisableOverrides")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsDisableOverrides.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsDisableOverrides.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsDisableOverrides.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsDisableOverrides.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsDisableOverrides.setFont(font)
        self.checkBoxGlobalOptionsDisableOverrides.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisableOverrides)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.labelGlobalChooseCompilationsMode = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalChooseCompilationsMode.setObjectName(u"labelGlobalChooseCompilationsMode")
        self.labelGlobalChooseCompilationsMode.setFont(font3)

        self.verticalLayout_16.addWidget(self.labelGlobalChooseCompilationsMode)

        self.frameGlobalCompilations = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.frameGlobalCompilations.setObjectName(u"frameGlobalCompilations")
        sizePolicy8.setHeightForWidth(self.frameGlobalCompilations.sizePolicy().hasHeightForWidth())
        self.frameGlobalCompilations.setSizePolicy(sizePolicy8)
        self.frameGlobalCompilations.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalCompilations.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalCompilations.setLineWidth(0)
        self.verticalLayout_37 = QVBoxLayout(self.frameGlobalCompilations)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.comboBoxGlobalChooseCompilationsMode = CustomComboBox(self.frameGlobalCompilations)
        self.comboBoxGlobalChooseCompilationsMode.addItem("")
        self.comboBoxGlobalChooseCompilationsMode.addItem("")
        self.comboBoxGlobalChooseCompilationsMode.addItem("")
        self.comboBoxGlobalChooseCompilationsMode.addItem("")
        self.comboBoxGlobalChooseCompilationsMode.setObjectName(u"comboBoxGlobalChooseCompilationsMode")
        sizePolicy6.setHeightForWidth(self.comboBoxGlobalChooseCompilationsMode.sizePolicy().hasHeightForWidth())
        self.comboBoxGlobalChooseCompilationsMode.setSizePolicy(sizePolicy6)
        self.comboBoxGlobalChooseCompilationsMode.setMinimumSize(QSize(256, 24))
        self.comboBoxGlobalChooseCompilationsMode.setMaximumSize(QSize(256, 24))
        self.comboBoxGlobalChooseCompilationsMode.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.verticalLayout_37.addWidget(self.comboBoxGlobalChooseCompilationsMode)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_37.addItem(self.verticalSpacer_2)

        self.labelGlobalCompilationsExplanation = QLabel(self.frameGlobalCompilations)
        self.labelGlobalCompilationsExplanation.setObjectName(u"labelGlobalCompilationsExplanation")
        self.labelGlobalCompilationsExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelGlobalCompilationsExplanation.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.labelGlobalCompilationsExplanation)


        self.verticalLayout_16.addWidget(self.frameGlobalCompilations, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacerGlobalOptions_1 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_1)

        self.labelGlobalOptionsOutput = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsOutput.setObjectName(u"labelGlobalOptionsOutput")
        self.labelGlobalOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsOutput.setFont(font3)
        self.labelGlobalOptionsOutput.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsOutput)

        self.checkBoxGlobalOptionsAlreadyProcessed = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsAlreadyProcessed.setObjectName(u"checkBoxGlobalOptionsAlreadyProcessed")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(9)
        self.checkBoxGlobalOptionsAlreadyProcessed.setFont(font8)

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsAlreadyProcessed)

        self.checkBoxGlobalOptionsOriginalHeader = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsOriginalHeader.setObjectName(u"checkBoxGlobalOptionsOriginalHeader")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsOriginalHeader)

        self.checkBoxGlobalOptionsUseMachine = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsUseMachine.setObjectName(u"checkBoxGlobalOptionsUseMachine")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsUseMachine)

        self.checkBoxGlobalOptionsSplitRegions = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsSplitRegions.setObjectName(u"checkBoxGlobalOptionsSplitRegions")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsSplitRegions)

        self.checkBoxGlobalOptionsRemovesDat = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsRemovesDat.setObjectName(u"checkBoxGlobalOptionsRemovesDat")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsRemovesDat)

        self.checkBoxGlobalOptionsKeepRemove = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsKeepRemove.setObjectName(u"checkBoxGlobalOptionsKeepRemove")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsKeepRemove)

        self.checkBoxGlobalOptions1G1RNames = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptions1G1RNames.setObjectName(u"checkBoxGlobalOptions1G1RNames")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptions1G1RNames)

        self.frameGlobalOptions1G1RPrefix = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.frameGlobalOptions1G1RPrefix.setObjectName(u"frameGlobalOptions1G1RPrefix")
        self.frameGlobalOptions1G1RPrefix.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameGlobalOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptions1G1RPrefix.setSizePolicy(sizePolicy8)
        self.frameGlobalOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        brush4 = QBrush(QColor(240, 240, 240, 0))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        brush5 = QBrush(QColor(227, 227, 227, 0))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        brush6 = QBrush(QColor(160, 160, 160, 0))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        brush8 = QBrush(QColor(0, 255, 127, 0))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        brush9 = QBrush(QColor(105, 105, 105, 0))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        brush10 = QBrush(QColor(246, 246, 246, 0))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameGlobalOptions1G1RPrefix.setPalette(palette10)
        self.labelGlobalOptions1G1RPrefix = QLabel(self.frameGlobalOptions1G1RPrefix)
        self.labelGlobalOptions1G1RPrefix.setObjectName(u"labelGlobalOptions1G1RPrefix")
        self.labelGlobalOptions1G1RPrefix.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditGlobalOptions1G1RPrefix = CustomLineEdit(self.frameGlobalOptions1G1RPrefix)
        self.lineEditGlobalOptions1G1RPrefix.setObjectName(u"lineEditGlobalOptions1G1RPrefix")
        self.lineEditGlobalOptions1G1RPrefix.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditGlobalOptions1G1RPrefix.setMinimumSize(QSize(0, 24))
        self.labelGlobalOptions1G1RSuffix = QLabel(self.frameGlobalOptions1G1RPrefix)
        self.labelGlobalOptions1G1RSuffix.setObjectName(u"labelGlobalOptions1G1RSuffix")
        self.labelGlobalOptions1G1RSuffix.setGeometry(QRect(19, 58, 521, 20))
        self.lineEditGlobalOptions1G1RSuffix = CustomLineEdit(self.frameGlobalOptions1G1RPrefix)
        self.lineEditGlobalOptions1G1RSuffix.setObjectName(u"lineEditGlobalOptions1G1RSuffix")
        self.lineEditGlobalOptions1G1RSuffix.setGeometry(QRect(20, 83, 521, 24))
        self.lineEditGlobalOptions1G1RSuffix.setMinimumSize(QSize(0, 24))

        self.verticalLayout_16.addWidget(self.frameGlobalOptions1G1RPrefix)

        self.verticalSpacerGlobalOptions_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_2)

        self.labelGlobalOptionsOnline = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsOnline.setObjectName(u"labelGlobalOptionsOnline")
        self.labelGlobalOptionsOnline.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsOnline.setFont(font3)
        self.labelGlobalOptionsOnline.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsOnline)

        self.labelGlobalOnlineExplanation = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOnlineExplanation.setObjectName(u"labelGlobalOnlineExplanation")
        self.labelGlobalOnlineExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelGlobalOnlineExplanation.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.labelGlobalOnlineExplanation)

        self.verticalSpacerGlobalOptions_5 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_5)

        self.checkBoxGlobalOptionsMIA = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsMIA.setObjectName(u"checkBoxGlobalOptionsMIA")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsMIA.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsMIA.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsMIA.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsMIA.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsMIA.setFont(font)
        self.checkBoxGlobalOptionsMIA.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsMIA)

        self.checkBoxGlobalOptionsRetroAchievements = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsRetroAchievements.setObjectName(u"checkBoxGlobalOptionsRetroAchievements")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsRetroAchievements.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsRetroAchievements.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsRetroAchievements.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsRetroAchievements.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsRetroAchievements.setFont(font)
        self.checkBoxGlobalOptionsRetroAchievements.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsRetroAchievements)

        self.checkBoxGlobalOptionsPreferRetro = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferRetro.setObjectName(u"checkBoxGlobalOptionsPreferRetro")
        self.checkBoxGlobalOptionsPreferRetro.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferRetro.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsPreferRetro)

        self.verticalSpacerGlobalOptions_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_4)

        self.labelGlobalOptionsDebug = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsDebug.setObjectName(u"labelGlobalOptionsDebug")
        self.labelGlobalOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsDebug.setFont(font3)
        self.labelGlobalOptionsDebug.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsDebug)

        self.checkBoxGlobalOptionsReportWarnings = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsReportWarnings.setObjectName(u"checkBoxGlobalOptionsReportWarnings")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsReportWarnings)

        self.checkBoxGlobalOptionsPauseWarnings = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsPauseWarnings.setObjectName(u"checkBoxGlobalOptionsPauseWarnings")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsPauseWarnings)

        self.checkBoxGlobalOptionsLegacy = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsLegacy.setObjectName(u"checkBoxGlobalOptionsLegacy")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsLegacy)

        self.checkBoxGlobalOptionsDisableMultiCPU = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableMultiCPU.setObjectName(u"checkBoxGlobalOptionsDisableMultiCPU")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisableMultiCPU)

        self.checkBoxGlobalOptionsTrace = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsTrace.setObjectName(u"checkBoxGlobalOptionsTrace")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsTrace)

        self.frameGlobalOptionsTrace = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.frameGlobalOptionsTrace.setObjectName(u"frameGlobalOptionsTrace")
        self.frameGlobalOptionsTrace.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameGlobalOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptionsTrace.setSizePolicy(sizePolicy8)
        self.frameGlobalOptionsTrace.setMinimumSize(QSize(0, 55))
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameGlobalOptionsTrace.setPalette(palette11)
        self.labelGlobalOptionsTrace = QLabel(self.frameGlobalOptionsTrace)
        self.labelGlobalOptionsTrace.setObjectName(u"labelGlobalOptionsTrace")
        self.labelGlobalOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditGlobalOptionsTrace = CustomLineEdit(self.frameGlobalOptionsTrace)
        self.lineEditGlobalOptionsTrace.setObjectName(u"lineEditGlobalOptionsTrace")
        self.lineEditGlobalOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditGlobalOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_16.addWidget(self.frameGlobalOptionsTrace)

        self.verticalSpacerGlobalOptions_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_3)

        self.scrollAreaGlobalOptions.setWidget(self.scrollAreaWidgetContentsGlobalOptions)

        self.verticalLayout_14.addWidget(self.scrollAreaGlobalOptions)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalOptions, "")

        self.verticalLayout_7.addWidget(self.tabWidgetGlobalSettings)

        self.tabWidgetSettings.addTab(self.tabGlobalSettings, "")
        self.tabSystemSettings = QWidget()
        self.tabSystemSettings.setObjectName(u"tabSystemSettings")
        self.gridLayout_3 = QGridLayout(self.tabSystemSettings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelSystemSettings = QLabel(self.tabSystemSettings)
        self.labelSystemSettings.setObjectName(u"labelSystemSettings")
        self.labelSystemSettings.setFont(font)
        self.labelSystemSettings.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemSettings.setWordWrap(True)
        self.labelSystemSettings.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.labelSystemSettings, 0, 0, 1, 1)

        self.tabWidgetSystemSettings = QTabWidget(self.tabSystemSettings)
        self.tabWidgetSystemSettings.setObjectName(u"tabWidgetSystemSettings")
        self.tabWidgetSystemSettings.setFont(font)
        self.tabSystemPaths = QWidget()
        self.tabSystemPaths.setObjectName(u"tabSystemPaths")
        self.gridLayout_8 = QGridLayout(self.tabSystemPaths)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.labelSystemSelectOutput = QLabel(self.tabSystemPaths)
        self.labelSystemSelectOutput.setObjectName(u"labelSystemSelectOutput")
        self.labelSystemSelectOutput.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectOutput.setFont(font4)

        self.gridLayout_8.addWidget(self.labelSystemSelectOutput, 3, 3, 1, 1)

        self.buttonSystemClearMIAFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemClearMIAFile.setObjectName(u"buttonSystemClearMIAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearMIAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearMIAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearMIAFile.setFont(font1)
        self.buttonSystemClearMIAFile.setIcon(icon5)
        self.buttonSystemClearMIAFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearMIAFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemClearMIAFile, 11, 0, 2, 1)

        self.labelSystemOptionsTitle_2 = QLabel(self.tabSystemPaths)
        self.labelSystemOptionsTitle_2.setObjectName(u"labelSystemOptionsTitle_2")
        self.labelSystemOptionsTitle_2.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsTitle_2.setFont(font3)
        self.labelSystemOptionsTitle_2.setScaledContents(False)
        self.labelSystemOptionsTitle_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.labelSystemOptionsTitle_2, 2, 0, 1, 1)

        self.buttonSystemClearMetadataFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemClearMetadataFile.setObjectName(u"buttonSystemClearMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearMetadataFile.setFont(font1)
        self.buttonSystemClearMetadataFile.setIcon(icon5)
        self.buttonSystemClearMetadataFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearMetadataFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemClearMetadataFile, 9, 0, 2, 1)

        self.frameSystemReplace = QFrame(self.tabSystemPaths)
        self.frameSystemReplace.setObjectName(u"frameSystemReplace")
        self.frameSystemReplace.setMinimumSize(QSize(0, 0))
        self.frameSystemReplace.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemReplace.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_36 = QVBoxLayout(self.frameSystemReplace)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 6, 0, 12)
        self.checkBoxSystemReplaceInputDats = QCheckBox(self.frameSystemReplace)
        self.checkBoxSystemReplaceInputDats.setObjectName(u"checkBoxSystemReplaceInputDats")
        self.checkBoxSystemReplaceInputDats.setFont(font2)

        self.verticalLayout_36.addWidget(self.checkBoxSystemReplaceInputDats)


        self.gridLayout_8.addWidget(self.frameSystemReplace, 5, 0, 1, 4)

        self.labelSystemSelectMetadataFile = QLabel(self.tabSystemPaths)
        self.labelSystemSelectMetadataFile.setObjectName(u"labelSystemSelectMetadataFile")
        self.labelSystemSelectMetadataFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectMetadataFile.setFont(font4)

        self.gridLayout_8.addWidget(self.labelSystemSelectMetadataFile, 9, 3, 1, 1)

        self.labelSystemMIAFile = ElisionLabel(self.tabSystemPaths)
        self.labelSystemMIAFile.setObjectName(u"labelSystemMIAFile")
        sizePolicy5.setHeightForWidth(self.labelSystemMIAFile.sizePolicy().hasHeightForWidth())
        self.labelSystemMIAFile.setSizePolicy(sizePolicy5)
        self.labelSystemMIAFile.setMinimumSize(QSize(400, 0))
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemMIAFile.setPalette(palette12)
        self.labelSystemMIAFile.setFont(font2)

        self.gridLayout_8.addWidget(self.labelSystemMIAFile, 12, 3, 1, 1)

        self.buttonSystemClearRAFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemClearRAFile.setObjectName(u"buttonSystemClearRAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearRAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearRAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearRAFile.setFont(font1)
        self.buttonSystemClearRAFile.setIcon(icon5)
        self.buttonSystemClearRAFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearRAFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemClearRAFile, 19, 0, 2, 1)

        self.horizontalSpacerSystemPaths_1 = QSpacerItem(4, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacerSystemPaths_1, 7, 2, 1, 1)

        self.buttonSystemChooseRAFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemChooseRAFile.setObjectName(u"buttonSystemChooseRAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseRAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseRAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseRAFile.setFont(font1)
        icon14 = QIcon()
        icon14.addFile(u":/retoolFiles/images/icons8-diff-files-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonSystemChooseRAFile.setIcon(icon14)
        self.buttonSystemChooseRAFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseRAFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemChooseRAFile, 19, 1, 2, 1)

        self.labelSystemSelectCloneList = QLabel(self.tabSystemPaths)
        self.labelSystemSelectCloneList.setObjectName(u"labelSystemSelectCloneList")
        self.labelSystemSelectCloneList.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectCloneList.setFont(font4)

        self.gridLayout_8.addWidget(self.labelSystemSelectCloneList, 7, 3, 1, 1)

        self.labelSystemSelectRAFile = QLabel(self.tabSystemPaths)
        self.labelSystemSelectRAFile.setObjectName(u"labelSystemSelectRAFile")
        self.labelSystemSelectRAFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectRAFile.setFont(font4)

        self.gridLayout_8.addWidget(self.labelSystemSelectRAFile, 19, 3, 1, 1)

        self.buttonSystemChooseMetadataFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemChooseMetadataFile.setObjectName(u"buttonSystemChooseMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseMetadataFile.setFont(font1)
        self.buttonSystemChooseMetadataFile.setIcon(icon14)
        self.buttonSystemChooseMetadataFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseMetadataFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemChooseMetadataFile, 9, 1, 2, 1)

        self.labelSystemCloneList = ElisionLabel(self.tabSystemPaths)
        self.labelSystemCloneList.setObjectName(u"labelSystemCloneList")
        sizePolicy5.setHeightForWidth(self.labelSystemCloneList.sizePolicy().hasHeightForWidth())
        self.labelSystemCloneList.setSizePolicy(sizePolicy5)
        self.labelSystemCloneList.setMinimumSize(QSize(400, 0))
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemCloneList.setPalette(palette13)
        self.labelSystemCloneList.setFont(font2)

        self.gridLayout_8.addWidget(self.labelSystemCloneList, 8, 3, 1, 1)

        self.labelSystemMetadataFile = ElisionLabel(self.tabSystemPaths)
        self.labelSystemMetadataFile.setObjectName(u"labelSystemMetadataFile")
        sizePolicy5.setHeightForWidth(self.labelSystemMetadataFile.sizePolicy().hasHeightForWidth())
        self.labelSystemMetadataFile.setSizePolicy(sizePolicy5)
        self.labelSystemMetadataFile.setMinimumSize(QSize(400, 0))
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemMetadataFile.setPalette(palette14)
        self.labelSystemMetadataFile.setFont(font2)

        self.gridLayout_8.addWidget(self.labelSystemMetadataFile, 10, 3, 1, 1)

        self.buttonSystemChooseMIAFile = QPushButton(self.tabSystemPaths)
        self.buttonSystemChooseMIAFile.setObjectName(u"buttonSystemChooseMIAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseMIAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseMIAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseMIAFile.setFont(font1)
        self.buttonSystemChooseMIAFile.setIcon(icon14)
        self.buttonSystemChooseMIAFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseMIAFile.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemChooseMIAFile, 11, 1, 2, 1)

        self.buttonSystemClearCloneList = QPushButton(self.tabSystemPaths)
        self.buttonSystemClearCloneList.setObjectName(u"buttonSystemClearCloneList")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearCloneList.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearCloneList.setSizePolicy(sizePolicy6)
        self.buttonSystemClearCloneList.setFont(font1)
        self.buttonSystemClearCloneList.setIcon(icon5)
        self.buttonSystemClearCloneList.setIconSize(QSize(32, 32))
        self.buttonSystemClearCloneList.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemClearCloneList, 7, 0, 2, 1)

        self.labelSystemSelectMIAFile = QLabel(self.tabSystemPaths)
        self.labelSystemSelectMIAFile.setObjectName(u"labelSystemSelectMIAFile")
        self.labelSystemSelectMIAFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectMIAFile.setFont(font4)

        self.gridLayout_8.addWidget(self.labelSystemSelectMIAFile, 11, 3, 1, 1)

        self.buttonSystemChooseCloneList = QPushButton(self.tabSystemPaths)
        self.buttonSystemChooseCloneList.setObjectName(u"buttonSystemChooseCloneList")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseCloneList.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseCloneList.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseCloneList.setFont(font1)
        self.buttonSystemChooseCloneList.setIcon(icon14)
        self.buttonSystemChooseCloneList.setIconSize(QSize(32, 32))
        self.buttonSystemChooseCloneList.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemChooseCloneList, 7, 1, 2, 1)

        self.labelSystemRAFile = ElisionLabel(self.tabSystemPaths)
        self.labelSystemRAFile.setObjectName(u"labelSystemRAFile")
        sizePolicy5.setHeightForWidth(self.labelSystemRAFile.sizePolicy().hasHeightForWidth())
        self.labelSystemRAFile.setSizePolicy(sizePolicy5)
        self.labelSystemRAFile.setMinimumSize(QSize(400, 0))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemRAFile.setPalette(palette15)
        self.labelSystemRAFile.setFont(font2)

        self.gridLayout_8.addWidget(self.labelSystemRAFile, 20, 3, 1, 1)

        self.buttonSystemClearOutput = QPushButton(self.tabSystemPaths)
        self.buttonSystemClearOutput.setObjectName(u"buttonSystemClearOutput")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearOutput.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearOutput.setSizePolicy(sizePolicy6)
        self.buttonSystemClearOutput.setFont(font1)
        self.buttonSystemClearOutput.setIcon(icon5)
        self.buttonSystemClearOutput.setIconSize(QSize(32, 32))
        self.buttonSystemClearOutput.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemClearOutput, 3, 0, 2, 1)

        self.buttonSystemChooseOutput = QPushButton(self.tabSystemPaths)
        self.buttonSystemChooseOutput.setObjectName(u"buttonSystemChooseOutput")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseOutput.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseOutput.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseOutput.setFont(font1)
        self.buttonSystemChooseOutput.setAutoFillBackground(False)
        self.buttonSystemChooseOutput.setIcon(icon7)
        self.buttonSystemChooseOutput.setIconSize(QSize(32, 32))
        self.buttonSystemChooseOutput.setFlat(False)

        self.gridLayout_8.addWidget(self.buttonSystemChooseOutput, 3, 1, 2, 1)

        self.horizontalSpacerSystemPaths_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacerSystemPaths_2, 9, 4, 1, 1)

        self.labelSystemOptionsTitle_3 = QLabel(self.tabSystemPaths)
        self.labelSystemOptionsTitle_3.setObjectName(u"labelSystemOptionsTitle_3")
        self.labelSystemOptionsTitle_3.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsTitle_3.setFont(font3)
        self.labelSystemOptionsTitle_3.setScaledContents(False)
        self.labelSystemOptionsTitle_3.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.labelSystemOptionsTitle_3, 6, 0, 1, 4)

        self.labelSystemOutputFolder = ElisionLabel(self.tabSystemPaths)
        self.labelSystemOutputFolder.setObjectName(u"labelSystemOutputFolder")
        sizePolicy5.setHeightForWidth(self.labelSystemOutputFolder.sizePolicy().hasHeightForWidth())
        self.labelSystemOutputFolder.setSizePolicy(sizePolicy5)
        self.labelSystemOutputFolder.setMinimumSize(QSize(400, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemOutputFolder.setPalette(palette16)
        self.labelSystemOutputFolder.setFont(font2)

        self.gridLayout_8.addWidget(self.labelSystemOutputFolder, 4, 3, 1, 1)

        self.verticalSpacerSystemPaths = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacerSystemPaths, 32, 3, 1, 1)

        self.lineSystemCustomFilesAndFolders = QFrame(self.tabSystemPaths)
        self.lineSystemCustomFilesAndFolders.setObjectName(u"lineSystemCustomFilesAndFolders")
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemCustomFilesAndFolders.setPalette(palette17)
        self.lineSystemCustomFilesAndFolders.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemCustomFilesAndFolders.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_8.addWidget(self.lineSystemCustomFilesAndFolders, 1, 0, 1, 5)

        self.frameSystemPathsHeader = QFrame(self.tabSystemPaths)
        self.frameSystemPathsHeader.setObjectName(u"frameSystemPathsHeader")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frameSystemPathsHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemPathsHeader.setSizePolicy(sizePolicy12)
        self.frameSystemPathsHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemPathsHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemPathsHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemPathsHeader.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frameSystemPathsHeader)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelSystemCustomFilesAndFolders = QLabel(self.frameSystemPathsHeader)
        self.labelSystemCustomFilesAndFolders.setObjectName(u"labelSystemCustomFilesAndFolders")
        self.labelSystemCustomFilesAndFolders.setFont(font3)
        self.labelSystemCustomFilesAndFolders.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.labelSystemCustomFilesAndFolders)

        self.checkBoxSystemOverridePaths = QCheckBox(self.frameSystemPathsHeader)
        self.checkBoxSystemOverridePaths.setObjectName(u"checkBoxSystemOverridePaths")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverridePaths.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverridePaths.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.checkBoxSystemOverridePaths)


        self.gridLayout_8.addWidget(self.frameSystemPathsHeader, 0, 0, 1, 5)

        self.tabWidgetSystemSettings.addTab(self.tabSystemPaths, "")
        self.tabSystemRegions = QWidget()
        self.tabSystemRegions.setObjectName(u"tabSystemRegions")
        self.verticalLayout = QVBoxLayout(self.tabSystemRegions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridSystemRegions = QWidget(self.tabSystemRegions)
        self.gridSystemRegions.setObjectName(u"gridSystemRegions")
        self.gridLayoutSystemRegions = QGridLayout(self.gridSystemRegions)
        self.gridLayoutSystemRegions.setObjectName(u"gridLayoutSystemRegions")
        self.gridLayoutSystemRegions.setContentsMargins(1, 0, 0, 0)
        self.frameSystemRegionUpDown = QFrame(self.gridSystemRegions)
        self.frameSystemRegionUpDown.setObjectName(u"frameSystemRegionUpDown")
        sizePolicy9.setHeightForWidth(self.frameSystemRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionUpDown.setSizePolicy(sizePolicy9)
        self.frameSystemRegionUpDown.setMinimumSize(QSize(60, 0))
        self.frameSystemRegionUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegionUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frameSystemRegionUpDown)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacerSystemRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacerSystemRegionUpDownTop)

        self.buttonSystemRegionUp = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionUp.setObjectName(u"buttonSystemRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionUp.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionUp.setFont(font5)
        self.buttonSystemRegionUp.setIcon(icon12)

        self.verticalLayout_15.addWidget(self.buttonSystemRegionUp)

        self.buttonSystemRegionDown = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionDown.setObjectName(u"buttonSystemRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionDown.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionDown.setFont(font5)
        self.buttonSystemRegionDown.setIcon(icon13)

        self.verticalLayout_15.addWidget(self.buttonSystemRegionDown)

        self.verticalSpacerSystemRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacerSystemRegionUpDownBottom)


        self.gridLayoutSystemRegions.addWidget(self.frameSystemRegionUpDown, 3, 3, 1, 1)

        self.horizontalSpacerSystemRegions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemRegions.addItem(self.horizontalSpacerSystemRegions, 3, 4, 1, 1)

        self.labelSystemSelectedRegions = QLabel(self.gridSystemRegions)
        self.labelSystemSelectedRegions.setObjectName(u"labelSystemSelectedRegions")
        sizePolicy8.setHeightForWidth(self.labelSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedRegions.setSizePolicy(sizePolicy8)
        self.labelSystemSelectedRegions.setFont(font)
        self.labelSystemSelectedRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemRegions.addWidget(self.labelSystemSelectedRegions, 2, 2, 1, 1)

        self.frameSystemRegionLeftRight = QFrame(self.gridSystemRegions)
        self.frameSystemRegionLeftRight.setObjectName(u"frameSystemRegionLeftRight")
        sizePolicy9.setHeightForWidth(self.frameSystemRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionLeftRight.setSizePolicy(sizePolicy9)
        self.frameSystemRegionLeftRight.setMinimumSize(QSize(60, 0))
        self.frameSystemRegionLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegionLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frameSystemRegionLeftRight)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacerSystemRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacerSystemRegionLeftRightTop)

        self.buttonSystemRegionAllRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllRight.setObjectName(u"buttonSystemRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllRight.setFont(font5)
        self.buttonSystemRegionAllRight.setIcon(icon8)
        self.buttonSystemRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionAllRight)

        self.buttonSystemRegionRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionRight.setObjectName(u"buttonSystemRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionRight.setFont(font5)
        self.buttonSystemRegionRight.setIcon(icon9)
        self.buttonSystemRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionRight)

        self.buttonSystemRegionLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionLeft.setObjectName(u"buttonSystemRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionLeft.setFont(font5)
        self.buttonSystemRegionLeft.setIcon(icon10)

        self.verticalLayout_17.addWidget(self.buttonSystemRegionLeft)

        self.buttonSystemRegionAllLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllLeft.setObjectName(u"buttonSystemRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllLeft.setFont(font5)
        self.buttonSystemRegionAllLeft.setIcon(icon11)
        self.buttonSystemRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionAllLeft)

        self.verticalSpacerSystemRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacerSystemRegionLeftRightBottom)


        self.gridLayoutSystemRegions.addWidget(self.frameSystemRegionLeftRight, 3, 1, 1, 1)

        self.buttonSystemDefaultRegionOrder = QPushButton(self.gridSystemRegions)
        self.buttonSystemDefaultRegionOrder.setObjectName(u"buttonSystemDefaultRegionOrder")
        sizePolicy6.setHeightForWidth(self.buttonSystemDefaultRegionOrder.sizePolicy().hasHeightForWidth())
        self.buttonSystemDefaultRegionOrder.setSizePolicy(sizePolicy6)
        self.buttonSystemDefaultRegionOrder.setMinimumSize(QSize(286, 41))

        self.gridLayoutSystemRegions.addWidget(self.buttonSystemDefaultRegionOrder, 5, 0, 1, 2)

        self.listWidgetSystemAvailableRegions = CustomList(self.gridSystemRegions)
        self.listWidgetSystemAvailableRegions.setObjectName(u"listWidgetSystemAvailableRegions")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableRegions.setSizePolicy(sizePolicy7)
        self.listWidgetSystemAvailableRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemAvailableRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemAvailableRegions.setTabKeyNavigation(True)
        self.listWidgetSystemAvailableRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemAvailableRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemAvailableRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemAvailableRegions.setAlternatingRowColors(False)
        self.listWidgetSystemAvailableRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemAvailableRegions.setSortingEnabled(True)

        self.gridLayoutSystemRegions.addWidget(self.listWidgetSystemAvailableRegions, 3, 0, 1, 1)

        self.lineSystemRegionSeparator = QFrame(self.gridSystemRegions)
        self.lineSystemRegionSeparator.setObjectName(u"lineSystemRegionSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemRegionSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemRegionSeparator.setSizePolicy(sizePolicy3)
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemRegionSeparator.setPalette(palette18)
        self.lineSystemRegionSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemRegionSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutSystemRegions.addWidget(self.lineSystemRegionSeparator, 1, 0, 1, 5)

        self.labelSystemAvailableRegions = QLabel(self.gridSystemRegions)
        self.labelSystemAvailableRegions.setObjectName(u"labelSystemAvailableRegions")
        sizePolicy8.setHeightForWidth(self.labelSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableRegions.setSizePolicy(sizePolicy8)
        self.labelSystemAvailableRegions.setFont(font)
        self.labelSystemAvailableRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemRegions.addWidget(self.labelSystemAvailableRegions, 2, 0, 1, 1)

        self.frameSystemRegionsHeader = QFrame(self.gridSystemRegions)
        self.frameSystemRegionsHeader.setObjectName(u"frameSystemRegionsHeader")
        sizePolicy12.setHeightForWidth(self.frameSystemRegionsHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionsHeader.setSizePolicy(sizePolicy12)
        self.frameSystemRegionsHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemRegionsHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegionsHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemRegionsHeader.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frameSystemRegionsHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByRegions = QLabel(self.frameSystemRegionsHeader)
        self.labelSystemFilterByRegions.setObjectName(u"labelSystemFilterByRegions")
        sizePolicy8.setHeightForWidth(self.labelSystemFilterByRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByRegions.setSizePolicy(sizePolicy8)
        self.labelSystemFilterByRegions.setFont(font3)
        self.labelSystemFilterByRegions.setLineWidth(0)
        self.labelSystemFilterByRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout.addWidget(self.labelSystemFilterByRegions)

        self.checkBoxSystemOverrideRegions = QCheckBox(self.frameSystemRegionsHeader)
        self.checkBoxSystemOverrideRegions.setObjectName(u"checkBoxSystemOverrideRegions")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideRegions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideRegions.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.checkBoxSystemOverrideRegions)


        self.gridLayoutSystemRegions.addWidget(self.frameSystemRegionsHeader, 0, 0, 1, 5)

        self.verticalSpacerSystemRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutSystemRegions.addItem(self.verticalSpacerSystemRegionsEnglishButton, 4, 0, 1, 1)

        self.listWidgetSystemSelectedRegions = CustomListSelfDrag(self.gridSystemRegions)
        self.listWidgetSystemSelectedRegions.setObjectName(u"listWidgetSystemSelectedRegions")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedRegions.setSizePolicy(sizePolicy7)
        self.listWidgetSystemSelectedRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemSelectedRegions.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemSelectedRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemSelectedRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemSelectedRegions.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutSystemRegions.addWidget(self.listWidgetSystemSelectedRegions, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridSystemRegions)

        self.tabWidgetSystemSettings.addTab(self.tabSystemRegions, "")
        self.tabSystemLanguages = QWidget()
        self.tabSystemLanguages.setObjectName(u"tabSystemLanguages")
        self.verticalLayout_2 = QVBoxLayout(self.tabSystemLanguages)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridSystemLanguages = QWidget(self.tabSystemLanguages)
        self.gridSystemLanguages.setObjectName(u"gridSystemLanguages")
        self.gridLayoutSystemLanguages = QGridLayout(self.gridSystemLanguages)
        self.gridLayoutSystemLanguages.setObjectName(u"gridLayoutSystemLanguages")
        self.gridLayoutSystemLanguages.setContentsMargins(1, 0, 0, 0)
        self.listWidgetSystemAvailableLanguages = CustomList(self.gridSystemLanguages)
        self.listWidgetSystemAvailableLanguages.setObjectName(u"listWidgetSystemAvailableLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetSystemAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemAvailableLanguages.setSortingEnabled(True)
        self.listWidgetSystemAvailableLanguages.setProperty(u"self_drag", False)

        self.gridLayoutSystemLanguages.addWidget(self.listWidgetSystemAvailableLanguages, 3, 0, 1, 1)

        self.frameSystemLanguagesHeader = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguagesHeader.setObjectName(u"frameSystemLanguagesHeader")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.frameSystemLanguagesHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguagesHeader.setSizePolicy(sizePolicy13)
        self.frameSystemLanguagesHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemLanguagesHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguagesHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLanguagesHeader.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frameSystemLanguagesHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByLanguages = QLabel(self.frameSystemLanguagesHeader)
        self.labelSystemFilterByLanguages.setObjectName(u"labelSystemFilterByLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemFilterByLanguages.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByLanguages.setFont(font3)
        self.labelSystemFilterByLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.labelSystemFilterByLanguages)

        self.checkBoxSystemOverrideLanguages = QCheckBox(self.frameSystemLanguagesHeader)
        self.checkBoxSystemOverrideLanguages.setObjectName(u"checkBoxSystemOverrideLanguages")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideLanguages.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideLanguages.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.checkBoxSystemOverrideLanguages)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguagesHeader, 0, 0, 1, 5)

        self.horizontalSpacerSystemLanguages = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemLanguages.addItem(self.horizontalSpacerSystemLanguages, 3, 4, 1, 1)

        self.frameSystemLanguageLeftRight = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguageLeftRight.setObjectName(u"frameSystemLanguageLeftRight")
        sizePolicy9.setHeightForWidth(self.frameSystemLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageLeftRight.setSizePolicy(sizePolicy9)
        self.frameSystemLanguageLeftRight.setMinimumSize(QSize(60, 0))
        self.frameSystemLanguageLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguageLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_26 = QVBoxLayout(self.frameSystemLanguageLeftRight)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacerSystemLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightTop)

        self.buttonSystemLanguageAllRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllRight.setObjectName(u"buttonSystemLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllRight.setFont(font5)
        self.buttonSystemLanguageAllRight.setIcon(icon8)
        self.buttonSystemLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageAllRight)

        self.buttonSystemLanguageRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageRight.setObjectName(u"buttonSystemLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageRight.setFont(font5)
        self.buttonSystemLanguageRight.setIcon(icon9)
        self.buttonSystemLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageRight)

        self.buttonSystemLanguageLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageLeft.setObjectName(u"buttonSystemLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageLeft.setFont(font5)
        self.buttonSystemLanguageLeft.setIcon(icon10)

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageLeft)

        self.buttonSystemLanguageAllLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllLeft.setObjectName(u"buttonSystemLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllLeft.setFont(font5)
        self.buttonSystemLanguageAllLeft.setIcon(icon11)
        self.buttonSystemLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageAllLeft)

        self.verticalSpacerSystemLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightBottom)

        self.verticalSpacerSystemLanguageLeftRightBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightBuffer)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguageLeftRight, 3, 1, 1, 1)

        self.lineSystemLanguageSeparator = QFrame(self.gridSystemLanguages)
        self.lineSystemLanguageSeparator.setObjectName(u"lineSystemLanguageSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemLanguageSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemLanguageSeparator.setSizePolicy(sizePolicy3)
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemLanguageSeparator.setPalette(palette19)
        self.lineSystemLanguageSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemLanguageSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutSystemLanguages.addWidget(self.lineSystemLanguageSeparator, 1, 0, 1, 5)

        self.frameSystemLanguageUpDown = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguageUpDown.setObjectName(u"frameSystemLanguageUpDown")
        sizePolicy9.setHeightForWidth(self.frameSystemLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageUpDown.setSizePolicy(sizePolicy9)
        self.frameSystemLanguageUpDown.setMinimumSize(QSize(60, 0))
        self.frameSystemLanguageUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguageUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_28 = QVBoxLayout(self.frameSystemLanguageUpDown)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacerSystemLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownTop)

        self.buttonSystemLanguageUp = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageUp.setObjectName(u"buttonSystemLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageUp.setFont(font5)
        self.buttonSystemLanguageUp.setIcon(icon12)

        self.verticalLayout_28.addWidget(self.buttonSystemLanguageUp)

        self.buttonSystemLanguageDown = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageDown.setObjectName(u"buttonSystemLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageDown.setFont(font5)
        self.buttonSystemLanguageDown.setIcon(icon13)

        self.verticalLayout_28.addWidget(self.buttonSystemLanguageDown)

        self.verticalSpacerSystemLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownBottom)

        self.verticalSpacerSystemLanguageUpDownBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownBuffer)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguageUpDown, 3, 3, 1, 1)

        self.listWidgetSystemSelectedLanguages = CustomListSelfDrag(self.gridSystemLanguages)
        self.listWidgetSystemSelectedLanguages.setObjectName(u"listWidgetSystemSelectedLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetSystemSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemSelectedLanguages.setProperty(u"self_drag", True)

        self.gridLayoutSystemLanguages.addWidget(self.listWidgetSystemSelectedLanguages, 3, 2, 1, 1)

        self.labelSystemAvailableLanguages = QLabel(self.gridSystemLanguages)
        self.labelSystemAvailableLanguages.setObjectName(u"labelSystemAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemAvailableLanguages.setFont(font)
        self.labelSystemAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemLanguages.addWidget(self.labelSystemAvailableLanguages, 2, 0, 1, 1)

        self.labelSystemSelectedLanguages = QLabel(self.gridSystemLanguages)
        self.labelSystemSelectedLanguages.setObjectName(u"labelSystemSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemSelectedLanguages.setFont(font)
        self.labelSystemSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemLanguages.addWidget(self.labelSystemSelectedLanguages, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.gridSystemLanguages)

        self.tabWidgetSystemSettings.addTab(self.tabSystemLanguages, "")
        self.tabSystemVideo = QWidget()
        self.tabSystemVideo.setObjectName(u"tabSystemVideo")
        self.verticalLayout_18 = QVBoxLayout(self.tabSystemVideo)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridSystemVideo = QWidget(self.tabSystemVideo)
        self.gridSystemVideo.setObjectName(u"gridSystemVideo")
        self.gridLayoutSystemVideo = QGridLayout(self.gridSystemVideo)
        self.gridLayoutSystemVideo.setSpacing(6)
        self.gridLayoutSystemVideo.setObjectName(u"gridLayoutSystemVideo")
        self.gridLayoutSystemVideo.setContentsMargins(1, 0, 0, 0)
        self.horizontalSpacerSystemVideo_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_3, 4, 3, 1, 1)

        self.horizontalSpacerSystemVideo_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_2, 4, 4, 1, 1)

        self.frameSystemVideoDown = QFrame(self.gridSystemVideo)
        self.frameSystemVideoDown.setObjectName(u"frameSystemVideoDown")
        sizePolicy9.setHeightForWidth(self.frameSystemVideoDown.sizePolicy().hasHeightForWidth())
        self.frameSystemVideoDown.setSizePolicy(sizePolicy9)
        self.frameSystemVideoDown.setMinimumSize(QSize(60, 0))
        self.frameSystemVideoDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemVideoDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_29 = QVBoxLayout(self.frameSystemVideoDown)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacerSystemVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownTop)

        self.buttonSystemVideoStandardUp = QPushButton(self.frameSystemVideoDown)
        self.buttonSystemVideoStandardUp.setObjectName(u"buttonSystemVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardUp.setFont(font5)
        self.buttonSystemVideoStandardUp.setIcon(icon12)

        self.verticalLayout_29.addWidget(self.buttonSystemVideoStandardUp)

        self.buttonSystemVideoStandardDown = QPushButton(self.frameSystemVideoDown)
        self.buttonSystemVideoStandardDown.setObjectName(u"buttonSystemVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardDown.setFont(font5)
        self.buttonSystemVideoStandardDown.setIcon(icon13)

        self.verticalLayout_29.addWidget(self.buttonSystemVideoStandardDown)

        self.verticalSpacerSystemVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownBottom)

        self.verticalSpacerSystemVideoUpDownBuffer = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownBuffer)


        self.gridLayoutSystemVideo.addWidget(self.frameSystemVideoDown, 4, 1, 1, 1)

        self.lineSystemVideoStandardsSeparator = QFrame(self.gridSystemVideo)
        self.lineSystemVideoStandardsSeparator.setObjectName(u"lineSystemVideoStandardsSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemVideoStandardsSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemVideoStandardsSeparator.setSizePolicy(sizePolicy3)
        palette20 = QPalette()
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemVideoStandardsSeparator.setPalette(palette20)
        self.lineSystemVideoStandardsSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemVideoStandardsSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutSystemVideo.addWidget(self.lineSystemVideoStandardsSeparator, 1, 0, 1, 5)

        self.frameSystemVideoHeader = QFrame(self.gridSystemVideo)
        self.frameSystemVideoHeader.setObjectName(u"frameSystemVideoHeader")
        self.frameSystemVideoHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemVideoHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemVideoHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemVideoHeader.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameSystemVideoHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByVideo = QLabel(self.frameSystemVideoHeader)
        self.labelSystemFilterByVideo.setObjectName(u"labelSystemFilterByVideo")
        sizePolicy8.setHeightForWidth(self.labelSystemFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByVideo.setSizePolicy(sizePolicy8)
        self.labelSystemFilterByVideo.setMinimumSize(QSize(0, 20))
        self.labelSystemFilterByVideo.setFont(font3)
        self.labelSystemFilterByVideo.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.labelSystemFilterByVideo)

        self.checkBoxSystemOverrideVideo = QCheckBox(self.frameSystemVideoHeader)
        self.checkBoxSystemOverrideVideo.setObjectName(u"checkBoxSystemOverrideVideo")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideVideo.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideVideo.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.checkBoxSystemOverrideVideo)


        self.gridLayoutSystemVideo.addWidget(self.frameSystemVideoHeader, 0, 0, 1, 5)

        self.listWidgetSystemVideoStandards = CustomListSelfDrag(self.gridSystemVideo)
        self.listWidgetSystemVideoStandards.setObjectName(u"listWidgetSystemVideoStandards")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemVideoStandards.setSizePolicy(sizePolicy7)
        self.listWidgetSystemVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemVideoStandards.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemVideoStandards.setTabKeyNavigation(True)
        self.listWidgetSystemVideoStandards.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemVideoStandards.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemVideoStandards.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemVideoStandards.setAlternatingRowColors(False)
        self.listWidgetSystemVideoStandards.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutSystemVideo.addWidget(self.listWidgetSystemVideoStandards, 4, 0, 1, 1)

        self.horizontalSpacerSystemVideo_1 = QSpacerItem(220, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_1, 4, 2, 1, 1)

        self.labelSystemVideoStandardsOrder = QLabel(self.gridSystemVideo)
        self.labelSystemVideoStandardsOrder.setObjectName(u"labelSystemVideoStandardsOrder")
        sizePolicy8.setHeightForWidth(self.labelSystemVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelSystemVideoStandardsOrder.setSizePolicy(sizePolicy8)
        self.labelSystemVideoStandardsOrder.setFont(font)
        self.labelSystemVideoStandardsOrder.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemVideo.addWidget(self.labelSystemVideoStandardsOrder, 2, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.gridSystemVideo)

        self.tabWidgetSystemSettings.addTab(self.tabSystemVideo, "")
        self.tabSystemExclusions = QWidget()
        self.tabSystemExclusions.setObjectName(u"tabSystemExclusions")
        self.verticalLayout_21 = QVBoxLayout(self.tabSystemExclusions)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridSystemExclusions = QWidget(self.tabSystemExclusions)
        self.gridSystemExclusions.setObjectName(u"gridSystemExclusions")
        self.gridLayoutSystemExclusions = QGridLayout(self.gridSystemExclusions)
        self.gridLayoutSystemExclusions.setObjectName(u"gridLayoutSystemExclusions")
        self.gridLayoutSystemExclusions.setContentsMargins(1, 0, 0, 0)
        self.checkBoxSystemExcludeEducational = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeEducational.setObjectName(u"checkBoxSystemExcludeEducational")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeEducational, 10, 0, 1, 1)

        self.checkBoxSystemExcludeDemos = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeDemos.setObjectName(u"checkBoxSystemExcludeDemos")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeDemos, 9, 0, 1, 1)

        self.lineSystemExclude = QFrame(self.gridSystemExclusions)
        self.lineSystemExclude.setObjectName(u"lineSystemExclude")
        palette21 = QPalette()
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemExclude.setPalette(palette21)
        self.lineSystemExclude.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemExclude.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutSystemExclusions.addWidget(self.lineSystemExclude, 1, 0, 1, 6)

        self.checkBoxSystemExcludeBadDumps = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBadDumps.setObjectName(u"checkBoxSystemExcludeBadDumps")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBadDumps, 5, 0, 1, 1)

        self.checkBoxSystemExcludeCoverdiscs = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeCoverdiscs.setObjectName(u"checkBoxSystemExcludeCoverdiscs")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeCoverdiscs, 8, 0, 1, 1)

        self.checkBoxSystemExcludeAudio = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeAudio.setObjectName(u"checkBoxSystemExcludeAudio")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeAudio, 4, 0, 1, 1)

        self.verticalSpacerSystemExclude_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutSystemExclusions.addItem(self.verticalSpacerSystemExclude_2, 12, 0, 1, 1)

        self.horizontalSpacerSystemExclude_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_2, 2, 5, 1, 1)

        self.checkBoxSystemExcludeBonusDiscs = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBonusDiscs.setObjectName(u"checkBoxSystemExcludeBonusDiscs")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBonusDiscs, 7, 0, 1, 1)

        self.horizontalSpacerSystemExclude_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_3, 6, 1, 1, 1)

        self.checkBoxSystemExcludeApplications = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeApplications.setObjectName(u"checkBoxSystemExcludeApplications")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeApplications, 3, 0, 1, 1)

        self.checkBoxSystemExcludeAddOns = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeAddOns.setObjectName(u"checkBoxSystemExcludeAddOns")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeAddOns, 2, 0, 1, 1)

        self.checkBoxSystemExcludeBIOS = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBIOS.setObjectName(u"checkBoxSystemExcludeBIOS")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBIOS, 6, 0, 1, 1)

        self.frameSystemExcludeHeader = QFrame(self.gridSystemExclusions)
        self.frameSystemExcludeHeader.setObjectName(u"frameSystemExcludeHeader")
        self.frameSystemExcludeHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemExcludeHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemExcludeHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemExcludeHeader.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frameSystemExcludeHeader)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalExclude_2 = QLabel(self.frameSystemExcludeHeader)
        self.labelGlobalExclude_2.setObjectName(u"labelGlobalExclude_2")
        self.labelGlobalExclude_2.setMinimumSize(QSize(0, 20))
        self.labelGlobalExclude_2.setFont(font3)
        self.labelGlobalExclude_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_4.addWidget(self.labelGlobalExclude_2)

        self.checkBoxSystemOverrideExclusions = QCheckBox(self.frameSystemExcludeHeader)
        self.checkBoxSystemOverrideExclusions.setObjectName(u"checkBoxSystemOverrideExclusions")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideExclusions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideExclusions.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.checkBoxSystemOverrideExclusions)


        self.gridLayoutSystemExclusions.addWidget(self.frameSystemExcludeHeader, 0, 0, 1, 6)

        self.frameSystemExcludeSelectButtons = QFrame(self.gridSystemExclusions)
        self.frameSystemExcludeSelectButtons.setObjectName(u"frameSystemExcludeSelectButtons")
        sizePolicy7.setHeightForWidth(self.frameSystemExcludeSelectButtons.sizePolicy().hasHeightForWidth())
        self.frameSystemExcludeSelectButtons.setSizePolicy(sizePolicy7)
        self.frameSystemExcludeSelectButtons.setMinimumSize(QSize(120, 80))
        self.frameSystemExcludeSelectButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemExcludeSelectButtons.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemExcludeSelectButtons.setLineWidth(0)
        self.verticalLayout_20 = QVBoxLayout(self.frameSystemExcludeSelectButtons)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.buttonSystemSelectAllExclude = QPushButton(self.frameSystemExcludeSelectButtons)
        self.buttonSystemSelectAllExclude.setObjectName(u"buttonSystemSelectAllExclude")
        self.buttonSystemSelectAllExclude.setMinimumSize(QSize(0, 30))

        self.verticalLayout_20.addWidget(self.buttonSystemSelectAllExclude)

        self.buttonSystemDeselectAllExclude = QPushButton(self.frameSystemExcludeSelectButtons)
        self.buttonSystemDeselectAllExclude.setObjectName(u"buttonSystemDeselectAllExclude")
        self.buttonSystemDeselectAllExclude.setMinimumSize(QSize(0, 30))

        self.verticalLayout_20.addWidget(self.buttonSystemDeselectAllExclude)

        self.verticalSpacerSystemExclude_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacerSystemExclude_1)


        self.gridLayoutSystemExclusions.addWidget(self.frameSystemExcludeSelectButtons, 2, 4, 4, 1)

        self.horizontalSpacerSystemExclude_1 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_1, 6, 3, 1, 1)

        self.checkBoxSystemExcludeGames = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeGames.setObjectName(u"checkBoxSystemExcludeGames")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeGames, 11, 0, 1, 1)

        self.checkBoxSystemExcludeManuals = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeManuals.setObjectName(u"checkBoxSystemExcludeManuals")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeManuals, 2, 2, 1, 1)

        self.checkBoxSystemExcludeMIA = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeMIA.setObjectName(u"checkBoxSystemExcludeMIA")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeMIA, 3, 2, 1, 1)

        self.checkBoxSystemExcludeMultimedia = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeMultimedia.setObjectName(u"checkBoxSystemExcludeMultimedia")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeMultimedia, 4, 2, 1, 1)

        self.checkBoxSystemExcludePreproduction = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePreproduction.setObjectName(u"checkBoxSystemExcludePreproduction")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludePreproduction, 5, 2, 1, 1)

        self.checkBoxSystemExcludePromotional = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePromotional.setObjectName(u"checkBoxSystemExcludePromotional")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludePromotional, 6, 2, 1, 1)

        self.checkBoxSystemExcludeUnlicensedAll = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeUnlicensedAll.setObjectName(u"checkBoxSystemExcludeUnlicensedAll")
        self.checkBoxSystemExcludeUnlicensedAll.setTristate(False)

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeUnlicensedAll, 7, 2, 1, 1)

        self.checkBoxSystemExcludeVideo = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeVideo.setObjectName(u"checkBoxSystemExcludeVideo")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeVideo, 11, 2, 1, 1)

        self.frameSystemUnlicensedSubOptionsAftermarket = QHBoxLayout()
        self.frameSystemUnlicensedSubOptionsAftermarket.setObjectName(u"frameSystemUnlicensedSubOptionsAftermarket")
        self.unlicensedSystemSubOptionsSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameSystemUnlicensedSubOptionsAftermarket.addItem(self.unlicensedSystemSubOptionsSpacer)

        self.checkBoxSystemExcludeAftermarket = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeAftermarket.setObjectName(u"checkBoxSystemExcludeAftermarket")

        self.frameSystemUnlicensedSubOptionsAftermarket.addWidget(self.checkBoxSystemExcludeAftermarket)


        self.gridLayoutSystemExclusions.addLayout(self.frameSystemUnlicensedSubOptionsAftermarket, 8, 2, 1, 1)

        self.frameSystemUnlicensedSubOptionsPirate = QHBoxLayout()
        self.frameSystemUnlicensedSubOptionsPirate.setObjectName(u"frameSystemUnlicensedSubOptionsPirate")
        self.unlicensedsystemSubOptionsSpacerPirate = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameSystemUnlicensedSubOptionsPirate.addItem(self.unlicensedsystemSubOptionsSpacerPirate)

        self.checkBoxSystemExcludePirate = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePirate.setObjectName(u"checkBoxSystemExcludePirate")

        self.frameSystemUnlicensedSubOptionsPirate.addWidget(self.checkBoxSystemExcludePirate)


        self.gridLayoutSystemExclusions.addLayout(self.frameSystemUnlicensedSubOptionsPirate, 9, 2, 1, 1)

        self.frameSystemUnlicensedSubOptionsUnlicensed = QHBoxLayout()
        self.frameSystemUnlicensedSubOptionsUnlicensed.setObjectName(u"frameSystemUnlicensedSubOptionsUnlicensed")
        self.unlicensedSystemSubOptionsSpacerUnlicensed = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.frameSystemUnlicensedSubOptionsUnlicensed.addItem(self.unlicensedSystemSubOptionsSpacerUnlicensed)

        self.checkBoxSystemExcludeUnlicensed = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeUnlicensed.setObjectName(u"checkBoxSystemExcludeUnlicensed")

        self.frameSystemUnlicensedSubOptionsUnlicensed.addWidget(self.checkBoxSystemExcludeUnlicensed)


        self.gridLayoutSystemExclusions.addLayout(self.frameSystemUnlicensedSubOptionsUnlicensed, 10, 2, 1, 1)


        self.verticalLayout_21.addWidget(self.gridSystemExclusions)

        self.tabWidgetSystemSettings.addTab(self.tabSystemExclusions, "")
        self.tabSystemLocalization = QWidget()
        self.tabSystemLocalization.setObjectName(u"tabSystemLocalization")
        self.gridLayout_6 = QGridLayout(self.tabSystemLocalization)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridSystemLocalization = QWidget(self.tabSystemLocalization)
        self.gridSystemLocalization.setObjectName(u"gridSystemLocalization")
        self.gridLayoutGlobalLanguages_3 = QGridLayout(self.gridSystemLocalization)
        self.gridLayoutGlobalLanguages_3.setObjectName(u"gridLayoutGlobalLanguages_3")
        self.gridLayoutGlobalLanguages_3.setContentsMargins(1, 0, 0, 0)
        self.frameSystemLocalizationLeftRight = QFrame(self.gridSystemLocalization)
        self.frameSystemLocalizationLeftRight.setObjectName(u"frameSystemLocalizationLeftRight")
        sizePolicy9.setHeightForWidth(self.frameSystemLocalizationLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemLocalizationLeftRight.setSizePolicy(sizePolicy9)
        self.frameSystemLocalizationLeftRight.setMinimumSize(QSize(60, 0))
        self.frameSystemLocalizationLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalizationLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_33 = QVBoxLayout(self.frameSystemLocalizationLeftRight)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacerSystemLocalizationLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacerSystemLocalizationLeftRightTop)

        self.buttonSystemLocalizationAllRight = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationAllRight.setObjectName(u"buttonSystemLocalizationAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllRight.setFont(font5)
        self.buttonSystemLocalizationAllRight.setIcon(icon8)
        self.buttonSystemLocalizationAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_33.addWidget(self.buttonSystemLocalizationAllRight)

        self.buttonSystemLocalizationRight = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationRight.setObjectName(u"buttonSystemLocalizationRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationRight.setFont(font5)
        self.buttonSystemLocalizationRight.setIcon(icon9)
        self.buttonSystemLocalizationRight.setIconSize(QSize(16, 16))

        self.verticalLayout_33.addWidget(self.buttonSystemLocalizationRight)

        self.buttonSystemLocalizationLeft = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationLeft.setObjectName(u"buttonSystemLocalizationLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationLeft.setFont(font5)
        self.buttonSystemLocalizationLeft.setIcon(icon10)

        self.verticalLayout_33.addWidget(self.buttonSystemLocalizationLeft)

        self.buttonSystemLocalizationAllLeft = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationAllLeft.setObjectName(u"buttonSystemLocalizationAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllLeft.setFont(font5)
        self.buttonSystemLocalizationAllLeft.setIcon(icon11)
        self.buttonSystemLocalizationAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_33.addWidget(self.buttonSystemLocalizationAllLeft)

        self.verticalSpacerSystemLocalizationLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacerSystemLocalizationLeftRightBottom)


        self.gridLayoutGlobalLanguages_3.addWidget(self.frameSystemLocalizationLeftRight, 5, 1, 1, 1)

        self.frameSystemLocalizationUpDown = QFrame(self.gridSystemLocalization)
        self.frameSystemLocalizationUpDown.setObjectName(u"frameSystemLocalizationUpDown")
        sizePolicy9.setHeightForWidth(self.frameSystemLocalizationUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemLocalizationUpDown.setSizePolicy(sizePolicy9)
        self.frameSystemLocalizationUpDown.setMinimumSize(QSize(60, 0))
        self.frameSystemLocalizationUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalizationUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_34 = QVBoxLayout(self.frameSystemLocalizationUpDown)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalSpacerSystemLocalizationDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacerSystemLocalizationDownTop)

        self.buttonSystemLocalizationUp = QPushButton(self.frameSystemLocalizationUpDown)
        self.buttonSystemLocalizationUp.setObjectName(u"buttonSystemLocalizationUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationUp.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationUp.setFont(font5)
        self.buttonSystemLocalizationUp.setIcon(icon12)

        self.verticalLayout_34.addWidget(self.buttonSystemLocalizationUp)

        self.buttonSystemLocalizationDown = QPushButton(self.frameSystemLocalizationUpDown)
        self.buttonSystemLocalizationDown.setObjectName(u"buttonSystemLocalizationDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationDown.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationDown.setFont(font5)
        self.buttonSystemLocalizationDown.setIcon(icon13)

        self.verticalLayout_34.addWidget(self.buttonSystemLocalizationDown)

        self.verticalSpacerSystemLocalizationUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacerSystemLocalizationUpDownBottom)


        self.gridLayoutGlobalLanguages_3.addWidget(self.frameSystemLocalizationUpDown, 5, 3, 1, 1)

        self.labelSystemLocalizeNames = QLabel(self.gridSystemLocalization)
        self.labelSystemLocalizeNames.setObjectName(u"labelSystemLocalizeNames")
        self.labelSystemLocalizeNames.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemLocalizeNames.setWordWrap(True)
        self.labelSystemLocalizeNames.setOpenExternalLinks(True)
        self.labelSystemLocalizeNames.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutGlobalLanguages_3.addWidget(self.labelSystemLocalizeNames, 2, 0, 1, 5)

        self.lineSystemLocalizationSeparator = QFrame(self.gridSystemLocalization)
        self.lineSystemLocalizationSeparator.setObjectName(u"lineSystemLocalizationSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemLocalizationSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemLocalizationSeparator.setSizePolicy(sizePolicy3)
        palette22 = QPalette()
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemLocalizationSeparator.setPalette(palette22)
        self.lineSystemLocalizationSeparator.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemLocalizationSeparator.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalLanguages_3.addWidget(self.lineSystemLocalizationSeparator, 1, 0, 1, 5)

        self.verticalSpacerSystemLocalizationList = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalLanguages_3.addItem(self.verticalSpacerSystemLocalizationList, 3, 0, 1, 4)

        self.listWidgetSystemLocalizationAvailableLanguages = CustomList(self.gridSystemLocalization)
        self.listWidgetSystemLocalizationAvailableLanguages.setObjectName(u"listWidgetSystemLocalizationAvailableLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemLocalizationAvailableLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetSystemLocalizationAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemLocalizationAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemLocalizationAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemLocalizationAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemLocalizationAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemLocalizationAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemLocalizationAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemLocalizationAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemLocalizationAvailableLanguages.setSortingEnabled(True)

        self.gridLayoutGlobalLanguages_3.addWidget(self.listWidgetSystemLocalizationAvailableLanguages, 5, 0, 1, 1)

        self.labelSystemLocalizationSelectedLanguages = QLabel(self.gridSystemLocalization)
        self.labelSystemLocalizationSelectedLanguages.setObjectName(u"labelSystemLocalizationSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemLocalizationSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemLocalizationSelectedLanguages.setFont(font)
        self.labelSystemLocalizationSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages_3.addWidget(self.labelSystemLocalizationSelectedLanguages, 4, 2, 1, 1)

        self.listWidgetSystemLocalizationSelectedLanguages = CustomListSelfDrag(self.gridSystemLocalization)
        self.listWidgetSystemLocalizationSelectedLanguages.setObjectName(u"listWidgetSystemLocalizationSelectedLanguages")
        sizePolicy7.setHeightForWidth(self.listWidgetSystemLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemLocalizationSelectedLanguages.setSizePolicy(sizePolicy7)
        self.listWidgetSystemLocalizationSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemLocalizationSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemLocalizationSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemLocalizationSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemLocalizationSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemLocalizationSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemLocalizationSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemLocalizationSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayoutGlobalLanguages_3.addWidget(self.listWidgetSystemLocalizationSelectedLanguages, 5, 2, 1, 1)

        self.labelSystemLocalizationAvailableLanguages = QLabel(self.gridSystemLocalization)
        self.labelSystemLocalizationAvailableLanguages.setObjectName(u"labelSystemLocalizationAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemLocalizationAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemLocalizationAvailableLanguages.setFont(font)
        self.labelSystemLocalizationAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalLanguages_3.addWidget(self.labelSystemLocalizationAvailableLanguages, 4, 0, 1, 1)

        self.horizontalSpacerSystemLocalization = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutGlobalLanguages_3.addItem(self.horizontalSpacerSystemLocalization, 5, 4, 1, 1)


        self.gridLayout_6.addWidget(self.gridSystemLocalization, 1, 0, 1, 1)

        self.frameSystemLocalizationHeader = QFrame(self.tabSystemLocalization)
        self.frameSystemLocalizationHeader.setObjectName(u"frameSystemLocalizationHeader")
        sizePolicy13.setHeightForWidth(self.frameSystemLocalizationHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemLocalizationHeader.setSizePolicy(sizePolicy13)
        self.frameSystemLocalizationHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemLocalizationHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalizationHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLocalizationHeader.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frameSystemLocalizationHeader)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelSystemUseLocalNames = QLabel(self.frameSystemLocalizationHeader)
        self.labelSystemUseLocalNames.setObjectName(u"labelSystemUseLocalNames")
        sizePolicy8.setHeightForWidth(self.labelSystemUseLocalNames.sizePolicy().hasHeightForWidth())
        self.labelSystemUseLocalNames.setSizePolicy(sizePolicy8)
        self.labelSystemUseLocalNames.setMinimumSize(QSize(0, 0))
        self.labelSystemUseLocalNames.setFont(font3)
        self.labelSystemUseLocalNames.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_7.addWidget(self.labelSystemUseLocalNames)

        self.checkBoxSystemOverrideLocalization = QCheckBox(self.frameSystemLocalizationHeader)
        self.checkBoxSystemOverrideLocalization.setObjectName(u"checkBoxSystemOverrideLocalization")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideLocalization.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideLocalization.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.checkBoxSystemOverrideLocalization)


        self.gridLayout_6.addWidget(self.frameSystemLocalizationHeader, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemLocalization, "")
        self.tabSystemOverrides = QWidget()
        self.tabSystemOverrides.setObjectName(u"tabSystemOverrides")
        self.verticalLayout_4 = QVBoxLayout(self.tabSystemOverrides)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, 9)
        self.scrollAreaSystemOverrides = QScrollArea(self.tabSystemOverrides)
        self.scrollAreaSystemOverrides.setObjectName(u"scrollAreaSystemOverrides")
        self.scrollAreaSystemOverrides.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaSystemOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemOverrides.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemOverrides.setWidgetResizable(True)
        self.scrollAreaSystemOverrides.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsSystemOverrides = QWidget()
        self.scrollAreaWidgetContentsSystemOverrides.setObjectName(u"scrollAreaWidgetContentsSystemOverrides")
        self.scrollAreaWidgetContentsSystemOverrides.setGeometry(QRect(0, 0, 590, 396))
        self.scrollAreaWidgetContentsSystemOverrides.setMinimumSize(QSize(0, 0))
        self.gridLayoutSystemUserFilters = QGridLayout(self.scrollAreaWidgetContentsSystemOverrides)
        self.gridLayoutSystemUserFilters.setObjectName(u"gridLayoutSystemUserFilters")
        self.gridLayoutSystemUserFilters.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayoutSystemUserFilters.setContentsMargins(1, 0, 0, 0)
        self.textEditSystemInclude = CustomTextEdit(self.scrollAreaWidgetContentsSystemOverrides)
        self.textEditSystemInclude.setObjectName(u"textEditSystemInclude")
        sizePolicy.setHeightForWidth(self.textEditSystemInclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemInclude.setSizePolicy(sizePolicy)
        self.textEditSystemInclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemInclude.setTabChangesFocus(True)
        self.textEditSystemInclude.setAcceptRichText(False)

        self.gridLayoutSystemUserFilters.addWidget(self.textEditSystemInclude, 5, 0, 1, 1)

        self.horizontalSpacerSystemOverrides = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayoutSystemUserFilters.addItem(self.horizontalSpacerSystemOverrides, 5, 1, 1, 1)

        self.lineSystemOverrideByText = QFrame(self.scrollAreaWidgetContentsSystemOverrides)
        self.lineSystemOverrideByText.setObjectName(u"lineSystemOverrideByText")
        palette23 = QPalette()
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemOverrideByText.setPalette(palette23)
        self.lineSystemOverrideByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemOverrideByText.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutSystemUserFilters.addWidget(self.lineSystemOverrideByText, 1, 0, 1, 3)

        self.verticalSpacerSystemOverrides = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutSystemUserFilters.addItem(self.verticalSpacerSystemOverrides, 3, 0, 1, 3)

        self.labelSystemOverrideInclude = QLabel(self.scrollAreaWidgetContentsSystemOverrides)
        self.labelSystemOverrideInclude.setObjectName(u"labelSystemOverrideInclude")
        sizePolicy8.setHeightForWidth(self.labelSystemOverrideInclude.sizePolicy().hasHeightForWidth())
        self.labelSystemOverrideInclude.setSizePolicy(sizePolicy8)
        self.labelSystemOverrideInclude.setFont(font6)
        self.labelSystemOverrideInclude.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSystemOverrideInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemOverrideInclude, 4, 0, 1, 1)

        self.labelSystemOverrideExclude = QLabel(self.scrollAreaWidgetContentsSystemOverrides)
        self.labelSystemOverrideExclude.setObjectName(u"labelSystemOverrideExclude")
        sizePolicy3.setHeightForWidth(self.labelSystemOverrideExclude.sizePolicy().hasHeightForWidth())
        self.labelSystemOverrideExclude.setSizePolicy(sizePolicy3)
        self.labelSystemOverrideExclude.setMinimumSize(QSize(0, 0))
        self.labelSystemOverrideExclude.setFont(font6)
        self.labelSystemOverrideExclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemOverrideExclude, 4, 2, 1, 1)

        self.labelSystemOverrideByText = QLabel(self.scrollAreaWidgetContentsSystemOverrides)
        self.labelSystemOverrideByText.setObjectName(u"labelSystemOverrideByText")
        self.labelSystemOverrideByText.setMinimumSize(QSize(0, 20))
        self.labelSystemOverrideByText.setFont(font3)
        self.labelSystemOverrideByText.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemOverrideByText, 0, 0, 1, 3)

        self.labelSystemOverride = QLabel(self.scrollAreaWidgetContentsSystemOverrides)
        self.labelSystemOverride.setObjectName(u"labelSystemOverride")
        self.labelSystemOverride.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemOverride.setWordWrap(True)
        self.labelSystemOverride.setOpenExternalLinks(True)
        self.labelSystemOverride.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemOverride, 2, 0, 1, 3)

        self.textEditSystemExclude = CustomTextEdit(self.scrollAreaWidgetContentsSystemOverrides)
        self.textEditSystemExclude.setObjectName(u"textEditSystemExclude")
        sizePolicy.setHeightForWidth(self.textEditSystemExclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemExclude.setSizePolicy(sizePolicy)
        self.textEditSystemExclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemExclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemExclude.setTabChangesFocus(True)
        self.textEditSystemExclude.setAcceptRichText(False)

        self.gridLayoutSystemUserFilters.addWidget(self.textEditSystemExclude, 5, 2, 1, 1)

        self.scrollAreaSystemOverrides.setWidget(self.scrollAreaWidgetContentsSystemOverrides)

        self.verticalLayout_4.addWidget(self.scrollAreaSystemOverrides)

        self.tabWidgetSystemSettings.addTab(self.tabSystemOverrides, "")
        self.tabSystemPostFilter = QWidget()
        self.tabSystemPostFilter.setObjectName(u"tabSystemPostFilter")
        sizePolicy8.setHeightForWidth(self.tabSystemPostFilter.sizePolicy().hasHeightForWidth())
        self.tabSystemPostFilter.setSizePolicy(sizePolicy8)
        self.verticalLayout_30 = QVBoxLayout(self.tabSystemPostFilter)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.scrollAreaSystemPostFilters = QScrollArea(self.tabSystemPostFilter)
        self.scrollAreaSystemPostFilters.setObjectName(u"scrollAreaSystemPostFilters")
        self.scrollAreaSystemPostFilters.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaSystemPostFilters.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemPostFilters.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemPostFilters.setLineWidth(0)
        self.scrollAreaSystemPostFilters.setMidLineWidth(0)
        self.scrollAreaSystemPostFilters.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemPostFilters.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollAreaSystemPostFilters.setWidgetResizable(True)
        self.scrollAreaSystemPostFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContentsSystemPostFilters = QWidget()
        self.scrollAreaWidgetContentsSystemPostFilters.setObjectName(u"scrollAreaWidgetContentsSystemPostFilters")
        self.scrollAreaWidgetContentsSystemPostFilters.setGeometry(QRect(0, 0, 590, 396))
        sizePolicy8.setHeightForWidth(self.scrollAreaWidgetContentsSystemPostFilters.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemPostFilters.setSizePolicy(sizePolicy8)
        self.gridLayoutGlobalUserFilters_4 = QGridLayout(self.scrollAreaWidgetContentsSystemPostFilters)
        self.gridLayoutGlobalUserFilters_4.setObjectName(u"gridLayoutGlobalUserFilters_4")
        self.gridLayoutGlobalUserFilters_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayoutGlobalUserFilters_4.setContentsMargins(1, 0, 0, 0)
        self.labelSystemFilters = QLabel(self.scrollAreaWidgetContentsSystemPostFilters)
        self.labelSystemFilters.setObjectName(u"labelSystemFilters")
        self.labelSystemFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemFilters.setWordWrap(True)
        self.labelSystemFilters.setOpenExternalLinks(True)
        self.labelSystemFilters.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.gridLayoutGlobalUserFilters_4.addWidget(self.labelSystemFilters, 2, 0, 1, 2)

        self.textEditSystemFilterInclude = CustomTextEdit(self.scrollAreaWidgetContentsSystemPostFilters)
        self.textEditSystemFilterInclude.setObjectName(u"textEditSystemFilterInclude")
        self.textEditSystemFilterInclude.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.textEditSystemFilterInclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemFilterInclude.setSizePolicy(sizePolicy10)
        self.textEditSystemFilterInclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemFilterInclude.setMaximumSize(QSize(16777211, 16777215))
        self.textEditSystemFilterInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemFilterInclude.setTabChangesFocus(True)
        self.textEditSystemFilterInclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters_4.addWidget(self.textEditSystemFilterInclude, 5, 0, 1, 2)

        self.lineSystemFilterByText = QFrame(self.scrollAreaWidgetContentsSystemPostFilters)
        self.lineSystemFilterByText.setObjectName(u"lineSystemFilterByText")
        palette24 = QPalette()
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemFilterByText.setPalette(palette24)
        self.lineSystemFilterByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemFilterByText.setFrameShape(QFrame.Shape.HLine)

        self.gridLayoutGlobalUserFilters_4.addWidget(self.lineSystemFilterByText, 1, 0, 1, 2)

        self.verticalSpacerSystemFilters = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayoutGlobalUserFilters_4.addItem(self.verticalSpacerSystemFilters, 3, 0, 1, 2)

        self.labelSystemFilterInclude = QLabel(self.scrollAreaWidgetContentsSystemPostFilters)
        self.labelSystemFilterInclude.setObjectName(u"labelSystemFilterInclude")
        sizePolicy8.setHeightForWidth(self.labelSystemFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterInclude.setSizePolicy(sizePolicy8)
        self.labelSystemFilterInclude.setFont(font6)
        self.labelSystemFilterInclude.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSystemFilterInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayoutGlobalUserFilters_4.addWidget(self.labelSystemFilterInclude, 4, 0, 1, 1)

        self.FrameSystemPostFilterHeader = QFrame(self.scrollAreaWidgetContentsSystemPostFilters)
        self.FrameSystemPostFilterHeader.setObjectName(u"FrameSystemPostFilterHeader")
        sizePolicy5.setHeightForWidth(self.FrameSystemPostFilterHeader.sizePolicy().hasHeightForWidth())
        self.FrameSystemPostFilterHeader.setSizePolicy(sizePolicy5)
        self.FrameSystemPostFilterHeader.setMinimumSize(QSize(0, 20))
        self.FrameSystemPostFilterHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.FrameSystemPostFilterHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.FrameSystemPostFilterHeader.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.FrameSystemPostFilterHeader)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelSystemlFilterByText = QLabel(self.FrameSystemPostFilterHeader)
        self.labelSystemlFilterByText.setObjectName(u"labelSystemlFilterByText")
        self.labelSystemlFilterByText.setMinimumSize(QSize(0, 20))
        self.labelSystemlFilterByText.setFont(font3)
        self.labelSystemlFilterByText.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_5.addWidget(self.labelSystemlFilterByText)

        self.checkBoxSystemOverridePostFilter = QCheckBox(self.FrameSystemPostFilterHeader)
        self.checkBoxSystemOverridePostFilter.setObjectName(u"checkBoxSystemOverridePostFilter")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverridePostFilter.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverridePostFilter.setSizePolicy(sizePolicy6)

        self.horizontalLayout_5.addWidget(self.checkBoxSystemOverridePostFilter)


        self.gridLayoutGlobalUserFilters_4.addWidget(self.FrameSystemPostFilterHeader, 0, 0, 1, 2)

        self.scrollAreaSystemPostFilters.setWidget(self.scrollAreaWidgetContentsSystemPostFilters)

        self.verticalLayout_30.addWidget(self.scrollAreaSystemPostFilters)

        self.tabWidgetSystemSettings.addTab(self.tabSystemPostFilter, "")
        self.tabSystemOptions = QWidget()
        self.tabSystemOptions.setObjectName(u"tabSystemOptions")
        self.verticalLayout_3 = QVBoxLayout(self.tabSystemOptions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, 0)
        self.frameSystemOptionsHeader = QFrame(self.tabSystemOptions)
        self.frameSystemOptionsHeader.setObjectName(u"frameSystemOptionsHeader")
        sizePolicy3.setHeightForWidth(self.frameSystemOptionsHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemOptionsHeader.setSizePolicy(sizePolicy3)
        self.frameSystemOptionsHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemOptionsHeader.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemOptionsHeader.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemOptionsHeader.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frameSystemOptionsHeader)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 0, 0, 0)
        self.checkBoxSystemOverrideOptions = QCheckBox(self.frameSystemOptionsHeader)
        self.checkBoxSystemOverrideOptions.setObjectName(u"checkBoxSystemOverrideOptions")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideOptions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideOptions.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.checkBoxSystemOverrideOptions, 0, 1, 1, 1)

        self.labelSystemOptions = QLabel(self.frameSystemOptionsHeader)
        self.labelSystemOptions.setObjectName(u"labelSystemOptions")
        self.labelSystemOptions.setMinimumSize(QSize(0, 20))
        self.labelSystemOptions.setFont(font3)
        self.labelSystemOptions.setScaledContents(False)
        self.labelSystemOptions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.labelSystemOptions, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frameSystemOptionsHeader)

        self.lineSystemOptions = QFrame(self.tabSystemOptions)
        self.lineSystemOptions.setObjectName(u"lineSystemOptions")
        palette25 = QPalette()
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemOptions.setPalette(palette25)
        self.lineSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemOptions.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.lineSystemOptions)

        self.scrollAreaSystemOptions = QScrollArea(self.tabSystemOptions)
        self.scrollAreaSystemOptions.setObjectName(u"scrollAreaSystemOptions")
        sizePolicy8.setHeightForWidth(self.scrollAreaSystemOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaSystemOptions.setSizePolicy(sizePolicy8)
        self.scrollAreaSystemOptions.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollAreaSystemOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemOptions.setLineWidth(0)
        self.scrollAreaSystemOptions.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollAreaSystemOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemOptions.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollAreaSystemOptions.setWidgetResizable(True)
        self.layoutScrollAreaSystemOptions = QWidget()
        self.layoutScrollAreaSystemOptions.setObjectName(u"layoutScrollAreaSystemOptions")
        self.layoutScrollAreaSystemOptions.setGeometry(QRect(0, -614, 573, 1124))
        sizePolicy8.setHeightForWidth(self.layoutScrollAreaSystemOptions.sizePolicy().hasHeightForWidth())
        self.layoutScrollAreaSystemOptions.setSizePolicy(sizePolicy8)
        self.verticalLayout_22 = QVBoxLayout(self.layoutScrollAreaSystemOptions)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 18, 18)
        self.labelSystemOptionsTitle = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsTitle.setObjectName(u"labelSystemOptionsTitle")
        self.labelSystemOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsTitle.setFont(font3)
        self.labelSystemOptionsTitle.setScaledContents(False)
        self.labelSystemOptionsTitle.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsTitle)

        self.checkBoxSystemOptionsDisable1G1R = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisable1G1R.setObjectName(u"checkBoxSystemOptionsDisable1G1R")
        self.checkBoxSystemOptionsDisable1G1R.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDisable1G1R.setFont(font7)
        self.checkBoxSystemOptionsDisable1G1R.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisable1G1R)

        self.checkBoxSystemOptionsPreferRegions = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsPreferRegions.setObjectName(u"checkBoxSystemOptionsPreferRegions")
        self.checkBoxSystemOptionsPreferRegions.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferRegions.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsPreferRegions)

        self.checkBoxSystemOptionsModernPlatforms = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsModernPlatforms.setObjectName(u"checkBoxSystemOptionsModernPlatforms")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsModernPlatforms.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsModernPlatforms.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsModernPlatforms.setFont(font)
        self.checkBoxSystemOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsModernPlatforms)

        self.checkBoxSystemOptionsPreferOldest = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsPreferOldest.setObjectName(u"checkBoxSystemOptionsPreferOldest")
        self.checkBoxSystemOptionsPreferOldest.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferOldest.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsPreferOldest)

        self.checkBoxSystemOptionsDemoteUnlicensed = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDemoteUnlicensed.setObjectName(u"checkBoxSystemOptionsDemoteUnlicensed")
        self.checkBoxSystemOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxSystemOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDemoteUnlicensed)

        self.checkBoxSystemOptionsDisableOverrides = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisableOverrides.setObjectName(u"checkBoxSystemOptionsDisableOverrides")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsDisableOverrides.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsDisableOverrides.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsDisableOverrides.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDisableOverrides.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsDisableOverrides.setFont(font)
        self.checkBoxSystemOptionsDisableOverrides.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisableOverrides)

        self.verticalSpacer_3 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_3)

        self.labelSystemChooseCompilationsMode = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemChooseCompilationsMode.setObjectName(u"labelSystemChooseCompilationsMode")
        self.labelSystemChooseCompilationsMode.setFont(font3)

        self.verticalLayout_22.addWidget(self.labelSystemChooseCompilationsMode)

        self.frameSytemCompilations = QFrame(self.layoutScrollAreaSystemOptions)
        self.frameSytemCompilations.setObjectName(u"frameSytemCompilations")
        sizePolicy8.setHeightForWidth(self.frameSytemCompilations.sizePolicy().hasHeightForWidth())
        self.frameSytemCompilations.setSizePolicy(sizePolicy8)
        self.frameSytemCompilations.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSytemCompilations.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSytemCompilations.setLineWidth(0)
        self.verticalLayout_38 = QVBoxLayout(self.frameSytemCompilations)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.comboBoxSystemChooseCompilationsMode = CustomComboBox(self.frameSytemCompilations)
        self.comboBoxSystemChooseCompilationsMode.addItem("")
        self.comboBoxSystemChooseCompilationsMode.addItem("")
        self.comboBoxSystemChooseCompilationsMode.addItem("")
        self.comboBoxSystemChooseCompilationsMode.addItem("")
        self.comboBoxSystemChooseCompilationsMode.setObjectName(u"comboBoxSystemChooseCompilationsMode")
        sizePolicy6.setHeightForWidth(self.comboBoxSystemChooseCompilationsMode.sizePolicy().hasHeightForWidth())
        self.comboBoxSystemChooseCompilationsMode.setSizePolicy(sizePolicy6)
        self.comboBoxSystemChooseCompilationsMode.setMinimumSize(QSize(256, 24))
        self.comboBoxSystemChooseCompilationsMode.setMaximumSize(QSize(256, 24))
        self.comboBoxSystemChooseCompilationsMode.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.verticalLayout_38.addWidget(self.comboBoxSystemChooseCompilationsMode)

        self.verticalSpacer_4 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_4)

        self.labelSystemCompilationsExplanation = QLabel(self.frameSytemCompilations)
        self.labelSystemCompilationsExplanation.setObjectName(u"labelSystemCompilationsExplanation")
        self.labelSystemCompilationsExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelSystemCompilationsExplanation.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.labelSystemCompilationsExplanation)


        self.verticalLayout_22.addWidget(self.frameSytemCompilations, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacerSystemOptions_1 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_1)

        self.labelSystemOptionsOutput = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsOutput.setObjectName(u"labelSystemOptionsOutput")
        self.labelSystemOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsOutput.setFont(font3)
        self.labelSystemOptionsOutput.setLineWidth(0)
        self.labelSystemOptionsOutput.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsOutput)

        self.checkBoxSystemOptionsAlreadyProcessed = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsAlreadyProcessed.setObjectName(u"checkBoxSystemOptionsAlreadyProcessed")
        self.checkBoxSystemOptionsAlreadyProcessed.setFont(font8)

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsAlreadyProcessed)

        self.checkBoxSystemOptionsOriginalHeader = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsOriginalHeader.setObjectName(u"checkBoxSystemOptionsOriginalHeader")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsOriginalHeader)

        self.checkBoxSystemOptionsUseMachine = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsUseMachine.setObjectName(u"checkBoxSystemOptionsUseMachine")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsUseMachine)

        self.checkBoxSystemOptionsSplitRegions = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsSplitRegions.setObjectName(u"checkBoxSystemOptionsSplitRegions")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsSplitRegions)

        self.checkBoxSystemOptionsRemovesDat = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsRemovesDat.setObjectName(u"checkBoxSystemOptionsRemovesDat")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsRemovesDat)

        self.checkBoxSystemOptionsKeepRemove = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsKeepRemove.setObjectName(u"checkBoxSystemOptionsKeepRemove")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsKeepRemove)

        self.checkBoxSystemOptions1G1RNames = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptions1G1RNames.setObjectName(u"checkBoxSystemOptions1G1RNames")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptions1G1RNames)

        self.frameSystemOptions1G1RPrefix = QFrame(self.layoutScrollAreaSystemOptions)
        self.frameSystemOptions1G1RPrefix.setObjectName(u"frameSystemOptions1G1RPrefix")
        self.frameSystemOptions1G1RPrefix.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameSystemOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameSystemOptions1G1RPrefix.setSizePolicy(sizePolicy8)
        self.frameSystemOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette26 = QPalette()
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        palette26.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette26.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette26.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameSystemOptions1G1RPrefix.setPalette(palette26)
        self.labelSystemOptions1G1RPrefix = QLabel(self.frameSystemOptions1G1RPrefix)
        self.labelSystemOptions1G1RPrefix.setObjectName(u"labelSystemOptions1G1RPrefix")
        self.labelSystemOptions1G1RPrefix.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditSystemOptions1G1RPrefix = CustomLineEdit(self.frameSystemOptions1G1RPrefix)
        self.lineEditSystemOptions1G1RPrefix.setObjectName(u"lineEditSystemOptions1G1RPrefix")
        self.lineEditSystemOptions1G1RPrefix.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditSystemOptions1G1RPrefix.setMinimumSize(QSize(0, 24))
        self.labelSystemOptions1G1RSuffix = QLabel(self.frameSystemOptions1G1RPrefix)
        self.labelSystemOptions1G1RSuffix.setObjectName(u"labelSystemOptions1G1RSuffix")
        self.labelSystemOptions1G1RSuffix.setGeometry(QRect(19, 58, 521, 20))
        self.lineEditSystemOptions1G1RSuffix = CustomLineEdit(self.frameSystemOptions1G1RPrefix)
        self.lineEditSystemOptions1G1RSuffix.setObjectName(u"lineEditSystemOptions1G1RSuffix")
        self.lineEditSystemOptions1G1RSuffix.setGeometry(QRect(20, 83, 521, 24))
        self.lineEditSystemOptions1G1RSuffix.setMinimumSize(QSize(0, 24))

        self.verticalLayout_22.addWidget(self.frameSystemOptions1G1RPrefix)

        self.verticalSpacerSystemOptions_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_2)

        self.labelSystemOptionsOnline = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsOnline.setObjectName(u"labelSystemOptionsOnline")
        self.labelSystemOptionsOnline.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsOnline.setFont(font3)
        self.labelSystemOptionsOnline.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsOnline)

        self.labelSystemOnlineExplanation = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOnlineExplanation.setObjectName(u"labelSystemOnlineExplanation")
        self.labelSystemOnlineExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelSystemOnlineExplanation.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.labelSystemOnlineExplanation)

        self.verticalSpacerSystemOptions_5 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_5)

        self.checkBoxSystemOptionsMIA = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsMIA.setObjectName(u"checkBoxSystemOptionsMIA")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsMIA.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsMIA.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsMIA.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsMIA.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsMIA.setFont(font)
        self.checkBoxSystemOptionsMIA.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsMIA)

        self.checkBoxSystemOptionsRetroAchievements = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsRetroAchievements.setObjectName(u"checkBoxSystemOptionsRetroAchievements")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsRetroAchievements.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsRetroAchievements.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsRetroAchievements.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsRetroAchievements.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsRetroAchievements.setFont(font)
        self.checkBoxSystemOptionsRetroAchievements.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsRetroAchievements)

        self.checkBoxSystemOptionsPreferRetro = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsPreferRetro.setObjectName(u"checkBoxSystemOptionsPreferRetro")
        self.checkBoxSystemOptionsPreferRetro.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferRetro.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsPreferRetro)

        self.verticalSpacerSystemOptions_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_4)

        self.labelSystemOptionsDebug = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsDebug.setObjectName(u"labelSystemOptionsDebug")
        self.labelSystemOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsDebug.setFont(font3)
        self.labelSystemOptionsDebug.setLineWidth(0)
        self.labelSystemOptionsDebug.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsDebug)

        self.checkBoxSystemOptionsReportWarnings = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsReportWarnings.setObjectName(u"checkBoxSystemOptionsReportWarnings")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsReportWarnings)

        self.checkBoxSystemOptionsPauseWarnings = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsPauseWarnings.setObjectName(u"checkBoxSystemOptionsPauseWarnings")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsPauseWarnings)

        self.checkBoxSystemOptionsLegacy = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsLegacy.setObjectName(u"checkBoxSystemOptionsLegacy")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsLegacy)

        self.checkBoxSystemOptionsDisableMultiCPU = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisableMultiCPU.setObjectName(u"checkBoxSystemOptionsDisableMultiCPU")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisableMultiCPU)

        self.checkBoxSystemOptionsTrace = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsTrace.setObjectName(u"checkBoxSystemOptionsTrace")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsTrace)

        self.frameSystemOptionsTrace = QFrame(self.layoutScrollAreaSystemOptions)
        self.frameSystemOptionsTrace.setObjectName(u"frameSystemOptionsTrace")
        self.frameSystemOptionsTrace.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameSystemOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameSystemOptionsTrace.setSizePolicy(sizePolicy8)
        self.frameSystemOptionsTrace.setMinimumSize(QSize(0, 55))
        palette27 = QPalette()
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameSystemOptionsTrace.setPalette(palette27)
        self.labelSystemOptionsTrace = QLabel(self.frameSystemOptionsTrace)
        self.labelSystemOptionsTrace.setObjectName(u"labelSystemOptionsTrace")
        self.labelSystemOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditSystemOptionsTrace = CustomLineEdit(self.frameSystemOptionsTrace)
        self.lineEditSystemOptionsTrace.setObjectName(u"lineEditSystemOptionsTrace")
        self.lineEditSystemOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditSystemOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_22.addWidget(self.frameSystemOptionsTrace)

        self.verticalSpacerSystemOptions_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_3)

        self.scrollAreaSystemOptions.setWidget(self.layoutScrollAreaSystemOptions)

        self.verticalLayout_3.addWidget(self.scrollAreaSystemOptions)

        self.tabWidgetSystemSettings.addTab(self.tabSystemOptions, "")

        self.gridLayout_3.addWidget(self.tabWidgetSystemSettings, 1, 0, 1, 1)

        self.tabWidgetSettings.addTab(self.tabSystemSettings, "")

        self.gridLayoutRight.addWidget(self.tabWidgetSettings, 3, 0, 1, 2)

        self.labelSettingsSaved = QLabel(self.gridLayoutRightSettings)
        self.labelSettingsSaved.setObjectName(u"labelSettingsSaved")
        palette28 = QPalette()
        palette28.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette28.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette28.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette28.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette28.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette28.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSettingsSaved.setPalette(palette28)
        self.labelSettingsSaved.setFont(font8)
        self.labelSettingsSaved.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayoutRight.addWidget(self.labelSettingsSaved, 1, 1, 1, 1)

        self.labelChooseYourSettings = QLabel(self.gridLayoutRightSettings)
        self.labelChooseYourSettings.setObjectName(u"labelChooseYourSettings")
        self.labelChooseYourSettings.setFont(font3)

        self.gridLayoutRight.addWidget(self.labelChooseYourSettings, 1, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutRightSettings)

        self.gridLayout.addWidget(self.splitter, 2, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.overwriteInputDats = QFrame(self.centralwidget)
        self.overwriteInputDats.setObjectName(u"overwriteInputDats")
        sizePolicy12.setHeightForWidth(self.overwriteInputDats.sizePolicy().hasHeightForWidth())
        self.overwriteInputDats.setSizePolicy(sizePolicy12)
        self.overwriteInputDats.setFont(font2)
        self.overwriteInputDats.setFrameShape(QFrame.Shape.NoFrame)
        self.overwriteInputDats.setFrameShadow(QFrame.Shadow.Plain)
        self.overwriteInputDats.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.overwriteInputDats)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, -1, 0)

        self.gridLayout_2.addWidget(self.overwriteInputDats, 3, 0, 1, 1)

        self.frameProcessDatFile = QFrame(self.centralwidget)
        self.frameProcessDatFile.setObjectName(u"frameProcessDatFile")
        sizePolicy12.setHeightForWidth(self.frameProcessDatFile.sizePolicy().hasHeightForWidth())
        self.frameProcessDatFile.setSizePolicy(sizePolicy12)
        self.frameProcessDatFile.setMinimumSize(QSize(0, 0))
        self.frameProcessDatFile.setFrameShape(QFrame.Shape.NoFrame)
        self.frameProcessDatFile.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frameProcessDatFile)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutBottom = QWidget(self.frameProcessDatFile)
        self.horizontalLayoutBottom.setObjectName(u"horizontalLayoutBottom")
        self.horizontalLayoutOutputGo = QHBoxLayout(self.horizontalLayoutBottom)
        self.horizontalLayoutOutputGo.setObjectName(u"horizontalLayoutOutputGo")
        self.horizontalLayoutOutputGo.setContentsMargins(0, 0, 9, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutOutputGo.addItem(self.horizontalSpacer)

        self.buttonGo = CustomPushButton(self.horizontalLayoutBottom)
        self.buttonGo.setObjectName(u"buttonGo")
        sizePolicy6.setHeightForWidth(self.buttonGo.sizePolicy().hasHeightForWidth())
        self.buttonGo.setSizePolicy(sizePolicy6)
        self.buttonGo.setMinimumSize(QSize(130, 41))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(10)
        font9.setBold(False)
        self.buttonGo.setFont(font9)

        self.horizontalLayoutOutputGo.addWidget(self.buttonGo, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_5.addWidget(self.horizontalLayoutBottom)


        self.gridLayout_2.addWidget(self.frameProcessDatFile, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.buttonAddDats, self.buttonAddFolder)
        QWidget.setTabOrder(self.buttonAddFolder, self.buttonAddFolderRecursive)
        QWidget.setTabOrder(self.buttonAddFolderRecursive, self.buttonDeleteDats)
        QWidget.setTabOrder(self.buttonDeleteDats, self.buttonClearDats)
        QWidget.setTabOrder(self.buttonClearDats, self.listWidgetOpenFiles)
        QWidget.setTabOrder(self.listWidgetOpenFiles, self.tabWidgetSettings)
        QWidget.setTabOrder(self.tabWidgetSettings, self.tabWidgetGlobalSettings)
        QWidget.setTabOrder(self.tabWidgetGlobalSettings, self.listWidgetGlobalAvailableRegions)
        QWidget.setTabOrder(self.listWidgetGlobalAvailableRegions, self.buttonGlobalRegionAllRight)
        QWidget.setTabOrder(self.buttonGlobalRegionAllRight, self.buttonGlobalRegionRight)
        QWidget.setTabOrder(self.buttonGlobalRegionRight, self.buttonGlobalRegionLeft)
        QWidget.setTabOrder(self.buttonGlobalRegionLeft, self.buttonGlobalRegionAllLeft)
        QWidget.setTabOrder(self.buttonGlobalRegionAllLeft, self.listWidgetGlobalSelectedRegions)
        QWidget.setTabOrder(self.listWidgetGlobalSelectedRegions, self.buttonGlobalRegionUp)
        QWidget.setTabOrder(self.buttonGlobalRegionUp, self.buttonGlobalRegionDown)
        QWidget.setTabOrder(self.buttonGlobalRegionDown, self.buttonGlobalDefaultRegionOrder)
        QWidget.setTabOrder(self.buttonGlobalDefaultRegionOrder, self.listWidgetGlobalAvailableLanguages)
        QWidget.setTabOrder(self.listWidgetGlobalAvailableLanguages, self.buttonGlobalLanguageAllRight)
        QWidget.setTabOrder(self.buttonGlobalLanguageAllRight, self.buttonGlobalLanguageRight)
        QWidget.setTabOrder(self.buttonGlobalLanguageRight, self.buttonGlobalLanguageLeft)
        QWidget.setTabOrder(self.buttonGlobalLanguageLeft, self.buttonGlobalLanguageAllLeft)
        QWidget.setTabOrder(self.buttonGlobalLanguageAllLeft, self.listWidgetGlobalSelectedLanguages)
        QWidget.setTabOrder(self.listWidgetGlobalSelectedLanguages, self.buttonGlobalLanguageUp)
        QWidget.setTabOrder(self.buttonGlobalLanguageUp, self.buttonGlobalLanguageDown)
        QWidget.setTabOrder(self.buttonGlobalLanguageDown, self.listWidgetGlobalVideoStandards)
        QWidget.setTabOrder(self.listWidgetGlobalVideoStandards, self.buttonGlobalVideoStandardUp)
        QWidget.setTabOrder(self.buttonGlobalVideoStandardUp, self.buttonGlobalVideoStandardDown)
        QWidget.setTabOrder(self.buttonGlobalVideoStandardDown, self.checkBoxGlobalExcludeAddOns)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeAddOns, self.checkBoxGlobalExcludeApplications)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeApplications, self.checkBoxGlobalExcludeAudio)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeAudio, self.checkBoxGlobalExcludeBadDumps)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeBadDumps, self.checkBoxGlobalExcludeBIOS)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeBIOS, self.checkBoxGlobalExcludeBonusDiscs)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeBonusDiscs, self.checkBoxGlobalExcludeCoverdiscs)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeCoverdiscs, self.checkBoxGlobalExcludeDemos)
        QWidget.setTabOrder(self.checkBoxGlobalExcludeDemos, self.buttonGlobalSelectAllExclude)
        QWidget.setTabOrder(self.buttonGlobalSelectAllExclude, self.buttonGlobalDeselectAllExclude)
        QWidget.setTabOrder(self.buttonGlobalDeselectAllExclude, self.checkBoxGlobalOptionsSplitRegions)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsSplitRegions, self.checkBoxGlobalOptionsRemovesDat)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsRemovesDat, self.checkBoxGlobalOptionsKeepRemove)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsKeepRemove, self.checkBoxGlobalOptions1G1RNames)
        QWidget.setTabOrder(self.checkBoxGlobalOptions1G1RNames, self.lineEditGlobalOptions1G1RPrefix)
        QWidget.setTabOrder(self.lineEditGlobalOptions1G1RPrefix, self.lineEditGlobalOptions1G1RSuffix)
        QWidget.setTabOrder(self.lineEditGlobalOptions1G1RSuffix, self.checkBoxGlobalOptionsReportWarnings)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsReportWarnings, self.checkBoxGlobalOptionsPauseWarnings)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsPauseWarnings, self.checkBoxGlobalOptionsLegacy)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsLegacy, self.checkBoxGlobalOptionsDisableMultiCPU)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsDisableMultiCPU, self.checkBoxGlobalOptionsTrace)
        QWidget.setTabOrder(self.checkBoxGlobalOptionsTrace, self.lineEditGlobalOptionsTrace)
        QWidget.setTabOrder(self.lineEditGlobalOptionsTrace, self.tabWidgetSystemSettings)
        QWidget.setTabOrder(self.tabWidgetSystemSettings, self.buttonSystemClearOutput)
        QWidget.setTabOrder(self.buttonSystemClearOutput, self.buttonSystemChooseOutput)
        QWidget.setTabOrder(self.buttonSystemChooseOutput, self.buttonSystemClearCloneList)
        QWidget.setTabOrder(self.buttonSystemClearCloneList, self.buttonSystemChooseCloneList)
        QWidget.setTabOrder(self.buttonSystemChooseCloneList, self.buttonSystemClearMetadataFile)
        QWidget.setTabOrder(self.buttonSystemClearMetadataFile, self.buttonSystemChooseMetadataFile)
        QWidget.setTabOrder(self.buttonSystemChooseMetadataFile, self.checkBoxSystemOverrideRegions)
        QWidget.setTabOrder(self.checkBoxSystemOverrideRegions, self.listWidgetSystemAvailableRegions)
        QWidget.setTabOrder(self.listWidgetSystemAvailableRegions, self.buttonSystemRegionAllRight)
        QWidget.setTabOrder(self.buttonSystemRegionAllRight, self.buttonSystemRegionRight)
        QWidget.setTabOrder(self.buttonSystemRegionRight, self.buttonSystemRegionLeft)
        QWidget.setTabOrder(self.buttonSystemRegionLeft, self.buttonSystemRegionAllLeft)
        QWidget.setTabOrder(self.buttonSystemRegionAllLeft, self.listWidgetSystemSelectedRegions)
        QWidget.setTabOrder(self.listWidgetSystemSelectedRegions, self.buttonSystemRegionUp)
        QWidget.setTabOrder(self.buttonSystemRegionUp, self.buttonSystemRegionDown)
        QWidget.setTabOrder(self.buttonSystemRegionDown, self.buttonSystemDefaultRegionOrder)
        QWidget.setTabOrder(self.buttonSystemDefaultRegionOrder, self.checkBoxSystemOverrideLanguages)
        QWidget.setTabOrder(self.checkBoxSystemOverrideLanguages, self.listWidgetSystemAvailableLanguages)
        QWidget.setTabOrder(self.listWidgetSystemAvailableLanguages, self.buttonSystemLanguageAllRight)
        QWidget.setTabOrder(self.buttonSystemLanguageAllRight, self.buttonSystemLanguageRight)
        QWidget.setTabOrder(self.buttonSystemLanguageRight, self.buttonSystemLanguageLeft)
        QWidget.setTabOrder(self.buttonSystemLanguageLeft, self.buttonSystemLanguageAllLeft)
        QWidget.setTabOrder(self.buttonSystemLanguageAllLeft, self.listWidgetSystemSelectedLanguages)
        QWidget.setTabOrder(self.listWidgetSystemSelectedLanguages, self.buttonSystemLanguageUp)
        QWidget.setTabOrder(self.buttonSystemLanguageUp, self.buttonSystemLanguageDown)
        QWidget.setTabOrder(self.buttonSystemLanguageDown, self.checkBoxSystemOverrideVideo)
        QWidget.setTabOrder(self.checkBoxSystemOverrideVideo, self.listWidgetSystemVideoStandards)
        QWidget.setTabOrder(self.listWidgetSystemVideoStandards, self.buttonSystemVideoStandardUp)
        QWidget.setTabOrder(self.buttonSystemVideoStandardUp, self.buttonSystemVideoStandardDown)
        QWidget.setTabOrder(self.buttonSystemVideoStandardDown, self.checkBoxSystemOverrideExclusions)
        QWidget.setTabOrder(self.checkBoxSystemOverrideExclusions, self.checkBoxSystemExcludeAddOns)
        QWidget.setTabOrder(self.checkBoxSystemExcludeAddOns, self.checkBoxSystemExcludeApplications)
        QWidget.setTabOrder(self.checkBoxSystemExcludeApplications, self.checkBoxSystemExcludeAudio)
        QWidget.setTabOrder(self.checkBoxSystemExcludeAudio, self.checkBoxSystemExcludeBadDumps)
        QWidget.setTabOrder(self.checkBoxSystemExcludeBadDumps, self.checkBoxSystemExcludeBIOS)
        QWidget.setTabOrder(self.checkBoxSystemExcludeBIOS, self.checkBoxSystemExcludeBonusDiscs)
        QWidget.setTabOrder(self.checkBoxSystemExcludeBonusDiscs, self.checkBoxSystemExcludeCoverdiscs)
        QWidget.setTabOrder(self.checkBoxSystemExcludeCoverdiscs, self.checkBoxSystemExcludeDemos)
        QWidget.setTabOrder(self.checkBoxSystemExcludeDemos, self.checkBoxSystemExcludeEducational)
        QWidget.setTabOrder(self.checkBoxSystemExcludeEducational, self.buttonSystemSelectAllExclude)
        QWidget.setTabOrder(self.buttonSystemSelectAllExclude, self.buttonSystemDeselectAllExclude)
        QWidget.setTabOrder(self.buttonSystemDeselectAllExclude, self.checkBoxSystemOverrideOptions)
        QWidget.setTabOrder(self.checkBoxSystemOverrideOptions, self.checkBoxSystemOptionsDisable1G1R)
        QWidget.setTabOrder(self.checkBoxSystemOptionsDisable1G1R, self.checkBoxSystemOptionsPreferRegions)
        QWidget.setTabOrder(self.checkBoxSystemOptionsPreferRegions, self.checkBoxSystemOptionsModernPlatforms)
        QWidget.setTabOrder(self.checkBoxSystemOptionsModernPlatforms, self.checkBoxSystemOptionsDemoteUnlicensed)
        QWidget.setTabOrder(self.checkBoxSystemOptionsDemoteUnlicensed, self.checkBoxSystemOptionsDisableOverrides)
        QWidget.setTabOrder(self.checkBoxSystemOptionsDisableOverrides, self.checkBoxSystemOptionsSplitRegions)
        QWidget.setTabOrder(self.checkBoxSystemOptionsSplitRegions, self.checkBoxSystemOptionsRemovesDat)
        QWidget.setTabOrder(self.checkBoxSystemOptionsRemovesDat, self.checkBoxSystemOptionsKeepRemove)
        QWidget.setTabOrder(self.checkBoxSystemOptionsKeepRemove, self.checkBoxSystemOptions1G1RNames)
        QWidget.setTabOrder(self.checkBoxSystemOptions1G1RNames, self.lineEditSystemOptions1G1RPrefix)
        QWidget.setTabOrder(self.lineEditSystemOptions1G1RPrefix, self.lineEditSystemOptions1G1RSuffix)
        QWidget.setTabOrder(self.lineEditSystemOptions1G1RSuffix, self.checkBoxSystemOptionsReportWarnings)
        QWidget.setTabOrder(self.checkBoxSystemOptionsReportWarnings, self.checkBoxSystemOptionsPauseWarnings)
        QWidget.setTabOrder(self.checkBoxSystemOptionsPauseWarnings, self.checkBoxSystemOptionsLegacy)
        QWidget.setTabOrder(self.checkBoxSystemOptionsLegacy, self.checkBoxSystemOptionsDisableMultiCPU)
        QWidget.setTabOrder(self.checkBoxSystemOptionsDisableMultiCPU, self.checkBoxSystemOptionsTrace)
        QWidget.setTabOrder(self.checkBoxSystemOptionsTrace, self.lineEditSystemOptionsTrace)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionCloneListNameTool)
        self.menuFile.addAction(self.actionCloneListUpdates)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocs)
        self.menuHelp.addAction(self.actionGitHub)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidgetSettings.setCurrentIndex(0)
        self.tabWidgetGlobalSettings.setCurrentIndex(0)
        self.tabWidgetSystemSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Retool", None))
        self.actionGitHub.setText(QCoreApplication.translate("MainWindow", u"Report an issue", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionCloneListUpdates.setText(QCoreApplication.translate("MainWindow", u"Update clone lists", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCloneListNameTool.setText(QCoreApplication.translate("MainWindow", u"Title tool", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.buttonAddDats.setToolTip(QCoreApplication.translate("MainWindow", u"Add DAT files to the list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddDats.setText("")
#if QT_CONFIG(tooltip)
        self.buttonAddFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Add a folder of DAT files to the list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddFolder.setText("")
#if QT_CONFIG(tooltip)
        self.buttonAddFolderRecursive.setToolTip(QCoreApplication.translate("MainWindow", u"Add a folder of DAT files recursively to the list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddFolderRecursive.setText("")
#if QT_CONFIG(tooltip)
        self.buttonDeleteDats.setToolTip(QCoreApplication.translate("MainWindow", u"Remove selected DAT files from the list. You can also\n"
"do this by pressing DEL on the keyboard.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonDeleteDats.setText("")
#if QT_CONFIG(tooltip)
        self.buttonClearDats.setToolTip(QCoreApplication.translate("MainWindow", u"Remove all DAT files from the list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClearDats.setText("")
#if QT_CONFIG(tooltip)
        self.buttonQuickImport.setToolTip(QCoreApplication.translate("MainWindow", u"Add DAT files recursively from your quick import folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonQuickImport.setText("")

        __sortingEnabled = self.listWidgetOpenFiles.isSortingEnabled()
        self.listWidgetOpenFiles.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetOpenFiles.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"No DAT files added yet", None));
        self.listWidgetOpenFiles.setSortingEnabled(__sortingEnabled)

        self.labelSelectInput.setText(QCoreApplication.translate("MainWindow", u"Add DAT files that you want to filter", None))
#if QT_CONFIG(tooltip)
        self.tabWidgetSettings.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.labelGlobalSettings.setText(QCoreApplication.translate("MainWindow", u"These settings are applied to every DAT file that Retool processes.", None))
        self.labelGlobalSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalReplaceInputDats.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes input DAT files and replaces them with Retool versions in the same folder.\n"
"Only use this if you can recover the original DAT files from elsewhere. Useful\n"
"for RomVault or DatVault users operating directly on their DatRoot files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalReplaceInputDats.setText(QCoreApplication.translate("MainWindow", u"Replace input DAT files", None))
        self.labelGlobalOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected", None))
        self.labelGlobalCustomFilesAndFolders.setText(QCoreApplication.translate("MainWindow", u"Set folders to use when processing DAT files", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalChooseOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalChooseOutput.setText("")
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalPaths), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.labelGlobalFilterByRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.labelGlobalSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
        self.labelGlobalAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setText("")
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
        self.labelGlobalSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available languages to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all languages in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setText("")
        self.labelGlobalAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelGlobalFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setText("")
        self.labelGlobalVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
        self.labelGlobalFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalVideo), QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeDemos.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Demos\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 (@barai)\n"
"\u2022 (Demo [1-9])\n"
"\u2022 (Demo-CD)\n"
"\u2022 (GameCube Preview)\n"
"\u2022 (Kiosk *|* Kiosk)\n"
"\u2022 (Preview)\n"
"\u2022 Kiosk Demo Disc\n"
"\u2022 PS2 Kiosk\n"
"\u2022 PSP System Kiosk\n"
"\u2022 Sample\n"
"\u2022 Taikenban\n"
"\u2022 Trial Edition", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeDemos.setText(QCoreApplication.translate("MainWindow", u"Demos, kiosks, and samples", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensedAll.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles unauthorized by console manufacturers, marked by the\n"
"following text in the name:\n"
"\n"
"\u2022 (Aftermarket)\n"
"\u2022 (Pirate)\n"
"\u2022 (Unl)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensedAll.setText(QCoreApplication.translate("MainWindow", u"Unlicensed (all)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeApplications.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Applications\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022  (Program)\n"
"\u2022  (Test Program)\n"
"\u2022  Check Program\n"
"\u2022  Sample Program", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeApplications.setText(QCoreApplication.translate("MainWindow", u"Applications", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Manual)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setText(QCoreApplication.translate("MainWindow", u"Manuals", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\". These could\n"
"be anything other than the main title content, like patches,\n"
"manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePromotional.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Promotional\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Promo)\n"
"\u2022 EPK\n"
"\u2022 Press Kit", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePromotional.setText(QCoreApplication.translate("MainWindow", u"Promotional", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
        self.labelGlobalExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\". These might be used as\n"
"soundtracks by games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\". These were\n"
"discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeVideo.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Video\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 (Game Boy Advance Video)\n"
"\u2022 (Preview Trailer)\n"
"\u2022 (Movie Trailer)\n"
"\u2022 (Trailer)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeVideo.setText(QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Pirate)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setText(QCoreApplication.translate("MainWindow", u"Pirate", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\".", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeGames.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Games\". Retool assumes\n"
"uncategorized titles are games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeGames.setText(QCoreApplication.translate("MainWindow", u"Games", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setToolTip(QCoreApplication.translate("MainWindow", u"Titles with ROMs declared as missing in action in the DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setText(QCoreApplication.translate("MainWindow", u"MIA", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePreproduction.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Preproduction\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Alpha [0-99])\n"
"\u2022 (Beta [0-99])\n"
"\u2022 (Pre-Production)\n"
"\u2022 (Possible Proto)\n"
"\u2022 (Proto [0-99])", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePreproduction.setText(QCoreApplication.translate("MainWindow", u"Preproduction", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Multimedia\". These might include\n"
"games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setText(QCoreApplication.translate("MainWindow", u"Multimedia", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAftermarket.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Aftermarket)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAftermarket.setText(QCoreApplication.translate("MainWindow", u"Aftermarket", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Unl)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Unlicensed", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
        self.labelGlobalLocalizeNames.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use local names if they are available in metadata files or clone lists. For example, <span style=\" font-style:italic;\">\u30b7\u30e3\u30a4\u30cb\u30f3\u30b0\u25cf\u30d5\u30a9\u30fc\u30b9</span><a name=\"char-node\"/><span style=\" font-family:'u2000'; font-style:italic;\">\u2161</span><span style=\" font-style:italic;\"> \u300e\u53e4\u306e\u5c01\u5370\u300f </span>instead of <span style=\" font-style:italic;\">Shining Force II - Inishie no Fuuin</span>. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-local-names\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.</p><p>Add the languages you want local names for to the following list. Some titles are multi-region, and have multiple local names \u2014 if English is your preferred language, make sure to put it at the top of the order.</p></body></html>", None))
        self.labelGlobalLocalizationSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Localize in this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationDown.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available languages to the end of the localize list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the localize list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all languages in the localize list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllLeft.setText("")
        self.labelGlobalLocalizationAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelGlobalUseLocalNames.setText(QCoreApplication.translate("MainWindow", u"Use local title names for these languages", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalLocalization), QCoreApplication.translate("MainWindow", u"Local names", None))
        self.labelGlobalOverride.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Override Retool and force exclude or include specific titles by adding your own text to match against. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also exclude/include any match's related clones.</p></body></html>", None))
        self.labelGlobalOverrideByText.setText(QCoreApplication.translate("MainWindow", u"Override by text", None))
        self.labelGlobalOverrideInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.labelGlobalOverrideExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalOverrides), QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.labelGlobalFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter after Retool has finished processing", None))
        self.labelGlobalFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.labelGlobalFilters.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>After Retool has finished processing, only include titles that match the text listed here. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.</p></body></html>", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalPostFilter), QCoreApplication.translate("MainWindow", u"Post filters", None))
        self.labelGlobalOptions.setText(QCoreApplication.translate("MainWindow", u"Global options", None))
        self.labelGlobalOptionsTitle.setText(QCoreApplication.translate("MainWindow", u"Title options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisable1G1R.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore clone lists, and treat each title as unique. Useful if you\n"
"want to keep everything from a specific set of regions and/or\n"
"languages.\n"
"\n"
"If this is disabled, it's because you've enabled \"Output DAT file in legacy\n"
"parent/clone format\", which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisable1G1R.setText(QCoreApplication.translate("MainWindow", u"Disable 1G1R filtering", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferRegions.setToolTip(QCoreApplication.translate("MainWindow", u"By default, region priority is treated as lower than language priority. This is so you get\n"
"titles you can understand, along with region-exclusive supersets that contain more\n"
"content.\n"
"\n"
"This option forces strict adherence to region priority regardless of language support and\n"
"superset status. You might get titles with languages you don't understand, or that have\n"
"less content.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferRegions.setText(QCoreApplication.translate("MainWindow", u"Prefer regions over languages", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsModernPlatforms.setToolTip(QCoreApplication.translate("MainWindow", u"For the sake of emulator compatibility, Retool prefers versions of\n"
"games released on the original system instead of those ripped from\n"
"rereleases on platforms like Virtual Console and Steam. This option\n"
"reverses that behavior.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsModernPlatforms.setText(QCoreApplication.translate("MainWindow", u"Prefer titles ripped from modern rereleases over original system releases", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferOldest.setToolTip(QCoreApplication.translate("MainWindow", u"Useful for speedrunners and those concerned about censorship, who often want unpatched\n"
"versions of games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferOldest.setText(QCoreApplication.translate("MainWindow", u"Prefer oldest production versions instead of newest", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Sometimes games are rereleased long after the lifespan of a console,\n"
"in regions they weren't originally available in. By default Retool\n"
"selects these titles if they match your preferred region/language\n"
"priorities.\n"
"\n"
"Enable this option to choose a production version of a title over\n"
"the unlicensed or aftermarket title if possible. This might\n"
"select titles from a lower priority region, or with lower priority\n"
"languages, or with less features.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Prefer licensed over unlicensed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableOverrides.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore both global and system overrides.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableOverrides.setText(QCoreApplication.translate("MainWindow", u"Disable global and system overrides", None))
        self.labelGlobalChooseCompilationsMode.setText(QCoreApplication.translate("MainWindow", u"Compilations handling", None))
        self.comboBoxGlobalChooseCompilationsMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.comboBoxGlobalChooseCompilationsMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Prefer individual titles", None))
        self.comboBoxGlobalChooseCompilationsMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Keep individual titles and compilations", None))
        self.comboBoxGlobalChooseCompilationsMode.setItemText(3, QCoreApplication.translate("MainWindow", u"Optimize for least possible title duplication", None))

        self.labelGlobalCompilationsExplanation.setText(QCoreApplication.translate("MainWindow", u"Chooses individual titles most of the time. Only chooses compilations when they have a\n"
"higher region, language, or clone list priority, or contain unique titles. When choosing\n"
"a compilation for unique titles, if other titles in the compilation have individual\n"
"equivalents, the individual titles are also included, leading to some title duplication.", None))
        self.labelGlobalOptionsOutput.setText(QCoreApplication.translate("MainWindow", u"Output options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsAlreadyProcessed.setToolTip(QCoreApplication.translate("MainWindow", u"Let DAT files be processed even if Retool has already processed them.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsAlreadyProcessed.setText(QCoreApplication.translate("MainWindow", u"Allow processing of already processed files", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsOriginalHeader.setToolTip(QCoreApplication.translate("MainWindow", u"By default Retool changes header fields so you can tell in ROM managers if DAT files have\n"
"been modified. Enable this if you want to load Retool DAT files as updates to original\n"
"Redump and No-Intro DAT files already loaded in your ROM manager.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsOriginalHeader.setText(QCoreApplication.translate("MainWindow", u"Don't modify input DAT file's existing header fields", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsUseMachine.setToolTip(QCoreApplication.translate("MainWindow", u"Exports each title node using the MAME standard of <machine>\n"
"instead of <game>.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsUseMachine.setText(QCoreApplication.translate("MainWindow", u"Use <machine> instead of <game> in output DAT files", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsSplitRegions.setToolTip(QCoreApplication.translate("MainWindow", u"Instead of one output DAT file containing all the filtered results, split\n"
"the output into multiple DAT files based on the regions you've selected.\n"
"\n"
"If this is disabled, it's because you've enabled \"Output DAT file in legacy\n"
"parent/clone format\", which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsSplitRegions.setText(QCoreApplication.translate("MainWindow", u"Split the output into multiple DAT files based on region", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsRemovesDat.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, create another\n"
"DAT file containing the titles Retool removed.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsRemovesDat.setText(QCoreApplication.translate("MainWindow", u"Also output DAT files of all the removed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsKeepRemove.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file\n"
"that lists what titles have been kept, and what\n"
"titles have been removed.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsKeepRemove.setText(QCoreApplication.translate("MainWindow", u"Also output reports of what titles have been kept and removed", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptions1G1RNames.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file that lists only\n"
"the name of each title in the output DAT file, and optionally add a prefix\n"
"and suffix to each name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptions1G1RNames.setText(QCoreApplication.translate("MainWindow", u"Also output lists of title names from output DAT files", None))
        self.labelGlobalOptions1G1RPrefix.setText(QCoreApplication.translate("MainWindow", u"Add text to the start of each title (start with http://, https//, or ftp:// to URL encode)", None))
        self.labelGlobalOptions1G1RSuffix.setText(QCoreApplication.translate("MainWindow", u"Add text to the end of each title", None))
        self.labelGlobalOptionsOnline.setText(QCoreApplication.translate("MainWindow", u"Online features", None))
        self.labelGlobalOnlineExplanation.setText(QCoreApplication.translate("MainWindow", u"These features use data supplied by third parties. When those third parties stop updating,\n"
"Retool might make choices that are out-of-date.", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsMIA.setToolTip(QCoreApplication.translate("MainWindow", u"For files that no one has (missing in action), add mia=\"yes\" to rom/file tags.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsMIA.setText(QCoreApplication.translate("MainWindow", u"Add MIA attributes to DAT files (DatVault users should leave this disabled)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsRetroAchievements.setToolTip(QCoreApplication.translate("MainWindow", u"For titles that support RetroAchievements, add retroachievements=\"yes\"\n"
"to game/machine tags.\n"
"\n"
"For Redump, you need to use alternative DAT files that use either CHD\n"
"or RVZ image formats, like the MAME Redump DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsRetroAchievements.setText(QCoreApplication.translate("MainWindow", u"Add RetroAchievements attributes to DAT files (Requires CHD or RVZ DAT files for Redump)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferRetro.setToolTip(QCoreApplication.translate("MainWindow", u"Prioritizes titles that support RetroAchievements.\n"
"\n"
"For Redump, you need to use alternative DAT files that use either CHD\n"
"or RVZ image formats, like the MAME Redump DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferRetro.setText(QCoreApplication.translate("MainWindow", u"Prefer titles with RetroAchievements (Requires CHD or RVZ DAT files for Redump)", None))
        self.labelGlobalOptionsDebug.setText(QCoreApplication.translate("MainWindow", u"Debug options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsReportWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Turn on warnings when there are mismatches\n"
"between the clone list and the DAT file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsReportWarnings.setText(QCoreApplication.translate("MainWindow", u"Report clone list warnings during processing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPauseWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Pause Retool each time a clone list warning is issued.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPauseWarnings.setText(QCoreApplication.translate("MainWindow", u"Pause on clone list warnings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsLegacy.setToolTip(QCoreApplication.translate("MainWindow", u"Not recommended unless you're debugging or comparing outputs between\n"
"DAT file versions.\n"
"\n"
"If this is disabled, it's because you've disabled 1G1R filtering or\n"
"chosen to split by region, which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsLegacy.setText(QCoreApplication.translate("MainWindow", u"Output DAT files in legacy parent/clone format", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableMultiCPU.setToolTip(QCoreApplication.translate("MainWindow", u"Forces Retool to use only a single CPU\n"
"core, at the cost of performance.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableMultiCPU.setText(QCoreApplication.translate("MainWindow", u"Disable multiprocessor usage", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsTrace.setToolTip(QCoreApplication.translate("MainWindow", u"Follows a title through Retool's selection process for debugging.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Trace a title through Retool's process (no DAT files are created)", None))
        self.labelGlobalOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Enter a regex string to trace (case insensitive)", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabGlobalSettings), QCoreApplication.translate("MainWindow", u"Global settings", None))
        self.labelSystemSettings.setText(QCoreApplication.translate("MainWindow", u"Add a DAT file, and then select it in the list to enable system-specific settings.", None))
        self.labelSystemSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearMIAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default MIA file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearMIAFile.setText("")
        self.labelSystemOptionsTitle_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default metadata file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearMetadataFile.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxSystemReplaceInputDats.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes input DAT files and replaces them with Retool versions in the same folder.\n"
"Only use this if you can recover the original DAT files from elsewhere. Useful\n"
"for RomVault or DatVault users operating directly on their DatRoot files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemReplaceInputDats.setText(QCoreApplication.translate("MainWindow", u"Replace input DAT files", None))
        self.labelSystemSelectMetadataFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom metadata file", None))
        self.labelSystemMIAFile.setText(QCoreApplication.translate("MainWindow", u"No custom MIA file selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearRAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default RetroAchievements file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearRAFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseRAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom RetroAchievements file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseRAFile.setText("")
        self.labelSystemSelectCloneList.setText(QCoreApplication.translate("MainWindow", u"Select a custom clone list", None))
        self.labelSystemSelectRAFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom RetroAchievements file", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom metadata file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseMetadataFile.setText("")
        self.labelSystemCloneList.setText(QCoreApplication.translate("MainWindow", u"No custom clone list selected, using default location", None))
        self.labelSystemMetadataFile.setText(QCoreApplication.translate("MainWindow", u"No custom metadata file selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseMIAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom MIA file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseMIAFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemClearCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Use default clone list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearCloneList.setText("")
        self.labelSystemSelectMIAFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom MIA file", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom clone list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseCloneList.setText("")
        self.labelSystemRAFile.setText(QCoreApplication.translate("MainWindow", u"No custom RetroAchievements file selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Use global output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearOutput.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseOutput.setText("")
        self.labelSystemOptionsTitle_3.setText(QCoreApplication.translate("MainWindow", u"Support files", None))
        self.labelSystemOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected, using global settings", None))
        self.labelSystemCustomFilesAndFolders.setText(QCoreApplication.translate("MainWindow", u"Set files and folders to use when processing this DAT file", None))
        self.checkBoxSystemOverridePaths.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemPaths), QCoreApplication.translate("MainWindow", u"Paths", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setText("")
        self.labelSystemSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
        self.labelSystemAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
        self.labelSystemFilterByRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.checkBoxSystemOverrideRegions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
        self.labelSystemFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.checkBoxSystemOverrideLanguages.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available languages to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all languages in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setText("")
        self.labelSystemAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelSystemSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setText("")
        self.labelSystemFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.checkBoxSystemOverrideVideo.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemVideo), QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\".", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeDemos.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Demos\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 (@barai)\n"
"\u2022 (Demo [1-9])\n"
"\u2022 (Demo-CD)\n"
"\u2022 (GameCube Preview)\n"
"\u2022 (Kiosk *|* Kiosk)\n"
"\u2022 (Preview)\n"
"\u2022 Kiosk Demo Disc\n"
"\u2022 PS2 Kiosk\n"
"\u2022 PSP System Kiosk\n"
"\u2022 Sample\n"
"\u2022 Taikenban\n"
"\u2022 Trial Edition", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeDemos.setText(QCoreApplication.translate("MainWindow", u"Demos, kiosks, and samples", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\". These were\n"
"discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\". These might be used as\n"
"soundtracks by games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\". These could\n"
"be anything other than the main title content, like patches,\n"
"manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeApplications.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Applications\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022  (Program)\n"
"\u2022  (Test Program)\n"
"\u2022  Check Program\n"
"\u2022  Sample Program", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeApplications.setText(QCoreApplication.translate("MainWindow", u"Applications", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
        self.labelGlobalExclude_2.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles", None))
        self.checkBoxSystemOverrideExclusions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeGames.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Games\". Retool assumes\n"
"uncategorized titles are games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeGames.setText(QCoreApplication.translate("MainWindow", u"Games", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeManuals.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Manual)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeManuals.setText(QCoreApplication.translate("MainWindow", u"Manuals", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMIA.setToolTip(QCoreApplication.translate("MainWindow", u"Titles with ROMs declared as missing in action in the DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMIA.setText(QCoreApplication.translate("MainWindow", u"MIA", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMultimedia.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Multimedia\". These might include\n"
"games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMultimedia.setText(QCoreApplication.translate("MainWindow", u"Multimedia", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePreproduction.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Preproduction\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Alpha [0-99])\n"
"\u2022 (Beta [0-99])\n"
"\u2022 (Pre-Production)\n"
"\u2022 (Possible Proto)\n"
"\u2022 (Proto [0-99])", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePreproduction.setText(QCoreApplication.translate("MainWindow", u"Preproduction", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePromotional.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Promotional\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Promo)\n"
"\u2022 EPK\n"
"\u2022 Press Kit", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePromotional.setText(QCoreApplication.translate("MainWindow", u"Promotional", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensedAll.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles unauthorized by console manufacturers, marked by the\n"
"following text in the name:\n"
"\n"
"\u2022 (Aftermarket)\n"
"\u2022 (Pirate)\n"
"\u2022 (Unl)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensedAll.setText(QCoreApplication.translate("MainWindow", u"Unlicensed (all)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeVideo.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Video\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 (Game Boy Advance Video)\n"
"\u2022 (Preview Trailer)\n"
"\u2022 (Movie Trailer)\n"
"\u2022 (Trailer)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeVideo.setText(QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAftermarket.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Aftermarket)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAftermarket.setText(QCoreApplication.translate("MainWindow", u"Aftermarket", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePirate.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Pirate)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePirate.setText(QCoreApplication.translate("MainWindow", u"Pirate", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Unl)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Unlicensed", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available languages to the end of the localize list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the localize list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all languages in the localize list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected languages down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationDown.setText("")
        self.labelSystemLocalizeNames.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use local names if they are available in metadata files or clone lists. For example, <span style=\" font-style:italic;\">\u30b7\u30e3\u30a4\u30cb\u30f3\u30b0\u25cf\u30d5\u30a9\u30fc\u30b9</span><a name=\"char-node\"/><span style=\" font-family:'u2000'; font-style:italic;\">\u2161</span><span style=\" font-style:italic;\"> \u300e\u53e4\u306e\u5c01\u5370\u300f </span>instead of <span style=\" font-style:italic;\">Shining Force II - Inishie no Fuuin</span>. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-local-names\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.</p><p>Add the languages you want local names for to the following list. Some titles are multi-region, and have multiple local names \u2014 if English is your preferred language, make sure to put it at the top of the order.</p></body></html>", None))
        self.labelSystemLocalizationSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Localize in this language order", None))
        self.labelSystemLocalizationAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelSystemUseLocalNames.setText(QCoreApplication.translate("MainWindow", u"Use local title names for these languages", None))
        self.checkBoxSystemOverrideLocalization.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemLocalization), QCoreApplication.translate("MainWindow", u"Local names", None))
        self.labelSystemOverrideInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.labelSystemOverrideExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.labelSystemOverrideByText.setText(QCoreApplication.translate("MainWindow", u"Override by text", None))
        self.labelSystemOverride.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Override Retool and force exclude or include specific titles by adding your own text to match against. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also exclude/include any match's related clones.</p></body></html>", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemOverrides), QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.labelSystemFilters.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>After Retool has finished processing, only include titles that match the text listed here. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.</p></body></html>", None))
        self.labelSystemFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.labelSystemlFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter after Retool has finished processing", None))
        self.checkBoxSystemOverridePostFilter.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemPostFilter), QCoreApplication.translate("MainWindow", u"Post filters", None))
        self.checkBoxSystemOverrideOptions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemOptions.setText(QCoreApplication.translate("MainWindow", u"System options", None))
        self.labelSystemOptionsTitle.setText(QCoreApplication.translate("MainWindow", u"Title options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisable1G1R.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore clone lists, and treat each title as unique. Useful if you\n"
"want to keep everything from a specific set of regions and/or\n"
"languages.\n"
"\n"
"If this is disabled, it's because you've enabled \"Output DAT file in legacy\n"
"parent/clone format\", which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisable1G1R.setText(QCoreApplication.translate("MainWindow", u"Disable 1G1R filtering", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferRegions.setToolTip(QCoreApplication.translate("MainWindow", u"By default, region priority is treated as lower than language priority. This is so you get\n"
"titles you can understand, along with region-exclusive supersets that contain more\n"
"content.\n"
"\n"
"This option forces strict adherence to region priority regardless of language support and\n"
"superset status. You might get titles with languages you don't understand, or that have\n"
"less content.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferRegions.setText(QCoreApplication.translate("MainWindow", u"Prefer regions over languages", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsModernPlatforms.setToolTip(QCoreApplication.translate("MainWindow", u"For the sake of emulator compatibility, Retool prefers versions of\n"
"games released on the original system instead of those ripped from\n"
"rereleases on platforms like Virtual Console and Steam. This option\n"
"reverses that behavior.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsModernPlatforms.setText(QCoreApplication.translate("MainWindow", u"Prefer titles ripped from modern rereleases over original system releases", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferOldest.setToolTip(QCoreApplication.translate("MainWindow", u"Useful for speedrunners and those concerned about censorship, who often want unpatched\n"
"versions of games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferOldest.setText(QCoreApplication.translate("MainWindow", u"Prefer oldest production versions instead of newest", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDemoteUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Sometimes games are rereleased long after the lifespan of a console,\n"
"in regions they weren't originally available in. By default Retool\n"
"selects these titles if they match your preferred region/language\n"
"priorities.\n"
"\n"
"Enable this option to choose a production version of a title over\n"
"the unlicensed or aftermarket title if possible. This might\n"
"select titles from a lower priority region, or with lower priority\n"
"languages, or with less features.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDemoteUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Prefer licensed over unlicensed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableOverrides.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore both global and system overrides.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableOverrides.setText(QCoreApplication.translate("MainWindow", u"Disable global and system overrides", None))
        self.labelSystemChooseCompilationsMode.setText(QCoreApplication.translate("MainWindow", u"Compilations handling", None))
        self.comboBoxSystemChooseCompilationsMode.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.comboBoxSystemChooseCompilationsMode.setItemText(1, QCoreApplication.translate("MainWindow", u"Prefer individual titles", None))
        self.comboBoxSystemChooseCompilationsMode.setItemText(2, QCoreApplication.translate("MainWindow", u"Keep individual titles and compilations", None))
        self.comboBoxSystemChooseCompilationsMode.setItemText(3, QCoreApplication.translate("MainWindow", u"Optimize for least possible title duplication", None))

        self.labelSystemCompilationsExplanation.setText(QCoreApplication.translate("MainWindow", u"Chooses individual titles most of the time. Only chooses compilations when they have a\n"
"higher region, language, or clone list priority, or contain unique titles. When choosing\n"
"a compilation for unique titles, if other titles in the compilation have individual\n"
"equivalents, the individual titles are also included, leading to some title duplication.", None))
        self.labelSystemOptionsOutput.setText(QCoreApplication.translate("MainWindow", u"Output options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsAlreadyProcessed.setToolTip(QCoreApplication.translate("MainWindow", u"Let DAT files be processed even if Retool has already processed them.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsAlreadyProcessed.setText(QCoreApplication.translate("MainWindow", u"Allow processing of already processed files", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsOriginalHeader.setToolTip(QCoreApplication.translate("MainWindow", u"By default Retool changes header fields so you can tell in ROM managers if DAT files have\n"
"been modified. Enable this if you want to load Retool DAT files as updates to original\n"
"Redump and No-Intro DAT files already loaded in your ROM manager.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsOriginalHeader.setText(QCoreApplication.translate("MainWindow", u"Don't modify input DAT file's existing header fields", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsUseMachine.setToolTip(QCoreApplication.translate("MainWindow", u"Exports each title node using the MAME standard of <machine>\n"
"instead of <game>.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsUseMachine.setText(QCoreApplication.translate("MainWindow", u"Use <machine> instead of <game> in output DAT files", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsSplitRegions.setToolTip(QCoreApplication.translate("MainWindow", u"Instead of one output DAT file containing all the filtered results, split\n"
"the output into multiple DAT files based on the regions you've selected.\n"
"\n"
"If this is disabled, it's because you've enabled \"Output DAT file in legacy\n"
"parent/clone format\", which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsSplitRegions.setText(QCoreApplication.translate("MainWindow", u"Split the output into multiple DAT files based on region", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsRemovesDat.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, create another\n"
"DAT file containing the titles Retool removed.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsRemovesDat.setText(QCoreApplication.translate("MainWindow", u"Also output DAT files of all the removed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsKeepRemove.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file\n"
"that lists what titles have been kept, and what\n"
"titles have been removed.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsKeepRemove.setText(QCoreApplication.translate("MainWindow", u"Also output reports of what titles have been kept and removed", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptions1G1RNames.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file that lists only\n"
"the name of each title in the output DAT file, and optionally add a prefix\n"
"and suffix to each name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptions1G1RNames.setText(QCoreApplication.translate("MainWindow", u"Also output lists of title names from output DAT files", None))
        self.labelSystemOptions1G1RPrefix.setText(QCoreApplication.translate("MainWindow", u"Add text to the start of each title (start with http://, https//, or ftp:// to URL encode)", None))
        self.labelSystemOptions1G1RSuffix.setText(QCoreApplication.translate("MainWindow", u"Add text to the end of each title", None))
        self.labelSystemOptionsOnline.setText(QCoreApplication.translate("MainWindow", u"Online features", None))
        self.labelSystemOnlineExplanation.setText(QCoreApplication.translate("MainWindow", u"These features use data supplied by third parties. When those third parties stop updating,\n"
"Retool might make choices that are out-of-date.", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsMIA.setToolTip(QCoreApplication.translate("MainWindow", u"For files that no one has (missing in action), add mia=\"yes\" to rom/file tags.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsMIA.setText(QCoreApplication.translate("MainWindow", u"Add MIA attributes to files (DatVault users should leave this disabled)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsRetroAchievements.setToolTip(QCoreApplication.translate("MainWindow", u"For titles that support RetroAchievements, add retroachievements=\"yes\"\n"
"to game/machine tags.\n"
"\n"
"For Redump, you need to use alternative DAT files that use either CHD\n"
"or RVZ image formats, like the MAME Redump DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsRetroAchievements.setText(QCoreApplication.translate("MainWindow", u"Add RetroAchievements attributes to DAT files (Requires CHD or RVZ DAT files for Redump)", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferRetro.setToolTip(QCoreApplication.translate("MainWindow", u"Prioritizes titles that support RetroAchievements.\n"
"\n"
"For Redump, you need to use alternative DAT files that use either CHD\n"
"or RVZ image formats, like the MAME Redump DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferRetro.setText(QCoreApplication.translate("MainWindow", u"Prefer titles with RetroAchievements (Requires CHD or RVZ DAT files for Redump)", None))
        self.labelSystemOptionsDebug.setText(QCoreApplication.translate("MainWindow", u"Debug options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsReportWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Turn on warnings when there are mismatches\n"
"between the clone list and the DAT file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsReportWarnings.setText(QCoreApplication.translate("MainWindow", u"Report clone list warnings during processing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPauseWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Pause Retool each time a clone list warning is issued.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPauseWarnings.setText(QCoreApplication.translate("MainWindow", u"Pause on clone list warnings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsLegacy.setToolTip(QCoreApplication.translate("MainWindow", u"Not recommended unless you're debugging or comparing outputs between\n"
"DAT file versions.\n"
"\n"
"If this is disabled, it's because you've disabled 1G1R filtering or\n"
"chosen to split by region, which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsLegacy.setText(QCoreApplication.translate("MainWindow", u"Output DAT files in legacy parent/clone format", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableMultiCPU.setToolTip(QCoreApplication.translate("MainWindow", u"Forces Retool to use only a single CPU\n"
"core, at the cost of performance.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableMultiCPU.setText(QCoreApplication.translate("MainWindow", u"Disable multiprocessor usage", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsTrace.setToolTip(QCoreApplication.translate("MainWindow", u"Follows a title through Retool's selection process for debugging.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Trace a title through Retool's process (no DAT files are created)", None))
        self.labelSystemOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Enter a regex string to trace (case insensitive)", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabSystemSettings), QCoreApplication.translate("MainWindow", u"System settings", None))
        self.labelSettingsSaved.setText(QCoreApplication.translate("MainWindow", u"Settings are saved automatically", None))
        self.labelChooseYourSettings.setText(QCoreApplication.translate("MainWindow", u"Choose your settings", None))
        self.buttonGo.setText(QCoreApplication.translate("MainWindow", u"Process DAT files", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

