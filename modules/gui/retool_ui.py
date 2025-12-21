# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from modules.gui.gui_widgets import (CustomComboBox, CustomLineEdit, CustomList, CustomListDropFiles,
    CustomListSelfDrag, CustomPushButton, CustomTextEdit, ElisionLabel)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 715)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1080, 715))
        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/retoolIcon/images/retool.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setIconSize(QSize(256, 256))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionGitHub = QAction(MainWindow)
        self.actionGitHub.setObjectName(u"actionGitHub")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setMenuRole(QAction.MenuRole.NoRole)
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
        self.actionSettings.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.centralwidget.setAutoFillBackground(False)
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
        font1 = QFont()
        font1.setPointSize(8)
        self.listWidgetOpenFiles.setFont(font1)
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
        font2 = QFont()
        font2.setBold(True)
        self.labelSelectInput.setFont(font2)

        self.gridLayoutLeft.addWidget(self.labelSelectInput, 0, 2, 1, 1)

        self.splitter.addWidget(self.gridLayoutLeftFiles)
        self.gridLayoutRightSettings = QWidget(self.splitter)
        self.gridLayoutRightSettings.setObjectName(u"gridLayoutRightSettings")
        self.gridLayoutRightSettings.setMinimumSize(QSize(740, 0))
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
        self.tabWidgetGlobalSettings.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidgetGlobalSettings.setUsesScrollButtons(True)
        self.tabGlobalPaths = QWidget()
        self.tabGlobalPaths.setObjectName(u"tabGlobalPaths")
        self.gridLayout_10 = QGridLayout(self.tabGlobalPaths)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollAreaGlobalPaths = QScrollArea(self.tabGlobalPaths)
        self.scrollAreaGlobalPaths.setObjectName(u"scrollAreaGlobalPaths")
        self.scrollAreaGlobalPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalPaths.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalPaths.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalPaths = QWidget()
        self.scrollAreaWidgetContentsGlobalPaths.setObjectName(u"scrollAreaWidgetContentsGlobalPaths")
        self.scrollAreaWidgetContentsGlobalPaths.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalPaths.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalPaths.setSizePolicy(sizePolicy)
        self.verticalLayout_43 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalPaths)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalPaths = QFrame(self.scrollAreaWidgetContentsGlobalPaths)
        self.tabContentsGlobalPaths.setObjectName(u"tabContentsGlobalPaths")
        self.tabContentsGlobalPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalPaths.setLineWidth(0)
        self.verticalLayout_44 = QVBoxLayout(self.tabContentsGlobalPaths)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalPaths = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalPaths.setObjectName(u"horizontalLayoutHeaderGlobalPaths")
        self.labelGlobalPaths = QLabel(self.tabContentsGlobalPaths)
        self.labelGlobalPaths.setObjectName(u"labelGlobalPaths")
        sizePolicy3.setHeightForWidth(self.labelGlobalPaths.sizePolicy().hasHeightForWidth())
        self.labelGlobalPaths.setSizePolicy(sizePolicy3)
        self.labelGlobalPaths.setMinimumSize(QSize(0, 0))
        self.labelGlobalPaths.setFont(font2)

        self.horizontalLayoutHeaderGlobalPaths.addWidget(self.labelGlobalPaths)

        self.frameOverrideGlobalPaths = QFrame(self.tabContentsGlobalPaths)
        self.frameOverrideGlobalPaths.setObjectName(u"frameOverrideGlobalPaths")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalPaths.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalPaths.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalPaths.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_45 = QVBoxLayout(self.frameOverrideGlobalPaths)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalPaths.addWidget(self.frameOverrideGlobalPaths)

        self.horizontalLayoutHeaderGlobalPaths.setStretch(0, 1)

        self.verticalLayout_44.addLayout(self.horizontalLayoutHeaderGlobalPaths)

        self.lineGlobalPaths = QFrame(self.tabContentsGlobalPaths)
        self.lineGlobalPaths.setObjectName(u"lineGlobalPaths")
        palette = QPalette()
        brush = QBrush(QColor(85, 85, 85, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalPaths.setPalette(palette)
        self.lineGlobalPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalPaths.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_44.addWidget(self.lineGlobalPaths)

        self.verticalLayoutGlobalPathsContent = QVBoxLayout()
        self.verticalLayoutGlobalPathsContent.setSpacing(10)
        self.verticalLayoutGlobalPathsContent.setObjectName(u"verticalLayoutGlobalPathsContent")
        self.horizontalLayoutGlobalOutputSettings = QHBoxLayout()
        self.horizontalLayoutGlobalOutputSettings.setSpacing(6)
        self.horizontalLayoutGlobalOutputSettings.setObjectName(u"horizontalLayoutGlobalOutputSettings")
        self.horizontalLayoutGlobalOutputSettings.setContentsMargins(0, -1, -1, -1)
        self.buttonGlobalChooseOutput = QPushButton(self.tabContentsGlobalPaths)
        self.buttonGlobalChooseOutput.setObjectName(u"buttonGlobalChooseOutput")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonGlobalChooseOutput.sizePolicy().hasHeightForWidth())
        self.buttonGlobalChooseOutput.setSizePolicy(sizePolicy6)
        self.buttonGlobalChooseOutput.setMinimumSize(QSize(44, 48))
        self.buttonGlobalChooseOutput.setMaximumSize(QSize(44, 48))
        font3 = QFont()
        font3.setPointSize(10)
        self.buttonGlobalChooseOutput.setFont(font3)
        self.buttonGlobalChooseOutput.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/retoolFiles/images/icons8-live-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalChooseOutput.setIcon(icon1)
        self.buttonGlobalChooseOutput.setIconSize(QSize(32, 32))
        self.buttonGlobalChooseOutput.setFlat(False)

        self.horizontalLayoutGlobalOutputSettings.addWidget(self.buttonGlobalChooseOutput)

        self.verticalLayoutGlobalOutputLabels = QVBoxLayout()
        self.verticalLayoutGlobalOutputLabels.setObjectName(u"verticalLayoutGlobalOutputLabels")
        self.labelGlobalSelectOutput = QLabel(self.tabContentsGlobalPaths)
        self.labelGlobalSelectOutput.setObjectName(u"labelGlobalSelectOutput")
        self.labelGlobalSelectOutput.setMinimumSize(QSize(400, 0))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        self.labelGlobalSelectOutput.setFont(font4)

        self.verticalLayoutGlobalOutputLabels.addWidget(self.labelGlobalSelectOutput)

        self.labelGlobalOutputFolder = ElisionLabel(self.tabContentsGlobalPaths)
        self.labelGlobalOutputFolder.setObjectName(u"labelGlobalOutputFolder")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.labelGlobalOutputFolder.sizePolicy().hasHeightForWidth())
        self.labelGlobalOutputFolder.setSizePolicy(sizePolicy7)
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
        self.labelGlobalOutputFolder.setFont(font1)

        self.verticalLayoutGlobalOutputLabels.addWidget(self.labelGlobalOutputFolder)


        self.horizontalLayoutGlobalOutputSettings.addLayout(self.verticalLayoutGlobalOutputLabels)


        self.verticalLayoutGlobalPathsContent.addLayout(self.horizontalLayoutGlobalOutputSettings)

        self.checkBoxGlobalReplaceInputDats = QCheckBox(self.tabContentsGlobalPaths)
        self.checkBoxGlobalReplaceInputDats.setObjectName(u"checkBoxGlobalReplaceInputDats")
        self.checkBoxGlobalReplaceInputDats.setFont(font1)
        self.checkBoxGlobalReplaceInputDats.setIconSize(QSize(16, 16))
        self.checkBoxGlobalReplaceInputDats.setChecked(False)

        self.verticalLayoutGlobalPathsContent.addWidget(self.checkBoxGlobalReplaceInputDats)

        self.verticalSpacerGlobalPaths = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutGlobalPathsContent.addItem(self.verticalSpacerGlobalPaths)


        self.verticalLayout_44.addLayout(self.verticalLayoutGlobalPathsContent)

        self.verticalLayout_44.setStretch(2, 1)

        self.verticalLayout_43.addWidget(self.tabContentsGlobalPaths)

        self.scrollAreaGlobalPaths.setWidget(self.scrollAreaWidgetContentsGlobalPaths)

        self.gridLayout_10.addWidget(self.scrollAreaGlobalPaths, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalPaths, "")
        self.tabGlobalRegions = QWidget()
        self.tabGlobalRegions.setObjectName(u"tabGlobalRegions")
        self.gridLayout_9 = QGridLayout(self.tabGlobalRegions)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollAreaGlobalRegions = QScrollArea(self.tabGlobalRegions)
        self.scrollAreaGlobalRegions.setObjectName(u"scrollAreaGlobalRegions")
        self.scrollAreaGlobalRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalRegions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalRegions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalRegions = QWidget()
        self.scrollAreaWidgetContentsGlobalRegions.setObjectName(u"scrollAreaWidgetContentsGlobalRegions")
        self.scrollAreaWidgetContentsGlobalRegions.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalRegions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalRegions.setSizePolicy(sizePolicy)
        self.verticalLayout_46 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalRegions)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalRegions = QFrame(self.scrollAreaWidgetContentsGlobalRegions)
        self.tabContentsGlobalRegions.setObjectName(u"tabContentsGlobalRegions")
        self.tabContentsGlobalRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalRegions.setLineWidth(0)
        self.verticalLayout_47 = QVBoxLayout(self.tabContentsGlobalRegions)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalRegions = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalRegions.setObjectName(u"horizontalLayoutHeaderGlobalRegions")
        self.labelGlobalRegions = QLabel(self.tabContentsGlobalRegions)
        self.labelGlobalRegions.setObjectName(u"labelGlobalRegions")
        sizePolicy3.setHeightForWidth(self.labelGlobalRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalRegions.setSizePolicy(sizePolicy3)
        self.labelGlobalRegions.setMinimumSize(QSize(0, 0))
        self.labelGlobalRegions.setFont(font2)

        self.horizontalLayoutHeaderGlobalRegions.addWidget(self.labelGlobalRegions)

        self.frameOverrideGlobalRegions = QFrame(self.tabContentsGlobalRegions)
        self.frameOverrideGlobalRegions.setObjectName(u"frameOverrideGlobalRegions")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalRegions.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalRegions.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalRegions.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_49 = QVBoxLayout(self.frameOverrideGlobalRegions)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalRegions.addWidget(self.frameOverrideGlobalRegions)

        self.horizontalLayoutHeaderGlobalRegions.setStretch(0, 1)

        self.verticalLayout_47.addLayout(self.horizontalLayoutHeaderGlobalRegions)

        self.lineGlobalRegions = QFrame(self.tabContentsGlobalRegions)
        self.lineGlobalRegions.setObjectName(u"lineGlobalRegions")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalRegions.setPalette(palette2)
        self.lineGlobalRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalRegions.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_47.addWidget(self.lineGlobalRegions)

        self.frameGlobalRegions = QFrame(self.tabContentsGlobalRegions)
        self.frameGlobalRegions.setObjectName(u"frameGlobalRegions")
        self.frameGlobalRegions.setMinimumSize(QSize(0, 64))
        self.frameGlobalRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frameGlobalRegions)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalAvailableRegions = QFrame(self.frameGlobalRegions)
        self.frameGlobalAvailableRegions.setObjectName(u"frameGlobalAvailableRegions")
        sizePolicy5.setHeightForWidth(self.frameGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.frameGlobalAvailableRegions.setSizePolicy(sizePolicy5)
        self.frameGlobalAvailableRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalAvailableRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalAvailableRegions.setLineWidth(0)
        self.verticalLayout_35 = QVBoxLayout(self.frameGlobalAvailableRegions)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalAvailableRegions = QLabel(self.frameGlobalAvailableRegions)
        self.labelGlobalAvailableRegions.setObjectName(u"labelGlobalAvailableRegions")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.labelGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableRegions.setSizePolicy(sizePolicy8)
        self.labelGlobalAvailableRegions.setFont(font)
        self.labelGlobalAvailableRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_35.addWidget(self.labelGlobalAvailableRegions)

        self.listWidgetGlobalAvailableRegions = CustomList(self.frameGlobalAvailableRegions)
        self.listWidgetGlobalAvailableRegions.setObjectName(u"listWidgetGlobalAvailableRegions")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableRegions.setSizePolicy(sizePolicy9)
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

        self.verticalLayout_35.addWidget(self.listWidgetGlobalAvailableRegions)


        self.horizontalLayout_8.addWidget(self.frameGlobalAvailableRegions)

        self.frameGlobalRegionLeftRight = QFrame(self.frameGlobalRegions)
        self.frameGlobalRegionLeftRight.setObjectName(u"frameGlobalRegionLeftRight")
        sizePolicy5.setHeightForWidth(self.frameGlobalRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionLeftRight.setSizePolicy(sizePolicy5)
        self.frameGlobalRegionLeftRight.setMinimumSize(QSize(64, 0))
        self.frameGlobalRegionLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalRegionLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalRegionLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalRegionLeftRight.setLineWidth(0)
        self.verticalLayout_39 = QVBoxLayout(self.frameGlobalRegionLeftRight)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalSpacerGlobalRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacerGlobalRegionLeftRightTop)

        self.buttonGlobalRegionAllRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllRight.setObjectName(u"buttonGlobalRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionAllRight.setMaximumSize(QSize(40, 41))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.buttonGlobalRegionAllRight.setFont(font5)
        icon2 = QIcon()
        icon2.addFile(u":/arrows/images/icons8-end-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionAllRight.setIcon(icon2)
        self.buttonGlobalRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_39.addWidget(self.buttonGlobalRegionAllRight)

        self.buttonGlobalRegionRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionRight.setObjectName(u"buttonGlobalRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionRight.setMaximumSize(QSize(40, 41))
        self.buttonGlobalRegionRight.setFont(font5)
        icon3 = QIcon()
        icon3.addFile(u":/arrows/images/icons8-sort-right-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionRight.setIcon(icon3)
        self.buttonGlobalRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_39.addWidget(self.buttonGlobalRegionRight)

        self.buttonGlobalRegionLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionLeft.setObjectName(u"buttonGlobalRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalRegionLeft.setFont(font5)
        icon4 = QIcon()
        icon4.addFile(u":/arrows/images/icons8-sort-left-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionLeft.setIcon(icon4)

        self.verticalLayout_39.addWidget(self.buttonGlobalRegionLeft)

        self.buttonGlobalRegionAllLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllLeft.setObjectName(u"buttonGlobalRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalRegionAllLeft.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u":/arrows/images/icons8-skip-to-start-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionAllLeft.setIcon(icon5)
        self.buttonGlobalRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_39.addWidget(self.buttonGlobalRegionAllLeft)

        self.verticalSpacerGlobalRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacerGlobalRegionLeftRightBottom)


        self.horizontalLayout_8.addWidget(self.frameGlobalRegionLeftRight)

        self.frameGlobalSelectedRegions = QFrame(self.frameGlobalRegions)
        self.frameGlobalSelectedRegions.setObjectName(u"frameGlobalSelectedRegions")
        sizePolicy5.setHeightForWidth(self.frameGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.frameGlobalSelectedRegions.setSizePolicy(sizePolicy5)
        self.frameGlobalSelectedRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalSelectedRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalSelectedRegions.setLineWidth(0)
        self.verticalLayout_50 = QVBoxLayout(self.frameGlobalSelectedRegions)
        self.verticalLayout_50.setSpacing(10)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalSelectedRegions = QLabel(self.frameGlobalSelectedRegions)
        self.labelGlobalSelectedRegions.setObjectName(u"labelGlobalSelectedRegions")
        sizePolicy8.setHeightForWidth(self.labelGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedRegions.setSizePolicy(sizePolicy8)
        self.labelGlobalSelectedRegions.setFont(font)
        self.labelGlobalSelectedRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_50.addWidget(self.labelGlobalSelectedRegions)

        self.listWidgetGlobalSelectedRegions = CustomListSelfDrag(self.frameGlobalSelectedRegions)
        self.listWidgetGlobalSelectedRegions.setObjectName(u"listWidgetGlobalSelectedRegions")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedRegions.setSizePolicy(sizePolicy9)
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

        self.verticalLayout_50.addWidget(self.listWidgetGlobalSelectedRegions)


        self.horizontalLayout_8.addWidget(self.frameGlobalSelectedRegions)

        self.frameGlobalRegionUpDown = QFrame(self.frameGlobalRegions)
        self.frameGlobalRegionUpDown.setObjectName(u"frameGlobalRegionUpDown")
        sizePolicy5.setHeightForWidth(self.frameGlobalRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionUpDown.setSizePolicy(sizePolicy5)
        self.frameGlobalRegionUpDown.setMinimumSize(QSize(64, 0))
        self.frameGlobalRegionUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalRegionUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalRegionUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalRegionUpDown.setLineWidth(0)
        self.verticalLayout_51 = QVBoxLayout(self.frameGlobalRegionUpDown)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalSpacerGlobalRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacerGlobalRegionUpDownTop)

        self.buttonGlobalRegionUp = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionUp.setObjectName(u"buttonGlobalRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionUp.setMaximumSize(QSize(40, 41))
        self.buttonGlobalRegionUp.setFont(font5)
        icon6 = QIcon()
        icon6.addFile(u":/arrows/images/icons8-sort-up-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionUp.setIcon(icon6)

        self.verticalLayout_51.addWidget(self.buttonGlobalRegionUp)

        self.buttonGlobalRegionDown = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionDown.setObjectName(u"buttonGlobalRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionDown.setMaximumSize(QSize(40, 41))
        self.buttonGlobalRegionDown.setFont(font5)
        icon7 = QIcon()
        icon7.addFile(u":/arrows/images/icons8-sort-down-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonGlobalRegionDown.setIcon(icon7)

        self.verticalLayout_51.addWidget(self.buttonGlobalRegionDown)

        self.verticalSpacerGlobalRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacerGlobalRegionUpDownBottom)


        self.horizontalLayout_8.addWidget(self.frameGlobalRegionUpDown)

        self.horizontalSpacerGlobalRegions = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacerGlobalRegions)


        self.verticalLayout_47.addWidget(self.frameGlobalRegions)

        self.verticalLayoutGlobalRegions = QVBoxLayout()
        self.verticalLayoutGlobalRegions.setSpacing(10)
        self.verticalLayoutGlobalRegions.setObjectName(u"verticalLayoutGlobalRegions")
        self.verticalSpacerGlobalRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayoutGlobalRegions.addItem(self.verticalSpacerGlobalRegionsEnglishButton)

        self.buttonGlobalDefaultRegionOrder = QPushButton(self.tabContentsGlobalRegions)
        self.buttonGlobalDefaultRegionOrder.setObjectName(u"buttonGlobalDefaultRegionOrder")
        sizePolicy6.setHeightForWidth(self.buttonGlobalDefaultRegionOrder.sizePolicy().hasHeightForWidth())
        self.buttonGlobalDefaultRegionOrder.setSizePolicy(sizePolicy6)
        self.buttonGlobalDefaultRegionOrder.setMinimumSize(QSize(286, 41))

        self.verticalLayoutGlobalRegions.addWidget(self.buttonGlobalDefaultRegionOrder)


        self.verticalLayout_47.addLayout(self.verticalLayoutGlobalRegions)

        self.verticalLayout_47.setStretch(3, 1)

        self.verticalLayout_46.addWidget(self.tabContentsGlobalRegions)

        self.scrollAreaGlobalRegions.setWidget(self.scrollAreaWidgetContentsGlobalRegions)

        self.gridLayout_9.addWidget(self.scrollAreaGlobalRegions, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalRegions, "")
        self.tabGlobalLanguages = QWidget()
        self.tabGlobalLanguages.setObjectName(u"tabGlobalLanguages")
        self.gridLayout_11 = QGridLayout(self.tabGlobalLanguages)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollAreaGlobalLanguages = QScrollArea(self.tabGlobalLanguages)
        self.scrollAreaGlobalLanguages.setObjectName(u"scrollAreaGlobalLanguages")
        self.scrollAreaGlobalLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalLanguages.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalLanguages.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalLanguages = QWidget()
        self.scrollAreaWidgetContentsGlobalLanguages.setObjectName(u"scrollAreaWidgetContentsGlobalLanguages")
        self.scrollAreaWidgetContentsGlobalLanguages.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalLanguages.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalLanguages.setSizePolicy(sizePolicy)
        self.verticalLayout_52 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalLanguages)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalLanguages = QFrame(self.scrollAreaWidgetContentsGlobalLanguages)
        self.tabContentsGlobalLanguages.setObjectName(u"tabContentsGlobalLanguages")
        self.tabContentsGlobalLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalLanguages.setLineWidth(0)
        self.verticalLayout_53 = QVBoxLayout(self.tabContentsGlobalLanguages)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalLanguages = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalLanguages.setObjectName(u"horizontalLayoutHeaderGlobalLanguages")
        self.labelGlobalFilterByLanguages = QLabel(self.tabContentsGlobalLanguages)
        self.labelGlobalFilterByLanguages.setObjectName(u"labelGlobalFilterByLanguages")
        sizePolicy3.setHeightForWidth(self.labelGlobalFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByLanguages.setSizePolicy(sizePolicy3)
        self.labelGlobalFilterByLanguages.setMinimumSize(QSize(0, 0))
        self.labelGlobalFilterByLanguages.setFont(font2)

        self.horizontalLayoutHeaderGlobalLanguages.addWidget(self.labelGlobalFilterByLanguages)

        self.frameOverrideGlobalLanguages = QFrame(self.tabContentsGlobalLanguages)
        self.frameOverrideGlobalLanguages.setObjectName(u"frameOverrideGlobalLanguages")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalLanguages.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalLanguages.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalLanguages.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_54 = QVBoxLayout(self.frameOverrideGlobalLanguages)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalLanguages.addWidget(self.frameOverrideGlobalLanguages)

        self.horizontalLayoutHeaderGlobalLanguages.setStretch(0, 1)

        self.verticalLayout_53.addLayout(self.horizontalLayoutHeaderGlobalLanguages)

        self.lineGlobalLanguages = QFrame(self.tabContentsGlobalLanguages)
        self.lineGlobalLanguages.setObjectName(u"lineGlobalLanguages")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalLanguages.setPalette(palette3)
        self.lineGlobalLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalLanguages.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_53.addWidget(self.lineGlobalLanguages)

        self.frameGlobalLanguages = QFrame(self.tabContentsGlobalLanguages)
        self.frameGlobalLanguages.setObjectName(u"frameGlobalLanguages")
        self.frameGlobalLanguages.setMinimumSize(QSize(0, 64))
        self.frameGlobalLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalLanguages.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frameGlobalLanguages)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalAvailableLanguages = QFrame(self.frameGlobalLanguages)
        self.frameGlobalAvailableLanguages.setObjectName(u"frameGlobalAvailableLanguages")
        sizePolicy5.setHeightForWidth(self.frameGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.frameGlobalAvailableLanguages.setSizePolicy(sizePolicy5)
        self.frameGlobalAvailableLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalAvailableLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalAvailableLanguages.setLineWidth(0)
        self.verticalLayout_40 = QVBoxLayout(self.frameGlobalAvailableLanguages)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalAvailableLanguages = QLabel(self.frameGlobalAvailableLanguages)
        self.labelGlobalAvailableLanguages.setObjectName(u"labelGlobalAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalAvailableLanguages.setFont(font)
        self.labelGlobalAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_40.addWidget(self.labelGlobalAvailableLanguages)

        self.listWidgetGlobalAvailableLanguages = CustomList(self.frameGlobalAvailableLanguages)
        self.listWidgetGlobalAvailableLanguages.setObjectName(u"listWidgetGlobalAvailableLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetGlobalAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalAvailableLanguages.setSortingEnabled(True)
        self.listWidgetGlobalAvailableLanguages.setProperty(u"self_drag", False)
        self.listWidgetGlobalAvailableLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_40.addWidget(self.listWidgetGlobalAvailableLanguages)


        self.horizontalLayout_9.addWidget(self.frameGlobalAvailableLanguages)

        self.frameGlobalLanguageLeftRight = QFrame(self.frameGlobalLanguages)
        self.frameGlobalLanguageLeftRight.setObjectName(u"frameGlobalLanguageLeftRight")
        sizePolicy5.setHeightForWidth(self.frameGlobalLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageLeftRight.setSizePolicy(sizePolicy5)
        self.frameGlobalLanguageLeftRight.setMinimumSize(QSize(64, 0))
        self.frameGlobalLanguageLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalLanguageLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLanguageLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalLanguageLeftRight.setLineWidth(0)
        self.verticalLayout_55 = QVBoxLayout(self.frameGlobalLanguageLeftRight)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalSpacerGlobalLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacerGlobalLanguageLeftRightTop)

        self.buttonGlobalLanguageAllRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllRight.setObjectName(u"buttonGlobalLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllRight.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllRight.setFont(font5)
        self.buttonGlobalLanguageAllRight.setIcon(icon2)
        self.buttonGlobalLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_55.addWidget(self.buttonGlobalLanguageAllRight)

        self.buttonGlobalLanguageRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageRight.setObjectName(u"buttonGlobalLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageRight.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageRight.setFont(font5)
        self.buttonGlobalLanguageRight.setIcon(icon3)
        self.buttonGlobalLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_55.addWidget(self.buttonGlobalLanguageRight)

        self.buttonGlobalLanguageLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageLeft.setObjectName(u"buttonGlobalLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageLeft.setFont(font5)
        self.buttonGlobalLanguageLeft.setIcon(icon4)

        self.verticalLayout_55.addWidget(self.buttonGlobalLanguageLeft)

        self.buttonGlobalLanguageAllLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllLeft.setObjectName(u"buttonGlobalLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllLeft.setFont(font5)
        self.buttonGlobalLanguageAllLeft.setIcon(icon5)
        self.buttonGlobalLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_55.addWidget(self.buttonGlobalLanguageAllLeft)

        self.verticalSpacerGlobalLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacerGlobalLanguageLeftRightBottom)

        self.verticalSpacerGlobalLanguageLeftRightBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_55.addItem(self.verticalSpacerGlobalLanguageLeftRightBottomBuffer)


        self.horizontalLayout_9.addWidget(self.frameGlobalLanguageLeftRight)

        self.frameGlobalSelectedLanguages = QFrame(self.frameGlobalLanguages)
        self.frameGlobalSelectedLanguages.setObjectName(u"frameGlobalSelectedLanguages")
        sizePolicy5.setHeightForWidth(self.frameGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.frameGlobalSelectedLanguages.setSizePolicy(sizePolicy5)
        self.frameGlobalSelectedLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalSelectedLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalSelectedLanguages.setLineWidth(0)
        self.verticalLayout_56 = QVBoxLayout(self.frameGlobalSelectedLanguages)
        self.verticalLayout_56.setSpacing(10)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalSelectedLanguages = QLabel(self.frameGlobalSelectedLanguages)
        self.labelGlobalSelectedLanguages.setObjectName(u"labelGlobalSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalSelectedLanguages.setFont(font)
        self.labelGlobalSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_56.addWidget(self.labelGlobalSelectedLanguages)

        self.listWidgetGlobalSelectedLanguages = CustomListSelfDrag(self.frameGlobalSelectedLanguages)
        self.listWidgetGlobalSelectedLanguages.setObjectName(u"listWidgetGlobalSelectedLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetGlobalSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalSelectedLanguages.setProperty(u"self_drag", True)
        self.listWidgetGlobalSelectedLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_56.addWidget(self.listWidgetGlobalSelectedLanguages)


        self.horizontalLayout_9.addWidget(self.frameGlobalSelectedLanguages)

        self.frameGlobalLanguageUpDown = QFrame(self.frameGlobalLanguages)
        self.frameGlobalLanguageUpDown.setObjectName(u"frameGlobalLanguageUpDown")
        sizePolicy5.setHeightForWidth(self.frameGlobalLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageUpDown.setSizePolicy(sizePolicy5)
        self.frameGlobalLanguageUpDown.setMinimumSize(QSize(64, 0))
        self.frameGlobalLanguageUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalLanguageUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLanguageUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalLanguageUpDown.setLineWidth(0)
        self.verticalLayout_57 = QVBoxLayout(self.frameGlobalLanguageUpDown)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalSpacerGlobalLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacerGlobalLanguageUpDownTop)

        self.buttonGlobalLanguageUp = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageUp.setObjectName(u"buttonGlobalLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageUp.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageUp.setFont(font5)
        self.buttonGlobalLanguageUp.setIcon(icon6)

        self.verticalLayout_57.addWidget(self.buttonGlobalLanguageUp)

        self.buttonGlobalLanguageDown = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageDown.setObjectName(u"buttonGlobalLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageDown.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLanguageDown.setFont(font5)
        self.buttonGlobalLanguageDown.setIcon(icon7)

        self.verticalLayout_57.addWidget(self.buttonGlobalLanguageDown)

        self.verticalSpacerGlobalLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacerGlobalLanguageUpDownBottom)

        self.verticalSpacerGlobalLanguageUpDownBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_57.addItem(self.verticalSpacerGlobalLanguageUpDownBottomBuffer)


        self.horizontalLayout_9.addWidget(self.frameGlobalLanguageUpDown)

        self.horizontalSpacerGlobalLanguages = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacerGlobalLanguages)


        self.verticalLayout_53.addWidget(self.frameGlobalLanguages)


        self.verticalLayout_52.addWidget(self.tabContentsGlobalLanguages)

        self.scrollAreaGlobalLanguages.setWidget(self.scrollAreaWidgetContentsGlobalLanguages)

        self.gridLayout_11.addWidget(self.scrollAreaGlobalLanguages, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalLanguages, "")
        self.tabGlobalVideo = QWidget()
        self.tabGlobalVideo.setObjectName(u"tabGlobalVideo")
        self.gridLayout_12 = QGridLayout(self.tabGlobalVideo)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollAreaGlobalVideo = QScrollArea(self.tabGlobalVideo)
        self.scrollAreaGlobalVideo.setObjectName(u"scrollAreaGlobalVideo")
        self.scrollAreaGlobalVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalVideo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalVideo.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalVideo = QWidget()
        self.scrollAreaWidgetContentsGlobalVideo.setObjectName(u"scrollAreaWidgetContentsGlobalVideo")
        self.scrollAreaWidgetContentsGlobalVideo.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalVideo.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalVideo.setSizePolicy(sizePolicy)
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalVideo)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalVideo = QFrame(self.scrollAreaWidgetContentsGlobalVideo)
        self.tabContentsGlobalVideo.setObjectName(u"tabContentsGlobalVideo")
        self.tabContentsGlobalVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalVideo.setLineWidth(0)
        self.verticalLayout_59 = QVBoxLayout(self.tabContentsGlobalVideo)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderVideo = QHBoxLayout()
        self.horizontalLayoutHeaderVideo.setObjectName(u"horizontalLayoutHeaderVideo")
        self.labelGlobalFilterByVideo = QLabel(self.tabContentsGlobalVideo)
        self.labelGlobalFilterByVideo.setObjectName(u"labelGlobalFilterByVideo")
        sizePolicy3.setHeightForWidth(self.labelGlobalFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByVideo.setSizePolicy(sizePolicy3)
        self.labelGlobalFilterByVideo.setMinimumSize(QSize(0, 0))
        self.labelGlobalFilterByVideo.setFont(font2)

        self.horizontalLayoutHeaderVideo.addWidget(self.labelGlobalFilterByVideo)

        self.frameOverrideGlobalVideo = QFrame(self.tabContentsGlobalVideo)
        self.frameOverrideGlobalVideo.setObjectName(u"frameOverrideGlobalVideo")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalVideo.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalVideo.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalVideo.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_60 = QVBoxLayout(self.frameOverrideGlobalVideo)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderVideo.addWidget(self.frameOverrideGlobalVideo)

        self.horizontalLayoutHeaderVideo.setStretch(0, 1)

        self.verticalLayout_59.addLayout(self.horizontalLayoutHeaderVideo)

        self.lineGlobalVideoStandards = QFrame(self.tabContentsGlobalVideo)
        self.lineGlobalVideoStandards.setObjectName(u"lineGlobalVideoStandards")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalVideoStandards.setPalette(palette4)
        self.lineGlobalVideoStandards.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalVideoStandards.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_59.addWidget(self.lineGlobalVideoStandards)

        self.frameGlobalVideo = QFrame(self.tabContentsGlobalVideo)
        self.frameGlobalVideo.setObjectName(u"frameGlobalVideo")
        self.frameGlobalVideo.setMinimumSize(QSize(0, 64))
        self.frameGlobalVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalVideo.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.frameGlobalVideo)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalVideoOrder = QFrame(self.frameGlobalVideo)
        self.frameGlobalVideoOrder.setObjectName(u"frameGlobalVideoOrder")
        sizePolicy5.setHeightForWidth(self.frameGlobalVideoOrder.sizePolicy().hasHeightForWidth())
        self.frameGlobalVideoOrder.setSizePolicy(sizePolicy5)
        self.frameGlobalVideoOrder.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalVideoOrder.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalVideoOrder.setLineWidth(0)
        self.verticalLayout_61 = QVBoxLayout(self.frameGlobalVideoOrder)
        self.verticalLayout_61.setSpacing(10)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalVideoStandardsOrder = QLabel(self.frameGlobalVideoOrder)
        self.labelGlobalVideoStandardsOrder.setObjectName(u"labelGlobalVideoStandardsOrder")
        sizePolicy8.setHeightForWidth(self.labelGlobalVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelGlobalVideoStandardsOrder.setSizePolicy(sizePolicy8)
        self.labelGlobalVideoStandardsOrder.setFont(font)
        self.labelGlobalVideoStandardsOrder.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_61.addWidget(self.labelGlobalVideoStandardsOrder)

        self.listWidgetGlobalVideoStandards = CustomListSelfDrag(self.frameGlobalVideoOrder)
        self.listWidgetGlobalVideoStandards.setObjectName(u"listWidgetGlobalVideoStandards")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalVideoStandards.setSizePolicy(sizePolicy9)
        self.listWidgetGlobalVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalVideoStandards.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalVideoStandards.setTabKeyNavigation(True)
        self.listWidgetGlobalVideoStandards.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalVideoStandards.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalVideoStandards.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalVideoStandards.setAlternatingRowColors(False)
        self.listWidgetGlobalVideoStandards.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalVideoStandards.setProperty(u"self_drag", True)
        self.listWidgetGlobalVideoStandards.setProperty(u"is_drag_drop", True)

        self.verticalLayout_61.addWidget(self.listWidgetGlobalVideoStandards)


        self.horizontalLayout_10.addWidget(self.frameGlobalVideoOrder)

        self.frameGlobalVideoStandardUpDown = QFrame(self.frameGlobalVideo)
        self.frameGlobalVideoStandardUpDown.setObjectName(u"frameGlobalVideoStandardUpDown")
        sizePolicy5.setHeightForWidth(self.frameGlobalVideoStandardUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalVideoStandardUpDown.setSizePolicy(sizePolicy5)
        self.frameGlobalVideoStandardUpDown.setMinimumSize(QSize(64, 0))
        self.frameGlobalVideoStandardUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalVideoStandardUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalVideoStandardUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalVideoStandardUpDown.setLineWidth(0)
        self.verticalLayout_64 = QVBoxLayout(self.frameGlobalVideoStandardUpDown)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalSpacerGlobalVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacerGlobalVideoUpDownTop)

        self.buttonGlobalVideoStandardUp = QPushButton(self.frameGlobalVideoStandardUpDown)
        self.buttonGlobalVideoStandardUp.setObjectName(u"buttonGlobalVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardUp.setMaximumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardUp.setFont(font5)
        self.buttonGlobalVideoStandardUp.setIcon(icon6)

        self.verticalLayout_64.addWidget(self.buttonGlobalVideoStandardUp)

        self.buttonGlobalVideoStandardDown = QPushButton(self.frameGlobalVideoStandardUpDown)
        self.buttonGlobalVideoStandardDown.setObjectName(u"buttonGlobalVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardDown.setMaximumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardDown.setFont(font5)
        self.buttonGlobalVideoStandardDown.setIcon(icon7)

        self.verticalLayout_64.addWidget(self.buttonGlobalVideoStandardDown)

        self.verticalSpacerGlobalVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacerGlobalVideoUpDownBottom)

        self.verticalSpacerGlobalVideoUpDownBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_64.addItem(self.verticalSpacerGlobalVideoUpDownBottomBuffer)


        self.horizontalLayout_10.addWidget(self.frameGlobalVideoStandardUpDown)

        self.horizontalSpacerGlobalVideo = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacerGlobalVideo)


        self.verticalLayout_59.addWidget(self.frameGlobalVideo)


        self.verticalLayout_58.addWidget(self.tabContentsGlobalVideo)

        self.scrollAreaGlobalVideo.setWidget(self.scrollAreaWidgetContentsGlobalVideo)

        self.gridLayout_12.addWidget(self.scrollAreaGlobalVideo, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalVideo, "")
        self.tabGlobalExclusions = QWidget()
        self.tabGlobalExclusions.setObjectName(u"tabGlobalExclusions")
        self.gridLayout_13 = QGridLayout(self.tabGlobalExclusions)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scrollAreaGlobalExclusions = QScrollArea(self.tabGlobalExclusions)
        self.scrollAreaGlobalExclusions.setObjectName(u"scrollAreaGlobalExclusions")
        self.scrollAreaGlobalExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalExclusions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalExclusions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalExclusions = QWidget()
        self.scrollAreaWidgetContentsGlobalExclusions.setObjectName(u"scrollAreaWidgetContentsGlobalExclusions")
        self.scrollAreaWidgetContentsGlobalExclusions.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalExclusions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalExclusions.setSizePolicy(sizePolicy)
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalExclusions)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalExclusions = QFrame(self.scrollAreaWidgetContentsGlobalExclusions)
        self.tabContentsGlobalExclusions.setObjectName(u"tabContentsGlobalExclusions")
        self.tabContentsGlobalExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalExclusions.setLineWidth(0)
        self.verticalLayout_63 = QVBoxLayout(self.tabContentsGlobalExclusions)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalExclusions = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalExclusions.setObjectName(u"horizontalLayoutHeaderGlobalExclusions")
        self.labelGlobalExclusions = QLabel(self.tabContentsGlobalExclusions)
        self.labelGlobalExclusions.setObjectName(u"labelGlobalExclusions")
        sizePolicy3.setHeightForWidth(self.labelGlobalExclusions.sizePolicy().hasHeightForWidth())
        self.labelGlobalExclusions.setSizePolicy(sizePolicy3)
        self.labelGlobalExclusions.setMinimumSize(QSize(0, 0))
        self.labelGlobalExclusions.setFont(font2)

        self.horizontalLayoutHeaderGlobalExclusions.addWidget(self.labelGlobalExclusions)

        self.frameOverrideGlobalExclusions = QFrame(self.tabContentsGlobalExclusions)
        self.frameOverrideGlobalExclusions.setObjectName(u"frameOverrideGlobalExclusions")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalExclusions.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalExclusions.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalExclusions.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_65 = QVBoxLayout(self.frameOverrideGlobalExclusions)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalExclusions.addWidget(self.frameOverrideGlobalExclusions)

        self.horizontalLayoutHeaderGlobalExclusions.setStretch(0, 1)

        self.verticalLayout_63.addLayout(self.horizontalLayoutHeaderGlobalExclusions)

        self.lineGlobalExclusions = QFrame(self.tabContentsGlobalExclusions)
        self.lineGlobalExclusions.setObjectName(u"lineGlobalExclusions")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalExclusions.setPalette(palette5)
        self.lineGlobalExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalExclusions.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_63.addWidget(self.lineGlobalExclusions)

        self.horizontalLayoutGlobalExclusions = QHBoxLayout()
        self.horizontalLayoutGlobalExclusions.setSpacing(24)
        self.horizontalLayoutGlobalExclusions.setObjectName(u"horizontalLayoutGlobalExclusions")
        self.verticalLayout1GlobalExclusions = QVBoxLayout()
        self.verticalLayout1GlobalExclusions.setSpacing(8)
        self.verticalLayout1GlobalExclusions.setObjectName(u"verticalLayout1GlobalExclusions")
        self.checkBoxGlobalExcludeAddOns = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeAddOns.setObjectName(u"checkBoxGlobalExcludeAddOns")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeAddOns)

        self.checkBoxGlobalExcludeApplications = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeApplications.setObjectName(u"checkBoxGlobalExcludeApplications")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeApplications)

        self.checkBoxGlobalExcludeAudio = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeAudio.setObjectName(u"checkBoxGlobalExcludeAudio")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeAudio)

        self.checkBoxGlobalExcludeBadDumps = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeBadDumps.setObjectName(u"checkBoxGlobalExcludeBadDumps")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeBadDumps)

        self.checkBoxGlobalExcludeBIOS = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeBIOS.setObjectName(u"checkBoxGlobalExcludeBIOS")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeBIOS)

        self.checkBoxGlobalExcludeBonusDiscs = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeBonusDiscs.setObjectName(u"checkBoxGlobalExcludeBonusDiscs")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeBonusDiscs)

        self.checkBoxGlobalExcludeCoverdiscs = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeCoverdiscs.setObjectName(u"checkBoxGlobalExcludeCoverdiscs")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeCoverdiscs)

        self.checkBoxGlobalExcludeDemos = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeDemos.setObjectName(u"checkBoxGlobalExcludeDemos")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeDemos)

        self.checkBoxGlobalExcludeEducational = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeEducational.setObjectName(u"checkBoxGlobalExcludeEducational")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeEducational)

        self.checkBoxGlobalExcludeGames = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeGames.setObjectName(u"checkBoxGlobalExcludeGames")

        self.verticalLayout1GlobalExclusions.addWidget(self.checkBoxGlobalExcludeGames)

        self.verticalSpacer1GlobalExclusions = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout1GlobalExclusions.addItem(self.verticalSpacer1GlobalExclusions)


        self.horizontalLayoutGlobalExclusions.addLayout(self.verticalLayout1GlobalExclusions)

        self.verticalLayout2GlobalExclusions = QVBoxLayout()
        self.verticalLayout2GlobalExclusions.setSpacing(8)
        self.verticalLayout2GlobalExclusions.setObjectName(u"verticalLayout2GlobalExclusions")
        self.checkBoxGlobalExcludeManuals = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeManuals.setObjectName(u"checkBoxGlobalExcludeManuals")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludeManuals)

        self.checkBoxGlobalExcludeMIA = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeMIA.setObjectName(u"checkBoxGlobalExcludeMIA")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludeMIA)

        self.checkBoxGlobalExcludeMultimedia = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeMultimedia.setObjectName(u"checkBoxGlobalExcludeMultimedia")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludeMultimedia)

        self.checkBoxGlobalExcludePreproduction = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludePreproduction.setObjectName(u"checkBoxGlobalExcludePreproduction")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludePreproduction)

        self.checkBoxGlobalExcludePromotional = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludePromotional.setObjectName(u"checkBoxGlobalExcludePromotional")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludePromotional)

        self.checkBoxGlobalExcludeUnlicensedAll = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeUnlicensedAll.setObjectName(u"checkBoxGlobalExcludeUnlicensedAll")
        self.checkBoxGlobalExcludeUnlicensedAll.setTristate(False)

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludeUnlicensedAll)

        self.frameUnlicensedSubOptionsGlobalExclusions = QFrame(self.tabContentsGlobalExclusions)
        self.frameUnlicensedSubOptionsGlobalExclusions.setObjectName(u"frameUnlicensedSubOptionsGlobalExclusions")
        self.frameUnlicensedSubOptionsGlobalExclusions.setMinimumSize(QSize(0, 40))
        self.frameUnlicensedSubOptionsGlobalExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameUnlicensedSubOptionsGlobalExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameUnlicensedSubOptionsGlobalExclusions.setLineWidth(0)
        self.horizontalLayout_12 = QHBoxLayout(self.frameUnlicensedSubOptionsGlobalExclusions)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerUnlicensedSubOptionsGlobalExclusions = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacerUnlicensedSubOptionsGlobalExclusions)

        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions = QVBoxLayout()
        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions.setSpacing(8)
        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions.setObjectName(u"verticalLayoutUnlicensedSubOptionsGlobalExclusions")
        self.checkBoxGlobalExcludeAftermarket = QCheckBox(self.frameUnlicensedSubOptionsGlobalExclusions)
        self.checkBoxGlobalExcludeAftermarket.setObjectName(u"checkBoxGlobalExcludeAftermarket")

        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions.addWidget(self.checkBoxGlobalExcludeAftermarket)

        self.checkBoxGlobalExcludePirate = QCheckBox(self.frameUnlicensedSubOptionsGlobalExclusions)
        self.checkBoxGlobalExcludePirate.setObjectName(u"checkBoxGlobalExcludePirate")

        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions.addWidget(self.checkBoxGlobalExcludePirate)

        self.checkBoxGlobalExcludeUnlicensed = QCheckBox(self.frameUnlicensedSubOptionsGlobalExclusions)
        self.checkBoxGlobalExcludeUnlicensed.setObjectName(u"checkBoxGlobalExcludeUnlicensed")

        self.verticalLayoutUnlicensedSubOptionsGlobalExclusions.addWidget(self.checkBoxGlobalExcludeUnlicensed)


        self.horizontalLayout_12.addLayout(self.verticalLayoutUnlicensedSubOptionsGlobalExclusions)


        self.verticalLayout2GlobalExclusions.addWidget(self.frameUnlicensedSubOptionsGlobalExclusions)

        self.checkBoxGlobalExcludeVideo = QCheckBox(self.tabContentsGlobalExclusions)
        self.checkBoxGlobalExcludeVideo.setObjectName(u"checkBoxGlobalExcludeVideo")

        self.verticalLayout2GlobalExclusions.addWidget(self.checkBoxGlobalExcludeVideo)

        self.verticalSpacer2GlobalExclusions = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout2GlobalExclusions.addItem(self.verticalSpacer2GlobalExclusions)


        self.horizontalLayoutGlobalExclusions.addLayout(self.verticalLayout2GlobalExclusions)

        self.verticalLayout3GlobalExclusions = QVBoxLayout()
        self.verticalLayout3GlobalExclusions.setObjectName(u"verticalLayout3GlobalExclusions")
        self.frameGlobalExclusionsSelectDeselect = QFrame(self.tabContentsGlobalExclusions)
        self.frameGlobalExclusionsSelectDeselect.setObjectName(u"frameGlobalExclusionsSelectDeselect")
        self.frameGlobalExclusionsSelectDeselect.setMinimumSize(QSize(0, 20))
        self.frameGlobalExclusionsSelectDeselect.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalExclusionsSelectDeselect.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalExclusionsSelectDeselect.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frameGlobalExclusionsSelectDeselect)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.buttonGlobalSelectAllExclude = QPushButton(self.frameGlobalExclusionsSelectDeselect)
        self.buttonGlobalSelectAllExclude.setObjectName(u"buttonGlobalSelectAllExclude")
        sizePolicy6.setHeightForWidth(self.buttonGlobalSelectAllExclude.sizePolicy().hasHeightForWidth())
        self.buttonGlobalSelectAllExclude.setSizePolicy(sizePolicy6)
        self.buttonGlobalSelectAllExclude.setMinimumSize(QSize(120, 30))

        self.verticalLayout_6.addWidget(self.buttonGlobalSelectAllExclude)

        self.buttonGlobalDeselectAllExclude = QPushButton(self.frameGlobalExclusionsSelectDeselect)
        self.buttonGlobalDeselectAllExclude.setObjectName(u"buttonGlobalDeselectAllExclude")
        sizePolicy6.setHeightForWidth(self.buttonGlobalDeselectAllExclude.sizePolicy().hasHeightForWidth())
        self.buttonGlobalDeselectAllExclude.setSizePolicy(sizePolicy6)
        self.buttonGlobalDeselectAllExclude.setMinimumSize(QSize(120, 30))

        self.verticalLayout_6.addWidget(self.buttonGlobalDeselectAllExclude)


        self.verticalLayout3GlobalExclusions.addWidget(self.frameGlobalExclusionsSelectDeselect)

        self.verticalSpacer3GlobalExclusions = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout3GlobalExclusions.addItem(self.verticalSpacer3GlobalExclusions)

        self.verticalLayout3GlobalExclusions.setStretch(1, 4)

        self.horizontalLayoutGlobalExclusions.addLayout(self.verticalLayout3GlobalExclusions)

        self.horizontalSpacerGlobalExclusions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclusions)


        self.verticalLayout_63.addLayout(self.horizontalLayoutGlobalExclusions)

        self.verticalSpacerGlobalExclusions = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacerGlobalExclusions)


        self.verticalLayout_62.addWidget(self.tabContentsGlobalExclusions)

        self.scrollAreaGlobalExclusions.setWidget(self.scrollAreaWidgetContentsGlobalExclusions)

        self.gridLayout_13.addWidget(self.scrollAreaGlobalExclusions, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalExclusions, "")
        self.tabGlobalLocalization = QWidget()
        self.tabGlobalLocalization.setObjectName(u"tabGlobalLocalization")
        self.gridLayout_14 = QGridLayout(self.tabGlobalLocalization)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.scrollAreaGlobalLocalization = QScrollArea(self.tabGlobalLocalization)
        self.scrollAreaGlobalLocalization.setObjectName(u"scrollAreaGlobalLocalization")
        self.scrollAreaGlobalLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalLocalization.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalLocalization.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalLocalization = QWidget()
        self.scrollAreaWidgetContentsGlobalLocalization.setObjectName(u"scrollAreaWidgetContentsGlobalLocalization")
        self.scrollAreaWidgetContentsGlobalLocalization.setGeometry(QRect(0, 0, 649, 429))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalLocalization.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalLocalization.setSizePolicy(sizePolicy)
        self.verticalLayout_66 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalLocalization)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalLocalization = QFrame(self.scrollAreaWidgetContentsGlobalLocalization)
        self.tabContentsGlobalLocalization.setObjectName(u"tabContentsGlobalLocalization")
        self.tabContentsGlobalLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalLocalization.setLineWidth(0)
        self.verticalLayout_67 = QVBoxLayout(self.tabContentsGlobalLocalization)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalLocalization = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalLocalization.setObjectName(u"horizontalLayoutHeaderGlobalLocalization")
        self.labelGlobalUseLocalNames = QLabel(self.tabContentsGlobalLocalization)
        self.labelGlobalUseLocalNames.setObjectName(u"labelGlobalUseLocalNames")
        sizePolicy3.setHeightForWidth(self.labelGlobalUseLocalNames.sizePolicy().hasHeightForWidth())
        self.labelGlobalUseLocalNames.setSizePolicy(sizePolicy3)
        self.labelGlobalUseLocalNames.setMinimumSize(QSize(0, 0))
        self.labelGlobalUseLocalNames.setFont(font2)

        self.horizontalLayoutHeaderGlobalLocalization.addWidget(self.labelGlobalUseLocalNames)

        self.frameOverrideGlobalLocalization = QFrame(self.tabContentsGlobalLocalization)
        self.frameOverrideGlobalLocalization.setObjectName(u"frameOverrideGlobalLocalization")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalLocalization.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalLocalization.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalLocalization.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_68 = QVBoxLayout(self.frameOverrideGlobalLocalization)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalLocalization.addWidget(self.frameOverrideGlobalLocalization)

        self.horizontalLayoutHeaderGlobalLocalization.setStretch(0, 1)

        self.verticalLayout_67.addLayout(self.horizontalLayoutHeaderGlobalLocalization)

        self.lineGlobalLocalization = QFrame(self.tabContentsGlobalLocalization)
        self.lineGlobalLocalization.setObjectName(u"lineGlobalLocalization")
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalLocalization.setPalette(palette6)
        self.lineGlobalLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalLocalization.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_67.addWidget(self.lineGlobalLocalization)

        self.labelGlobalLocalizeNames = QLabel(self.tabContentsGlobalLocalization)
        self.labelGlobalLocalizeNames.setObjectName(u"labelGlobalLocalizeNames")
        self.labelGlobalLocalizeNames.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalLocalizeNames.setWordWrap(True)
        self.labelGlobalLocalizeNames.setOpenExternalLinks(True)
        self.labelGlobalLocalizeNames.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_67.addWidget(self.labelGlobalLocalizeNames)

        self.verticalSpacerGlobalLocalizationList = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_67.addItem(self.verticalSpacerGlobalLocalizationList)

        self.frameGlobalLocalization = QFrame(self.tabContentsGlobalLocalization)
        self.frameGlobalLocalization.setObjectName(u"frameGlobalLocalization")
        self.frameGlobalLocalization.setMinimumSize(QSize(0, 64))
        self.frameGlobalLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frameGlobalLocalization)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalAvailableLocalization = QFrame(self.frameGlobalLocalization)
        self.frameGlobalAvailableLocalization.setObjectName(u"frameGlobalAvailableLocalization")
        sizePolicy5.setHeightForWidth(self.frameGlobalAvailableLocalization.sizePolicy().hasHeightForWidth())
        self.frameGlobalAvailableLocalization.setSizePolicy(sizePolicy5)
        self.frameGlobalAvailableLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalAvailableLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalAvailableLocalization.setLineWidth(0)
        self.verticalLayout_69 = QVBoxLayout(self.frameGlobalAvailableLocalization)
        self.verticalLayout_69.setSpacing(10)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalLocalizationAvailableLanguages = QLabel(self.frameGlobalAvailableLocalization)
        self.labelGlobalLocalizationAvailableLanguages.setObjectName(u"labelGlobalLocalizationAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalLocalizationAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalLocalizationAvailableLanguages.setFont(font)
        self.labelGlobalLocalizationAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_69.addWidget(self.labelGlobalLocalizationAvailableLanguages)

        self.listWidgetGlobalLocalizationAvailableLanguages = CustomList(self.frameGlobalAvailableLocalization)
        self.listWidgetGlobalLocalizationAvailableLanguages.setObjectName(u"listWidgetGlobalLocalizationAvailableLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalLocalizationAvailableLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetGlobalLocalizationAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalLocalizationAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalLocalizationAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalLocalizationAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalLocalizationAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalLocalizationAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalLocalizationAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalLocalizationAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalLocalizationAvailableLanguages.setSortingEnabled(True)
        self.listWidgetGlobalLocalizationAvailableLanguages.setProperty(u"self_drag", False)
        self.listWidgetGlobalLocalizationAvailableLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_69.addWidget(self.listWidgetGlobalLocalizationAvailableLanguages)


        self.horizontalLayout_11.addWidget(self.frameGlobalAvailableLocalization)

        self.frameGlobalLocalizationLeftRight = QFrame(self.frameGlobalLocalization)
        self.frameGlobalLocalizationLeftRight.setObjectName(u"frameGlobalLocalizationLeftRight")
        sizePolicy5.setHeightForWidth(self.frameGlobalLocalizationLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalLocalizationLeftRight.setSizePolicy(sizePolicy5)
        self.frameGlobalLocalizationLeftRight.setMinimumSize(QSize(64, 0))
        self.frameGlobalLocalizationLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalLocalizationLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLocalizationLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalLocalizationLeftRight.setLineWidth(0)
        self.verticalLayout_70 = QVBoxLayout(self.frameGlobalLocalizationLeftRight)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalSpacerGlobalLocalizationLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_70.addItem(self.verticalSpacerGlobalLocalizationLeftRightTop)

        self.buttonGlobalLocalizationAllRight = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationAllRight.setObjectName(u"buttonGlobalLocalizationAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllRight.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllRight.setFont(font5)
        self.buttonGlobalLocalizationAllRight.setIcon(icon2)
        self.buttonGlobalLocalizationAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_70.addWidget(self.buttonGlobalLocalizationAllRight)

        self.buttonGlobalLocalizationRight = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationRight.setObjectName(u"buttonGlobalLocalizationRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationRight.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationRight.setFont(font5)
        self.buttonGlobalLocalizationRight.setIcon(icon3)
        self.buttonGlobalLocalizationRight.setIconSize(QSize(16, 16))

        self.verticalLayout_70.addWidget(self.buttonGlobalLocalizationRight)

        self.buttonGlobalLocalizationLeft = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationLeft.setObjectName(u"buttonGlobalLocalizationLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationLeft.setFont(font5)
        self.buttonGlobalLocalizationLeft.setIcon(icon4)

        self.verticalLayout_70.addWidget(self.buttonGlobalLocalizationLeft)

        self.buttonGlobalLocalizationAllLeft = QPushButton(self.frameGlobalLocalizationLeftRight)
        self.buttonGlobalLocalizationAllLeft.setObjectName(u"buttonGlobalLocalizationAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationAllLeft.setFont(font5)
        self.buttonGlobalLocalizationAllLeft.setIcon(icon5)
        self.buttonGlobalLocalizationAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_70.addWidget(self.buttonGlobalLocalizationAllLeft)

        self.verticalSpacerGlobalLocalizationLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_70.addItem(self.verticalSpacerGlobalLocalizationLeftRightBottom)


        self.horizontalLayout_11.addWidget(self.frameGlobalLocalizationLeftRight)

        self.frameGlobalSelectedLocalization = QFrame(self.frameGlobalLocalization)
        self.frameGlobalSelectedLocalization.setObjectName(u"frameGlobalSelectedLocalization")
        sizePolicy5.setHeightForWidth(self.frameGlobalSelectedLocalization.sizePolicy().hasHeightForWidth())
        self.frameGlobalSelectedLocalization.setSizePolicy(sizePolicy5)
        self.frameGlobalSelectedLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalSelectedLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalSelectedLocalization.setLineWidth(0)
        self.verticalLayout_71 = QVBoxLayout(self.frameGlobalSelectedLocalization)
        self.verticalLayout_71.setSpacing(10)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalLocalizationSelectedLanguages = QLabel(self.frameGlobalSelectedLocalization)
        self.labelGlobalLocalizationSelectedLanguages.setObjectName(u"labelGlobalLocalizationSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelGlobalLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalLocalizationSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelGlobalLocalizationSelectedLanguages.setFont(font)
        self.labelGlobalLocalizationSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_71.addWidget(self.labelGlobalLocalizationSelectedLanguages)

        self.listWidgetGlobalLocalizationSelectedLanguages = CustomListSelfDrag(self.frameGlobalSelectedLocalization)
        self.listWidgetGlobalLocalizationSelectedLanguages.setObjectName(u"listWidgetGlobalLocalizationSelectedLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetGlobalLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalLocalizationSelectedLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetGlobalLocalizationSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalLocalizationSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetGlobalLocalizationSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalLocalizationSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetGlobalLocalizationSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetGlobalLocalizationSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetGlobalLocalizationSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalLocalizationSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetGlobalLocalizationSelectedLanguages.setProperty(u"self_drag", True)
        self.listWidgetGlobalLocalizationSelectedLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_71.addWidget(self.listWidgetGlobalLocalizationSelectedLanguages)


        self.horizontalLayout_11.addWidget(self.frameGlobalSelectedLocalization)

        self.frameGlobalLocalizationUpDown = QFrame(self.frameGlobalLocalization)
        self.frameGlobalLocalizationUpDown.setObjectName(u"frameGlobalLocalizationUpDown")
        sizePolicy5.setHeightForWidth(self.frameGlobalLocalizationUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalLocalizationUpDown.setSizePolicy(sizePolicy5)
        self.frameGlobalLocalizationUpDown.setMinimumSize(QSize(64, 0))
        self.frameGlobalLocalizationUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameGlobalLocalizationUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalLocalizationUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalLocalizationUpDown.setLineWidth(0)
        self.verticalLayout_72 = QVBoxLayout(self.frameGlobalLocalizationUpDown)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalSpacerGlobalLocalizationDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacerGlobalLocalizationDownTop)

        self.buttonGlobalLocalizationUp = QPushButton(self.frameGlobalLocalizationUpDown)
        self.buttonGlobalLocalizationUp.setObjectName(u"buttonGlobalLocalizationUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationUp.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationUp.setFont(font5)
        self.buttonGlobalLocalizationUp.setIcon(icon6)

        self.verticalLayout_72.addWidget(self.buttonGlobalLocalizationUp)

        self.buttonGlobalLocalizationDown = QPushButton(self.frameGlobalLocalizationUpDown)
        self.buttonGlobalLocalizationDown.setObjectName(u"buttonGlobalLocalizationDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLocalizationDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLocalizationDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalLocalizationDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLocalizationDown.setMaximumSize(QSize(40, 41))
        self.buttonGlobalLocalizationDown.setFont(font5)
        self.buttonGlobalLocalizationDown.setIcon(icon7)

        self.verticalLayout_72.addWidget(self.buttonGlobalLocalizationDown)

        self.verticalSpacerGlobalLocalizationUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacerGlobalLocalizationUpDownBottom)


        self.horizontalLayout_11.addWidget(self.frameGlobalLocalizationUpDown)

        self.horizontalSpacerGlobalLocalization = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacerGlobalLocalization)


        self.verticalLayout_67.addWidget(self.frameGlobalLocalization)


        self.verticalLayout_66.addWidget(self.tabContentsGlobalLocalization)

        self.scrollAreaGlobalLocalization.setWidget(self.scrollAreaWidgetContentsGlobalLocalization)

        self.gridLayout_14.addWidget(self.scrollAreaGlobalLocalization, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalLocalization, "")
        self.tabGlobalOverrides = QWidget()
        self.tabGlobalOverrides.setObjectName(u"tabGlobalOverrides")
        self.gridLayout_5 = QGridLayout(self.tabGlobalOverrides)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollAreaGlobalOverrides = QScrollArea(self.tabGlobalOverrides)
        self.scrollAreaGlobalOverrides.setObjectName(u"scrollAreaGlobalOverrides")
        self.scrollAreaGlobalOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalOverrides.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalOverrides.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalOverrides = QWidget()
        self.scrollAreaWidgetContentsGlobalOverrides.setObjectName(u"scrollAreaWidgetContentsGlobalOverrides")
        self.scrollAreaWidgetContentsGlobalOverrides.setGeometry(QRect(0, 0, 649, 413))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalOverrides.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalOverrides.setSizePolicy(sizePolicy)
        self.verticalLayout_73 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalOverrides)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalOverrides = QFrame(self.scrollAreaWidgetContentsGlobalOverrides)
        self.tabContentsGlobalOverrides.setObjectName(u"tabContentsGlobalOverrides")
        self.tabContentsGlobalOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalOverrides.setLineWidth(0)
        self.verticalLayout_74 = QVBoxLayout(self.tabContentsGlobalOverrides)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalOverrides = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalOverrides.setObjectName(u"horizontalLayoutHeaderGlobalOverrides")
        self.labelGlobalOverrideByText = QLabel(self.tabContentsGlobalOverrides)
        self.labelGlobalOverrideByText.setObjectName(u"labelGlobalOverrideByText")
        sizePolicy3.setHeightForWidth(self.labelGlobalOverrideByText.sizePolicy().hasHeightForWidth())
        self.labelGlobalOverrideByText.setSizePolicy(sizePolicy3)
        self.labelGlobalOverrideByText.setMinimumSize(QSize(0, 0))
        self.labelGlobalOverrideByText.setFont(font2)

        self.horizontalLayoutHeaderGlobalOverrides.addWidget(self.labelGlobalOverrideByText)

        self.frameOverrideGlobalOverrides = QFrame(self.tabContentsGlobalOverrides)
        self.frameOverrideGlobalOverrides.setObjectName(u"frameOverrideGlobalOverrides")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalOverrides.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalOverrides.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalOverrides.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_75 = QVBoxLayout(self.frameOverrideGlobalOverrides)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalOverrides.addWidget(self.frameOverrideGlobalOverrides)

        self.horizontalLayoutHeaderGlobalOverrides.setStretch(0, 1)

        self.verticalLayout_74.addLayout(self.horizontalLayoutHeaderGlobalOverrides)

        self.lineGlobalOverrides = QFrame(self.tabContentsGlobalOverrides)
        self.lineGlobalOverrides.setObjectName(u"lineGlobalOverrides")
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalOverrides.setPalette(palette7)
        self.lineGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalOverrides.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_74.addWidget(self.lineGlobalOverrides)

        self.labelGlobalOverride = QLabel(self.tabContentsGlobalOverrides)
        self.labelGlobalOverride.setObjectName(u"labelGlobalOverride")
        self.labelGlobalOverride.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalOverride.setWordWrap(True)
        self.labelGlobalOverride.setOpenExternalLinks(True)
        self.labelGlobalOverride.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_74.addWidget(self.labelGlobalOverride)

        self.verticalSpacerGlobalOverrides = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_74.addItem(self.verticalSpacerGlobalOverrides)

        self.frameGlobalOverrides = QFrame(self.tabContentsGlobalOverrides)
        self.frameGlobalOverrides.setObjectName(u"frameGlobalOverrides")
        self.frameGlobalOverrides.setMinimumSize(QSize(0, 64))
        self.frameGlobalOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frameGlobalOverrides)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalOverridesInclude = QFrame(self.frameGlobalOverrides)
        self.frameGlobalOverridesInclude.setObjectName(u"frameGlobalOverridesInclude")
        sizePolicy7.setHeightForWidth(self.frameGlobalOverridesInclude.sizePolicy().hasHeightForWidth())
        self.frameGlobalOverridesInclude.setSizePolicy(sizePolicy7)
        self.frameGlobalOverridesInclude.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalOverridesInclude.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalOverridesInclude.setLineWidth(0)
        self.verticalLayout_76 = QVBoxLayout(self.frameGlobalOverridesInclude)
        self.verticalLayout_76.setSpacing(10)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalOverrideInclude = QLabel(self.frameGlobalOverridesInclude)
        self.labelGlobalOverrideInclude.setObjectName(u"labelGlobalOverrideInclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalOverrideInclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalOverrideInclude.setSizePolicy(sizePolicy8)
        self.labelGlobalOverrideInclude.setFont(font)
        self.labelGlobalOverrideInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_76.addWidget(self.labelGlobalOverrideInclude)

        self.textEditGlobalInclude = CustomTextEdit(self.frameGlobalOverridesInclude)
        self.textEditGlobalInclude.setObjectName(u"textEditGlobalInclude")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.textEditGlobalInclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalInclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalInclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalInclude.setTabChangesFocus(True)
        self.textEditGlobalInclude.setAcceptRichText(False)

        self.verticalLayout_76.addWidget(self.textEditGlobalInclude)


        self.horizontalLayout_13.addWidget(self.frameGlobalOverridesInclude)

        self.horizontalSpacerGlobalOverrides = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacerGlobalOverrides)

        self.frameGlobalOverridesExclude = QFrame(self.frameGlobalOverrides)
        self.frameGlobalOverridesExclude.setObjectName(u"frameGlobalOverridesExclude")
        sizePolicy7.setHeightForWidth(self.frameGlobalOverridesExclude.sizePolicy().hasHeightForWidth())
        self.frameGlobalOverridesExclude.setSizePolicy(sizePolicy7)
        self.frameGlobalOverridesExclude.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalOverridesExclude.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalOverridesExclude.setLineWidth(0)
        self.verticalLayout_78 = QVBoxLayout(self.frameGlobalOverridesExclude)
        self.verticalLayout_78.setSpacing(10)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalOverrideExclude = QLabel(self.frameGlobalOverridesExclude)
        self.labelGlobalOverrideExclude.setObjectName(u"labelGlobalOverrideExclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalOverrideExclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalOverrideExclude.setSizePolicy(sizePolicy8)
        self.labelGlobalOverrideExclude.setFont(font)
        self.labelGlobalOverrideExclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_78.addWidget(self.labelGlobalOverrideExclude)

        self.textEditGlobalExclude = CustomTextEdit(self.frameGlobalOverridesExclude)
        self.textEditGlobalExclude.setObjectName(u"textEditGlobalExclude")
        sizePolicy10.setHeightForWidth(self.textEditGlobalExclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalExclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalExclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalExclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalExclude.setTabChangesFocus(True)
        self.textEditGlobalExclude.setAcceptRichText(False)

        self.verticalLayout_78.addWidget(self.textEditGlobalExclude)


        self.horizontalLayout_13.addWidget(self.frameGlobalOverridesExclude)

        self.horizontalSpacerGlobalOverrides1pxSoExcludeBorderShows = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacerGlobalOverrides1pxSoExcludeBorderShows)


        self.verticalLayout_74.addWidget(self.frameGlobalOverrides)


        self.verticalLayout_73.addWidget(self.tabContentsGlobalOverrides)

        self.scrollAreaGlobalOverrides.setWidget(self.scrollAreaWidgetContentsGlobalOverrides)

        self.gridLayout_5.addWidget(self.scrollAreaGlobalOverrides, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalOverrides, "")
        self.tabGlobalPostFilter = QWidget()
        self.tabGlobalPostFilter.setObjectName(u"tabGlobalPostFilter")
        self.gridLayout_15 = QGridLayout(self.tabGlobalPostFilter)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.scrollAreaGlobalPostFilter = QScrollArea(self.tabGlobalPostFilter)
        self.scrollAreaGlobalPostFilter.setObjectName(u"scrollAreaGlobalPostFilter")
        self.scrollAreaGlobalPostFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalPostFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalPostFilter.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalPostFilter.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalFilter = QWidget()
        self.scrollAreaWidgetContentsGlobalFilter.setObjectName(u"scrollAreaWidgetContentsGlobalFilter")
        self.scrollAreaWidgetContentsGlobalFilter.setGeometry(QRect(0, 0, 649, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalFilter.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalFilter.setSizePolicy(sizePolicy)
        self.verticalLayout_77 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalFilter)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalFilter = QFrame(self.scrollAreaWidgetContentsGlobalFilter)
        self.tabContentsGlobalFilter.setObjectName(u"tabContentsGlobalFilter")
        self.tabContentsGlobalFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalFilter.setLineWidth(0)
        self.verticalLayout_79 = QVBoxLayout(self.tabContentsGlobalFilter)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderGlobalFilter = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalFilter.setObjectName(u"horizontalLayoutHeaderGlobalFilter")
        self.labelGlobalFilterByText = QLabel(self.tabContentsGlobalFilter)
        self.labelGlobalFilterByText.setObjectName(u"labelGlobalFilterByText")
        sizePolicy3.setHeightForWidth(self.labelGlobalFilterByText.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByText.setSizePolicy(sizePolicy3)
        self.labelGlobalFilterByText.setMinimumSize(QSize(0, 0))
        self.labelGlobalFilterByText.setFont(font2)

        self.horizontalLayoutHeaderGlobalFilter.addWidget(self.labelGlobalFilterByText)

        self.frameOverrideGlobalFilter = QFrame(self.tabContentsGlobalFilter)
        self.frameOverrideGlobalFilter.setObjectName(u"frameOverrideGlobalFilter")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalFilter.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalFilter.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalFilter.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_80 = QVBoxLayout(self.frameOverrideGlobalFilter)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalFilter.addWidget(self.frameOverrideGlobalFilter)

        self.horizontalLayoutHeaderGlobalFilter.setStretch(0, 1)

        self.verticalLayout_79.addLayout(self.horizontalLayoutHeaderGlobalFilter)

        self.lineGlobalFilterByText = QFrame(self.tabContentsGlobalFilter)
        self.lineGlobalFilterByText.setObjectName(u"lineGlobalFilterByText")
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalFilterByText.setPalette(palette8)
        self.lineGlobalFilterByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalFilterByText.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_79.addWidget(self.lineGlobalFilterByText)

        self.labelGlobalFilters = QLabel(self.tabContentsGlobalFilter)
        self.labelGlobalFilters.setObjectName(u"labelGlobalFilters")
        self.labelGlobalFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelGlobalFilters.setWordWrap(True)
        self.labelGlobalFilters.setOpenExternalLinks(True)
        self.labelGlobalFilters.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_79.addWidget(self.labelGlobalFilters)

        self.verticalSpacerGlobalFilters = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_79.addItem(self.verticalSpacerGlobalFilters)

        self.frameGlobalFilter = QFrame(self.tabContentsGlobalFilter)
        self.frameGlobalFilter.setObjectName(u"frameGlobalFilter")
        self.frameGlobalFilter.setMinimumSize(QSize(0, 64))
        self.frameGlobalFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frameGlobalFilter)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalFilterContents = QFrame(self.frameGlobalFilter)
        self.frameGlobalFilterContents.setObjectName(u"frameGlobalFilterContents")
        sizePolicy7.setHeightForWidth(self.frameGlobalFilterContents.sizePolicy().hasHeightForWidth())
        self.frameGlobalFilterContents.setSizePolicy(sizePolicy7)
        self.frameGlobalFilterContents.setFrameShape(QFrame.Shape.NoFrame)
        self.frameGlobalFilterContents.setFrameShadow(QFrame.Shadow.Plain)
        self.frameGlobalFilterContents.setLineWidth(0)
        self.verticalLayout_81 = QVBoxLayout(self.frameGlobalFilterContents)
        self.verticalLayout_81.setSpacing(10)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalFilterInclude = QLabel(self.frameGlobalFilterContents)
        self.labelGlobalFilterInclude.setObjectName(u"labelGlobalFilterInclude")
        sizePolicy8.setHeightForWidth(self.labelGlobalFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterInclude.setSizePolicy(sizePolicy8)
        self.labelGlobalFilterInclude.setFont(font)
        self.labelGlobalFilterInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_81.addWidget(self.labelGlobalFilterInclude)

        self.textEditGlobalFilterInclude = CustomTextEdit(self.frameGlobalFilterContents)
        self.textEditGlobalFilterInclude.setObjectName(u"textEditGlobalFilterInclude")
        self.textEditGlobalFilterInclude.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.textEditGlobalFilterInclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalFilterInclude.setSizePolicy(sizePolicy10)
        self.textEditGlobalFilterInclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalFilterInclude.setMaximumSize(QSize(16777211, 16777215))
        self.textEditGlobalFilterInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditGlobalFilterInclude.setTabChangesFocus(True)
        self.textEditGlobalFilterInclude.setAcceptRichText(False)

        self.verticalLayout_81.addWidget(self.textEditGlobalFilterInclude)


        self.horizontalLayout_14.addWidget(self.frameGlobalFilterContents)

        self.horizontalSpacerGlobalFilter1pxSoExcludeBorderShows = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacerGlobalFilter1pxSoExcludeBorderShows)


        self.verticalLayout_79.addWidget(self.frameGlobalFilter)


        self.verticalLayout_77.addWidget(self.tabContentsGlobalFilter)

        self.scrollAreaGlobalPostFilter.setWidget(self.scrollAreaWidgetContentsGlobalFilter)

        self.gridLayout_15.addWidget(self.scrollAreaGlobalPostFilter, 0, 0, 1, 1)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalPostFilter, "")
        self.tabGlobalOptions = QWidget()
        self.tabGlobalOptions.setObjectName(u"tabGlobalOptions")
        self.gridLayout_16 = QGridLayout(self.tabGlobalOptions)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollAreaGlobalOptions = QScrollArea(self.tabGlobalOptions)
        self.scrollAreaGlobalOptions.setObjectName(u"scrollAreaGlobalOptions")
        self.scrollAreaGlobalOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGlobalOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaGlobalOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaGlobalOptions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalOptions = QWidget()
        self.scrollAreaWidgetContentsGlobalOptions.setObjectName(u"scrollAreaWidgetContentsGlobalOptions")
        self.scrollAreaWidgetContentsGlobalOptions.setGeometry(QRect(0, 0, 649, 1075))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsGlobalOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalOptions.setSizePolicy(sizePolicy)
        self.verticalLayout_82 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalOptions)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.tabContentsGlobalOptions = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.tabContentsGlobalOptions.setObjectName(u"tabContentsGlobalOptions")
        self.tabContentsGlobalOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsGlobalOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsGlobalOptions.setLineWidth(0)
        self.verticalLayout_83 = QVBoxLayout(self.tabContentsGlobalOptions)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalOptionsTitle = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalOptionsTitle.setObjectName(u"labelGlobalOptionsTitle")
        self.labelGlobalOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsTitle.setFont(font2)
        self.labelGlobalOptionsTitle.setScaledContents(False)
        self.labelGlobalOptionsTitle.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_83.addWidget(self.labelGlobalOptionsTitle)

        self.checkBoxGlobalOptionsDisable1G1R = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisable1G1R.setObjectName(u"checkBoxGlobalOptionsDisable1G1R")
        self.checkBoxGlobalOptionsDisable1G1R.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setKerning(True)
        self.checkBoxGlobalOptionsDisable1G1R.setFont(font6)
        self.checkBoxGlobalOptionsDisable1G1R.setStyleSheet(u"")
        self.checkBoxGlobalOptionsDisable1G1R.setTristate(False)

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsDisable1G1R)

        self.checkBoxGlobalOptionsPreferRegions = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferRegions.setObjectName(u"checkBoxGlobalOptionsPreferRegions")
        self.checkBoxGlobalOptionsPreferRegions.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferRegions.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsPreferRegions)

        self.checkBoxGlobalOptionsModernPlatforms = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsModernPlatforms.setObjectName(u"checkBoxGlobalOptionsModernPlatforms")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsModernPlatforms.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsModernPlatforms.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsModernPlatforms.setFont(font)
        self.checkBoxGlobalOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsModernPlatforms)

        self.checkBoxGlobalOptionsPreferOldest = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferOldest.setObjectName(u"checkBoxGlobalOptionsPreferOldest")
        self.checkBoxGlobalOptionsPreferOldest.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferOldest.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsPreferOldest)

        self.checkBoxGlobalOptionsDemoteUnlicensed = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setObjectName(u"checkBoxGlobalOptionsDemoteUnlicensed")
        self.checkBoxGlobalOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsDemoteUnlicensed)

        self.checkBoxGlobalOptionsDisableOverrides = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableOverrides.setObjectName(u"checkBoxGlobalOptionsDisableOverrides")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsDisableOverrides.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsDisableOverrides.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsDisableOverrides.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsDisableOverrides.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsDisableOverrides.setFont(font)
        self.checkBoxGlobalOptionsDisableOverrides.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsDisableOverrides)

        self.verticalSpacerGlobalOptions_1 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_1)

        self.labelGlobalChooseCompilationsMode = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalChooseCompilationsMode.setObjectName(u"labelGlobalChooseCompilationsMode")
        self.labelGlobalChooseCompilationsMode.setFont(font2)

        self.verticalLayout_83.addWidget(self.labelGlobalChooseCompilationsMode)

        self.comboBoxGlobalChooseCompilationsMode = CustomComboBox(self.tabContentsGlobalOptions)
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

        self.verticalLayout_83.addWidget(self.comboBoxGlobalChooseCompilationsMode)

        self.verticalSpacerGlobalOptions_2 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_2)

        self.labelGlobalCompilationsExplanation = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalCompilationsExplanation.setObjectName(u"labelGlobalCompilationsExplanation")
        self.labelGlobalCompilationsExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelGlobalCompilationsExplanation.setWordWrap(True)

        self.verticalLayout_83.addWidget(self.labelGlobalCompilationsExplanation)

        self.verticalSpacerGlobalOptions_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_3)

        self.labelGlobalOptionsOutput = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalOptionsOutput.setObjectName(u"labelGlobalOptionsOutput")
        self.labelGlobalOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsOutput.setFont(font2)
        self.labelGlobalOptionsOutput.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_83.addWidget(self.labelGlobalOptionsOutput)

        self.checkBoxGlobalOptionsAlreadyProcessed = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsAlreadyProcessed.setObjectName(u"checkBoxGlobalOptionsAlreadyProcessed")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsAlreadyProcessed)

        self.checkBoxGlobalOptionsOriginalHeader = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsOriginalHeader.setObjectName(u"checkBoxGlobalOptionsOriginalHeader")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsOriginalHeader)

        self.checkBoxGlobalOptionsUseMachine = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsUseMachine.setObjectName(u"checkBoxGlobalOptionsUseMachine")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsUseMachine)

        self.checkBoxGlobalOptionsSplitRegions = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsSplitRegions.setObjectName(u"checkBoxGlobalOptionsSplitRegions")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsSplitRegions)

        self.checkBoxGlobalOptionsRemovesDat = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsRemovesDat.setObjectName(u"checkBoxGlobalOptionsRemovesDat")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsRemovesDat)

        self.checkBoxGlobalOptionsKeepRemove = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsKeepRemove.setObjectName(u"checkBoxGlobalOptionsKeepRemove")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsKeepRemove)

        self.checkBoxGlobalOptions1G1RNames = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptions1G1RNames.setObjectName(u"checkBoxGlobalOptions1G1RNames")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptions1G1RNames)

        self.frameGlobalOptions1G1RPrefix = QFrame(self.tabContentsGlobalOptions)
        self.frameGlobalOptions1G1RPrefix.setObjectName(u"frameGlobalOptions1G1RPrefix")
        self.frameGlobalOptions1G1RPrefix.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameGlobalOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptions1G1RPrefix.setSizePolicy(sizePolicy8)
        self.frameGlobalOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        brush4 = QBrush(QColor(240, 240, 240, 0))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        brush5 = QBrush(QColor(227, 227, 227, 0))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        brush6 = QBrush(QColor(160, 160, 160, 0))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        brush8 = QBrush(QColor(0, 255, 127, 0))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        brush9 = QBrush(QColor(105, 105, 105, 0))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        brush10 = QBrush(QColor(246, 246, 246, 0))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameGlobalOptions1G1RPrefix.setPalette(palette9)
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

        self.verticalLayout_83.addWidget(self.frameGlobalOptions1G1RPrefix)

        self.verticalSpacerGlobalOptions_4 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_4)

        self.labelGlobalOptionsOnline = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalOptionsOnline.setObjectName(u"labelGlobalOptionsOnline")
        self.labelGlobalOptionsOnline.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsOnline.setFont(font2)
        self.labelGlobalOptionsOnline.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_83.addWidget(self.labelGlobalOptionsOnline)

        self.labelGlobalOnlineExplanation = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalOnlineExplanation.setObjectName(u"labelGlobalOnlineExplanation")
        self.labelGlobalOnlineExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelGlobalOnlineExplanation.setWordWrap(True)

        self.verticalLayout_83.addWidget(self.labelGlobalOnlineExplanation)

        self.verticalSpacerGlobalOptions_5 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_5)

        self.checkBoxGlobalOptionsMIA = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsMIA.setObjectName(u"checkBoxGlobalOptionsMIA")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsMIA.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsMIA.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsMIA.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsMIA.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsMIA.setFont(font)
        self.checkBoxGlobalOptionsMIA.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsMIA)

        self.checkBoxGlobalOptionsRetroAchievements = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsRetroAchievements.setObjectName(u"checkBoxGlobalOptionsRetroAchievements")
        sizePolicy11.setHeightForWidth(self.checkBoxGlobalOptionsRetroAchievements.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsRetroAchievements.setSizePolicy(sizePolicy11)
        self.checkBoxGlobalOptionsRetroAchievements.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsRetroAchievements.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxGlobalOptionsRetroAchievements.setFont(font)
        self.checkBoxGlobalOptionsRetroAchievements.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsRetroAchievements)

        self.checkBoxGlobalOptionsPreferRetro = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferRetro.setObjectName(u"checkBoxGlobalOptionsPreferRetro")
        self.checkBoxGlobalOptionsPreferRetro.setMinimumSize(QSize(0, 0))
        self.checkBoxGlobalOptionsPreferRetro.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsPreferRetro)

        self.verticalSpacerGlobalOptions_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_6)

        self.labelGlobalOptionsDebug = QLabel(self.tabContentsGlobalOptions)
        self.labelGlobalOptionsDebug.setObjectName(u"labelGlobalOptionsDebug")
        self.labelGlobalOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsDebug.setFont(font2)
        self.labelGlobalOptionsDebug.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_83.addWidget(self.labelGlobalOptionsDebug)

        self.checkBoxGlobalOptionsReportWarnings = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsReportWarnings.setObjectName(u"checkBoxGlobalOptionsReportWarnings")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsReportWarnings)

        self.checkBoxGlobalOptionsPauseWarnings = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsPauseWarnings.setObjectName(u"checkBoxGlobalOptionsPauseWarnings")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsPauseWarnings)

        self.checkBoxGlobalOptionsLegacy = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsLegacy.setObjectName(u"checkBoxGlobalOptionsLegacy")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsLegacy)

        self.checkBoxGlobalOptionsDisableMultiCPU = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableMultiCPU.setObjectName(u"checkBoxGlobalOptionsDisableMultiCPU")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsDisableMultiCPU)

        self.checkBoxGlobalOptionsTrace = QCheckBox(self.tabContentsGlobalOptions)
        self.checkBoxGlobalOptionsTrace.setObjectName(u"checkBoxGlobalOptionsTrace")

        self.verticalLayout_83.addWidget(self.checkBoxGlobalOptionsTrace)

        self.frameGlobalOptionsTrace = QFrame(self.tabContentsGlobalOptions)
        self.frameGlobalOptionsTrace.setObjectName(u"frameGlobalOptionsTrace")
        self.frameGlobalOptionsTrace.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameGlobalOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptionsTrace.setSizePolicy(sizePolicy8)
        self.frameGlobalOptionsTrace.setMinimumSize(QSize(0, 55))
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
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
        self.frameGlobalOptionsTrace.setPalette(palette10)
        self.labelGlobalOptionsTrace = QLabel(self.frameGlobalOptionsTrace)
        self.labelGlobalOptionsTrace.setObjectName(u"labelGlobalOptionsTrace")
        self.labelGlobalOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditGlobalOptionsTrace = CustomLineEdit(self.frameGlobalOptionsTrace)
        self.lineEditGlobalOptionsTrace.setObjectName(u"lineEditGlobalOptionsTrace")
        self.lineEditGlobalOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditGlobalOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_83.addWidget(self.frameGlobalOptionsTrace)

        self.verticalSpacerGlobalOptions_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_83.addItem(self.verticalSpacerGlobalOptions_7)


        self.verticalLayout_82.addWidget(self.tabContentsGlobalOptions)

        self.scrollAreaGlobalOptions.setWidget(self.scrollAreaWidgetContentsGlobalOptions)

        self.gridLayout_16.addWidget(self.scrollAreaGlobalOptions, 3, 0, 1, 1)

        self.horizontalLayoutHeaderGlobalOptions = QHBoxLayout()
        self.horizontalLayoutHeaderGlobalOptions.setObjectName(u"horizontalLayoutHeaderGlobalOptions")
        self.labelGlobalOptions = QLabel(self.tabGlobalOptions)
        self.labelGlobalOptions.setObjectName(u"labelGlobalOptions")
        sizePolicy3.setHeightForWidth(self.labelGlobalOptions.sizePolicy().hasHeightForWidth())
        self.labelGlobalOptions.setSizePolicy(sizePolicy3)
        self.labelGlobalOptions.setMinimumSize(QSize(0, 0))
        self.labelGlobalOptions.setFont(font2)

        self.horizontalLayoutHeaderGlobalOptions.addWidget(self.labelGlobalOptions)

        self.frameOverrideGlobalOptions = QFrame(self.tabGlobalOptions)
        self.frameOverrideGlobalOptions.setObjectName(u"frameOverrideGlobalOptions")
        sizePolicy5.setHeightForWidth(self.frameOverrideGlobalOptions.sizePolicy().hasHeightForWidth())
        self.frameOverrideGlobalOptions.setSizePolicy(sizePolicy5)
        self.frameOverrideGlobalOptions.setMinimumSize(QSize(200, 24))
        self.frameOverrideGlobalOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideGlobalOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_84 = QVBoxLayout(self.frameOverrideGlobalOptions)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderGlobalOptions.addWidget(self.frameOverrideGlobalOptions)

        self.horizontalLayoutHeaderGlobalOptions.setStretch(0, 1)

        self.gridLayout_16.addLayout(self.horizontalLayoutHeaderGlobalOptions, 1, 0, 1, 1)

        self.lineGlobalOptions = QFrame(self.tabGlobalOptions)
        self.lineGlobalOptions.setObjectName(u"lineGlobalOptions")
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineGlobalOptions.setPalette(palette11)
        self.lineGlobalOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineGlobalOptions.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_16.addWidget(self.lineGlobalOptions, 2, 0, 1, 1)

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
        self.gridLayout_7 = QGridLayout(self.tabSystemPaths)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollAreaSystemPaths = QScrollArea(self.tabSystemPaths)
        self.scrollAreaSystemPaths.setObjectName(u"scrollAreaSystemPaths")
        self.scrollAreaSystemPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemPaths.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemPaths.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemPaths = QWidget()
        self.scrollAreaWidgetContentsSystemPaths.setObjectName(u"scrollAreaWidgetContentsSystemPaths")
        self.scrollAreaWidgetContentsSystemPaths.setGeometry(QRect(0, 0, 649, 404))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemPaths.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemPaths.setSizePolicy(sizePolicy)
        self.verticalLayout_41 = QVBoxLayout(self.scrollAreaWidgetContentsSystemPaths)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemPaths = QFrame(self.scrollAreaWidgetContentsSystemPaths)
        self.tabContentsSystemPaths.setObjectName(u"tabContentsSystemPaths")
        self.tabContentsSystemPaths.setMinimumSize(QSize(0, 20))
        self.tabContentsSystemPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemPaths.setLineWidth(0)
        self.verticalLayout_42 = QVBoxLayout(self.tabContentsSystemPaths)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemPaths = QHBoxLayout()
        self.horizontalLayoutHeaderSystemPaths.setObjectName(u"horizontalLayoutHeaderSystemPaths")
        self.labelSystemCustomFilesAndFolders = QLabel(self.tabContentsSystemPaths)
        self.labelSystemCustomFilesAndFolders.setObjectName(u"labelSystemCustomFilesAndFolders")
        sizePolicy3.setHeightForWidth(self.labelSystemCustomFilesAndFolders.sizePolicy().hasHeightForWidth())
        self.labelSystemCustomFilesAndFolders.setSizePolicy(sizePolicy3)
        self.labelSystemCustomFilesAndFolders.setMinimumSize(QSize(0, 0))
        self.labelSystemCustomFilesAndFolders.setFont(font2)

        self.horizontalLayoutHeaderSystemPaths.addWidget(self.labelSystemCustomFilesAndFolders)

        self.frameOverrideSystemPaths = QFrame(self.tabContentsSystemPaths)
        self.frameOverrideSystemPaths.setObjectName(u"frameOverrideSystemPaths")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemPaths.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemPaths.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemPaths.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemPaths.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemPaths.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_48 = QVBoxLayout(self.frameOverrideSystemPaths)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverridePaths = QCheckBox(self.frameOverrideSystemPaths)
        self.checkBoxSystemOverridePaths.setObjectName(u"checkBoxSystemOverridePaths")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverridePaths.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverridePaths.setSizePolicy(sizePolicy3)

        self.verticalLayout_48.addWidget(self.checkBoxSystemOverridePaths, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemPaths.addWidget(self.frameOverrideSystemPaths)

        self.horizontalLayoutHeaderSystemPaths.setStretch(0, 1)

        self.verticalLayout_42.addLayout(self.horizontalLayoutHeaderSystemPaths)

        self.lineSystemCustomFilesAndFolders = QFrame(self.tabContentsSystemPaths)
        self.lineSystemCustomFilesAndFolders.setObjectName(u"lineSystemCustomFilesAndFolders")
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemCustomFilesAndFolders.setPalette(palette12)
        self.lineSystemCustomFilesAndFolders.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemCustomFilesAndFolders.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_42.addWidget(self.lineSystemCustomFilesAndFolders)

        self.labelSystemPathsOutput = QLabel(self.tabContentsSystemPaths)
        self.labelSystemPathsOutput.setObjectName(u"labelSystemPathsOutput")
        self.labelSystemPathsOutput.setMinimumSize(QSize(0, 20))
        self.labelSystemPathsOutput.setFont(font2)
        self.labelSystemPathsOutput.setScaledContents(False)
        self.labelSystemPathsOutput.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_42.addWidget(self.labelSystemPathsOutput)

        self.verticalLayoutSystemContentsSystemPaths = QVBoxLayout()
        self.verticalLayoutSystemContentsSystemPaths.setSpacing(10)
        self.verticalLayoutSystemContentsSystemPaths.setObjectName(u"verticalLayoutSystemContentsSystemPaths")
        self.horizontalLayoutSystemPaths1 = QHBoxLayout()
        self.horizontalLayoutSystemPaths1.setSpacing(6)
        self.horizontalLayoutSystemPaths1.setObjectName(u"horizontalLayoutSystemPaths1")
        self.horizontalLayoutSystemPaths1.setContentsMargins(0, -1, -1, -1)
        self.buttonSystemClearOutput = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemClearOutput.setObjectName(u"buttonSystemClearOutput")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearOutput.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearOutput.setSizePolicy(sizePolicy6)
        self.buttonSystemClearOutput.setMinimumSize(QSize(44, 48))
        self.buttonSystemClearOutput.setMaximumSize(QSize(44, 48))
        self.buttonSystemClearOutput.setFont(font3)
        icon8 = QIcon()
        icon8.addFile(u":/retoolFiles/images/icons8-multiply-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonSystemClearOutput.setIcon(icon8)
        self.buttonSystemClearOutput.setIconSize(QSize(32, 32))
        self.buttonSystemClearOutput.setFlat(False)

        self.horizontalLayoutSystemPaths1.addWidget(self.buttonSystemClearOutput)

        self.buttonSystemChooseOutput = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemChooseOutput.setObjectName(u"buttonSystemChooseOutput")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseOutput.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseOutput.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseOutput.setMinimumSize(QSize(44, 48))
        self.buttonSystemChooseOutput.setMaximumSize(QSize(44, 48))
        self.buttonSystemChooseOutput.setFont(font3)
        self.buttonSystemChooseOutput.setAutoFillBackground(False)
        self.buttonSystemChooseOutput.setIcon(icon1)
        self.buttonSystemChooseOutput.setIconSize(QSize(32, 32))
        self.buttonSystemChooseOutput.setFlat(False)

        self.horizontalLayoutSystemPaths1.addWidget(self.buttonSystemChooseOutput)

        self.verticalLayoutSystemPathsLabels1 = QVBoxLayout()
        self.verticalLayoutSystemPathsLabels1.setObjectName(u"verticalLayoutSystemPathsLabels1")
        self.labelSystemSelectOutput = QLabel(self.tabContentsSystemPaths)
        self.labelSystemSelectOutput.setObjectName(u"labelSystemSelectOutput")
        self.labelSystemSelectOutput.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectOutput.setFont(font4)

        self.verticalLayoutSystemPathsLabels1.addWidget(self.labelSystemSelectOutput)

        self.labelSystemOutputFolder = ElisionLabel(self.tabContentsSystemPaths)
        self.labelSystemOutputFolder.setObjectName(u"labelSystemOutputFolder")
        sizePolicy7.setHeightForWidth(self.labelSystemOutputFolder.sizePolicy().hasHeightForWidth())
        self.labelSystemOutputFolder.setSizePolicy(sizePolicy7)
        self.labelSystemOutputFolder.setMinimumSize(QSize(400, 0))
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemOutputFolder.setPalette(palette13)
        self.labelSystemOutputFolder.setFont(font1)

        self.verticalLayoutSystemPathsLabels1.addWidget(self.labelSystemOutputFolder)


        self.horizontalLayoutSystemPaths1.addLayout(self.verticalLayoutSystemPathsLabels1)


        self.verticalLayoutSystemContentsSystemPaths.addLayout(self.horizontalLayoutSystemPaths1)

        self.checkBoxSystemReplaceInputDats = QCheckBox(self.tabContentsSystemPaths)
        self.checkBoxSystemReplaceInputDats.setObjectName(u"checkBoxSystemReplaceInputDats")
        self.checkBoxSystemReplaceInputDats.setFont(font1)

        self.verticalLayoutSystemContentsSystemPaths.addWidget(self.checkBoxSystemReplaceInputDats)

        self.labelSystemPathsSupportFiles = QLabel(self.tabContentsSystemPaths)
        self.labelSystemPathsSupportFiles.setObjectName(u"labelSystemPathsSupportFiles")
        self.labelSystemPathsSupportFiles.setMinimumSize(QSize(0, 20))
        self.labelSystemPathsSupportFiles.setFont(font2)
        self.labelSystemPathsSupportFiles.setScaledContents(False)
        self.labelSystemPathsSupportFiles.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayoutSystemContentsSystemPaths.addWidget(self.labelSystemPathsSupportFiles)

        self.horizontalLayoutSystemPaths2 = QHBoxLayout()
        self.horizontalLayoutSystemPaths2.setSpacing(6)
        self.horizontalLayoutSystemPaths2.setObjectName(u"horizontalLayoutSystemPaths2")
        self.horizontalLayoutSystemPaths2.setContentsMargins(0, -1, -1, -1)
        self.buttonSystemClearCloneList = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemClearCloneList.setObjectName(u"buttonSystemClearCloneList")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearCloneList.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearCloneList.setSizePolicy(sizePolicy6)
        self.buttonSystemClearCloneList.setMinimumSize(QSize(44, 48))
        self.buttonSystemClearCloneList.setMaximumSize(QSize(44, 48))
        self.buttonSystemClearCloneList.setFont(font3)
        self.buttonSystemClearCloneList.setIcon(icon8)
        self.buttonSystemClearCloneList.setIconSize(QSize(32, 32))
        self.buttonSystemClearCloneList.setFlat(False)

        self.horizontalLayoutSystemPaths2.addWidget(self.buttonSystemClearCloneList)

        self.buttonSystemChooseCloneList = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemChooseCloneList.setObjectName(u"buttonSystemChooseCloneList")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseCloneList.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseCloneList.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseCloneList.setMinimumSize(QSize(44, 48))
        self.buttonSystemChooseCloneList.setMaximumSize(QSize(44, 48))
        self.buttonSystemChooseCloneList.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/retoolFiles/images/icons8-diff-files-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonSystemChooseCloneList.setIcon(icon9)
        self.buttonSystemChooseCloneList.setIconSize(QSize(32, 32))
        self.buttonSystemChooseCloneList.setFlat(False)

        self.horizontalLayoutSystemPaths2.addWidget(self.buttonSystemChooseCloneList)

        self.verticalLayoutSystemPathsLabels2 = QVBoxLayout()
        self.verticalLayoutSystemPathsLabels2.setObjectName(u"verticalLayoutSystemPathsLabels2")
        self.labelSystemSelectCloneList = QLabel(self.tabContentsSystemPaths)
        self.labelSystemSelectCloneList.setObjectName(u"labelSystemSelectCloneList")
        self.labelSystemSelectCloneList.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectCloneList.setFont(font4)

        self.verticalLayoutSystemPathsLabels2.addWidget(self.labelSystemSelectCloneList)

        self.labelSystemCloneList = ElisionLabel(self.tabContentsSystemPaths)
        self.labelSystemCloneList.setObjectName(u"labelSystemCloneList")
        sizePolicy7.setHeightForWidth(self.labelSystemCloneList.sizePolicy().hasHeightForWidth())
        self.labelSystemCloneList.setSizePolicy(sizePolicy7)
        self.labelSystemCloneList.setMinimumSize(QSize(400, 0))
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemCloneList.setPalette(palette14)
        self.labelSystemCloneList.setFont(font1)

        self.verticalLayoutSystemPathsLabels2.addWidget(self.labelSystemCloneList)


        self.horizontalLayoutSystemPaths2.addLayout(self.verticalLayoutSystemPathsLabels2)


        self.verticalLayoutSystemContentsSystemPaths.addLayout(self.horizontalLayoutSystemPaths2)

        self.horizontalLayoutSystemPaths3 = QHBoxLayout()
        self.horizontalLayoutSystemPaths3.setSpacing(6)
        self.horizontalLayoutSystemPaths3.setObjectName(u"horizontalLayoutSystemPaths3")
        self.horizontalLayoutSystemPaths3.setContentsMargins(0, -1, -1, -1)
        self.buttonSystemClearMetadataFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemClearMetadataFile.setObjectName(u"buttonSystemClearMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearMetadataFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemClearMetadataFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemClearMetadataFile.setFont(font3)
        self.buttonSystemClearMetadataFile.setIcon(icon8)
        self.buttonSystemClearMetadataFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearMetadataFile.setFlat(False)

        self.horizontalLayoutSystemPaths3.addWidget(self.buttonSystemClearMetadataFile)

        self.buttonSystemChooseMetadataFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemChooseMetadataFile.setObjectName(u"buttonSystemChooseMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseMetadataFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemChooseMetadataFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemChooseMetadataFile.setFont(font3)
        self.buttonSystemChooseMetadataFile.setIcon(icon9)
        self.buttonSystemChooseMetadataFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseMetadataFile.setFlat(False)

        self.horizontalLayoutSystemPaths3.addWidget(self.buttonSystemChooseMetadataFile)

        self.verticalLayoutSystemPathsLabels3 = QVBoxLayout()
        self.verticalLayoutSystemPathsLabels3.setObjectName(u"verticalLayoutSystemPathsLabels3")
        self.labelSystemSelectMetadataFile = QLabel(self.tabContentsSystemPaths)
        self.labelSystemSelectMetadataFile.setObjectName(u"labelSystemSelectMetadataFile")
        self.labelSystemSelectMetadataFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectMetadataFile.setFont(font4)

        self.verticalLayoutSystemPathsLabels3.addWidget(self.labelSystemSelectMetadataFile)

        self.labelSystemMetadataFile = ElisionLabel(self.tabContentsSystemPaths)
        self.labelSystemMetadataFile.setObjectName(u"labelSystemMetadataFile")
        sizePolicy7.setHeightForWidth(self.labelSystemMetadataFile.sizePolicy().hasHeightForWidth())
        self.labelSystemMetadataFile.setSizePolicy(sizePolicy7)
        self.labelSystemMetadataFile.setMinimumSize(QSize(400, 0))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemMetadataFile.setPalette(palette15)
        self.labelSystemMetadataFile.setFont(font1)

        self.verticalLayoutSystemPathsLabels3.addWidget(self.labelSystemMetadataFile)


        self.horizontalLayoutSystemPaths3.addLayout(self.verticalLayoutSystemPathsLabels3)


        self.verticalLayoutSystemContentsSystemPaths.addLayout(self.horizontalLayoutSystemPaths3)

        self.horizontalLayoutSystemPaths4 = QHBoxLayout()
        self.horizontalLayoutSystemPaths4.setSpacing(6)
        self.horizontalLayoutSystemPaths4.setObjectName(u"horizontalLayoutSystemPaths4")
        self.horizontalLayoutSystemPaths4.setContentsMargins(0, -1, -1, -1)
        self.buttonSystemClearMIAFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemClearMIAFile.setObjectName(u"buttonSystemClearMIAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearMIAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearMIAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearMIAFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemClearMIAFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemClearMIAFile.setFont(font3)
        self.buttonSystemClearMIAFile.setIcon(icon8)
        self.buttonSystemClearMIAFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearMIAFile.setFlat(False)

        self.horizontalLayoutSystemPaths4.addWidget(self.buttonSystemClearMIAFile)

        self.buttonSystemChooseMIAFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemChooseMIAFile.setObjectName(u"buttonSystemChooseMIAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseMIAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseMIAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseMIAFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemChooseMIAFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemChooseMIAFile.setFont(font3)
        self.buttonSystemChooseMIAFile.setIcon(icon9)
        self.buttonSystemChooseMIAFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseMIAFile.setFlat(False)

        self.horizontalLayoutSystemPaths4.addWidget(self.buttonSystemChooseMIAFile)

        self.verticalLayoutSystemPathsLabels4 = QVBoxLayout()
        self.verticalLayoutSystemPathsLabels4.setObjectName(u"verticalLayoutSystemPathsLabels4")
        self.labelSystemSelectMIAFile = QLabel(self.tabContentsSystemPaths)
        self.labelSystemSelectMIAFile.setObjectName(u"labelSystemSelectMIAFile")
        self.labelSystemSelectMIAFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectMIAFile.setFont(font4)

        self.verticalLayoutSystemPathsLabels4.addWidget(self.labelSystemSelectMIAFile)

        self.labelSystemMIAFile = ElisionLabel(self.tabContentsSystemPaths)
        self.labelSystemMIAFile.setObjectName(u"labelSystemMIAFile")
        sizePolicy7.setHeightForWidth(self.labelSystemMIAFile.sizePolicy().hasHeightForWidth())
        self.labelSystemMIAFile.setSizePolicy(sizePolicy7)
        self.labelSystemMIAFile.setMinimumSize(QSize(400, 0))
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemMIAFile.setPalette(palette16)
        self.labelSystemMIAFile.setFont(font1)

        self.verticalLayoutSystemPathsLabels4.addWidget(self.labelSystemMIAFile)


        self.horizontalLayoutSystemPaths4.addLayout(self.verticalLayoutSystemPathsLabels4)


        self.verticalLayoutSystemContentsSystemPaths.addLayout(self.horizontalLayoutSystemPaths4)

        self.horizontalLayoutSystemPaths5 = QHBoxLayout()
        self.horizontalLayoutSystemPaths5.setSpacing(6)
        self.horizontalLayoutSystemPaths5.setObjectName(u"horizontalLayoutSystemPaths5")
        self.horizontalLayoutSystemPaths5.setContentsMargins(0, -1, -1, -1)
        self.buttonSystemClearRAFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemClearRAFile.setObjectName(u"buttonSystemClearRAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemClearRAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemClearRAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemClearRAFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemClearRAFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemClearRAFile.setFont(font3)
        self.buttonSystemClearRAFile.setIcon(icon8)
        self.buttonSystemClearRAFile.setIconSize(QSize(32, 32))
        self.buttonSystemClearRAFile.setFlat(False)

        self.horizontalLayoutSystemPaths5.addWidget(self.buttonSystemClearRAFile)

        self.buttonSystemChooseRAFile = QPushButton(self.tabContentsSystemPaths)
        self.buttonSystemChooseRAFile.setObjectName(u"buttonSystemChooseRAFile")
        sizePolicy6.setHeightForWidth(self.buttonSystemChooseRAFile.sizePolicy().hasHeightForWidth())
        self.buttonSystemChooseRAFile.setSizePolicy(sizePolicy6)
        self.buttonSystemChooseRAFile.setMinimumSize(QSize(44, 48))
        self.buttonSystemChooseRAFile.setMaximumSize(QSize(44, 48))
        self.buttonSystemChooseRAFile.setFont(font3)
        self.buttonSystemChooseRAFile.setIcon(icon9)
        self.buttonSystemChooseRAFile.setIconSize(QSize(32, 32))
        self.buttonSystemChooseRAFile.setFlat(False)

        self.horizontalLayoutSystemPaths5.addWidget(self.buttonSystemChooseRAFile)

        self.verticalLayoutSystemPathsLabels5 = QVBoxLayout()
        self.verticalLayoutSystemPathsLabels5.setObjectName(u"verticalLayoutSystemPathsLabels5")
        self.labelSystemSelectRAFile = QLabel(self.tabContentsSystemPaths)
        self.labelSystemSelectRAFile.setObjectName(u"labelSystemSelectRAFile")
        self.labelSystemSelectRAFile.setMinimumSize(QSize(400, 0))
        self.labelSystemSelectRAFile.setFont(font4)

        self.verticalLayoutSystemPathsLabels5.addWidget(self.labelSystemSelectRAFile)

        self.labelSystemRAFile = ElisionLabel(self.tabContentsSystemPaths)
        self.labelSystemRAFile.setObjectName(u"labelSystemRAFile")
        sizePolicy7.setHeightForWidth(self.labelSystemRAFile.sizePolicy().hasHeightForWidth())
        self.labelSystemRAFile.setSizePolicy(sizePolicy7)
        self.labelSystemRAFile.setMinimumSize(QSize(400, 0))
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        self.labelSystemRAFile.setPalette(palette17)
        self.labelSystemRAFile.setFont(font1)

        self.verticalLayoutSystemPathsLabels5.addWidget(self.labelSystemRAFile)


        self.horizontalLayoutSystemPaths5.addLayout(self.verticalLayoutSystemPathsLabels5)


        self.verticalLayoutSystemContentsSystemPaths.addLayout(self.horizontalLayoutSystemPaths5)

        self.verticalSpacerSystemPaths = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutSystemContentsSystemPaths.addItem(self.verticalSpacerSystemPaths)


        self.verticalLayout_42.addLayout(self.verticalLayoutSystemContentsSystemPaths)

        self.verticalLayout_42.setStretch(3, 1)

        self.verticalLayout_41.addWidget(self.tabContentsSystemPaths)

        self.scrollAreaSystemPaths.setWidget(self.scrollAreaWidgetContentsSystemPaths)

        self.gridLayout_7.addWidget(self.scrollAreaSystemPaths, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemPaths, "")
        self.tabSystemRegions = QWidget()
        self.tabSystemRegions.setObjectName(u"tabSystemRegions")
        self.gridLayout_8 = QGridLayout(self.tabSystemRegions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollAreaSystemRegions = QScrollArea(self.tabSystemRegions)
        self.scrollAreaSystemRegions.setObjectName(u"scrollAreaSystemRegions")
        self.scrollAreaSystemRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemRegions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemRegions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemRegions = QWidget()
        self.scrollAreaWidgetContentsSystemRegions.setObjectName(u"scrollAreaWidgetContentsSystemRegions")
        self.scrollAreaWidgetContentsSystemRegions.setGeometry(QRect(0, 0, 640, 189))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemRegions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemRegions.setSizePolicy(sizePolicy)
        self.verticalLayout_85 = QVBoxLayout(self.scrollAreaWidgetContentsSystemRegions)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemRegions = QFrame(self.scrollAreaWidgetContentsSystemRegions)
        self.tabContentsSystemRegions.setObjectName(u"tabContentsSystemRegions")
        self.tabContentsSystemRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemRegions.setLineWidth(0)
        self.verticalLayout_86 = QVBoxLayout(self.tabContentsSystemRegions)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemRegions = QHBoxLayout()
        self.horizontalLayoutHeaderSystemRegions.setObjectName(u"horizontalLayoutHeaderSystemRegions")
        self.labelSystemFilterByRegions = QLabel(self.tabContentsSystemRegions)
        self.labelSystemFilterByRegions.setObjectName(u"labelSystemFilterByRegions")
        sizePolicy3.setHeightForWidth(self.labelSystemFilterByRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByRegions.setSizePolicy(sizePolicy3)
        self.labelSystemFilterByRegions.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByRegions.setFont(font2)

        self.horizontalLayoutHeaderSystemRegions.addWidget(self.labelSystemFilterByRegions)

        self.frameOverrideSystemRegions = QFrame(self.tabContentsSystemRegions)
        self.frameOverrideSystemRegions.setObjectName(u"frameOverrideSystemRegions")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemRegions.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemRegions.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemRegions.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_93 = QVBoxLayout(self.frameOverrideSystemRegions)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideRegions = QCheckBox(self.frameOverrideSystemRegions)
        self.checkBoxSystemOverrideRegions.setObjectName(u"checkBoxSystemOverrideRegions")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideRegions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideRegions.setSizePolicy(sizePolicy3)

        self.verticalLayout_93.addWidget(self.checkBoxSystemOverrideRegions, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemRegions.addWidget(self.frameOverrideSystemRegions)

        self.horizontalLayoutHeaderSystemRegions.setStretch(0, 1)

        self.verticalLayout_86.addLayout(self.horizontalLayoutHeaderSystemRegions)

        self.lineSystemRegions = QFrame(self.tabContentsSystemRegions)
        self.lineSystemRegions.setObjectName(u"lineSystemRegions")
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemRegions.setPalette(palette18)
        self.lineSystemRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemRegions.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_86.addWidget(self.lineSystemRegions)

        self.frameSystemRegions = QFrame(self.tabContentsSystemRegions)
        self.frameSystemRegions.setObjectName(u"frameSystemRegions")
        self.frameSystemRegions.setMinimumSize(QSize(0, 64))
        self.frameSystemRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frameSystemRegions)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frameSystemAvailableRegions = QFrame(self.frameSystemRegions)
        self.frameSystemAvailableRegions.setObjectName(u"frameSystemAvailableRegions")
        sizePolicy5.setHeightForWidth(self.frameSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.frameSystemAvailableRegions.setSizePolicy(sizePolicy5)
        self.frameSystemAvailableRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemAvailableRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemAvailableRegions.setLineWidth(0)
        self.verticalLayout_36 = QVBoxLayout(self.frameSystemAvailableRegions)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.labelSystemAvailableRegions = QLabel(self.frameSystemAvailableRegions)
        self.labelSystemAvailableRegions.setObjectName(u"labelSystemAvailableRegions")
        sizePolicy8.setHeightForWidth(self.labelSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableRegions.setSizePolicy(sizePolicy8)
        self.labelSystemAvailableRegions.setFont(font)
        self.labelSystemAvailableRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_36.addWidget(self.labelSystemAvailableRegions)

        self.listWidgetSystemAvailableRegions = CustomList(self.frameSystemAvailableRegions)
        self.listWidgetSystemAvailableRegions.setObjectName(u"listWidgetSystemAvailableRegions")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableRegions.setSizePolicy(sizePolicy9)
        self.listWidgetSystemAvailableRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemAvailableRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemAvailableRegions.setTabKeyNavigation(True)
        self.listWidgetSystemAvailableRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemAvailableRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemAvailableRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemAvailableRegions.setAlternatingRowColors(False)
        self.listWidgetSystemAvailableRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemAvailableRegions.setSortingEnabled(True)

        self.verticalLayout_36.addWidget(self.listWidgetSystemAvailableRegions)


        self.horizontalLayout_15.addWidget(self.frameSystemAvailableRegions)

        self.frameSystemRegionLeftRight = QFrame(self.frameSystemRegions)
        self.frameSystemRegionLeftRight.setObjectName(u"frameSystemRegionLeftRight")
        sizePolicy5.setHeightForWidth(self.frameSystemRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionLeftRight.setSizePolicy(sizePolicy5)
        self.frameSystemRegionLeftRight.setMinimumSize(QSize(64, 0))
        self.frameSystemRegionLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameSystemRegionLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegionLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemRegionLeftRight.setLineWidth(0)
        self.verticalLayout_88 = QVBoxLayout(self.frameSystemRegionLeftRight)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalSpacerSystemRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacerSystemRegionLeftRightTop)

        self.buttonSystemRegionAllRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllRight.setObjectName(u"buttonSystemRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionAllRight.setFont(font5)
        self.buttonSystemRegionAllRight.setIcon(icon2)
        self.buttonSystemRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_88.addWidget(self.buttonSystemRegionAllRight)

        self.buttonSystemRegionRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionRight.setObjectName(u"buttonSystemRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionRight.setFont(font5)
        self.buttonSystemRegionRight.setIcon(icon3)
        self.buttonSystemRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_88.addWidget(self.buttonSystemRegionRight)

        self.buttonSystemRegionLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionLeft.setObjectName(u"buttonSystemRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionLeft.setFont(font5)
        self.buttonSystemRegionLeft.setIcon(icon4)

        self.verticalLayout_88.addWidget(self.buttonSystemRegionLeft)

        self.buttonSystemRegionAllLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllLeft.setObjectName(u"buttonSystemRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionAllLeft.setFont(font5)
        self.buttonSystemRegionAllLeft.setIcon(icon5)
        self.buttonSystemRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_88.addWidget(self.buttonSystemRegionAllLeft)

        self.verticalSpacerSystemRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacerSystemRegionLeftRightBottom)


        self.horizontalLayout_15.addWidget(self.frameSystemRegionLeftRight)

        self.frameSystemSelectedRegions = QFrame(self.frameSystemRegions)
        self.frameSystemSelectedRegions.setObjectName(u"frameSystemSelectedRegions")
        sizePolicy5.setHeightForWidth(self.frameSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.frameSystemSelectedRegions.setSizePolicy(sizePolicy5)
        self.frameSystemSelectedRegions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemSelectedRegions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemSelectedRegions.setLineWidth(0)
        self.verticalLayout_89 = QVBoxLayout(self.frameSystemSelectedRegions)
        self.verticalLayout_89.setSpacing(10)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.labelSystemSelectedRegions = QLabel(self.frameSystemSelectedRegions)
        self.labelSystemSelectedRegions.setObjectName(u"labelSystemSelectedRegions")
        sizePolicy8.setHeightForWidth(self.labelSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedRegions.setSizePolicy(sizePolicy8)
        self.labelSystemSelectedRegions.setFont(font)
        self.labelSystemSelectedRegions.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_89.addWidget(self.labelSystemSelectedRegions)

        self.listWidgetSystemSelectedRegions = CustomListSelfDrag(self.frameSystemSelectedRegions)
        self.listWidgetSystemSelectedRegions.setObjectName(u"listWidgetSystemSelectedRegions")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedRegions.setSizePolicy(sizePolicy9)
        self.listWidgetSystemSelectedRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedRegions.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemSelectedRegions.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedRegions.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemSelectedRegions.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemSelectedRegions.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemSelectedRegions.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedRegions.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.verticalLayout_89.addWidget(self.listWidgetSystemSelectedRegions)


        self.horizontalLayout_15.addWidget(self.frameSystemSelectedRegions)

        self.frameSystemRegionUpDown = QFrame(self.frameSystemRegions)
        self.frameSystemRegionUpDown.setObjectName(u"frameSystemRegionUpDown")
        sizePolicy5.setHeightForWidth(self.frameSystemRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionUpDown.setSizePolicy(sizePolicy5)
        self.frameSystemRegionUpDown.setMinimumSize(QSize(64, 0))
        self.frameSystemRegionUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameSystemRegionUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemRegionUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemRegionUpDown.setLineWidth(0)
        self.verticalLayout_90 = QVBoxLayout(self.frameSystemRegionUpDown)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalSpacerSystemRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_90.addItem(self.verticalSpacerSystemRegionUpDownTop)

        self.buttonSystemRegionUp = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionUp.setObjectName(u"buttonSystemRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionUp.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionUp.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionUp.setFont(font5)
        self.buttonSystemRegionUp.setIcon(icon6)

        self.verticalLayout_90.addWidget(self.buttonSystemRegionUp)

        self.buttonSystemRegionDown = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionDown.setObjectName(u"buttonSystemRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionDown.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionDown.setMaximumSize(QSize(40, 41))
        self.buttonSystemRegionDown.setFont(font5)
        self.buttonSystemRegionDown.setIcon(icon7)

        self.verticalLayout_90.addWidget(self.buttonSystemRegionDown)

        self.verticalSpacerSystemRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_90.addItem(self.verticalSpacerSystemRegionUpDownBottom)


        self.horizontalLayout_15.addWidget(self.frameSystemRegionUpDown)

        self.horizontalSpacerSystemRegions = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacerSystemRegions)


        self.verticalLayout_86.addWidget(self.frameSystemRegions)

        self.verticalLayoutSystemRegions = QVBoxLayout()
        self.verticalLayoutSystemRegions.setSpacing(10)
        self.verticalLayoutSystemRegions.setObjectName(u"verticalLayoutSystemRegions")
        self.verticalSpacerSystemRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayoutSystemRegions.addItem(self.verticalSpacerSystemRegionsEnglishButton)

        self.buttonSystemDefaultRegionOrder = QPushButton(self.tabContentsSystemRegions)
        self.buttonSystemDefaultRegionOrder.setObjectName(u"buttonSystemDefaultRegionOrder")
        sizePolicy6.setHeightForWidth(self.buttonSystemDefaultRegionOrder.sizePolicy().hasHeightForWidth())
        self.buttonSystemDefaultRegionOrder.setSizePolicy(sizePolicy6)
        self.buttonSystemDefaultRegionOrder.setMinimumSize(QSize(286, 41))

        self.verticalLayoutSystemRegions.addWidget(self.buttonSystemDefaultRegionOrder)


        self.verticalLayout_86.addLayout(self.verticalLayoutSystemRegions)

        self.verticalLayout_86.setStretch(3, 1)

        self.verticalLayout_85.addWidget(self.tabContentsSystemRegions)

        self.scrollAreaSystemRegions.setWidget(self.scrollAreaWidgetContentsSystemRegions)

        self.gridLayout_8.addWidget(self.scrollAreaSystemRegions, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemRegions, "")
        self.tabSystemLanguages = QWidget()
        self.tabSystemLanguages.setObjectName(u"tabSystemLanguages")
        self.gridLayout_17 = QGridLayout(self.tabSystemLanguages)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.scrollAreaSystemLanguages = QScrollArea(self.tabSystemLanguages)
        self.scrollAreaSystemLanguages.setObjectName(u"scrollAreaSystemLanguages")
        self.scrollAreaSystemLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemLanguages.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemLanguages.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemLanguages = QWidget()
        self.scrollAreaWidgetContentsSystemLanguages.setObjectName(u"scrollAreaWidgetContentsSystemLanguages")
        self.scrollAreaWidgetContentsSystemLanguages.setGeometry(QRect(0, 0, 640, 119))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemLanguages.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemLanguages.setSizePolicy(sizePolicy)
        self.verticalLayout_87 = QVBoxLayout(self.scrollAreaWidgetContentsSystemLanguages)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemLanguages = QFrame(self.scrollAreaWidgetContentsSystemLanguages)
        self.tabContentsSystemLanguages.setObjectName(u"tabContentsSystemLanguages")
        self.tabContentsSystemLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemLanguages.setLineWidth(0)
        self.verticalLayout_91 = QVBoxLayout(self.tabContentsSystemLanguages)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemLanguages = QHBoxLayout()
        self.horizontalLayoutHeaderSystemLanguages.setObjectName(u"horizontalLayoutHeaderSystemLanguages")
        self.labelSystemFilterByLanguages = QLabel(self.tabContentsSystemLanguages)
        self.labelSystemFilterByLanguages.setObjectName(u"labelSystemFilterByLanguages")
        sizePolicy3.setHeightForWidth(self.labelSystemFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByLanguages.setSizePolicy(sizePolicy3)
        self.labelSystemFilterByLanguages.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByLanguages.setFont(font2)

        self.horizontalLayoutHeaderSystemLanguages.addWidget(self.labelSystemFilterByLanguages)

        self.frameOverrideSystemLanguages = QFrame(self.tabContentsSystemLanguages)
        self.frameOverrideSystemLanguages.setObjectName(u"frameOverrideSystemLanguages")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemLanguages.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemLanguages.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemLanguages.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_98 = QVBoxLayout(self.frameOverrideSystemLanguages)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideLanguages = QCheckBox(self.frameOverrideSystemLanguages)
        self.checkBoxSystemOverrideLanguages.setObjectName(u"checkBoxSystemOverrideLanguages")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideLanguages.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideLanguages.setSizePolicy(sizePolicy3)

        self.verticalLayout_98.addWidget(self.checkBoxSystemOverrideLanguages, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemLanguages.addWidget(self.frameOverrideSystemLanguages)

        self.horizontalLayoutHeaderSystemLanguages.setStretch(0, 1)

        self.verticalLayout_91.addLayout(self.horizontalLayoutHeaderSystemLanguages)

        self.lineSystemLanguages = QFrame(self.tabContentsSystemLanguages)
        self.lineSystemLanguages.setObjectName(u"lineSystemLanguages")
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemLanguages.setPalette(palette19)
        self.lineSystemLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemLanguages.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_91.addWidget(self.lineSystemLanguages)

        self.frameSystemLanguages = QFrame(self.tabContentsSystemLanguages)
        self.frameSystemLanguages.setObjectName(u"frameSystemLanguages")
        self.frameSystemLanguages.setMinimumSize(QSize(0, 64))
        self.frameSystemLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLanguages.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.frameSystemLanguages)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frameSystemAvailableLanguages = QFrame(self.frameSystemLanguages)
        self.frameSystemAvailableLanguages.setObjectName(u"frameSystemAvailableLanguages")
        sizePolicy5.setHeightForWidth(self.frameSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.frameSystemAvailableLanguages.setSizePolicy(sizePolicy5)
        self.frameSystemAvailableLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemAvailableLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemAvailableLanguages.setLineWidth(0)
        self.verticalLayout_94 = QVBoxLayout(self.frameSystemAvailableLanguages)
        self.verticalLayout_94.setSpacing(10)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.labelSystemAvailableLanguages = QLabel(self.frameSystemAvailableLanguages)
        self.labelSystemAvailableLanguages.setObjectName(u"labelSystemAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemAvailableLanguages.setFont(font)
        self.labelSystemAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_94.addWidget(self.labelSystemAvailableLanguages)

        self.listWidgetSystemAvailableLanguages = CustomList(self.frameSystemAvailableLanguages)
        self.listWidgetSystemAvailableLanguages.setObjectName(u"listWidgetSystemAvailableLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableLanguages.setSizePolicy(sizePolicy9)
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
        self.listWidgetSystemAvailableLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_94.addWidget(self.listWidgetSystemAvailableLanguages)


        self.horizontalLayout_16.addWidget(self.frameSystemAvailableLanguages)

        self.frameSystemLanguageLeftRight = QFrame(self.frameSystemLanguages)
        self.frameSystemLanguageLeftRight.setObjectName(u"frameSystemLanguageLeftRight")
        sizePolicy5.setHeightForWidth(self.frameSystemLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageLeftRight.setSizePolicy(sizePolicy5)
        self.frameSystemLanguageLeftRight.setMinimumSize(QSize(64, 0))
        self.frameSystemLanguageLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameSystemLanguageLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguageLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLanguageLeftRight.setLineWidth(0)
        self.verticalLayout_95 = QVBoxLayout(self.frameSystemLanguageLeftRight)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalSpacerSystemLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_95.addItem(self.verticalSpacerSystemLanguageLeftRightTop)

        self.buttonSystemLanguageAllRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllRight.setObjectName(u"buttonSystemLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageAllRight.setFont(font5)
        self.buttonSystemLanguageAllRight.setIcon(icon2)
        self.buttonSystemLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_95.addWidget(self.buttonSystemLanguageAllRight)

        self.buttonSystemLanguageRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageRight.setObjectName(u"buttonSystemLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageRight.setFont(font5)
        self.buttonSystemLanguageRight.setIcon(icon3)
        self.buttonSystemLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_95.addWidget(self.buttonSystemLanguageRight)

        self.buttonSystemLanguageLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageLeft.setObjectName(u"buttonSystemLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageLeft.setFont(font5)
        self.buttonSystemLanguageLeft.setIcon(icon4)

        self.verticalLayout_95.addWidget(self.buttonSystemLanguageLeft)

        self.buttonSystemLanguageAllLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllLeft.setObjectName(u"buttonSystemLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageAllLeft.setFont(font5)
        self.buttonSystemLanguageAllLeft.setIcon(icon5)
        self.buttonSystemLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_95.addWidget(self.buttonSystemLanguageAllLeft)

        self.verticalSpacerSystemLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_95.addItem(self.verticalSpacerSystemLanguageLeftRightBottom)

        self.verticalSpacerSystemLanguageLeftRightBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_95.addItem(self.verticalSpacerSystemLanguageLeftRightBottomBuffer)


        self.horizontalLayout_16.addWidget(self.frameSystemLanguageLeftRight)

        self.frameSystemSelectedLanguages = QFrame(self.frameSystemLanguages)
        self.frameSystemSelectedLanguages.setObjectName(u"frameSystemSelectedLanguages")
        sizePolicy5.setHeightForWidth(self.frameSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.frameSystemSelectedLanguages.setSizePolicy(sizePolicy5)
        self.frameSystemSelectedLanguages.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemSelectedLanguages.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemSelectedLanguages.setLineWidth(0)
        self.verticalLayout_96 = QVBoxLayout(self.frameSystemSelectedLanguages)
        self.verticalLayout_96.setSpacing(10)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.labelSystemSelectedLanguages = QLabel(self.frameSystemSelectedLanguages)
        self.labelSystemSelectedLanguages.setObjectName(u"labelSystemSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemSelectedLanguages.setFont(font)
        self.labelSystemSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_96.addWidget(self.labelSystemSelectedLanguages)

        self.listWidgetSystemSelectedLanguages = CustomListSelfDrag(self.frameSystemSelectedLanguages)
        self.listWidgetSystemSelectedLanguages.setObjectName(u"listWidgetSystemSelectedLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetSystemSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemSelectedLanguages.setProperty(u"self_drag", True)
        self.listWidgetSystemSelectedLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_96.addWidget(self.listWidgetSystemSelectedLanguages)


        self.horizontalLayout_16.addWidget(self.frameSystemSelectedLanguages)

        self.frameSystemLanguageUpDown = QFrame(self.frameSystemLanguages)
        self.frameSystemLanguageUpDown.setObjectName(u"frameSystemLanguageUpDown")
        sizePolicy5.setHeightForWidth(self.frameSystemLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageUpDown.setSizePolicy(sizePolicy5)
        self.frameSystemLanguageUpDown.setMinimumSize(QSize(64, 0))
        self.frameSystemLanguageUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameSystemLanguageUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLanguageUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLanguageUpDown.setLineWidth(0)
        self.verticalLayout_97 = QVBoxLayout(self.frameSystemLanguageUpDown)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalSpacerSystemLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_97.addItem(self.verticalSpacerSystemLanguageUpDownTop)

        self.buttonSystemLanguageUp = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageUp.setObjectName(u"buttonSystemLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageUp.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageUp.setFont(font5)
        self.buttonSystemLanguageUp.setIcon(icon6)

        self.verticalLayout_97.addWidget(self.buttonSystemLanguageUp)

        self.buttonSystemLanguageDown = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageDown.setObjectName(u"buttonSystemLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageDown.setMaximumSize(QSize(40, 41))
        self.buttonSystemLanguageDown.setFont(font5)
        self.buttonSystemLanguageDown.setIcon(icon7)

        self.verticalLayout_97.addWidget(self.buttonSystemLanguageDown)

        self.verticalSpacerSystemLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_97.addItem(self.verticalSpacerSystemLanguageUpDownBottom)

        self.verticalSpacerSystemLanguageUpDownBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_97.addItem(self.verticalSpacerSystemLanguageUpDownBottomBuffer)


        self.horizontalLayout_16.addWidget(self.frameSystemLanguageUpDown)

        self.horizontalSpacerSystemLanguages = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacerSystemLanguages)


        self.verticalLayout_91.addWidget(self.frameSystemLanguages)


        self.verticalLayout_87.addWidget(self.tabContentsSystemLanguages)

        self.scrollAreaSystemLanguages.setWidget(self.scrollAreaWidgetContentsSystemLanguages)

        self.gridLayout_17.addWidget(self.scrollAreaSystemLanguages, 1, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemLanguages, "")
        self.tabSystemVideo = QWidget()
        self.tabSystemVideo.setObjectName(u"tabSystemVideo")
        self.gridLayout_18 = QGridLayout(self.tabSystemVideo)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.scrollAreaSystemVideo = QScrollArea(self.tabSystemVideo)
        self.scrollAreaSystemVideo.setObjectName(u"scrollAreaSystemVideo")
        self.scrollAreaSystemVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemVideo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemVideo.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemVideo = QWidget()
        self.scrollAreaWidgetContentsSystemVideo.setObjectName(u"scrollAreaWidgetContentsSystemVideo")
        self.scrollAreaWidgetContentsSystemVideo.setGeometry(QRect(0, 0, 580, 119))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemVideo.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemVideo.setSizePolicy(sizePolicy)
        self.verticalLayout_92 = QVBoxLayout(self.scrollAreaWidgetContentsSystemVideo)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemVideo = QFrame(self.scrollAreaWidgetContentsSystemVideo)
        self.tabContentsSystemVideo.setObjectName(u"tabContentsSystemVideo")
        self.tabContentsSystemVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemVideo.setLineWidth(0)
        self.verticalLayout_99 = QVBoxLayout(self.tabContentsSystemVideo)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemVideo = QHBoxLayout()
        self.horizontalLayoutHeaderSystemVideo.setObjectName(u"horizontalLayoutHeaderSystemVideo")
        self.labelSystemFilterByVideo = QLabel(self.tabContentsSystemVideo)
        self.labelSystemFilterByVideo.setObjectName(u"labelSystemFilterByVideo")
        sizePolicy3.setHeightForWidth(self.labelSystemFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByVideo.setSizePolicy(sizePolicy3)
        self.labelSystemFilterByVideo.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByVideo.setFont(font2)

        self.horizontalLayoutHeaderSystemVideo.addWidget(self.labelSystemFilterByVideo)

        self.frameOverrideSystemVideo = QFrame(self.tabContentsSystemVideo)
        self.frameOverrideSystemVideo.setObjectName(u"frameOverrideSystemVideo")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemVideo.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemVideo.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemVideo.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_103 = QVBoxLayout(self.frameOverrideSystemVideo)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideVideo = QCheckBox(self.frameOverrideSystemVideo)
        self.checkBoxSystemOverrideVideo.setObjectName(u"checkBoxSystemOverrideVideo")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideVideo.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideVideo.setSizePolicy(sizePolicy3)

        self.verticalLayout_103.addWidget(self.checkBoxSystemOverrideVideo, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemVideo.addWidget(self.frameOverrideSystemVideo)

        self.horizontalLayoutHeaderSystemVideo.setStretch(0, 1)

        self.verticalLayout_99.addLayout(self.horizontalLayoutHeaderSystemVideo)

        self.lineSystemVideoStandards = QFrame(self.tabContentsSystemVideo)
        self.lineSystemVideoStandards.setObjectName(u"lineSystemVideoStandards")
        palette20 = QPalette()
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemVideoStandards.setPalette(palette20)
        self.lineSystemVideoStandards.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemVideoStandards.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_99.addWidget(self.lineSystemVideoStandards)

        self.frameSystemVideo = QFrame(self.tabContentsSystemVideo)
        self.frameSystemVideo.setObjectName(u"frameSystemVideo")
        self.frameSystemVideo.setMinimumSize(QSize(0, 64))
        self.frameSystemVideo.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemVideo.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemVideo.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.frameSystemVideo)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frameSystemVideoOrder = QFrame(self.frameSystemVideo)
        self.frameSystemVideoOrder.setObjectName(u"frameSystemVideoOrder")
        sizePolicy5.setHeightForWidth(self.frameSystemVideoOrder.sizePolicy().hasHeightForWidth())
        self.frameSystemVideoOrder.setSizePolicy(sizePolicy5)
        self.frameSystemVideoOrder.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemVideoOrder.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemVideoOrder.setLineWidth(0)
        self.verticalLayout_101 = QVBoxLayout(self.frameSystemVideoOrder)
        self.verticalLayout_101.setSpacing(10)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.labelSystemVideoStandardsOrder = QLabel(self.frameSystemVideoOrder)
        self.labelSystemVideoStandardsOrder.setObjectName(u"labelSystemVideoStandardsOrder")
        sizePolicy8.setHeightForWidth(self.labelSystemVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelSystemVideoStandardsOrder.setSizePolicy(sizePolicy8)
        self.labelSystemVideoStandardsOrder.setFont(font)
        self.labelSystemVideoStandardsOrder.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_101.addWidget(self.labelSystemVideoStandardsOrder)

        self.listWidgetSystemVideoStandards = CustomListSelfDrag(self.frameSystemVideoOrder)
        self.listWidgetSystemVideoStandards.setObjectName(u"listWidgetSystemVideoStandards")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemVideoStandards.setSizePolicy(sizePolicy9)
        self.listWidgetSystemVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemVideoStandards.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemVideoStandards.setTabKeyNavigation(True)
        self.listWidgetSystemVideoStandards.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemVideoStandards.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemVideoStandards.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemVideoStandards.setAlternatingRowColors(False)
        self.listWidgetSystemVideoStandards.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemVideoStandards.setProperty(u"self_drag", True)
        self.listWidgetSystemVideoStandards.setProperty(u"is_drag_drop", True)

        self.verticalLayout_101.addWidget(self.listWidgetSystemVideoStandards)


        self.horizontalLayout_17.addWidget(self.frameSystemVideoOrder)

        self.frameSystemVideoStandardUpDown = QFrame(self.frameSystemVideo)
        self.frameSystemVideoStandardUpDown.setObjectName(u"frameSystemVideoStandardUpDown")
        sizePolicy5.setHeightForWidth(self.frameSystemVideoStandardUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemVideoStandardUpDown.setSizePolicy(sizePolicy5)
        self.frameSystemVideoStandardUpDown.setMinimumSize(QSize(64, 0))
        self.frameSystemVideoStandardUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameSystemVideoStandardUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemVideoStandardUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemVideoStandardUpDown.setLineWidth(0)
        self.verticalLayout_102 = QVBoxLayout(self.frameSystemVideoStandardUpDown)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalSpacerSystemVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_102.addItem(self.verticalSpacerSystemVideoUpDownTop)

        self.buttonSystemVideoStandardUp = QPushButton(self.frameSystemVideoStandardUpDown)
        self.buttonSystemVideoStandardUp.setObjectName(u"buttonSystemVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardUp.setMaximumSize(QSize(40, 41))
        self.buttonSystemVideoStandardUp.setFont(font5)
        self.buttonSystemVideoStandardUp.setIcon(icon6)

        self.verticalLayout_102.addWidget(self.buttonSystemVideoStandardUp)

        self.buttonSystemVideoStandardDown = QPushButton(self.frameSystemVideoStandardUpDown)
        self.buttonSystemVideoStandardDown.setObjectName(u"buttonSystemVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardDown.setMaximumSize(QSize(40, 41))
        self.buttonSystemVideoStandardDown.setFont(font5)
        self.buttonSystemVideoStandardDown.setIcon(icon7)

        self.verticalLayout_102.addWidget(self.buttonSystemVideoStandardDown)

        self.verticalSpacerSytemVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_102.addItem(self.verticalSpacerSytemVideoUpDownBottom)

        self.verticalSpacerSystemVideoUpDownBottomBuffer = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_102.addItem(self.verticalSpacerSystemVideoUpDownBottomBuffer)


        self.horizontalLayout_17.addWidget(self.frameSystemVideoStandardUpDown)

        self.horizontalSpacerSystemVideo = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacerSystemVideo)


        self.verticalLayout_99.addWidget(self.frameSystemVideo)


        self.verticalLayout_92.addWidget(self.tabContentsSystemVideo)

        self.scrollAreaSystemVideo.setWidget(self.scrollAreaWidgetContentsSystemVideo)

        self.gridLayout_18.addWidget(self.scrollAreaSystemVideo, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemVideo, "")
        self.tabSystemExclusions = QWidget()
        self.tabSystemExclusions.setObjectName(u"tabSystemExclusions")
        self.gridLayout_19 = QGridLayout(self.tabSystemExclusions)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.scrollAreaSystemExclusions = QScrollArea(self.tabSystemExclusions)
        self.scrollAreaSystemExclusions.setObjectName(u"scrollAreaSystemExclusions")
        self.scrollAreaSystemExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemExclusions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemExclusions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemExclusions = QWidget()
        self.scrollAreaWidgetContentsSystemExclusions.setObjectName(u"scrollAreaWidgetContentsSystemExclusions")
        self.scrollAreaWidgetContentsSystemExclusions.setGeometry(QRect(0, 0, 514, 277))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemExclusions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemExclusions.setSizePolicy(sizePolicy)
        self.verticalLayout_100 = QVBoxLayout(self.scrollAreaWidgetContentsSystemExclusions)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemExclusions = QFrame(self.scrollAreaWidgetContentsSystemExclusions)
        self.tabContentsSystemExclusions.setObjectName(u"tabContentsSystemExclusions")
        self.tabContentsSystemExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemExclusions.setLineWidth(0)
        self.verticalLayout_104 = QVBoxLayout(self.tabContentsSystemExclusions)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemExclusions = QHBoxLayout()
        self.horizontalLayoutHeaderSystemExclusions.setObjectName(u"horizontalLayoutHeaderSystemExclusions")
        self.labelSystemExclusions = QLabel(self.tabContentsSystemExclusions)
        self.labelSystemExclusions.setObjectName(u"labelSystemExclusions")
        sizePolicy3.setHeightForWidth(self.labelSystemExclusions.sizePolicy().hasHeightForWidth())
        self.labelSystemExclusions.setSizePolicy(sizePolicy3)
        self.labelSystemExclusions.setMinimumSize(QSize(0, 0))
        self.labelSystemExclusions.setFont(font2)

        self.horizontalLayoutHeaderSystemExclusions.addWidget(self.labelSystemExclusions)

        self.frameOverrideSystemExclusions = QFrame(self.tabContentsSystemExclusions)
        self.frameOverrideSystemExclusions.setObjectName(u"frameOverrideSystemExclusions")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemExclusions.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemExclusions.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemExclusions.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_106 = QVBoxLayout(self.frameOverrideSystemExclusions)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideExclusions = QCheckBox(self.frameOverrideSystemExclusions)
        self.checkBoxSystemOverrideExclusions.setObjectName(u"checkBoxSystemOverrideExclusions")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideExclusions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideExclusions.setSizePolicy(sizePolicy3)

        self.verticalLayout_106.addWidget(self.checkBoxSystemOverrideExclusions, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemExclusions.addWidget(self.frameOverrideSystemExclusions)

        self.horizontalLayoutHeaderSystemExclusions.setStretch(0, 1)

        self.verticalLayout_104.addLayout(self.horizontalLayoutHeaderSystemExclusions)

        self.lineSystemExclusions = QFrame(self.tabContentsSystemExclusions)
        self.lineSystemExclusions.setObjectName(u"lineSystemExclusions")
        palette21 = QPalette()
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemExclusions.setPalette(palette21)
        self.lineSystemExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemExclusions.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_104.addWidget(self.lineSystemExclusions)

        self.horizontalLayoutSystemExclusions = QHBoxLayout()
        self.horizontalLayoutSystemExclusions.setSpacing(24)
        self.horizontalLayoutSystemExclusions.setObjectName(u"horizontalLayoutSystemExclusions")
        self.verticalLayout1SystemExclusions = QVBoxLayout()
        self.verticalLayout1SystemExclusions.setSpacing(8)
        self.verticalLayout1SystemExclusions.setObjectName(u"verticalLayout1SystemExclusions")
        self.checkBoxSystemExcludeAddOns = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeAddOns.setObjectName(u"checkBoxSystemExcludeAddOns")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeAddOns)

        self.checkBoxSystemExcludeApplications = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeApplications.setObjectName(u"checkBoxSystemExcludeApplications")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeApplications)

        self.checkBoxSystemExcludeAudio = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeAudio.setObjectName(u"checkBoxSystemExcludeAudio")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeAudio)

        self.checkBoxSystemExcludeBadDumps = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeBadDumps.setObjectName(u"checkBoxSystemExcludeBadDumps")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeBadDumps)

        self.checkBoxSystemExcludeBIOS = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeBIOS.setObjectName(u"checkBoxSystemExcludeBIOS")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeBIOS)

        self.checkBoxSystemExcludeBonusDiscs = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeBonusDiscs.setObjectName(u"checkBoxSystemExcludeBonusDiscs")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeBonusDiscs)

        self.checkBoxSystemExcludeCoverdiscs = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeCoverdiscs.setObjectName(u"checkBoxSystemExcludeCoverdiscs")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeCoverdiscs)

        self.checkBoxSystemExcludeDemos = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeDemos.setObjectName(u"checkBoxSystemExcludeDemos")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeDemos)

        self.checkBoxSystemExcludeEducational = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeEducational.setObjectName(u"checkBoxSystemExcludeEducational")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeEducational)

        self.checkBoxSystemExcludeGames = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeGames.setObjectName(u"checkBoxSystemExcludeGames")

        self.verticalLayout1SystemExclusions.addWidget(self.checkBoxSystemExcludeGames)

        self.verticalSpacer1SystemExclusions = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout1SystemExclusions.addItem(self.verticalSpacer1SystemExclusions)


        self.horizontalLayoutSystemExclusions.addLayout(self.verticalLayout1SystemExclusions)

        self.verticalLayout2SystemExclusions = QVBoxLayout()
        self.verticalLayout2SystemExclusions.setSpacing(8)
        self.verticalLayout2SystemExclusions.setObjectName(u"verticalLayout2SystemExclusions")
        self.checkBoxSystemExcludeManuals = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeManuals.setObjectName(u"checkBoxSystemExcludeManuals")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludeManuals)

        self.checkBoxSystemExcludeMIA = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeMIA.setObjectName(u"checkBoxSystemExcludeMIA")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludeMIA)

        self.checkBoxSystemExcludeMultimedia = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeMultimedia.setObjectName(u"checkBoxSystemExcludeMultimedia")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludeMultimedia)

        self.checkBoxSystemExcludePreproduction = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludePreproduction.setObjectName(u"checkBoxSystemExcludePreproduction")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludePreproduction)

        self.checkBoxSystemExcludePromotional = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludePromotional.setObjectName(u"checkBoxSystemExcludePromotional")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludePromotional)

        self.checkBoxSystemExcludeUnlicensedAll = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeUnlicensedAll.setObjectName(u"checkBoxSystemExcludeUnlicensedAll")
        self.checkBoxSystemExcludeUnlicensedAll.setTristate(False)

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludeUnlicensedAll)

        self.frameUnlicensedSubOptionsSystemExclusions = QFrame(self.tabContentsSystemExclusions)
        self.frameUnlicensedSubOptionsSystemExclusions.setObjectName(u"frameUnlicensedSubOptionsSystemExclusions")
        self.frameUnlicensedSubOptionsSystemExclusions.setMinimumSize(QSize(0, 40))
        self.frameUnlicensedSubOptionsSystemExclusions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameUnlicensedSubOptionsSystemExclusions.setFrameShadow(QFrame.Shadow.Plain)
        self.frameUnlicensedSubOptionsSystemExclusions.setLineWidth(0)
        self.horizontalLayout_18 = QHBoxLayout(self.frameUnlicensedSubOptionsSystemExclusions)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerUnlicensedSubOptionsSystemExclusions = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacerUnlicensedSubOptionsSystemExclusions)

        self.verticalLayoutUnlicensedSubOptionsSystemExclusions = QVBoxLayout()
        self.verticalLayoutUnlicensedSubOptionsSystemExclusions.setSpacing(8)
        self.verticalLayoutUnlicensedSubOptionsSystemExclusions.setObjectName(u"verticalLayoutUnlicensedSubOptionsSystemExclusions")
        self.checkBoxSystemExcludeAftermarket = QCheckBox(self.frameUnlicensedSubOptionsSystemExclusions)
        self.checkBoxSystemExcludeAftermarket.setObjectName(u"checkBoxSystemExcludeAftermarket")

        self.verticalLayoutUnlicensedSubOptionsSystemExclusions.addWidget(self.checkBoxSystemExcludeAftermarket)

        self.checkBoxSystemExcludePirate = QCheckBox(self.frameUnlicensedSubOptionsSystemExclusions)
        self.checkBoxSystemExcludePirate.setObjectName(u"checkBoxSystemExcludePirate")

        self.verticalLayoutUnlicensedSubOptionsSystemExclusions.addWidget(self.checkBoxSystemExcludePirate)

        self.checkBoxSystemExcludeUnlicensed = QCheckBox(self.frameUnlicensedSubOptionsSystemExclusions)
        self.checkBoxSystemExcludeUnlicensed.setObjectName(u"checkBoxSystemExcludeUnlicensed")

        self.verticalLayoutUnlicensedSubOptionsSystemExclusions.addWidget(self.checkBoxSystemExcludeUnlicensed)


        self.horizontalLayout_18.addLayout(self.verticalLayoutUnlicensedSubOptionsSystemExclusions)


        self.verticalLayout2SystemExclusions.addWidget(self.frameUnlicensedSubOptionsSystemExclusions)

        self.checkBoxSystemExcludeVideo = QCheckBox(self.tabContentsSystemExclusions)
        self.checkBoxSystemExcludeVideo.setObjectName(u"checkBoxSystemExcludeVideo")

        self.verticalLayout2SystemExclusions.addWidget(self.checkBoxSystemExcludeVideo)

        self.verticalSpacer2SystemExclusions = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout2SystemExclusions.addItem(self.verticalSpacer2SystemExclusions)


        self.horizontalLayoutSystemExclusions.addLayout(self.verticalLayout2SystemExclusions)

        self.verticalLayout3SystemExclusions = QVBoxLayout()
        self.verticalLayout3SystemExclusions.setObjectName(u"verticalLayout3SystemExclusions")
        self.frameSystemExclusionsSelectDeselect = QFrame(self.tabContentsSystemExclusions)
        self.frameSystemExclusionsSelectDeselect.setObjectName(u"frameSystemExclusionsSelectDeselect")
        self.frameSystemExclusionsSelectDeselect.setMinimumSize(QSize(0, 20))
        self.frameSystemExclusionsSelectDeselect.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemExclusionsSelectDeselect.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemExclusionsSelectDeselect.setLineWidth(0)
        self.verticalLayout_9 = QVBoxLayout(self.frameSystemExclusionsSelectDeselect)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.buttonSystemSelectAllExclude = QPushButton(self.frameSystemExclusionsSelectDeselect)
        self.buttonSystemSelectAllExclude.setObjectName(u"buttonSystemSelectAllExclude")
        sizePolicy6.setHeightForWidth(self.buttonSystemSelectAllExclude.sizePolicy().hasHeightForWidth())
        self.buttonSystemSelectAllExclude.setSizePolicy(sizePolicy6)
        self.buttonSystemSelectAllExclude.setMinimumSize(QSize(120, 30))

        self.verticalLayout_9.addWidget(self.buttonSystemSelectAllExclude)

        self.buttonSystemDeselectAllExclude = QPushButton(self.frameSystemExclusionsSelectDeselect)
        self.buttonSystemDeselectAllExclude.setObjectName(u"buttonSystemDeselectAllExclude")
        sizePolicy6.setHeightForWidth(self.buttonSystemDeselectAllExclude.sizePolicy().hasHeightForWidth())
        self.buttonSystemDeselectAllExclude.setSizePolicy(sizePolicy6)
        self.buttonSystemDeselectAllExclude.setMinimumSize(QSize(120, 30))

        self.verticalLayout_9.addWidget(self.buttonSystemDeselectAllExclude)


        self.verticalLayout3SystemExclusions.addWidget(self.frameSystemExclusionsSelectDeselect)

        self.verticalSpacer3SystemExclusions = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout3SystemExclusions.addItem(self.verticalSpacer3SystemExclusions)

        self.verticalLayout3SystemExclusions.setStretch(1, 4)

        self.horizontalLayoutSystemExclusions.addLayout(self.verticalLayout3SystemExclusions)

        self.horizontalSpacerSystemExclusions_ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclusions_)


        self.verticalLayout_104.addLayout(self.horizontalLayoutSystemExclusions)

        self.verticalSpacerSystemExclusions = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_104.addItem(self.verticalSpacerSystemExclusions)


        self.verticalLayout_100.addWidget(self.tabContentsSystemExclusions)

        self.scrollAreaSystemExclusions.setWidget(self.scrollAreaWidgetContentsSystemExclusions)

        self.gridLayout_19.addWidget(self.scrollAreaSystemExclusions, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemExclusions, "")
        self.tabSystemLocalization = QWidget()
        self.tabSystemLocalization.setObjectName(u"tabSystemLocalization")
        self.gridLayout_20 = QGridLayout(self.tabSystemLocalization)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.scrollAreaSystemLocalization = QScrollArea(self.tabSystemLocalization)
        self.scrollAreaSystemLocalization.setObjectName(u"scrollAreaSystemLocalization")
        self.scrollAreaSystemLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemLocalization.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemLocalization.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemLocalization = QWidget()
        self.scrollAreaWidgetContentsSystemLocalization.setObjectName(u"scrollAreaWidgetContentsSystemLocalization")
        self.scrollAreaWidgetContentsSystemLocalization.setGeometry(QRect(0, 0, 640, 429))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemLocalization.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemLocalization.setSizePolicy(sizePolicy)
        self.verticalLayout_105 = QVBoxLayout(self.scrollAreaWidgetContentsSystemLocalization)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemLocalization = QFrame(self.scrollAreaWidgetContentsSystemLocalization)
        self.tabContentsSystemLocalization.setObjectName(u"tabContentsSystemLocalization")
        self.tabContentsSystemLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemLocalization.setLineWidth(0)
        self.verticalLayout_107 = QVBoxLayout(self.tabContentsSystemLocalization)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemLocalization = QHBoxLayout()
        self.horizontalLayoutHeaderSystemLocalization.setObjectName(u"horizontalLayoutHeaderSystemLocalization")
        self.labelSystemUseLocalNames = QLabel(self.tabContentsSystemLocalization)
        self.labelSystemUseLocalNames.setObjectName(u"labelSystemUseLocalNames")
        sizePolicy3.setHeightForWidth(self.labelSystemUseLocalNames.sizePolicy().hasHeightForWidth())
        self.labelSystemUseLocalNames.setSizePolicy(sizePolicy3)
        self.labelSystemUseLocalNames.setMinimumSize(QSize(0, 0))
        self.labelSystemUseLocalNames.setFont(font2)

        self.horizontalLayoutHeaderSystemLocalization.addWidget(self.labelSystemUseLocalNames)

        self.frameOverrideSystemLocalization = QFrame(self.tabContentsSystemLocalization)
        self.frameOverrideSystemLocalization.setObjectName(u"frameOverrideSystemLocalization")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemLocalization.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemLocalization.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemLocalization.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_114 = QVBoxLayout(self.frameOverrideSystemLocalization)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideLocalization = QCheckBox(self.frameOverrideSystemLocalization)
        self.checkBoxSystemOverrideLocalization.setObjectName(u"checkBoxSystemOverrideLocalization")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideLocalization.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideLocalization.setSizePolicy(sizePolicy3)

        self.verticalLayout_114.addWidget(self.checkBoxSystemOverrideLocalization, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemLocalization.addWidget(self.frameOverrideSystemLocalization)

        self.horizontalLayoutHeaderSystemLocalization.setStretch(0, 1)

        self.verticalLayout_107.addLayout(self.horizontalLayoutHeaderSystemLocalization)

        self.lineSystemLocalizations = QFrame(self.tabContentsSystemLocalization)
        self.lineSystemLocalizations.setObjectName(u"lineSystemLocalizations")
        palette22 = QPalette()
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemLocalizations.setPalette(palette22)
        self.lineSystemLocalizations.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemLocalizations.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_107.addWidget(self.lineSystemLocalizations)

        self.labelSystemLocalizeNames = QLabel(self.tabContentsSystemLocalization)
        self.labelSystemLocalizeNames.setObjectName(u"labelSystemLocalizeNames")
        self.labelSystemLocalizeNames.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemLocalizeNames.setWordWrap(True)
        self.labelSystemLocalizeNames.setOpenExternalLinks(True)
        self.labelSystemLocalizeNames.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_107.addWidget(self.labelSystemLocalizeNames)

        self.verticalSpacerSystemLocalizationList = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_107.addItem(self.verticalSpacerSystemLocalizationList)

        self.frameSystemLocalization = QFrame(self.tabContentsSystemLocalization)
        self.frameSystemLocalization.setObjectName(u"frameSystemLocalization")
        self.frameSystemLocalization.setMinimumSize(QSize(0, 64))
        self.frameSystemLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_19 = QHBoxLayout(self.frameSystemLocalization)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frameSystemAvailableLocalization = QFrame(self.frameSystemLocalization)
        self.frameSystemAvailableLocalization.setObjectName(u"frameSystemAvailableLocalization")
        sizePolicy5.setHeightForWidth(self.frameSystemAvailableLocalization.sizePolicy().hasHeightForWidth())
        self.frameSystemAvailableLocalization.setSizePolicy(sizePolicy5)
        self.frameSystemAvailableLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemAvailableLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemAvailableLocalization.setLineWidth(0)
        self.verticalLayout_109 = QVBoxLayout(self.frameSystemAvailableLocalization)
        self.verticalLayout_109.setSpacing(10)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.labelSystemLocalizationAvailableLanguages = QLabel(self.frameSystemAvailableLocalization)
        self.labelSystemLocalizationAvailableLanguages.setObjectName(u"labelSystemLocalizationAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemLocalizationAvailableLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemLocalizationAvailableLanguages.setFont(font)
        self.labelSystemLocalizationAvailableLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_109.addWidget(self.labelSystemLocalizationAvailableLanguages)

        self.listWidgetSystemLocalizationAvailableLanguages = CustomList(self.frameSystemAvailableLocalization)
        self.listWidgetSystemLocalizationAvailableLanguages.setObjectName(u"listWidgetSystemLocalizationAvailableLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemLocalizationAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemLocalizationAvailableLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetSystemLocalizationAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemLocalizationAvailableLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemLocalizationAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemLocalizationAvailableLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemLocalizationAvailableLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemLocalizationAvailableLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemLocalizationAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemLocalizationAvailableLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemLocalizationAvailableLanguages.setSortingEnabled(True)
        self.listWidgetSystemLocalizationAvailableLanguages.setProperty(u"self_drag", False)
        self.listWidgetSystemLocalizationAvailableLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_109.addWidget(self.listWidgetSystemLocalizationAvailableLanguages)


        self.horizontalLayout_19.addWidget(self.frameSystemAvailableLocalization)

        self.frameSystemLocalizationLeftRight = QFrame(self.frameSystemLocalization)
        self.frameSystemLocalizationLeftRight.setObjectName(u"frameSystemLocalizationLeftRight")
        sizePolicy5.setHeightForWidth(self.frameSystemLocalizationLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemLocalizationLeftRight.setSizePolicy(sizePolicy5)
        self.frameSystemLocalizationLeftRight.setMinimumSize(QSize(64, 0))
        self.frameSystemLocalizationLeftRight.setMaximumSize(QSize(64, 16777215))
        self.frameSystemLocalizationLeftRight.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalizationLeftRight.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLocalizationLeftRight.setLineWidth(0)
        self.verticalLayout_110 = QVBoxLayout(self.frameSystemLocalizationLeftRight)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalSpacerSystemLocalizationLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_110.addItem(self.verticalSpacerSystemLocalizationLeftRightTop)

        self.buttonSystemLocalizationAllRight = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationAllRight.setObjectName(u"buttonSystemLocalizationAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllRight.setFont(font5)
        self.buttonSystemLocalizationAllRight.setIcon(icon2)
        self.buttonSystemLocalizationAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_110.addWidget(self.buttonSystemLocalizationAllRight)

        self.buttonSystemLocalizationRight = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationRight.setObjectName(u"buttonSystemLocalizationRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationRight.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationRight.setFont(font5)
        self.buttonSystemLocalizationRight.setIcon(icon3)
        self.buttonSystemLocalizationRight.setIconSize(QSize(16, 16))

        self.verticalLayout_110.addWidget(self.buttonSystemLocalizationRight)

        self.buttonSystemLocalizationLeft = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationLeft.setObjectName(u"buttonSystemLocalizationLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationLeft.setFont(font5)
        self.buttonSystemLocalizationLeft.setIcon(icon4)

        self.verticalLayout_110.addWidget(self.buttonSystemLocalizationLeft)

        self.buttonSystemLocalizationAllLeft = QPushButton(self.frameSystemLocalizationLeftRight)
        self.buttonSystemLocalizationAllLeft.setObjectName(u"buttonSystemLocalizationAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllLeft.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationAllLeft.setFont(font5)
        self.buttonSystemLocalizationAllLeft.setIcon(icon5)
        self.buttonSystemLocalizationAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_110.addWidget(self.buttonSystemLocalizationAllLeft)

        self.verticalSpacerSystemLocalizationLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_110.addItem(self.verticalSpacerSystemLocalizationLeftRightBottom)


        self.horizontalLayout_19.addWidget(self.frameSystemLocalizationLeftRight)

        self.frameSystemSelectedLocalization = QFrame(self.frameSystemLocalization)
        self.frameSystemSelectedLocalization.setObjectName(u"frameSystemSelectedLocalization")
        sizePolicy5.setHeightForWidth(self.frameSystemSelectedLocalization.sizePolicy().hasHeightForWidth())
        self.frameSystemSelectedLocalization.setSizePolicy(sizePolicy5)
        self.frameSystemSelectedLocalization.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemSelectedLocalization.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemSelectedLocalization.setLineWidth(0)
        self.verticalLayout_111 = QVBoxLayout(self.frameSystemSelectedLocalization)
        self.verticalLayout_111.setSpacing(10)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.labelSystemLocalizationSelectedLanguages = QLabel(self.frameSystemSelectedLocalization)
        self.labelSystemLocalizationSelectedLanguages.setObjectName(u"labelSystemLocalizationSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.labelSystemLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemLocalizationSelectedLanguages.setSizePolicy(sizePolicy8)
        self.labelSystemLocalizationSelectedLanguages.setFont(font)
        self.labelSystemLocalizationSelectedLanguages.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_111.addWidget(self.labelSystemLocalizationSelectedLanguages)

        self.listWidgetSystemLocalizationSelectedLanguages = CustomListSelfDrag(self.frameSystemSelectedLocalization)
        self.listWidgetSystemLocalizationSelectedLanguages.setObjectName(u"listWidgetSystemLocalizationSelectedLanguages")
        sizePolicy9.setHeightForWidth(self.listWidgetSystemLocalizationSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemLocalizationSelectedLanguages.setSizePolicy(sizePolicy9)
        self.listWidgetSystemLocalizationSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemLocalizationSelectedLanguages.setFrameShape(QFrame.Shape.Box)
        self.listWidgetSystemLocalizationSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemLocalizationSelectedLanguages.setProperty(u"showDropIndicator", True)
        self.listWidgetSystemLocalizationSelectedLanguages.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetSystemLocalizationSelectedLanguages.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.listWidgetSystemLocalizationSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemLocalizationSelectedLanguages.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidgetSystemLocalizationSelectedLanguages.setProperty(u"self_drag", True)
        self.listWidgetSystemLocalizationSelectedLanguages.setProperty(u"is_drag_drop", True)

        self.verticalLayout_111.addWidget(self.listWidgetSystemLocalizationSelectedLanguages)


        self.horizontalLayout_19.addWidget(self.frameSystemSelectedLocalization)

        self.frameSystemLocalizationUpDown = QFrame(self.frameSystemLocalization)
        self.frameSystemLocalizationUpDown.setObjectName(u"frameSystemLocalizationUpDown")
        sizePolicy5.setHeightForWidth(self.frameSystemLocalizationUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemLocalizationUpDown.setSizePolicy(sizePolicy5)
        self.frameSystemLocalizationUpDown.setMinimumSize(QSize(64, 0))
        self.frameSystemLocalizationUpDown.setMaximumSize(QSize(64, 16777215))
        self.frameSystemLocalizationUpDown.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemLocalizationUpDown.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemLocalizationUpDown.setLineWidth(0)
        self.verticalLayout_112 = QVBoxLayout(self.frameSystemLocalizationUpDown)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalSpacerSystemLocalizationDownTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_112.addItem(self.verticalSpacerSystemLocalizationDownTop)

        self.buttonSystemLocalizationUp = QPushButton(self.frameSystemLocalizationUpDown)
        self.buttonSystemLocalizationUp.setObjectName(u"buttonSystemLocalizationUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationUp.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationUp.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationUp.setFont(font5)
        self.buttonSystemLocalizationUp.setIcon(icon6)

        self.verticalLayout_112.addWidget(self.buttonSystemLocalizationUp)

        self.buttonSystemLocalizationDown = QPushButton(self.frameSystemLocalizationUpDown)
        self.buttonSystemLocalizationDown.setObjectName(u"buttonSystemLocalizationDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemLocalizationDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemLocalizationDown.setSizePolicy(sizePolicy6)
        self.buttonSystemLocalizationDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemLocalizationDown.setMaximumSize(QSize(40, 41))
        self.buttonSystemLocalizationDown.setFont(font5)
        self.buttonSystemLocalizationDown.setIcon(icon7)

        self.verticalLayout_112.addWidget(self.buttonSystemLocalizationDown)

        self.verticalSpacerSystemLocalizationUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_112.addItem(self.verticalSpacerSystemLocalizationUpDownBottom)


        self.horizontalLayout_19.addWidget(self.frameSystemLocalizationUpDown)

        self.horizontalSpacerSystemLocalization = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacerSystemLocalization)


        self.verticalLayout_107.addWidget(self.frameSystemLocalization)


        self.verticalLayout_105.addWidget(self.tabContentsSystemLocalization)

        self.scrollAreaSystemLocalization.setWidget(self.scrollAreaWidgetContentsSystemLocalization)

        self.gridLayout_20.addWidget(self.scrollAreaSystemLocalization, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemLocalization, "")
        self.tabSystemOverrides = QWidget()
        self.tabSystemOverrides.setObjectName(u"tabSystemOverrides")
        self.gridLayout_6 = QGridLayout(self.tabSystemOverrides)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollAreaSystemOverrides = QScrollArea(self.tabSystemOverrides)
        self.scrollAreaSystemOverrides.setObjectName(u"scrollAreaSystemOverrides")
        self.scrollAreaSystemOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemOverrides.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemOverrides.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemOverrides = QWidget()
        self.scrollAreaWidgetContentsSystemOverrides.setObjectName(u"scrollAreaWidgetContentsSystemOverrides")
        self.scrollAreaWidgetContentsSystemOverrides.setGeometry(QRect(0, 0, 315, 477))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemOverrides.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemOverrides.setSizePolicy(sizePolicy)
        self.verticalLayout_108 = QVBoxLayout(self.scrollAreaWidgetContentsSystemOverrides)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemOverrides = QFrame(self.scrollAreaWidgetContentsSystemOverrides)
        self.tabContentsSystemOverrides.setObjectName(u"tabContentsSystemOverrides")
        self.tabContentsSystemOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemOverrides.setLineWidth(0)
        self.verticalLayout_113 = QVBoxLayout(self.tabContentsSystemOverrides)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemOverrides = QHBoxLayout()
        self.horizontalLayoutHeaderSystemOverrides.setObjectName(u"horizontalLayoutHeaderSystemOverrides")
        self.labelSystemOverrideByText = QLabel(self.tabContentsSystemOverrides)
        self.labelSystemOverrideByText.setObjectName(u"labelSystemOverrideByText")
        sizePolicy3.setHeightForWidth(self.labelSystemOverrideByText.sizePolicy().hasHeightForWidth())
        self.labelSystemOverrideByText.setSizePolicy(sizePolicy3)
        self.labelSystemOverrideByText.setMinimumSize(QSize(0, 0))
        self.labelSystemOverrideByText.setFont(font2)

        self.horizontalLayoutHeaderSystemOverrides.addWidget(self.labelSystemOverrideByText)

        self.frameOverrideSystemOverrides = QFrame(self.tabContentsSystemOverrides)
        self.frameOverrideSystemOverrides.setObjectName(u"frameOverrideSystemOverrides")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemOverrides.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemOverrides.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemOverrides.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_118 = QVBoxLayout(self.frameOverrideSystemOverrides)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutHeaderSystemOverrides.addWidget(self.frameOverrideSystemOverrides)

        self.horizontalLayoutHeaderSystemOverrides.setStretch(0, 1)

        self.verticalLayout_113.addLayout(self.horizontalLayoutHeaderSystemOverrides)

        self.lineSystemOverrides = QFrame(self.tabContentsSystemOverrides)
        self.lineSystemOverrides.setObjectName(u"lineSystemOverrides")
        palette23 = QPalette()
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemOverrides.setPalette(palette23)
        self.lineSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemOverrides.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_113.addWidget(self.lineSystemOverrides)

        self.labelSystemOverride = QLabel(self.tabContentsSystemOverrides)
        self.labelSystemOverride.setObjectName(u"labelSystemOverride")
        self.labelSystemOverride.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemOverride.setWordWrap(True)
        self.labelSystemOverride.setOpenExternalLinks(True)
        self.labelSystemOverride.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_113.addWidget(self.labelSystemOverride)

        self.verticalSpacerSystemOverrides = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_113.addItem(self.verticalSpacerSystemOverrides)

        self.frameSystemOverrides = QFrame(self.tabContentsSystemOverrides)
        self.frameSystemOverrides.setObjectName(u"frameSystemOverrides")
        self.frameSystemOverrides.setMinimumSize(QSize(0, 64))
        self.frameSystemOverrides.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemOverrides.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frameSystemOverrides)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frameSystemOverridesInclude = QFrame(self.frameSystemOverrides)
        self.frameSystemOverridesInclude.setObjectName(u"frameSystemOverridesInclude")
        sizePolicy7.setHeightForWidth(self.frameSystemOverridesInclude.sizePolicy().hasHeightForWidth())
        self.frameSystemOverridesInclude.setSizePolicy(sizePolicy7)
        self.frameSystemOverridesInclude.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemOverridesInclude.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemOverridesInclude.setLineWidth(0)
        self.verticalLayout_116 = QVBoxLayout(self.frameSystemOverridesInclude)
        self.verticalLayout_116.setSpacing(10)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.labelSystemOverrideInclude = QLabel(self.frameSystemOverridesInclude)
        self.labelSystemOverrideInclude.setObjectName(u"labelSystemOverrideInclude")
        sizePolicy8.setHeightForWidth(self.labelSystemOverrideInclude.sizePolicy().hasHeightForWidth())
        self.labelSystemOverrideInclude.setSizePolicy(sizePolicy8)
        self.labelSystemOverrideInclude.setFont(font)
        self.labelSystemOverrideInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_116.addWidget(self.labelSystemOverrideInclude)

        self.textEditSystemInclude = CustomTextEdit(self.frameSystemOverridesInclude)
        self.textEditSystemInclude.setObjectName(u"textEditSystemInclude")
        sizePolicy10.setHeightForWidth(self.textEditSystemInclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemInclude.setSizePolicy(sizePolicy10)
        self.textEditSystemInclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemInclude.setTabChangesFocus(True)
        self.textEditSystemInclude.setAcceptRichText(False)

        self.verticalLayout_116.addWidget(self.textEditSystemInclude)


        self.horizontalLayout_20.addWidget(self.frameSystemOverridesInclude)

        self.horizontalSpacerSystemOverrides = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacerSystemOverrides)

        self.frameSystemOverridesExclude = QFrame(self.frameSystemOverrides)
        self.frameSystemOverridesExclude.setObjectName(u"frameSystemOverridesExclude")
        sizePolicy7.setHeightForWidth(self.frameSystemOverridesExclude.sizePolicy().hasHeightForWidth())
        self.frameSystemOverridesExclude.setSizePolicy(sizePolicy7)
        self.frameSystemOverridesExclude.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemOverridesExclude.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemOverridesExclude.setLineWidth(0)
        self.verticalLayout_117 = QVBoxLayout(self.frameSystemOverridesExclude)
        self.verticalLayout_117.setSpacing(10)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.labelSystemOverrideExclude = QLabel(self.frameSystemOverridesExclude)
        self.labelSystemOverrideExclude.setObjectName(u"labelSystemOverrideExclude")
        sizePolicy8.setHeightForWidth(self.labelSystemOverrideExclude.sizePolicy().hasHeightForWidth())
        self.labelSystemOverrideExclude.setSizePolicy(sizePolicy8)
        self.labelSystemOverrideExclude.setFont(font)
        self.labelSystemOverrideExclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_117.addWidget(self.labelSystemOverrideExclude)

        self.textEditSystemExclude = CustomTextEdit(self.frameSystemOverridesExclude)
        self.textEditSystemExclude.setObjectName(u"textEditSystemExclude")
        sizePolicy10.setHeightForWidth(self.textEditSystemExclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemExclude.setSizePolicy(sizePolicy10)
        self.textEditSystemExclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemExclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemExclude.setTabChangesFocus(True)
        self.textEditSystemExclude.setAcceptRichText(False)

        self.verticalLayout_117.addWidget(self.textEditSystemExclude)


        self.horizontalLayout_20.addWidget(self.frameSystemOverridesExclude)

        self.horizontalSpacerSystemOverrides1pxSoExcludeBorderShows = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacerSystemOverrides1pxSoExcludeBorderShows)


        self.verticalLayout_113.addWidget(self.frameSystemOverrides)


        self.verticalLayout_108.addWidget(self.tabContentsSystemOverrides)

        self.scrollAreaSystemOverrides.setWidget(self.scrollAreaWidgetContentsSystemOverrides)

        self.gridLayout_6.addWidget(self.scrollAreaSystemOverrides, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemOverrides, "")
        self.tabSystemPostFilter = QWidget()
        self.tabSystemPostFilter.setObjectName(u"tabSystemPostFilter")
        self.gridLayout_21 = QGridLayout(self.tabSystemPostFilter)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.scrollAreaSystemPostFilter = QScrollArea(self.tabSystemPostFilter)
        self.scrollAreaSystemPostFilter.setObjectName(u"scrollAreaSystemPostFilter")
        self.scrollAreaSystemPostFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemPostFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemPostFilter.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemPostFilter.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemFilter = QWidget()
        self.scrollAreaWidgetContentsSystemFilter.setObjectName(u"scrollAreaWidgetContentsSystemFilter")
        self.scrollAreaWidgetContentsSystemFilter.setGeometry(QRect(0, 0, 478, 413))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemFilter.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemFilter.setSizePolicy(sizePolicy)
        self.verticalLayout_115 = QVBoxLayout(self.scrollAreaWidgetContentsSystemFilter)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemFilter = QFrame(self.scrollAreaWidgetContentsSystemFilter)
        self.tabContentsSystemFilter.setObjectName(u"tabContentsSystemFilter")
        self.tabContentsSystemFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemFilter.setLineWidth(0)
        self.verticalLayout_119 = QVBoxLayout(self.tabContentsSystemFilter)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeaderSystemFilter = QHBoxLayout()
        self.horizontalLayoutHeaderSystemFilter.setObjectName(u"horizontalLayoutHeaderSystemFilter")
        self.labelSystemFilterByText = QLabel(self.tabContentsSystemFilter)
        self.labelSystemFilterByText.setObjectName(u"labelSystemFilterByText")
        sizePolicy3.setHeightForWidth(self.labelSystemFilterByText.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByText.setSizePolicy(sizePolicy3)
        self.labelSystemFilterByText.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByText.setFont(font2)

        self.horizontalLayoutHeaderSystemFilter.addWidget(self.labelSystemFilterByText)

        self.frameOverrideSystemFilter = QFrame(self.tabContentsSystemFilter)
        self.frameOverrideSystemFilter.setObjectName(u"frameOverrideSystemFilter")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemFilter.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemFilter.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemFilter.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_123 = QVBoxLayout(self.frameOverrideSystemFilter)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverridePostFilter = QCheckBox(self.frameOverrideSystemFilter)
        self.checkBoxSystemOverridePostFilter.setObjectName(u"checkBoxSystemOverridePostFilter")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverridePostFilter.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverridePostFilter.setSizePolicy(sizePolicy3)

        self.verticalLayout_123.addWidget(self.checkBoxSystemOverridePostFilter, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemFilter.addWidget(self.frameOverrideSystemFilter)

        self.horizontalLayoutHeaderSystemFilter.setStretch(0, 1)

        self.verticalLayout_119.addLayout(self.horizontalLayoutHeaderSystemFilter)

        self.lineSystemFilterByText = QFrame(self.tabContentsSystemFilter)
        self.lineSystemFilterByText.setObjectName(u"lineSystemFilterByText")
        palette24 = QPalette()
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemFilterByText.setPalette(palette24)
        self.lineSystemFilterByText.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemFilterByText.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_119.addWidget(self.lineSystemFilterByText)

        self.labelSystemFilters = QLabel(self.tabContentsSystemFilter)
        self.labelSystemFilters.setObjectName(u"labelSystemFilters")
        self.labelSystemFilters.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelSystemFilters.setWordWrap(True)
        self.labelSystemFilters.setOpenExternalLinks(True)
        self.labelSystemFilters.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_119.addWidget(self.labelSystemFilters)

        self.verticalSpacerSystemFilters = QSpacerItem(10, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_119.addItem(self.verticalSpacerSystemFilters)

        self.frameSystemFilter = QFrame(self.tabContentsSystemFilter)
        self.frameSystemFilter.setObjectName(u"frameSystemFilter")
        self.frameSystemFilter.setMinimumSize(QSize(0, 64))
        self.frameSystemFilter.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemFilter.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frameSystemFilter)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frameSystemFilterContents = QFrame(self.frameSystemFilter)
        self.frameSystemFilterContents.setObjectName(u"frameSystemFilterContents")
        sizePolicy7.setHeightForWidth(self.frameSystemFilterContents.sizePolicy().hasHeightForWidth())
        self.frameSystemFilterContents.setSizePolicy(sizePolicy7)
        self.frameSystemFilterContents.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSystemFilterContents.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSystemFilterContents.setLineWidth(0)
        self.verticalLayout_121 = QVBoxLayout(self.frameSystemFilterContents)
        self.verticalLayout_121.setSpacing(10)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterInclude = QLabel(self.frameSystemFilterContents)
        self.labelSystemFilterInclude.setObjectName(u"labelSystemFilterInclude")
        sizePolicy8.setHeightForWidth(self.labelSystemFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterInclude.setSizePolicy(sizePolicy8)
        self.labelSystemFilterInclude.setFont(font)
        self.labelSystemFilterInclude.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_121.addWidget(self.labelSystemFilterInclude)

        self.textEditSystemFilterInclude = CustomTextEdit(self.frameSystemFilterContents)
        self.textEditSystemFilterInclude.setObjectName(u"textEditSystemFilterInclude")
        self.textEditSystemFilterInclude.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.textEditSystemFilterInclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemFilterInclude.setSizePolicy(sizePolicy10)
        self.textEditSystemFilterInclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemFilterInclude.setMaximumSize(QSize(16777211, 16777215))
        self.textEditSystemFilterInclude.setFrameShape(QFrame.Shape.Box)
        self.textEditSystemFilterInclude.setTabChangesFocus(True)
        self.textEditSystemFilterInclude.setAcceptRichText(False)

        self.verticalLayout_121.addWidget(self.textEditSystemFilterInclude)


        self.horizontalLayout_21.addWidget(self.frameSystemFilterContents)

        self.horizontalSpacerSystemFilter1pxSoExcludeBorderShows = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacerSystemFilter1pxSoExcludeBorderShows)


        self.verticalLayout_119.addWidget(self.frameSystemFilter)


        self.verticalLayout_115.addWidget(self.tabContentsSystemFilter)

        self.scrollAreaSystemPostFilter.setWidget(self.scrollAreaWidgetContentsSystemFilter)

        self.gridLayout_21.addWidget(self.scrollAreaSystemPostFilter, 0, 0, 1, 1)

        self.tabWidgetSystemSettings.addTab(self.tabSystemPostFilter, "")
        self.tabSystemOptions = QWidget()
        self.tabSystemOptions.setObjectName(u"tabSystemOptions")
        self.gridLayout_22 = QGridLayout(self.tabSystemOptions)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayoutHeaderSystemOptions = QHBoxLayout()
        self.horizontalLayoutHeaderSystemOptions.setObjectName(u"horizontalLayoutHeaderSystemOptions")
        self.labelSystemOptions = QLabel(self.tabSystemOptions)
        self.labelSystemOptions.setObjectName(u"labelSystemOptions")
        sizePolicy3.setHeightForWidth(self.labelSystemOptions.sizePolicy().hasHeightForWidth())
        self.labelSystemOptions.setSizePolicy(sizePolicy3)
        self.labelSystemOptions.setMinimumSize(QSize(0, 0))
        self.labelSystemOptions.setFont(font2)

        self.horizontalLayoutHeaderSystemOptions.addWidget(self.labelSystemOptions)

        self.frameOverrideSystemOptions = QFrame(self.tabSystemOptions)
        self.frameOverrideSystemOptions.setObjectName(u"frameOverrideSystemOptions")
        sizePolicy5.setHeightForWidth(self.frameOverrideSystemOptions.sizePolicy().hasHeightForWidth())
        self.frameOverrideSystemOptions.setSizePolicy(sizePolicy5)
        self.frameOverrideSystemOptions.setMinimumSize(QSize(200, 24))
        self.frameOverrideSystemOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOverrideSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_126 = QVBoxLayout(self.frameOverrideSystemOptions)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemOverrideOptions = QCheckBox(self.frameOverrideSystemOptions)
        self.checkBoxSystemOverrideOptions.setObjectName(u"checkBoxSystemOverrideOptions")
        sizePolicy3.setHeightForWidth(self.checkBoxSystemOverrideOptions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideOptions.setSizePolicy(sizePolicy3)

        self.verticalLayout_126.addWidget(self.checkBoxSystemOverrideOptions, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayoutHeaderSystemOptions.addWidget(self.frameOverrideSystemOptions)

        self.horizontalLayoutHeaderSystemOptions.setStretch(0, 1)

        self.gridLayout_22.addLayout(self.horizontalLayoutHeaderSystemOptions, 1, 0, 1, 1)

        self.scrollAreaSystemOptions = QScrollArea(self.tabSystemOptions)
        self.scrollAreaSystemOptions.setObjectName(u"scrollAreaSystemOptions")
        self.scrollAreaSystemOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollAreaSystemOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollAreaSystemOptions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSystemOptions = QWidget()
        self.scrollAreaWidgetContentsSystemOptions.setObjectName(u"scrollAreaWidgetContentsSystemOptions")
        self.scrollAreaWidgetContentsSystemOptions.setGeometry(QRect(0, 0, 573, 1075))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContentsSystemOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsSystemOptions.setSizePolicy(sizePolicy)
        self.verticalLayout_120 = QVBoxLayout(self.scrollAreaWidgetContentsSystemOptions)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.tabContentsSystemOptions = QFrame(self.scrollAreaWidgetContentsSystemOptions)
        self.tabContentsSystemOptions.setObjectName(u"tabContentsSystemOptions")
        self.tabContentsSystemOptions.setFrameShape(QFrame.Shape.NoFrame)
        self.tabContentsSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.tabContentsSystemOptions.setLineWidth(0)
        self.verticalLayout_124 = QVBoxLayout(self.tabContentsSystemOptions)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.labelSystemOptionsTitle = QLabel(self.tabContentsSystemOptions)
        self.labelSystemOptionsTitle.setObjectName(u"labelSystemOptionsTitle")
        self.labelSystemOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsTitle.setFont(font2)
        self.labelSystemOptionsTitle.setScaledContents(False)
        self.labelSystemOptionsTitle.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_124.addWidget(self.labelSystemOptionsTitle)

        self.checkBoxSystemOptionsDisable1G1R = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsDisable1G1R.setObjectName(u"checkBoxSystemOptionsDisable1G1R")
        self.checkBoxSystemOptionsDisable1G1R.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDisable1G1R.setFont(font6)
        self.checkBoxSystemOptionsDisable1G1R.setStyleSheet(u"")
        self.checkBoxSystemOptionsDisable1G1R.setTristate(False)

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsDisable1G1R)

        self.checkBoxSystemOptionsPreferRegions = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsPreferRegions.setObjectName(u"checkBoxSystemOptionsPreferRegions")
        self.checkBoxSystemOptionsPreferRegions.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferRegions.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsPreferRegions)

        self.checkBoxSystemOptionsModernPlatforms = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsModernPlatforms.setObjectName(u"checkBoxSystemOptionsModernPlatforms")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsModernPlatforms.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsModernPlatforms.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsModernPlatforms.setFont(font)
        self.checkBoxSystemOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsModernPlatforms)

        self.checkBoxSystemOptionsPreferOldest = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsPreferOldest.setObjectName(u"checkBoxSystemOptionsPreferOldest")
        self.checkBoxSystemOptionsPreferOldest.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferOldest.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsPreferOldest)

        self.checkBoxSystemOptionsDemoteUnlicensed = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsDemoteUnlicensed.setObjectName(u"checkBoxSystemOptionsDemoteUnlicensed")
        self.checkBoxSystemOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxSystemOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsDemoteUnlicensed)

        self.checkBoxSystemOptionsDisableOverrides = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsDisableOverrides.setObjectName(u"checkBoxSystemOptionsDisableOverrides")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsDisableOverrides.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsDisableOverrides.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsDisableOverrides.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsDisableOverrides.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsDisableOverrides.setFont(font)
        self.checkBoxSystemOptionsDisableOverrides.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsDisableOverrides)

        self.verticalSpacerSystemOptions_1 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_1)

        self.labelSystemChooseCompilationsMode = QLabel(self.tabContentsSystemOptions)
        self.labelSystemChooseCompilationsMode.setObjectName(u"labelSystemChooseCompilationsMode")
        self.labelSystemChooseCompilationsMode.setFont(font2)

        self.verticalLayout_124.addWidget(self.labelSystemChooseCompilationsMode)

        self.comboBoxSystemChooseCompilationsMode = CustomComboBox(self.tabContentsSystemOptions)
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

        self.verticalLayout_124.addWidget(self.comboBoxSystemChooseCompilationsMode)

        self.verticalSpacerSystemOptions_2 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_2)

        self.labelSystemCompilationsExplanation = QLabel(self.tabContentsSystemOptions)
        self.labelSystemCompilationsExplanation.setObjectName(u"labelSystemCompilationsExplanation")
        self.labelSystemCompilationsExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelSystemCompilationsExplanation.setWordWrap(True)

        self.verticalLayout_124.addWidget(self.labelSystemCompilationsExplanation)

        self.verticalSpacerSystemOptions_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_3)

        self.labelSystemOptionsOutput = QLabel(self.tabContentsSystemOptions)
        self.labelSystemOptionsOutput.setObjectName(u"labelSystemOptionsOutput")
        self.labelSystemOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsOutput.setFont(font2)
        self.labelSystemOptionsOutput.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_124.addWidget(self.labelSystemOptionsOutput)

        self.checkBoxSystemOptionsAlreadyProcessed = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsAlreadyProcessed.setObjectName(u"checkBoxSystemOptionsAlreadyProcessed")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsAlreadyProcessed)

        self.checkBoxSystemOptionsOriginalHeader = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsOriginalHeader.setObjectName(u"checkBoxSystemOptionsOriginalHeader")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsOriginalHeader)

        self.checkBoxSystemOptionsUseMachine = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsUseMachine.setObjectName(u"checkBoxSystemOptionsUseMachine")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsUseMachine)

        self.checkBoxSystemOptionsSplitRegions = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsSplitRegions.setObjectName(u"checkBoxSystemOptionsSplitRegions")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsSplitRegions)

        self.checkBoxSystemOptionsRemovesDat = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsRemovesDat.setObjectName(u"checkBoxSystemOptionsRemovesDat")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsRemovesDat)

        self.checkBoxSystemOptionsKeepRemove = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsKeepRemove.setObjectName(u"checkBoxSystemOptionsKeepRemove")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsKeepRemove)

        self.checkBoxSystemOptions1G1RNames = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptions1G1RNames.setObjectName(u"checkBoxSystemOptions1G1RNames")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptions1G1RNames)

        self.frameSystemOptions1G1RPrefix = QFrame(self.tabContentsSystemOptions)
        self.frameSystemOptions1G1RPrefix.setObjectName(u"frameSystemOptions1G1RPrefix")
        self.frameSystemOptions1G1RPrefix.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameSystemOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameSystemOptions1G1RPrefix.setSizePolicy(sizePolicy8)
        self.frameSystemOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette25 = QPalette()
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush5)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush6)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush6)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush3)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush3)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush9)
        palette25.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush5)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush6)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush6)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush3)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush3)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush9)
        palette25.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush6)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush5)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush6)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush6)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush6)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush6)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush9)
        palette25.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        self.frameSystemOptions1G1RPrefix.setPalette(palette25)
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

        self.verticalLayout_124.addWidget(self.frameSystemOptions1G1RPrefix)

        self.verticalSpacerSystemOptions_4 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_4)

        self.labelSystemOptionsOnline = QLabel(self.tabContentsSystemOptions)
        self.labelSystemOptionsOnline.setObjectName(u"labelSystemOptionsOnline")
        self.labelSystemOptionsOnline.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsOnline.setFont(font2)
        self.labelSystemOptionsOnline.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_124.addWidget(self.labelSystemOptionsOnline)

        self.labelSystemOnlineExplanation = QLabel(self.tabContentsSystemOptions)
        self.labelSystemOnlineExplanation.setObjectName(u"labelSystemOnlineExplanation")
        self.labelSystemOnlineExplanation.setTextFormat(Qt.TextFormat.PlainText)
        self.labelSystemOnlineExplanation.setWordWrap(True)

        self.verticalLayout_124.addWidget(self.labelSystemOnlineExplanation)

        self.verticalSpacerSystemOptions_5 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_5)

        self.checkBoxSystemOptionsMIA = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsMIA.setObjectName(u"checkBoxSystemOptionsMIA")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsMIA.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsMIA.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsMIA.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsMIA.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsMIA.setFont(font)
        self.checkBoxSystemOptionsMIA.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsMIA)

        self.checkBoxSystemOptionsRetroAchievements = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsRetroAchievements.setObjectName(u"checkBoxSystemOptionsRetroAchievements")
        sizePolicy11.setHeightForWidth(self.checkBoxSystemOptionsRetroAchievements.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsRetroAchievements.setSizePolicy(sizePolicy11)
        self.checkBoxSystemOptionsRetroAchievements.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsRetroAchievements.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxSystemOptionsRetroAchievements.setFont(font)
        self.checkBoxSystemOptionsRetroAchievements.setStyleSheet(u"")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsRetroAchievements)

        self.checkBoxSystemOptionsPreferRetro = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsPreferRetro.setObjectName(u"checkBoxSystemOptionsPreferRetro")
        self.checkBoxSystemOptionsPreferRetro.setMinimumSize(QSize(0, 0))
        self.checkBoxSystemOptionsPreferRetro.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsPreferRetro)

        self.verticalSpacerSystemOptions_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_6)

        self.labelSystemOptionsDebug = QLabel(self.tabContentsSystemOptions)
        self.labelSystemOptionsDebug.setObjectName(u"labelSystemOptionsDebug")
        self.labelSystemOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsDebug.setFont(font2)
        self.labelSystemOptionsDebug.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_124.addWidget(self.labelSystemOptionsDebug)

        self.checkBoxSystemOptionsReportWarnings = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsReportWarnings.setObjectName(u"checkBoxSystemOptionsReportWarnings")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsReportWarnings)

        self.checkBoxSystemOptionsPauseWarnings = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsPauseWarnings.setObjectName(u"checkBoxSystemOptionsPauseWarnings")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsPauseWarnings)

        self.checkBoxSystemOptionsLegacy = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsLegacy.setObjectName(u"checkBoxSystemOptionsLegacy")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsLegacy)

        self.checkBoxSystemOptionsDisableMultiCPU = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsDisableMultiCPU.setObjectName(u"checkBoxSystemOptionsDisableMultiCPU")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsDisableMultiCPU)

        self.checkBoxSystemOptionsTrace = QCheckBox(self.tabContentsSystemOptions)
        self.checkBoxSystemOptionsTrace.setObjectName(u"checkBoxSystemOptionsTrace")

        self.verticalLayout_124.addWidget(self.checkBoxSystemOptionsTrace)

        self.frameSystemOptionsTrace = QFrame(self.tabContentsSystemOptions)
        self.frameSystemOptionsTrace.setObjectName(u"frameSystemOptionsTrace")
        self.frameSystemOptionsTrace.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.frameSystemOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameSystemOptionsTrace.setSizePolicy(sizePolicy8)
        self.frameSystemOptionsTrace.setMinimumSize(QSize(0, 55))
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
        self.frameSystemOptionsTrace.setPalette(palette26)
        self.labelSystemOptionsTrace = QLabel(self.frameSystemOptionsTrace)
        self.labelSystemOptionsTrace.setObjectName(u"labelSystemOptionsTrace")
        self.labelSystemOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditSystemOptionsTrace = CustomLineEdit(self.frameSystemOptionsTrace)
        self.lineEditSystemOptionsTrace.setObjectName(u"lineEditSystemOptionsTrace")
        self.lineEditSystemOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditSystemOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_124.addWidget(self.frameSystemOptionsTrace)

        self.verticalSpacerSystemOptions_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_124.addItem(self.verticalSpacerSystemOptions_7)


        self.verticalLayout_120.addWidget(self.tabContentsSystemOptions)

        self.scrollAreaSystemOptions.setWidget(self.scrollAreaWidgetContentsSystemOptions)

        self.gridLayout_22.addWidget(self.scrollAreaSystemOptions, 3, 0, 1, 1)

        self.lineSystemOptions = QFrame(self.tabSystemOptions)
        self.lineSystemOptions.setObjectName(u"lineSystemOptions")
        palette27 = QPalette()
        palette27.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette27.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette27.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self.lineSystemOptions.setPalette(palette27)
        self.lineSystemOptions.setFrameShadow(QFrame.Shadow.Plain)
        self.lineSystemOptions.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_22.addWidget(self.lineSystemOptions, 2, 0, 1, 1)

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
        font7 = QFont()
        font7.setPointSize(9)
        self.labelSettingsSaved.setFont(font7)
        self.labelSettingsSaved.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayoutRight.addWidget(self.labelSettingsSaved, 1, 1, 1, 1)

        self.labelChooseYourSettings = QLabel(self.gridLayoutRightSettings)
        self.labelChooseYourSettings.setObjectName(u"labelChooseYourSettings")
        self.labelChooseYourSettings.setFont(font2)

        self.gridLayoutRight.addWidget(self.labelChooseYourSettings, 1, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutRightSettings)

        self.gridLayout.addWidget(self.splitter, 2, 1, 1, 1)

        self.frameAddFiles = QFrame(self.frame)
        self.frameAddFiles.setObjectName(u"frameAddFiles")
        self.frameAddFiles.setMinimumSize(QSize(54, 0))
        self.frameAddFiles.setFrameShape(QFrame.Shape.NoFrame)
        self.frameAddFiles.setFrameShadow(QFrame.Shadow.Plain)
        self.buttonAddDats = QPushButton(self.frameAddFiles)
        self.buttonAddDats.setObjectName(u"buttonAddDats")
        self.buttonAddDats.setGeometry(QRect(2, 0, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonAddDats.sizePolicy().hasHeightForWidth())
        self.buttonAddDats.setSizePolicy(sizePolicy6)
        self.buttonAddDats.setMinimumSize(QSize(44, 48))
        self.buttonAddDats.setMaximumSize(QSize(44, 48))
        self.buttonAddDats.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u":/retoolFiles/images/icons8-add-list-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddDats.setIcon(icon10)
        self.buttonAddDats.setIconSize(QSize(32, 32))
        self.buttonAddFolder = QPushButton(self.frameAddFiles)
        self.buttonAddFolder.setObjectName(u"buttonAddFolder")
        self.buttonAddFolder.setGeometry(QRect(2, 50, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonAddFolder.sizePolicy().hasHeightForWidth())
        self.buttonAddFolder.setSizePolicy(sizePolicy6)
        self.buttonAddFolder.setMinimumSize(QSize(44, 48))
        self.buttonAddFolder.setMaximumSize(QSize(44, 48))
        self.buttonAddFolder.setFont(font3)
        icon11 = QIcon()
        icon11.addFile(u":/retoolFiles/images/icons8-add-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddFolder.setIcon(icon11)
        self.buttonAddFolder.setIconSize(QSize(32, 32))
        self.buttonAddFolderRecursive = QPushButton(self.frameAddFiles)
        self.buttonAddFolderRecursive.setObjectName(u"buttonAddFolderRecursive")
        self.buttonAddFolderRecursive.setGeometry(QRect(2, 100, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonAddFolderRecursive.sizePolicy().hasHeightForWidth())
        self.buttonAddFolderRecursive.setSizePolicy(sizePolicy6)
        self.buttonAddFolderRecursive.setMinimumSize(QSize(44, 48))
        self.buttonAddFolderRecursive.setMaximumSize(QSize(44, 48))
        self.buttonAddFolderRecursive.setFont(font3)
        icon12 = QIcon()
        icon12.addFile(u":/retoolFiles/images/icons8-recursive-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonAddFolderRecursive.setIcon(icon12)
        self.buttonAddFolderRecursive.setIconSize(QSize(32, 32))
        self.buttonDeleteDats = QPushButton(self.frameAddFiles)
        self.buttonDeleteDats.setObjectName(u"buttonDeleteDats")
        self.buttonDeleteDats.setGeometry(QRect(2, 220, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonDeleteDats.sizePolicy().hasHeightForWidth())
        self.buttonDeleteDats.setSizePolicy(sizePolicy6)
        self.buttonDeleteDats.setMinimumSize(QSize(44, 48))
        self.buttonDeleteDats.setMaximumSize(QSize(44, 48))
        self.buttonDeleteDats.setFont(font3)
        icon13 = QIcon()
        icon13.addFile(u":/retoolFiles/images/icons8-delete-file-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonDeleteDats.setIcon(icon13)
        self.buttonDeleteDats.setIconSize(QSize(32, 32))
        self.buttonClearDats = QPushButton(self.frameAddFiles)
        self.buttonClearDats.setObjectName(u"buttonClearDats")
        self.buttonClearDats.setGeometry(QRect(2, 270, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonClearDats.sizePolicy().hasHeightForWidth())
        self.buttonClearDats.setSizePolicy(sizePolicy6)
        self.buttonClearDats.setMinimumSize(QSize(44, 48))
        self.buttonClearDats.setMaximumSize(QSize(44, 48))
        self.buttonClearDats.setFont(font3)
        self.buttonClearDats.setIcon(icon8)
        self.buttonClearDats.setIconSize(QSize(32, 32))
        self.buttonQuickImport = QPushButton(self.frameAddFiles)
        self.buttonQuickImport.setObjectName(u"buttonQuickImport")
        self.buttonQuickImport.setGeometry(QRect(2, 150, 44, 48))
        sizePolicy6.setHeightForWidth(self.buttonQuickImport.sizePolicy().hasHeightForWidth())
        self.buttonQuickImport.setSizePolicy(sizePolicy6)
        self.buttonQuickImport.setMinimumSize(QSize(44, 48))
        self.buttonQuickImport.setMaximumSize(QSize(44, 48))
        self.buttonQuickImport.setFont(font3)
        icon14 = QIcon()
        icon14.addFile(u":/retoolFiles/images/icons8-add-quick-folder-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.buttonQuickImport.setIcon(icon14)
        self.buttonQuickImport.setIconSize(QSize(32, 32))
        self.lineAddRemoveSeparator = QFrame(self.frameAddFiles)
        self.lineAddRemoveSeparator.setObjectName(u"lineAddRemoveSeparator")
        self.lineAddRemoveSeparator.setGeometry(QRect(8, 200, 31, 20))
        self.lineAddRemoveSeparator.setFrameShape(QFrame.Shape.HLine)
        self.lineAddRemoveSeparator.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.frameAddFiles, 2, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frameProcessDatFile = QFrame(self.centralwidget)
        self.frameProcessDatFile.setObjectName(u"frameProcessDatFile")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frameProcessDatFile.sizePolicy().hasHeightForWidth())
        self.frameProcessDatFile.setSizePolicy(sizePolicy12)
        self.frameProcessDatFile.setMinimumSize(QSize(0, 0))
        self.frameProcessDatFile.setFrameShape(QFrame.Shape.NoFrame)
        self.frameProcessDatFile.setFrameShadow(QFrame.Shadow.Plain)
        self.frameProcessDatFile.setLineWidth(0)
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
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        self.buttonGo.setFont(font8)

        self.horizontalLayoutOutputGo.addWidget(self.buttonGo, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_5.addWidget(self.horizontalLayoutBottom)


        self.gridLayout_2.addWidget(self.frameProcessDatFile, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setEnabled(True)
        self.statusBar.setStyleSheet(u"border: None;")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.buttonAddDats, self.buttonAddFolder)
        QWidget.setTabOrder(self.buttonAddFolder, self.buttonAddFolderRecursive)
        QWidget.setTabOrder(self.buttonAddFolderRecursive, self.buttonDeleteDats)
        QWidget.setTabOrder(self.buttonDeleteDats, self.buttonClearDats)
        QWidget.setTabOrder(self.buttonClearDats, self.listWidgetOpenFiles)
        QWidget.setTabOrder(self.listWidgetOpenFiles, self.tabWidgetSettings)
        QWidget.setTabOrder(self.tabWidgetSettings, self.tabWidgetSystemSettings)

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
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About Retool", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionCloneListUpdates.setText(QCoreApplication.translate("MainWindow", u"Update clone lists", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCloneListNameTool.setText(QCoreApplication.translate("MainWindow", u"Title tool", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSettings.setIconText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)

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
        self.labelGlobalPaths.setText(QCoreApplication.translate("MainWindow", u"Set folders to use when processing DAT files", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalChooseOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalChooseOutput.setText("")
        self.labelGlobalSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder", None))
        self.labelGlobalOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalReplaceInputDats.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes input DAT files and replaces them with Retool versions in the same folder.\n"
"Only use this if you can recover the original DAT files from elsewhere. Useful\n"
"for RomVault or DatVault users operating directly on their DatRoot files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalReplaceInputDats.setText(QCoreApplication.translate("MainWindow", u"Replace input DAT files", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalPaths), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.labelGlobalRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.labelGlobalAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
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
        self.labelGlobalSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
        self.labelGlobalFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.labelGlobalAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setText("")
        self.labelGlobalSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setText("")
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
        self.labelGlobalFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.labelGlobalVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setText("")
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalVideo), QCoreApplication.translate("MainWindow", u"Video", None))
        self.labelGlobalExclusions.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
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
        self.checkBoxGlobalExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\". These might be used as\n"
"soundtracks by games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\". These could\n"
"be anything other than the main title content, like patches,\n"
"manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\". These were\n"
"discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
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
        self.checkBoxGlobalExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\".", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeGames.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Games\". Retool assumes\n"
"uncategorized titles are games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeGames.setText(QCoreApplication.translate("MainWindow", u"Games", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Manual)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setText(QCoreApplication.translate("MainWindow", u"Manuals", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setToolTip(QCoreApplication.translate("MainWindow", u"Titles with ROMs declared as missing in action in the DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setText(QCoreApplication.translate("MainWindow", u"MIA", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Multimedia\". These might include\n"
"games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setText(QCoreApplication.translate("MainWindow", u"Multimedia", None))
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
        self.checkBoxGlobalExcludePromotional.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Promotional\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Promo)\n"
"\u2022 EPK\n"
"\u2022 Press Kit", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePromotional.setText(QCoreApplication.translate("MainWindow", u"Promotional", None))
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
        self.checkBoxGlobalExcludeAftermarket.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Aftermarket)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAftermarket.setText(QCoreApplication.translate("MainWindow", u"Aftermarket", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Pirate)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setText(QCoreApplication.translate("MainWindow", u"Pirate", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Unl)\" in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Unlicensed", None))
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
        self.buttonGlobalSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
        self.labelGlobalUseLocalNames.setText(QCoreApplication.translate("MainWindow", u"Use local title names for these languages", None))
        self.labelGlobalLocalizeNames.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use local names if they are available in metadata files or clone lists. For example, <span style=\" font-style:italic;\">\u30b7\u30e3\u30a4\u30cb\u30f3\u30b0\u00b7\u30d5\u30a9\u30fc\u30b9</span><a name=\"char-node\"/><span style=\" font-style:italic;\">\u2161</span><span style=\" font-style:italic;\"> \u300e\u53e4\u306e\u5c01\u5370\u300f </span>instead of <span style=\" font-style:italic;\">Shining Force II - Inishie no Fuuin</span>. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-local-names\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.</p><p>Add the languages you want local names for to the following list. Some titles are multi-region, and have multiple local names \u2014 if English is your preferred language, make sure to put it at the top of the order.</p></body></html>", None))
        self.labelGlobalLocalizationAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationAllLeft.setText("")
        self.labelGlobalLocalizationSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Localize in this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLocalizationDown.setText("")
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalLocalization), QCoreApplication.translate("MainWindow", u"Local names", None))
        self.labelGlobalOverrideByText.setText(QCoreApplication.translate("MainWindow", u"Override by text", None))
        self.labelGlobalOverride.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Override Retool and force exclude or include specific titles by adding your own text to match against. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also exclude/include any match's related clones.</p></body></html>", None))
        self.labelGlobalOverrideInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.labelGlobalOverrideExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalOverrides), QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.labelGlobalFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter after Retool has finished processing", None))
        self.labelGlobalFilters.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>After Retool has finished processing, only include titles that match the text listed here. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.</p></body></html>", None))
        self.labelGlobalFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalPostFilter), QCoreApplication.translate("MainWindow", u"Post filters", None))
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
        self.labelGlobalOptions.setText(QCoreApplication.translate("MainWindow", u"Global options", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabGlobalSettings), QCoreApplication.translate("MainWindow", u"Global settings", None))
        self.labelSystemSettings.setText(QCoreApplication.translate("MainWindow", u"Add a DAT file, and then select it in the list to access its system-specific settings.", None))
        self.labelSystemCustomFilesAndFolders.setText(QCoreApplication.translate("MainWindow", u"Set files and folders to use when processing this DAT file", None))
        self.checkBoxSystemOverridePaths.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemPathsOutput.setText(QCoreApplication.translate("MainWindow", u"Output", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Use global output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearOutput.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseOutput.setText("")
        self.labelSystemSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder", None))
        self.labelSystemOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected, using global settings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemReplaceInputDats.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes input DAT files and replaces them with Retool versions in the same folder.\n"
"Only use this if you can recover the original DAT files from elsewhere. Useful\n"
"for RomVault or DatVault users operating directly on their DatRoot files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemReplaceInputDats.setText(QCoreApplication.translate("MainWindow", u"Replace input DAT files", None))
        self.labelSystemPathsSupportFiles.setText(QCoreApplication.translate("MainWindow", u"Support files", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Use default clone list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearCloneList.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom clone list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseCloneList.setText("")
        self.labelSystemSelectCloneList.setText(QCoreApplication.translate("MainWindow", u"Select a custom clone list", None))
        self.labelSystemCloneList.setText(QCoreApplication.translate("MainWindow", u"No custom clone list selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default metadata file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearMetadataFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom metadata file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseMetadataFile.setText("")
        self.labelSystemSelectMetadataFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom metadata file", None))
        self.labelSystemMetadataFile.setText(QCoreApplication.translate("MainWindow", u"No custom metadata file selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearMIAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default MIA file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearMIAFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseMIAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom MIA file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseMIAFile.setText("")
        self.labelSystemSelectMIAFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom MIA file", None))
        self.labelSystemMIAFile.setText(QCoreApplication.translate("MainWindow", u"No custom MIA file selected, using default location", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemClearRAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default RetroAchievements file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemClearRAFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemChooseRAFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom RetroAchievements file.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemChooseRAFile.setText("")
        self.labelSystemSelectRAFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom RetroAchievements file", None))
        self.labelSystemRAFile.setText(QCoreApplication.translate("MainWindow", u"No custom RetroAchievements file selected, using default location", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemPaths), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.labelSystemFilterByRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.checkBoxSystemOverrideRegions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
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
        self.labelSystemSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
        self.labelSystemFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.checkBoxSystemOverrideLanguages.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setText("")
        self.labelSystemSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setText("")
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
        self.labelSystemFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.checkBoxSystemOverrideVideo.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setText("")
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemVideo), QCoreApplication.translate("MainWindow", u"Video", None))
        self.labelSystemExclusions.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles", None))
        self.checkBoxSystemOverrideExclusions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
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
        self.checkBoxSystemExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\". These might be used as\n"
"soundtracks by games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\". These could\n"
"be anything other than the main title content, like patches,\n"
"manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\". These were\n"
"discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
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
        self.checkBoxSystemExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\".", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
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
        self.buttonSystemSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
        self.labelSystemUseLocalNames.setText(QCoreApplication.translate("MainWindow", u"Use local title names for these languages", None))
        self.checkBoxSystemOverrideLocalization.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemLocalizeNames.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use local names if they are available in metadata files or clone lists. For example, <span style=\" font-style:italic;\">\u30b7\u30e3\u30a4\u30cb\u30f3\u30b0\u00b7\u30d5\u30a9\u30fc\u30b9</span><a name=\"char-node\"/><span style=\" font-style:italic;\">\u2161</span><span style=\" font-style:italic;\"> \u300e\u53e4\u306e\u5c01\u5370\u300f </span>instead of <span style=\" font-style:italic;\">Shining Force II - Inishie no Fuuin</span>. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-local-names\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.</p><p>Add the languages you want local names for to the following list. Some titles are multi-region, and have multiple local names \u2014 if English is your preferred language, make sure to put it at the top of the order.</p></body></html>", None))
        self.labelSystemLocalizationAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationAllLeft.setText("")
        self.labelSystemLocalizationSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Localize in this language order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLocalizationDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLocalizationDown.setText("")
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemLocalization), QCoreApplication.translate("MainWindow", u"Local names", None))
        self.labelSystemOverrideByText.setText(QCoreApplication.translate("MainWindow", u"Override by text", None))
        self.labelSystemOverride.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Override Retool and force exclude or include specific titles by adding your own text to match against. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also exclude/include any match's related clones.</p></body></html>", None))
        self.labelSystemOverrideInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.labelSystemOverrideExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemOverrides), QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.labelSystemFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter after Retool has finished processing", None))
        self.checkBoxSystemOverridePostFilter.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemFilters.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>After Retool has finished processing, only include titles that match the text listed here. Each match must be on its own line, and is case insensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui-overrides-post-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.</p></body></html>", None))
        self.labelSystemFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemPostFilter), QCoreApplication.translate("MainWindow", u"Post filters", None))
        self.labelSystemOptions.setText(QCoreApplication.translate("MainWindow", u"System options", None))
        self.checkBoxSystemOverrideOptions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
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
        self.checkBoxSystemOptionsMIA.setText(QCoreApplication.translate("MainWindow", u"Add MIA attributes to DAT files (DatVault users should leave this disabled)", None))
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
        self.buttonGo.setText(QCoreApplication.translate("MainWindow", u"Process DAT files", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

