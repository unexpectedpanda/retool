# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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

from modules.gui.custom_widgets import (CustomLineEdit, CustomList, CustomListSelfDrag, CustomPushButton,
    CustomTextEdit, ElisionLabel)
from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        icon.addFile(u":/retoolIcon/images/retool.ico", QSize(), QIcon.Normal, QIcon.Off)
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
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(9)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(54, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.buttonAddDats = QPushButton(self.frame_2)
        self.buttonAddDats.setObjectName(u"buttonAddDats")
        self.buttonAddDats.setGeometry(QRect(2, 0, 44, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.buttonAddDats.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/retoolFiles/images/icons8-add-list-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonAddDats.setIcon(icon1)
        self.buttonAddDats.setIconSize(QSize(32, 32))
        self.buttonAddFolder = QPushButton(self.frame_2)
        self.buttonAddFolder.setObjectName(u"buttonAddFolder")
        self.buttonAddFolder.setGeometry(QRect(3, 50, 44, 40))
        self.buttonAddFolder.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/retoolFiles/images/icons8-add-folder-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonAddFolder.setIcon(icon2)
        self.buttonAddFolder.setIconSize(QSize(32, 32))
        self.buttonAddFolderRecursive = QPushButton(self.frame_2)
        self.buttonAddFolderRecursive.setObjectName(u"buttonAddFolderRecursive")
        self.buttonAddFolderRecursive.setGeometry(QRect(3, 100, 44, 40))
        self.buttonAddFolderRecursive.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/retoolFiles/images/icons8-recursive-folder-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonAddFolderRecursive.setIcon(icon3)
        self.buttonAddFolderRecursive.setIconSize(QSize(32, 32))
        self.buttonDeleteDats = QPushButton(self.frame_2)
        self.buttonDeleteDats.setObjectName(u"buttonDeleteDats")
        self.buttonDeleteDats.setGeometry(QRect(4, 150, 44, 40))
        self.buttonDeleteDats.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/retoolFiles/images/icons8-delete-file-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDeleteDats.setIcon(icon4)
        self.buttonDeleteDats.setIconSize(QSize(32, 32))
        self.buttonClearDats = QPushButton(self.frame_2)
        self.buttonClearDats.setObjectName(u"buttonClearDats")
        self.buttonClearDats.setGeometry(QRect(4, 200, 44, 40))
        self.buttonClearDats.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/retoolFiles/images/icons8-multiply-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClearDats.setIcon(icon5)
        self.buttonClearDats.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(80)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setMouseTracking(False)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.gridLayoutLeftFiles = QWidget(self.splitter)
        self.gridLayoutLeftFiles.setObjectName(u"gridLayoutLeftFiles")
        self.gridLayoutLeftFiles.setMouseTracking(False)
        self.gridLayoutLeft = QGridLayout(self.gridLayoutLeftFiles)
        self.gridLayoutLeft.setObjectName(u"gridLayoutLeft")
        self.gridLayoutLeft.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayoutLeft.setContentsMargins(6, 0, 3, 9)
        self.listWidgetOpenFiles = CustomList(self.gridLayoutLeftFiles)
        QListWidgetItem(self.listWidgetOpenFiles)
        self.listWidgetOpenFiles.setObjectName(u"listWidgetOpenFiles")
        self.listWidgetOpenFiles.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidgetOpenFiles.sizePolicy().hasHeightForWidth())
        self.listWidgetOpenFiles.setSizePolicy(sizePolicy2)
        self.listWidgetOpenFiles.setMinimumSize(QSize(187, 392))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        self.listWidgetOpenFiles.setFont(font2)
        self.listWidgetOpenFiles.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listWidgetOpenFiles.setProperty("showDropIndicator", False)
        self.listWidgetOpenFiles.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidgetOpenFiles.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetOpenFiles.setSortingEnabled(True)

        self.gridLayoutLeft.addWidget(self.listWidgetOpenFiles, 1, 2, 1, 1)

        self.labelSelectInput = QLabel(self.gridLayoutLeftFiles)
        self.labelSelectInput.setObjectName(u"labelSelectInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
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
        self.gridLayoutRight_2 = QWidget(self.splitter)
        self.gridLayoutRight_2.setObjectName(u"gridLayoutRight_2")
        self.gridLayoutRight_2.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayoutRight_2.setMouseTracking(False)
        self.gridLayoutRight = QGridLayout(self.gridLayoutRight_2)
        self.gridLayoutRight.setObjectName(u"gridLayoutRight")
        self.gridLayoutRight.setContentsMargins(3, 0, -1, -1)
        self.tabWidgetSettings = QTabWidget(self.gridLayoutRight_2)
        self.tabWidgetSettings.setObjectName(u"tabWidgetSettings")
        sizePolicy.setHeightForWidth(self.tabWidgetSettings.sizePolicy().hasHeightForWidth())
        self.tabWidgetSettings.setSizePolicy(sizePolicy)
        self.tabWidgetSettings.setMinimumSize(QSize(611, 481))
        self.tabWidgetSettings.setFont(font)
        self.tabGlobalSettings = QWidget()
        self.tabGlobalSettings.setObjectName(u"tabGlobalSettings")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        self.labelGlobalSettings.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.labelGlobalSettings)

        self.tabWidgetGlobalSettings = QTabWidget(self.tabGlobalSettings)
        self.tabWidgetGlobalSettings.setObjectName(u"tabWidgetGlobalSettings")
        self.tabWidgetGlobalSettings.setFont(font)
        self.tabGlobalRegions = QWidget()
        self.tabGlobalRegions.setObjectName(u"tabGlobalRegions")
        self.verticalLayout_6 = QVBoxLayout(self.tabGlobalRegions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridGlobalRegions = QWidget(self.tabGlobalRegions)
        self.gridGlobalRegions.setObjectName(u"gridGlobalRegions")
        self.gridLayoutGlobalRegions = QGridLayout(self.gridGlobalRegions)
        self.gridLayoutGlobalRegions.setObjectName(u"gridLayoutGlobalRegions")
        self.gridLayoutGlobalRegions.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalSelectedRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalSelectedRegions.setObjectName(u"labelGlobalSelectedRegions")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedRegions.setSizePolicy(sizePolicy5)
        self.labelGlobalSelectedRegions.setFont(font)
        self.labelGlobalSelectedRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalSelectedRegions, 2, 2, 1, 1)

        self.buttonGlobalDefaultRegionOrder = QPushButton(self.gridGlobalRegions)
        self.buttonGlobalDefaultRegionOrder.setObjectName(u"buttonGlobalDefaultRegionOrder")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonGlobalDefaultRegionOrder.sizePolicy().hasHeightForWidth())
        self.buttonGlobalDefaultRegionOrder.setSizePolicy(sizePolicy6)
        self.buttonGlobalDefaultRegionOrder.setMinimumSize(QSize(286, 41))

        self.gridLayoutGlobalRegions.addWidget(self.buttonGlobalDefaultRegionOrder, 5, 0, 1, 2)

        self.labelGlobalAvailableRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalAvailableRegions.setObjectName(u"labelGlobalAvailableRegions")
        sizePolicy5.setHeightForWidth(self.labelGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableRegions.setSizePolicy(sizePolicy5)
        self.labelGlobalAvailableRegions.setFont(font)
        self.labelGlobalAvailableRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalAvailableRegions, 2, 0, 1, 1)

        self.frameGlobalRegionUpDown = QFrame(self.gridGlobalRegions)
        self.frameGlobalRegionUpDown.setObjectName(u"frameGlobalRegionUpDown")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frameGlobalRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionUpDown.setSizePolicy(sizePolicy7)
        self.frameGlobalRegionUpDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalRegionUpDown.setFrameShape(QFrame.NoFrame)
        self.frameGlobalRegionUpDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frameGlobalRegionUpDown)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacerGlobalRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacerGlobalRegionUpDownTop)

        self.buttonGlobalRegionUp = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionUp.setObjectName(u"buttonGlobalRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionUp.setMinimumSize(QSize(40, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.buttonGlobalRegionUp.setFont(font4)
        icon6 = QIcon()
        icon6.addFile(u":/Arrows/images/icons8-sort-up-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionUp.setIcon(icon6)

        self.verticalLayout_13.addWidget(self.buttonGlobalRegionUp)

        self.buttonGlobalRegionDown = QPushButton(self.frameGlobalRegionUpDown)
        self.buttonGlobalRegionDown.setObjectName(u"buttonGlobalRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionDown.setFont(font4)
        icon7 = QIcon()
        icon7.addFile(u":/Arrows/images/icons8-sort-down-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionDown.setIcon(icon7)

        self.verticalLayout_13.addWidget(self.buttonGlobalRegionDown)

        self.verticalSpacerGlobalRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacerGlobalRegionUpDownBottom)


        self.gridLayoutGlobalRegions.addWidget(self.frameGlobalRegionUpDown, 3, 3, 1, 1)

        self.frameGlobalRegionLeftRight = QFrame(self.gridGlobalRegions)
        self.frameGlobalRegionLeftRight.setObjectName(u"frameGlobalRegionLeftRight")
        sizePolicy7.setHeightForWidth(self.frameGlobalRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalRegionLeftRight.setSizePolicy(sizePolicy7)
        self.frameGlobalRegionLeftRight.setMinimumSize(QSize(60, 0))
        self.frameGlobalRegionLeftRight.setFrameShape(QFrame.NoFrame)
        self.frameGlobalRegionLeftRight.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.frameGlobalRegionLeftRight)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacerGlobalRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacerGlobalRegionLeftRightTop)

        self.buttonGlobalRegionAllRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllRight.setObjectName(u"buttonGlobalRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionAllRight.setFont(font4)
        icon8 = QIcon()
        icon8.addFile(u":/Arrows/images/icons8-end-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionAllRight.setIcon(icon8)
        self.buttonGlobalRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionAllRight)

        self.buttonGlobalRegionRight = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionRight.setObjectName(u"buttonGlobalRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionRight.setFont(font4)
        icon9 = QIcon()
        icon9.addFile(u":/Arrows/images/icons8-sort-right-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionRight.setIcon(icon9)
        self.buttonGlobalRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionRight)

        self.buttonGlobalRegionLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionLeft.setObjectName(u"buttonGlobalRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionLeft.setFont(font4)
        icon10 = QIcon()
        icon10.addFile(u":/Arrows/images/icons8-sort-left-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionLeft.setIcon(icon10)

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionLeft)

        self.buttonGlobalRegionAllLeft = QPushButton(self.frameGlobalRegionLeftRight)
        self.buttonGlobalRegionAllLeft.setObjectName(u"buttonGlobalRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalRegionAllLeft.setFont(font4)
        icon11 = QIcon()
        icon11.addFile(u":/Arrows/images/icons8-skip-to-start-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGlobalRegionAllLeft.setIcon(icon11)
        self.buttonGlobalRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_12.addWidget(self.buttonGlobalRegionAllLeft)

        self.verticalSpacerGlobalRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacerGlobalRegionLeftRightBottom)


        self.gridLayoutGlobalRegions.addWidget(self.frameGlobalRegionLeftRight, 3, 1, 1, 1)

        self.listWidgetGlobalAvailableRegions = CustomList(self.gridGlobalRegions)
        self.listWidgetGlobalAvailableRegions.setObjectName(u"listWidgetGlobalAvailableRegions")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.listWidgetGlobalAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableRegions.setSizePolicy(sizePolicy8)
        self.listWidgetGlobalAvailableRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalAvailableRegions.setTabKeyNavigation(True)
        self.listWidgetGlobalAvailableRegions.setProperty("showDropIndicator", True)
        self.listWidgetGlobalAvailableRegions.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetGlobalAvailableRegions.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetGlobalAvailableRegions.setAlternatingRowColors(False)
        self.listWidgetGlobalAvailableRegions.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetGlobalAvailableRegions.setSortingEnabled(True)
        self.listWidgetGlobalAvailableRegions.setProperty("self_drag", False)
        self.listWidgetGlobalAvailableRegions.setProperty("is_drag_drop", True)

        self.gridLayoutGlobalRegions.addWidget(self.listWidgetGlobalAvailableRegions, 3, 0, 1, 1)

        self.listWidgetGlobalSelectedRegions = CustomListSelfDrag(self.gridGlobalRegions)
        self.listWidgetGlobalSelectedRegions.setObjectName(u"listWidgetGlobalSelectedRegions")
        sizePolicy8.setHeightForWidth(self.listWidgetGlobalSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedRegions.setSizePolicy(sizePolicy8)
        self.listWidgetGlobalSelectedRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalSelectedRegions.setTabKeyNavigation(True)
        self.listWidgetGlobalSelectedRegions.setProperty("showDropIndicator", True)
        self.listWidgetGlobalSelectedRegions.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetGlobalSelectedRegions.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetGlobalSelectedRegions.setAlternatingRowColors(False)
        self.listWidgetGlobalSelectedRegions.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetGlobalSelectedRegions.setProperty("self_drag", True)
        self.listWidgetGlobalSelectedRegions.setProperty("is_drag_drop", True)

        self.gridLayoutGlobalRegions.addWidget(self.listWidgetGlobalSelectedRegions, 3, 2, 1, 1)

        self.verticalSpacerGlobalRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayoutGlobalRegions.addItem(self.verticalSpacerGlobalRegionsEnglishButton, 4, 0, 1, 1)

        self.horizontalSpacerGlobalRegions = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutGlobalRegions.addItem(self.horizontalSpacerGlobalRegions, 3, 4, 1, 1)

        self.lineGlobalRegionSeparator = QFrame(self.gridGlobalRegions)
        self.lineGlobalRegionSeparator.setObjectName(u"lineGlobalRegionSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalRegionSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalRegionSeparator.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(85, 85, 85, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalRegionSeparator.setPalette(palette)
        self.lineGlobalRegionSeparator.setFrameShadow(QFrame.Plain)
        self.lineGlobalRegionSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutGlobalRegions.addWidget(self.lineGlobalRegionSeparator, 1, 0, 1, 5)

        self.labelGlobalFilterByRegions = QLabel(self.gridGlobalRegions)
        self.labelGlobalFilterByRegions.setObjectName(u"labelGlobalFilterByRegions")
        sizePolicy5.setHeightForWidth(self.labelGlobalFilterByRegions.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByRegions.setSizePolicy(sizePolicy5)
        self.labelGlobalFilterByRegions.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByRegions.setFont(font3)
        self.labelGlobalFilterByRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalRegions.addWidget(self.labelGlobalFilterByRegions, 0, 0, 1, 5)


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
        self.gridLayoutGlobalLanguages.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalLanguageLeftRight = QFrame(self.gridGlobalLanguages)
        self.frameGlobalLanguageLeftRight.setObjectName(u"frameGlobalLanguageLeftRight")
        sizePolicy7.setHeightForWidth(self.frameGlobalLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageLeftRight.setSizePolicy(sizePolicy7)
        self.frameGlobalLanguageLeftRight.setMinimumSize(QSize(60, 0))
        self.frameGlobalLanguageLeftRight.setFrameShape(QFrame.NoFrame)
        self.frameGlobalLanguageLeftRight.setFrameShadow(QFrame.Plain)
        self.verticalLayout_25 = QVBoxLayout(self.frameGlobalLanguageLeftRight)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacerGlobalLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightTop)

        self.buttonGlobalLanguageAllRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllRight.setObjectName(u"buttonGlobalLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllRight.setFont(font4)
        self.buttonGlobalLanguageAllRight.setIcon(icon8)
        self.buttonGlobalLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageAllRight)

        self.buttonGlobalLanguageRight = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageRight.setObjectName(u"buttonGlobalLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageRight.setFont(font4)
        self.buttonGlobalLanguageRight.setIcon(icon9)
        self.buttonGlobalLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageRight)

        self.buttonGlobalLanguageLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageLeft.setObjectName(u"buttonGlobalLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageLeft.setFont(font4)
        self.buttonGlobalLanguageLeft.setIcon(icon10)

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageLeft)

        self.buttonGlobalLanguageAllLeft = QPushButton(self.frameGlobalLanguageLeftRight)
        self.buttonGlobalLanguageAllLeft.setObjectName(u"buttonGlobalLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageAllLeft.setFont(font4)
        self.buttonGlobalLanguageAllLeft.setIcon(icon11)
        self.buttonGlobalLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_25.addWidget(self.buttonGlobalLanguageAllLeft)

        self.verticalSpacerGlobalLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightBottom)

        self.verticalSpacerGlobalLanguageLeftRightBuffer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacerGlobalLanguageLeftRightBuffer)


        self.gridLayoutGlobalLanguages.addWidget(self.frameGlobalLanguageLeftRight, 3, 1, 1, 1)

        self.horizontalSpacerGlobalLanguages = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutGlobalLanguages.addItem(self.horizontalSpacerGlobalLanguages, 3, 4, 1, 1)

        self.listWidgetGlobalAvailableLanguages = CustomList(self.gridGlobalLanguages)
        self.listWidgetGlobalAvailableLanguages.setObjectName(u"listWidgetGlobalAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.listWidgetGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalAvailableLanguages.setSizePolicy(sizePolicy8)
        self.listWidgetGlobalAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalAvailableLanguages.setProperty("showDropIndicator", True)
        self.listWidgetGlobalAvailableLanguages.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetGlobalAvailableLanguages.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetGlobalAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalAvailableLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetGlobalAvailableLanguages.setSortingEnabled(True)

        self.gridLayoutGlobalLanguages.addWidget(self.listWidgetGlobalAvailableLanguages, 3, 0, 1, 1)

        self.frameGlobalLanguageUpDown = QFrame(self.gridGlobalLanguages)
        self.frameGlobalLanguageUpDown.setObjectName(u"frameGlobalLanguageUpDown")
        sizePolicy7.setHeightForWidth(self.frameGlobalLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalLanguageUpDown.setSizePolicy(sizePolicy7)
        self.frameGlobalLanguageUpDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalLanguageUpDown.setFrameShape(QFrame.NoFrame)
        self.frameGlobalLanguageUpDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frameGlobalLanguageUpDown)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacerGlobalLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownTop)

        self.buttonGlobalLanguageUp = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageUp.setObjectName(u"buttonGlobalLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageUp.setFont(font4)
        self.buttonGlobalLanguageUp.setIcon(icon6)

        self.verticalLayout_24.addWidget(self.buttonGlobalLanguageUp)

        self.buttonGlobalLanguageDown = QPushButton(self.frameGlobalLanguageUpDown)
        self.buttonGlobalLanguageDown.setObjectName(u"buttonGlobalLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalLanguageDown.setFont(font4)
        self.buttonGlobalLanguageDown.setIcon(icon7)

        self.verticalLayout_24.addWidget(self.buttonGlobalLanguageDown)

        self.verticalSpacerGlobalLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownBottom)

        self.verticalSpacerGlobalLanguageUpDownBuffer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_24.addItem(self.verticalSpacerGlobalLanguageUpDownBuffer)


        self.gridLayoutGlobalLanguages.addWidget(self.frameGlobalLanguageUpDown, 3, 3, 1, 1)

        self.labelGlobalAvailableLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalAvailableLanguages.setObjectName(u"labelGlobalAvailableLanguages")
        sizePolicy5.setHeightForWidth(self.labelGlobalAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalAvailableLanguages.setSizePolicy(sizePolicy5)
        self.labelGlobalAvailableLanguages.setFont(font)
        self.labelGlobalAvailableLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalLanguages.addWidget(self.labelGlobalAvailableLanguages, 2, 0, 1, 1)

        self.labelGlobalSelectedLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalSelectedLanguages.setObjectName(u"labelGlobalSelectedLanguages")
        sizePolicy5.setHeightForWidth(self.labelGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalSelectedLanguages.setSizePolicy(sizePolicy5)
        self.labelGlobalSelectedLanguages.setFont(font)
        self.labelGlobalSelectedLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalLanguages.addWidget(self.labelGlobalSelectedLanguages, 2, 2, 1, 1)

        self.listWidgetGlobalSelectedLanguages = CustomListSelfDrag(self.gridGlobalLanguages)
        self.listWidgetGlobalSelectedLanguages.setObjectName(u"listWidgetGlobalSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.listWidgetGlobalSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalSelectedLanguages.setSizePolicy(sizePolicy8)
        self.listWidgetGlobalSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetGlobalSelectedLanguages.setProperty("showDropIndicator", True)
        self.listWidgetGlobalSelectedLanguages.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetGlobalSelectedLanguages.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetGlobalSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetGlobalSelectedLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayoutGlobalLanguages.addWidget(self.listWidgetGlobalSelectedLanguages, 3, 2, 1, 1)

        self.lineGlobalLanguageSeparator = QFrame(self.gridGlobalLanguages)
        self.lineGlobalLanguageSeparator.setObjectName(u"lineGlobalLanguageSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalLanguageSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalLanguageSeparator.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalLanguageSeparator.setPalette(palette1)
        self.lineGlobalLanguageSeparator.setFrameShadow(QFrame.Plain)
        self.lineGlobalLanguageSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutGlobalLanguages.addWidget(self.lineGlobalLanguageSeparator, 1, 0, 1, 5)

        self.labelGlobalFilterByLanguages = QLabel(self.gridGlobalLanguages)
        self.labelGlobalFilterByLanguages.setObjectName(u"labelGlobalFilterByLanguages")
        sizePolicy5.setHeightForWidth(self.labelGlobalFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByLanguages.setSizePolicy(sizePolicy5)
        self.labelGlobalFilterByLanguages.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByLanguages.setFont(font3)
        self.labelGlobalFilterByLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

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
        self.gridLayoutGlobalVideo.setContentsMargins(0, 0, 0, 0)
        self.frameGlobalVideoDown = QFrame(self.gridGlobalVideo)
        self.frameGlobalVideoDown.setObjectName(u"frameGlobalVideoDown")
        sizePolicy7.setHeightForWidth(self.frameGlobalVideoDown.sizePolicy().hasHeightForWidth())
        self.frameGlobalVideoDown.setSizePolicy(sizePolicy7)
        self.frameGlobalVideoDown.setMinimumSize(QSize(60, 0))
        self.frameGlobalVideoDown.setFrameShape(QFrame.NoFrame)
        self.frameGlobalVideoDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_27 = QVBoxLayout(self.frameGlobalVideoDown)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacerGlobalVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownTop)

        self.buttonGlobalVideoStandardUp = QPushButton(self.frameGlobalVideoDown)
        self.buttonGlobalVideoStandardUp.setObjectName(u"buttonGlobalVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardUp.setFont(font4)
        self.buttonGlobalVideoStandardUp.setIcon(icon6)

        self.verticalLayout_27.addWidget(self.buttonGlobalVideoStandardUp)

        self.buttonGlobalVideoStandardDown = QPushButton(self.frameGlobalVideoDown)
        self.buttonGlobalVideoStandardDown.setObjectName(u"buttonGlobalVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonGlobalVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonGlobalVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonGlobalVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonGlobalVideoStandardDown.setFont(font4)
        self.buttonGlobalVideoStandardDown.setIcon(icon7)

        self.verticalLayout_27.addWidget(self.buttonGlobalVideoStandardDown)

        self.verticalSpacerGlobalVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownBottom)

        self.verticalSpacerGlobalVideoUpDownBuffer = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacerGlobalVideoUpDownBuffer)


        self.gridLayoutGlobalVideo.addWidget(self.frameGlobalVideoDown, 4, 1, 1, 1)

        self.horizontalSpacerGlobalVideo_1 = QSpacerItem(220, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_1, 4, 2, 1, 1)

        self.listWidgetGlobalVideoStandards = CustomListSelfDrag(self.gridGlobalVideo)
        self.listWidgetGlobalVideoStandards.setObjectName(u"listWidgetGlobalVideoStandards")
        sizePolicy8.setHeightForWidth(self.listWidgetGlobalVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetGlobalVideoStandards.setSizePolicy(sizePolicy8)
        self.listWidgetGlobalVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetGlobalVideoStandards.setTabKeyNavigation(True)
        self.listWidgetGlobalVideoStandards.setProperty("showDropIndicator", True)
        self.listWidgetGlobalVideoStandards.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetGlobalVideoStandards.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetGlobalVideoStandards.setAlternatingRowColors(False)
        self.listWidgetGlobalVideoStandards.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayoutGlobalVideo.addWidget(self.listWidgetGlobalVideoStandards, 4, 0, 1, 1)

        self.horizontalSpacerGlobalVideo_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_3, 4, 4, 1, 1)

        self.labelGlobalVideoStandardsOrder = QLabel(self.gridGlobalVideo)
        self.labelGlobalVideoStandardsOrder.setObjectName(u"labelGlobalVideoStandardsOrder")
        sizePolicy5.setHeightForWidth(self.labelGlobalVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelGlobalVideoStandardsOrder.setSizePolicy(sizePolicy5)
        self.labelGlobalVideoStandardsOrder.setFont(font)
        self.labelGlobalVideoStandardsOrder.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalVideo.addWidget(self.labelGlobalVideoStandardsOrder, 2, 0, 1, 1)

        self.horizontalSpacerGlobalVideo_2 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutGlobalVideo.addItem(self.horizontalSpacerGlobalVideo_2, 4, 3, 1, 1)

        self.lineGlobalVideoStandardsSeparator = QFrame(self.gridGlobalVideo)
        self.lineGlobalVideoStandardsSeparator.setObjectName(u"lineGlobalVideoStandardsSeparator")
        sizePolicy3.setHeightForWidth(self.lineGlobalVideoStandardsSeparator.sizePolicy().hasHeightForWidth())
        self.lineGlobalVideoStandardsSeparator.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalVideoStandardsSeparator.setPalette(palette2)
        self.lineGlobalVideoStandardsSeparator.setFrameShadow(QFrame.Plain)
        self.lineGlobalVideoStandardsSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutGlobalVideo.addWidget(self.lineGlobalVideoStandardsSeparator, 1, 0, 1, 5)

        self.labelGlobalFilterByVideo = QLabel(self.gridGlobalVideo)
        self.labelGlobalFilterByVideo.setObjectName(u"labelGlobalFilterByVideo")
        sizePolicy5.setHeightForWidth(self.labelGlobalFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterByVideo.setSizePolicy(sizePolicy5)
        self.labelGlobalFilterByVideo.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByVideo.setFont(font3)
        self.labelGlobalFilterByVideo.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalVideo.addWidget(self.labelGlobalFilterByVideo, 0, 0, 1, 5)


        self.verticalLayout_9.addWidget(self.gridGlobalVideo)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalVideo, "")
        self.tabGlobalExclusions = QWidget()
        self.tabGlobalExclusions.setObjectName(u"tabGlobalExclusions")
        self.verticalLayout_10 = QVBoxLayout(self.tabGlobalExclusions)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayoutGlobalExclusions = QGridLayout()
        self.gridLayoutGlobalExclusions.setObjectName(u"gridLayoutGlobalExclusions")
        self.checkBoxGlobalExcludeBadDumps = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBadDumps.setObjectName(u"checkBoxGlobalExcludeBadDumps")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBadDumps, 6, 0, 1, 1)

        self.checkBoxGlobalExcludePirate = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePirate.setObjectName(u"checkBoxGlobalExcludePirate")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludePirate, 6, 2, 1, 1)

        self.checkBoxGlobalExcludeAudio = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeAudio.setObjectName(u"checkBoxGlobalExcludeAudio")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeAudio, 5, 0, 1, 1)

        self.checkBoxGlobalExcludeBonusDiscs = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBonusDiscs.setObjectName(u"checkBoxGlobalExcludeBonusDiscs")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBonusDiscs, 8, 0, 1, 1)

        self.checkBoxGlobalExcludeManuals = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeManuals.setObjectName(u"checkBoxGlobalExcludeManuals")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeManuals, 3, 2, 1, 1)

        self.lineGlobalExclude = QFrame(self.tabGlobalExclusions)
        self.lineGlobalExclude.setObjectName(u"lineGlobalExclude")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalExclude.setPalette(palette3)
        self.lineGlobalExclude.setFrameShadow(QFrame.Plain)
        self.lineGlobalExclude.setFrameShape(QFrame.HLine)

        self.gridLayoutGlobalExclusions.addWidget(self.lineGlobalExclude, 2, 0, 1, 6)

        self.checkBoxGlobalExcludeMultimedia = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeMultimedia.setObjectName(u"checkBoxGlobalExcludeMultimedia")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeMultimedia, 5, 2, 1, 1)

        self.horizontalSpacerGlobalExclude_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_3, 7, 3, 1, 1)

        self.checkBoxGlobalExcludeBIOS = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeBIOS.setObjectName(u"checkBoxGlobalExcludeBIOS")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeBIOS, 7, 0, 1, 1)

        self.checkBoxGlobalExcludeMIA = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeMIA.setObjectName(u"checkBoxGlobalExcludeMIA")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeMIA, 4, 2, 1, 1)

        self.checkBoxGlobalExcludeAddOns = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeAddOns.setObjectName(u"checkBoxGlobalExcludeAddOns")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeAddOns, 3, 0, 1, 1)

        self.horizontalSpacerGlobalExclude_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_1, 3, 5, 1, 1)

        self.verticalSpacerGlobalExclude_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayoutGlobalExclusions.addItem(self.verticalSpacerGlobalExclude_2, 12, 0, 1, 1)

        self.checkBoxGlobalExcludeUnlicensed = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeUnlicensed.setObjectName(u"checkBoxGlobalExcludeUnlicensed")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeUnlicensed, 9, 2, 1, 1)

        self.checkBoxGlobalExcludeVideo = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeVideo.setObjectName(u"checkBoxGlobalExcludeVideo")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeVideo, 10, 2, 1, 1)

        self.checkBoxGlobalExcludePromotional = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePromotional.setObjectName(u"checkBoxGlobalExcludePromotional")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludePromotional, 8, 2, 1, 1)

        self.checkBoxGlobalExcludeDemos = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeDemos.setObjectName(u"checkBoxGlobalExcludeDemos")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeDemos, 10, 0, 1, 1)

        self.checkBoxGlobalExcludeApplications = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeApplications.setObjectName(u"checkBoxGlobalExcludeApplications")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeApplications, 4, 0, 1, 1)

        self.checkBoxGlobalExcludeCoverdiscs = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeCoverdiscs.setObjectName(u"checkBoxGlobalExcludeCoverdiscs")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeCoverdiscs, 9, 0, 1, 1)

        self.checkBoxGlobalExcludePreproduction = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludePreproduction.setObjectName(u"checkBoxGlobalExcludePreproduction")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludePreproduction, 7, 2, 1, 1)

        self.labelGlobalExclude = QLabel(self.tabGlobalExclusions)
        self.labelGlobalExclude.setObjectName(u"labelGlobalExclude")
        self.labelGlobalExclude.setMinimumSize(QSize(0, 20))
        self.labelGlobalExclude.setFont(font3)
        self.labelGlobalExclude.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalExclusions.addWidget(self.labelGlobalExclude, 1, 0, 1, 6)

        self.horizontalSpacerGlobalExclude_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutGlobalExclusions.addItem(self.horizontalSpacerGlobalExclude_2, 7, 1, 1, 1)

        self.checkBoxGlobalExcludeEducational = QCheckBox(self.tabGlobalExclusions)
        self.checkBoxGlobalExcludeEducational.setObjectName(u"checkBoxGlobalExcludeEducational")

        self.gridLayoutGlobalExclusions.addWidget(self.checkBoxGlobalExcludeEducational, 11, 0, 1, 1)

        self.frameGlobalExcludeSelectButtons = QFrame(self.tabGlobalExclusions)
        self.frameGlobalExcludeSelectButtons.setObjectName(u"frameGlobalExcludeSelectButtons")
        sizePolicy8.setHeightForWidth(self.frameGlobalExcludeSelectButtons.sizePolicy().hasHeightForWidth())
        self.frameGlobalExcludeSelectButtons.setSizePolicy(sizePolicy8)
        self.frameGlobalExcludeSelectButtons.setMinimumSize(QSize(120, 80))
        self.frameGlobalExcludeSelectButtons.setFrameShape(QFrame.NoFrame)
        self.frameGlobalExcludeSelectButtons.setFrameShadow(QFrame.Plain)
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

        self.verticalSpacerGlobalExclude_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacerGlobalExclude_1)


        self.gridLayoutGlobalExclusions.addWidget(self.frameGlobalExcludeSelectButtons, 3, 4, 4, 1)


        self.verticalLayout_10.addLayout(self.gridLayoutGlobalExclusions)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalExclusions, "")
        self.tabGlobalOptions = QWidget()
        self.tabGlobalOptions.setObjectName(u"tabGlobalOptions")
        self.verticalLayout_14 = QVBoxLayout(self.tabGlobalOptions)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 9, -1, 0)
        self.scrollAreaGlobalOptions = QScrollArea(self.tabGlobalOptions)
        self.scrollAreaGlobalOptions.setObjectName(u"scrollAreaGlobalOptions")
        sizePolicy5.setHeightForWidth(self.scrollAreaGlobalOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaGlobalOptions.setSizePolicy(sizePolicy5)
        self.scrollAreaGlobalOptions.setFrameShape(QFrame.NoFrame)
        self.scrollAreaGlobalOptions.setFrameShadow(QFrame.Plain)
        self.scrollAreaGlobalOptions.setLineWidth(0)
        self.scrollAreaGlobalOptions.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaGlobalOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaGlobalOptions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollAreaGlobalOptions.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGlobalOptions = QWidget()
        self.scrollAreaWidgetContentsGlobalOptions.setObjectName(u"scrollAreaWidgetContentsGlobalOptions")
        self.scrollAreaWidgetContentsGlobalOptions.setGeometry(QRect(0, 0, 565, 760))
        sizePolicy5.setHeightForWidth(self.scrollAreaWidgetContentsGlobalOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsGlobalOptions.setSizePolicy(sizePolicy5)
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContentsGlobalOptions)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 18)
        self.labelGlobalOptions = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptions.setObjectName(u"labelGlobalOptions")
        self.labelGlobalOptions.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptions.setFont(font3)
        self.labelGlobalOptions.setScaledContents(False)
        self.labelGlobalOptions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptions)

        self.lineGlobalOptionsTitle = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.lineGlobalOptionsTitle.setObjectName(u"lineGlobalOptionsTitle")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalOptionsTitle.setPalette(palette4)
        self.lineGlobalOptionsTitle.setFrameShadow(QFrame.Plain)
        self.lineGlobalOptionsTitle.setFrameShape(QFrame.HLine)

        self.verticalLayout_16.addWidget(self.lineGlobalOptionsTitle)

        self.labelGlobalOptionsTitle = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsTitle.setObjectName(u"labelGlobalOptionsTitle")
        self.labelGlobalOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsTitle.setFont(font3)
        self.labelGlobalOptionsTitle.setScaledContents(False)
        self.labelGlobalOptionsTitle.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsTitle)

        self.checkBoxGlobalOptionsDisable1G1R = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisable1G1R.setObjectName(u"checkBoxGlobalOptionsDisable1G1R")
        self.checkBoxGlobalOptionsDisable1G1R.setMinimumSize(QSize(0, 20))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setKerning(True)
        self.checkBoxGlobalOptionsDisable1G1R.setFont(font5)
        self.checkBoxGlobalOptionsDisable1G1R.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisable1G1R)

        self.checkBoxGlobalOptionsIncludeHashless = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsIncludeHashless.setObjectName(u"checkBoxGlobalOptionsIncludeHashless")
        self.checkBoxGlobalOptionsIncludeHashless.setMinimumSize(QSize(0, 20))
        self.checkBoxGlobalOptionsIncludeHashless.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsIncludeHashless)

        self.checkBoxGlobalOptionsPreferRegions = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsPreferRegions.setObjectName(u"checkBoxGlobalOptionsPreferRegions")
        self.checkBoxGlobalOptionsPreferRegions.setMinimumSize(QSize(0, 20))
        self.checkBoxGlobalOptionsPreferRegions.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsPreferRegions)

        self.checkBoxGlobalOptionsModernPlatforms = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsModernPlatforms.setObjectName(u"checkBoxGlobalOptionsModernPlatforms")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.checkBoxGlobalOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsModernPlatforms.setSizePolicy(sizePolicy9)
        self.checkBoxGlobalOptionsModernPlatforms.setMinimumSize(QSize(0, 20))
        self.checkBoxGlobalOptionsModernPlatforms.setFont(font)
        self.checkBoxGlobalOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsModernPlatforms)

        self.checkBoxGlobalOptionsDemoteUnlicensed = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setObjectName(u"checkBoxGlobalOptionsDemoteUnlicensed")
        self.checkBoxGlobalOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 20))
        self.checkBoxGlobalOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDemoteUnlicensed)

        self.checkBoxGlobalOptionsDisableFilters = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableFilters.setObjectName(u"checkBoxGlobalOptionsDisableFilters")
        sizePolicy9.setHeightForWidth(self.checkBoxGlobalOptionsDisableFilters.sizePolicy().hasHeightForWidth())
        self.checkBoxGlobalOptionsDisableFilters.setSizePolicy(sizePolicy9)
        self.checkBoxGlobalOptionsDisableFilters.setMinimumSize(QSize(0, 20))
        self.checkBoxGlobalOptionsDisableFilters.setMaximumSize(QSize(16777215, 20))
        self.checkBoxGlobalOptionsDisableFilters.setFont(font)
        self.checkBoxGlobalOptionsDisableFilters.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisableFilters)

        self.verticalSpacerGlobalOptions_1 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_1)

        self.labelGlobalOptionsOutput = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsOutput.setObjectName(u"labelGlobalOptionsOutput")
        self.labelGlobalOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsOutput.setFont(font3)
        self.labelGlobalOptionsOutput.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_16.addWidget(self.labelGlobalOptionsOutput)

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
        sizePolicy5.setHeightForWidth(self.frameGlobalOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptions1G1RPrefix.setSizePolicy(sizePolicy5)
        self.frameGlobalOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette5 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(240, 240, 240, 0))
        brush3.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(227, 227, 227, 0))
        brush4.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        brush5 = QBrush(QColor(160, 160, 160, 0))
        brush5.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        brush7 = QBrush(QColor(0, 255, 127, 0))
        brush7.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(105, 105, 105, 0))
        brush8.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        brush9 = QBrush(QColor(246, 246, 246, 0))
        brush9.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.frameGlobalOptions1G1RPrefix.setPalette(palette5)
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

        self.verticalSpacerGlobalOptions_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_2)

        self.labelGlobalOptionsDebug = QLabel(self.scrollAreaWidgetContentsGlobalOptions)
        self.labelGlobalOptionsDebug.setObjectName(u"labelGlobalOptionsDebug")
        self.labelGlobalOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelGlobalOptionsDebug.setFont(font3)
        self.labelGlobalOptionsDebug.setTextInteractionFlags(Qt.NoTextInteraction)

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

        self.checkBoxGlobalOptionsBypassDTD = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsBypassDTD.setObjectName(u"checkBoxGlobalOptionsBypassDTD")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsBypassDTD)

        self.checkBoxGlobalOptionsDisableMultiCPU = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsDisableMultiCPU.setObjectName(u"checkBoxGlobalOptionsDisableMultiCPU")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsDisableMultiCPU)

        self.checkBoxGlobalOptionsTrace = QCheckBox(self.scrollAreaWidgetContentsGlobalOptions)
        self.checkBoxGlobalOptionsTrace.setObjectName(u"checkBoxGlobalOptionsTrace")

        self.verticalLayout_16.addWidget(self.checkBoxGlobalOptionsTrace)

        self.frameGlobalOptionsTrace = QFrame(self.scrollAreaWidgetContentsGlobalOptions)
        self.frameGlobalOptionsTrace.setObjectName(u"frameGlobalOptionsTrace")
        self.frameGlobalOptionsTrace.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.frameGlobalOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameGlobalOptionsTrace.setSizePolicy(sizePolicy5)
        self.frameGlobalOptionsTrace.setMinimumSize(QSize(0, 55))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.frameGlobalOptionsTrace.setPalette(palette6)
        self.labelGlobalOptionsTrace = QLabel(self.frameGlobalOptionsTrace)
        self.labelGlobalOptionsTrace.setObjectName(u"labelGlobalOptionsTrace")
        self.labelGlobalOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditGlobalOptionsTrace = CustomLineEdit(self.frameGlobalOptionsTrace)
        self.lineEditGlobalOptionsTrace.setObjectName(u"lineEditGlobalOptionsTrace")
        self.lineEditGlobalOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditGlobalOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_16.addWidget(self.frameGlobalOptionsTrace)

        self.verticalSpacerGlobalOptions_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacerGlobalOptions_3)

        self.scrollAreaGlobalOptions.setWidget(self.scrollAreaWidgetContentsGlobalOptions)

        self.verticalLayout_14.addWidget(self.scrollAreaGlobalOptions)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalOptions, "")
        self.tabGlobalUserFilters = QWidget()
        self.tabGlobalUserFilters.setObjectName(u"tabGlobalUserFilters")
        self.verticalLayout_11 = QVBoxLayout(self.tabGlobalUserFilters)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, -1, -1)
        self.scrollAreaGlobalUserFilters = QScrollArea(self.tabGlobalUserFilters)
        self.scrollAreaGlobalUserFilters.setObjectName(u"scrollAreaGlobalUserFilters")
        self.scrollAreaGlobalUserFilters.setFrameShape(QFrame.NoFrame)
        self.scrollAreaGlobalUserFilters.setFrameShadow(QFrame.Plain)
        self.scrollAreaGlobalUserFilters.setLineWidth(0)
        self.scrollAreaGlobalUserFilters.setMidLineWidth(0)
        self.scrollAreaGlobalUserFilters.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaGlobalUserFilters.setWidgetResizable(True)
        self.scrollAreaGlobalUserFilters.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContentsGlobalUserFilters = QWidget()
        self.scrollAreaWidgetContentsGlobalUserFilters.setObjectName(u"scrollAreaWidgetContentsGlobalUserFilters")
        self.scrollAreaWidgetContentsGlobalUserFilters.setGeometry(QRect(0, 0, 582, 393))
        self.gridLayoutGlobalUserFilters = QGridLayout(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.gridLayoutGlobalUserFilters.setObjectName(u"gridLayoutGlobalUserFilters")
        self.gridLayoutGlobalUserFilters.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayoutGlobalUserFilters.setContentsMargins(0, 0, 0, 10)
        self.textEditGlobalInclude = CustomTextEdit(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.textEditGlobalInclude.setObjectName(u"textEditGlobalInclude")
        sizePolicy.setHeightForWidth(self.textEditGlobalInclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalInclude.setSizePolicy(sizePolicy)
        self.textEditGlobalInclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalInclude.setTabChangesFocus(True)
        self.textEditGlobalInclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters.addWidget(self.textEditGlobalInclude, 5, 0, 1, 1)

        self.horizontalSpacerGlobalUserFilters = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutGlobalUserFilters.addItem(self.horizontalSpacerGlobalUserFilters, 5, 1, 1, 1)

        self.labelGlobalFilterExclude = QLabel(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.labelGlobalFilterExclude.setObjectName(u"labelGlobalFilterExclude")
        sizePolicy3.setHeightForWidth(self.labelGlobalFilterExclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterExclude.setSizePolicy(sizePolicy3)
        self.labelGlobalFilterExclude.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        self.labelGlobalFilterExclude.setFont(font6)
        self.labelGlobalFilterExclude.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalFilterExclude, 4, 2, 1, 1)

        self.labelGlobalFilter = QLabel(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.labelGlobalFilter.setObjectName(u"labelGlobalFilter")
        self.labelGlobalFilter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelGlobalFilter.setWordWrap(True)
        self.labelGlobalFilter.setOpenExternalLinks(True)
        self.labelGlobalFilter.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalFilter, 2, 0, 1, 3)

        self.labelGlobalFilterByText = QLabel(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.labelGlobalFilterByText.setObjectName(u"labelGlobalFilterByText")
        self.labelGlobalFilterByText.setMinimumSize(QSize(0, 20))
        self.labelGlobalFilterByText.setFont(font3)
        self.labelGlobalFilterByText.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalFilterByText, 0, 0, 1, 3)

        self.textEditGlobalExclude = CustomTextEdit(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.textEditGlobalExclude.setObjectName(u"textEditGlobalExclude")
        sizePolicy.setHeightForWidth(self.textEditGlobalExclude.sizePolicy().hasHeightForWidth())
        self.textEditGlobalExclude.setSizePolicy(sizePolicy)
        self.textEditGlobalExclude.setMinimumSize(QSize(0, 100))
        self.textEditGlobalExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditGlobalExclude.setTabChangesFocus(True)
        self.textEditGlobalExclude.setAcceptRichText(False)

        self.gridLayoutGlobalUserFilters.addWidget(self.textEditGlobalExclude, 5, 2, 1, 1)

        self.lineGlobalFilterByText = QFrame(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.lineGlobalFilterByText.setObjectName(u"lineGlobalFilterByText")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineGlobalFilterByText.setPalette(palette7)
        self.lineGlobalFilterByText.setFrameShadow(QFrame.Plain)
        self.lineGlobalFilterByText.setFrameShape(QFrame.HLine)

        self.gridLayoutGlobalUserFilters.addWidget(self.lineGlobalFilterByText, 1, 0, 1, 3)

        self.labelGlobalFilterInclude = QLabel(self.scrollAreaWidgetContentsGlobalUserFilters)
        self.labelGlobalFilterInclude.setObjectName(u"labelGlobalFilterInclude")
        sizePolicy5.setHeightForWidth(self.labelGlobalFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelGlobalFilterInclude.setSizePolicy(sizePolicy5)
        self.labelGlobalFilterInclude.setFont(font6)
        self.labelGlobalFilterInclude.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelGlobalFilterInclude.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutGlobalUserFilters.addWidget(self.labelGlobalFilterInclude, 4, 0, 1, 1)

        self.verticalSpacerGlobalUserFilters = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayoutGlobalUserFilters.addItem(self.verticalSpacerGlobalUserFilters, 3, 0, 1, 3)

        self.scrollAreaGlobalUserFilters.setWidget(self.scrollAreaWidgetContentsGlobalUserFilters)

        self.verticalLayout_11.addWidget(self.scrollAreaGlobalUserFilters)

        self.tabWidgetGlobalSettings.addTab(self.tabGlobalUserFilters, "")

        self.verticalLayout_7.addWidget(self.tabWidgetGlobalSettings)

        self.tabWidgetSettings.addTab(self.tabGlobalSettings, "")
        self.tabSystemSettings = QWidget()
        self.tabSystemSettings.setObjectName(u"tabSystemSettings")
        self.gridLayout_3 = QGridLayout(self.tabSystemSettings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelSystemSettings = QLabel(self.tabSystemSettings)
        self.labelSystemSettings.setObjectName(u"labelSystemSettings")
        self.labelSystemSettings.setFont(font)
        self.labelSystemSettings.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelSystemSettings.setWordWrap(True)
        self.labelSystemSettings.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_3.addWidget(self.labelSystemSettings, 0, 0, 1, 1)

        self.tabWidgetSystemSettings = QTabWidget(self.tabSystemSettings)
        self.tabWidgetSystemSettings.setObjectName(u"tabWidgetSystemSettings")
        self.tabWidgetSystemSettings.setFont(font)
        self.tabSystemPaths = QWidget()
        self.tabSystemPaths.setObjectName(u"tabSystemPaths")
        self.gridLayoutSystemPaths = QGridLayout(self.tabSystemPaths)
        self.gridLayoutSystemPaths.setObjectName(u"gridLayoutSystemPaths")
        self.gridLayoutSystemPaths.setVerticalSpacing(6)
        self.labelSelectSystemCloneList = QLabel(self.tabSystemPaths)
        self.labelSelectSystemCloneList.setObjectName(u"labelSelectSystemCloneList")
        self.labelSelectSystemCloneList.setMinimumSize(QSize(400, 0))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(8)
        font7.setBold(False)
        self.labelSelectSystemCloneList.setFont(font7)

        self.gridLayoutSystemPaths.addWidget(self.labelSelectSystemCloneList, 4, 3, 1, 2)

        self.buttonChooseSystemMetadataFile = QPushButton(self.tabSystemPaths)
        self.buttonChooseSystemMetadataFile.setObjectName(u"buttonChooseSystemMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonChooseSystemMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonChooseSystemMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonChooseSystemMetadataFile.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/retoolFiles/images/icons8-diff-files-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonChooseSystemMetadataFile.setIcon(icon12)
        self.buttonChooseSystemMetadataFile.setIconSize(QSize(32, 32))
        self.buttonChooseSystemMetadataFile.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonChooseSystemMetadataFile, 6, 1, 2, 1)

        self.buttonClearSystemCloneList = QPushButton(self.tabSystemPaths)
        self.buttonClearSystemCloneList.setObjectName(u"buttonClearSystemCloneList")
        sizePolicy6.setHeightForWidth(self.buttonClearSystemCloneList.sizePolicy().hasHeightForWidth())
        self.buttonClearSystemCloneList.setSizePolicy(sizePolicy6)
        self.buttonClearSystemCloneList.setFont(font1)
        self.buttonClearSystemCloneList.setIcon(icon5)
        self.buttonClearSystemCloneList.setIconSize(QSize(32, 32))
        self.buttonClearSystemCloneList.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonClearSystemCloneList, 4, 0, 2, 1)

        self.buttonChooseSystemOutput = QPushButton(self.tabSystemPaths)
        self.buttonChooseSystemOutput.setObjectName(u"buttonChooseSystemOutput")
        sizePolicy6.setHeightForWidth(self.buttonChooseSystemOutput.sizePolicy().hasHeightForWidth())
        self.buttonChooseSystemOutput.setSizePolicy(sizePolicy6)
        self.buttonChooseSystemOutput.setFont(font1)
        self.buttonChooseSystemOutput.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/retoolFiles/images/icons8-live-folder-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonChooseSystemOutput.setIcon(icon13)
        self.buttonChooseSystemOutput.setIconSize(QSize(32, 32))
        self.buttonChooseSystemOutput.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonChooseSystemOutput, 2, 1, 2, 1)

        self.horizontalSpacerSystemPaths_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSystemPaths.addItem(self.horizontalSpacerSystemPaths_2, 6, 5, 1, 1)

        self.buttonClearSystemOutput = QPushButton(self.tabSystemPaths)
        self.buttonClearSystemOutput.setObjectName(u"buttonClearSystemOutput")
        sizePolicy6.setHeightForWidth(self.buttonClearSystemOutput.sizePolicy().hasHeightForWidth())
        self.buttonClearSystemOutput.setSizePolicy(sizePolicy6)
        self.buttonClearSystemOutput.setFont(font1)
        self.buttonClearSystemOutput.setIcon(icon5)
        self.buttonClearSystemOutput.setIconSize(QSize(32, 32))
        self.buttonClearSystemOutput.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonClearSystemOutput, 2, 0, 2, 1)

        self.labelSelectSystemMetadataFile = QLabel(self.tabSystemPaths)
        self.labelSelectSystemMetadataFile.setObjectName(u"labelSelectSystemMetadataFile")
        self.labelSelectSystemMetadataFile.setMinimumSize(QSize(400, 0))
        self.labelSelectSystemMetadataFile.setFont(font7)

        self.gridLayoutSystemPaths.addWidget(self.labelSelectSystemMetadataFile, 6, 3, 1, 2)

        self.buttonClearSystemMetadataFile = QPushButton(self.tabSystemPaths)
        self.buttonClearSystemMetadataFile.setObjectName(u"buttonClearSystemMetadataFile")
        sizePolicy6.setHeightForWidth(self.buttonClearSystemMetadataFile.sizePolicy().hasHeightForWidth())
        self.buttonClearSystemMetadataFile.setSizePolicy(sizePolicy6)
        self.buttonClearSystemMetadataFile.setFont(font1)
        self.buttonClearSystemMetadataFile.setIcon(icon5)
        self.buttonClearSystemMetadataFile.setIconSize(QSize(32, 32))
        self.buttonClearSystemMetadataFile.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonClearSystemMetadataFile, 6, 0, 2, 1)

        self.frameSystemPathsHeader = QFrame(self.tabSystemPaths)
        self.frameSystemPathsHeader.setObjectName(u"frameSystemPathsHeader")
        sizePolicy3.setHeightForWidth(self.frameSystemPathsHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemPathsHeader.setSizePolicy(sizePolicy3)
        self.frameSystemPathsHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemPathsHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemPathsHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemPathsHeader.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frameSystemPathsHeader)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelSystemCustomFilesAndFolders = QLabel(self.frameSystemPathsHeader)
        self.labelSystemCustomFilesAndFolders.setObjectName(u"labelSystemCustomFilesAndFolders")
        self.labelSystemCustomFilesAndFolders.setFont(font3)
        self.labelSystemCustomFilesAndFolders.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.labelSystemCustomFilesAndFolders)

        self.checkBoxSystemOverridePaths = QCheckBox(self.frameSystemPathsHeader)
        self.checkBoxSystemOverridePaths.setObjectName(u"checkBoxSystemOverridePaths")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverridePaths.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverridePaths.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.checkBoxSystemOverridePaths)


        self.gridLayoutSystemPaths.addWidget(self.frameSystemPathsHeader, 0, 0, 1, 6)

        self.verticalSpacerSystemPaths = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayoutSystemPaths.addItem(self.verticalSpacerSystemPaths, 8, 3, 1, 1)

        self.lineSystemCustomFilesAndFolders = QFrame(self.tabSystemPaths)
        self.lineSystemCustomFilesAndFolders.setObjectName(u"lineSystemCustomFilesAndFolders")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemCustomFilesAndFolders.setPalette(palette8)
        self.lineSystemCustomFilesAndFolders.setFrameShadow(QFrame.Plain)
        self.lineSystemCustomFilesAndFolders.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemPaths.addWidget(self.lineSystemCustomFilesAndFolders, 1, 0, 1, 6)

        self.labelSelectSystemOutput = QLabel(self.tabSystemPaths)
        self.labelSelectSystemOutput.setObjectName(u"labelSelectSystemOutput")
        self.labelSelectSystemOutput.setMinimumSize(QSize(400, 0))
        self.labelSelectSystemOutput.setFont(font7)

        self.gridLayoutSystemPaths.addWidget(self.labelSelectSystemOutput, 2, 3, 1, 2)

        self.labelSystemMetadataFile = ElisionLabel(self.tabSystemPaths)
        self.labelSystemMetadataFile.setObjectName(u"labelSystemMetadataFile")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.labelSystemMetadataFile.sizePolicy().hasHeightForWidth())
        self.labelSystemMetadataFile.setSizePolicy(sizePolicy10)
        self.labelSystemMetadataFile.setMinimumSize(QSize(400, 0))
        palette9 = QPalette()
        brush10 = QBrush(QColor(119, 119, 119, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.labelSystemMetadataFile.setPalette(palette9)
        self.labelSystemMetadataFile.setFont(font2)

        self.gridLayoutSystemPaths.addWidget(self.labelSystemMetadataFile, 7, 3, 1, 2)

        self.buttonChooseSystemCloneList = QPushButton(self.tabSystemPaths)
        self.buttonChooseSystemCloneList.setObjectName(u"buttonChooseSystemCloneList")
        sizePolicy6.setHeightForWidth(self.buttonChooseSystemCloneList.sizePolicy().hasHeightForWidth())
        self.buttonChooseSystemCloneList.setSizePolicy(sizePolicy6)
        self.buttonChooseSystemCloneList.setFont(font1)
        self.buttonChooseSystemCloneList.setIcon(icon12)
        self.buttonChooseSystemCloneList.setIconSize(QSize(32, 32))
        self.buttonChooseSystemCloneList.setFlat(False)

        self.gridLayoutSystemPaths.addWidget(self.buttonChooseSystemCloneList, 4, 1, 2, 1)

        self.horizontalSpacerSystemPaths_1 = QSpacerItem(4, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemPaths.addItem(self.horizontalSpacerSystemPaths_1, 4, 2, 1, 1)

        self.labelSystemCloneList = ElisionLabel(self.tabSystemPaths)
        self.labelSystemCloneList.setObjectName(u"labelSystemCloneList")
        sizePolicy10.setHeightForWidth(self.labelSystemCloneList.sizePolicy().hasHeightForWidth())
        self.labelSystemCloneList.setSizePolicy(sizePolicy10)
        self.labelSystemCloneList.setMinimumSize(QSize(400, 0))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.labelSystemCloneList.setPalette(palette10)
        self.labelSystemCloneList.setFont(font2)

        self.gridLayoutSystemPaths.addWidget(self.labelSystemCloneList, 5, 3, 1, 2)

        self.labelSystemOutputFolder = ElisionLabel(self.tabSystemPaths)
        self.labelSystemOutputFolder.setObjectName(u"labelSystemOutputFolder")
        sizePolicy10.setHeightForWidth(self.labelSystemOutputFolder.sizePolicy().hasHeightForWidth())
        self.labelSystemOutputFolder.setSizePolicy(sizePolicy10)
        self.labelSystemOutputFolder.setMinimumSize(QSize(400, 0))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.labelSystemOutputFolder.setPalette(palette11)
        self.labelSystemOutputFolder.setFont(font2)

        self.gridLayoutSystemPaths.addWidget(self.labelSystemOutputFolder, 3, 3, 1, 2)

        self.tabWidgetSystemSettings.addTab(self.tabSystemPaths, "")
        self.tabSystemRegions = QWidget()
        self.tabSystemRegions.setObjectName(u"tabSystemRegions")
        self.verticalLayout = QVBoxLayout(self.tabSystemRegions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridSystemRegions = QWidget(self.tabSystemRegions)
        self.gridSystemRegions.setObjectName(u"gridSystemRegions")
        self.gridLayoutSystemRegions = QGridLayout(self.gridSystemRegions)
        self.gridLayoutSystemRegions.setObjectName(u"gridLayoutSystemRegions")
        self.gridLayoutSystemRegions.setContentsMargins(0, 0, 0, 0)
        self.frameSystemRegionUpDown = QFrame(self.gridSystemRegions)
        self.frameSystemRegionUpDown.setObjectName(u"frameSystemRegionUpDown")
        sizePolicy7.setHeightForWidth(self.frameSystemRegionUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionUpDown.setSizePolicy(sizePolicy7)
        self.frameSystemRegionUpDown.setMinimumSize(QSize(60, 0))
        self.frameSystemRegionUpDown.setFrameShape(QFrame.NoFrame)
        self.frameSystemRegionUpDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frameSystemRegionUpDown)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacerSystemRegionUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacerSystemRegionUpDownTop)

        self.buttonSystemRegionUp = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionUp.setObjectName(u"buttonSystemRegionUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionUp.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionUp.setFont(font4)
        self.buttonSystemRegionUp.setIcon(icon6)

        self.verticalLayout_15.addWidget(self.buttonSystemRegionUp)

        self.buttonSystemRegionDown = QPushButton(self.frameSystemRegionUpDown)
        self.buttonSystemRegionDown.setObjectName(u"buttonSystemRegionDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionDown.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionDown.setFont(font4)
        self.buttonSystemRegionDown.setIcon(icon7)

        self.verticalLayout_15.addWidget(self.buttonSystemRegionDown)

        self.verticalSpacerSystemRegionUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacerSystemRegionUpDownBottom)


        self.gridLayoutSystemRegions.addWidget(self.frameSystemRegionUpDown, 3, 3, 1, 1)

        self.horizontalSpacerSystemRegions = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSystemRegions.addItem(self.horizontalSpacerSystemRegions, 3, 4, 1, 1)

        self.labelSystemSelectedRegions = QLabel(self.gridSystemRegions)
        self.labelSystemSelectedRegions.setObjectName(u"labelSystemSelectedRegions")
        sizePolicy5.setHeightForWidth(self.labelSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedRegions.setSizePolicy(sizePolicy5)
        self.labelSystemSelectedRegions.setFont(font)
        self.labelSystemSelectedRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemRegions.addWidget(self.labelSystemSelectedRegions, 2, 2, 1, 1)

        self.frameSystemRegionLeftRight = QFrame(self.gridSystemRegions)
        self.frameSystemRegionLeftRight.setObjectName(u"frameSystemRegionLeftRight")
        sizePolicy7.setHeightForWidth(self.frameSystemRegionLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionLeftRight.setSizePolicy(sizePolicy7)
        self.frameSystemRegionLeftRight.setMinimumSize(QSize(60, 0))
        self.frameSystemRegionLeftRight.setFrameShape(QFrame.NoFrame)
        self.frameSystemRegionLeftRight.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frameSystemRegionLeftRight)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacerSystemRegionLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacerSystemRegionLeftRightTop)

        self.buttonSystemRegionAllRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllRight.setObjectName(u"buttonSystemRegionAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllRight.setFont(font4)
        self.buttonSystemRegionAllRight.setIcon(icon8)
        self.buttonSystemRegionAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionAllRight)

        self.buttonSystemRegionRight = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionRight.setObjectName(u"buttonSystemRegionRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionRight.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionRight.setFont(font4)
        self.buttonSystemRegionRight.setIcon(icon9)
        self.buttonSystemRegionRight.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionRight)

        self.buttonSystemRegionLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionLeft.setObjectName(u"buttonSystemRegionLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionLeft.setFont(font4)
        self.buttonSystemRegionLeft.setIcon(icon10)

        self.verticalLayout_17.addWidget(self.buttonSystemRegionLeft)

        self.buttonSystemRegionAllLeft = QPushButton(self.frameSystemRegionLeftRight)
        self.buttonSystemRegionAllLeft.setObjectName(u"buttonSystemRegionAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemRegionAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemRegionAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemRegionAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemRegionAllLeft.setFont(font4)
        self.buttonSystemRegionAllLeft.setIcon(icon11)
        self.buttonSystemRegionAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.buttonSystemRegionAllLeft)

        self.verticalSpacerSystemRegionLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        sizePolicy8.setHeightForWidth(self.listWidgetSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableRegions.setSizePolicy(sizePolicy8)
        self.listWidgetSystemAvailableRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemAvailableRegions.setTabKeyNavigation(True)
        self.listWidgetSystemAvailableRegions.setProperty("showDropIndicator", True)
        self.listWidgetSystemAvailableRegions.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetSystemAvailableRegions.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetSystemAvailableRegions.setAlternatingRowColors(False)
        self.listWidgetSystemAvailableRegions.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetSystemAvailableRegions.setSortingEnabled(True)

        self.gridLayoutSystemRegions.addWidget(self.listWidgetSystemAvailableRegions, 3, 0, 1, 1)

        self.lineSystemRegionSeparator = QFrame(self.gridSystemRegions)
        self.lineSystemRegionSeparator.setObjectName(u"lineSystemRegionSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemRegionSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemRegionSeparator.setSizePolicy(sizePolicy3)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemRegionSeparator.setPalette(palette12)
        self.lineSystemRegionSeparator.setFrameShadow(QFrame.Plain)
        self.lineSystemRegionSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemRegions.addWidget(self.lineSystemRegionSeparator, 1, 0, 1, 5)

        self.labelSystemAvailableRegions = QLabel(self.gridSystemRegions)
        self.labelSystemAvailableRegions.setObjectName(u"labelSystemAvailableRegions")
        sizePolicy5.setHeightForWidth(self.labelSystemAvailableRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableRegions.setSizePolicy(sizePolicy5)
        self.labelSystemAvailableRegions.setFont(font)
        self.labelSystemAvailableRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemRegions.addWidget(self.labelSystemAvailableRegions, 2, 0, 1, 1)

        self.frameSystemRegionsHeader = QFrame(self.gridSystemRegions)
        self.frameSystemRegionsHeader.setObjectName(u"frameSystemRegionsHeader")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frameSystemRegionsHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemRegionsHeader.setSizePolicy(sizePolicy11)
        self.frameSystemRegionsHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemRegionsHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemRegionsHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemRegionsHeader.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frameSystemRegionsHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByRegions = QLabel(self.frameSystemRegionsHeader)
        self.labelSystemFilterByRegions.setObjectName(u"labelSystemFilterByRegions")
        sizePolicy5.setHeightForWidth(self.labelSystemFilterByRegions.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByRegions.setSizePolicy(sizePolicy5)
        self.labelSystemFilterByRegions.setFont(font3)
        self.labelSystemFilterByRegions.setLineWidth(0)
        self.labelSystemFilterByRegions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.labelSystemFilterByRegions)

        self.checkBoxSystemOverrideRegions = QCheckBox(self.frameSystemRegionsHeader)
        self.checkBoxSystemOverrideRegions.setObjectName(u"checkBoxSystemOverrideRegions")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideRegions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideRegions.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.checkBoxSystemOverrideRegions)


        self.gridLayoutSystemRegions.addWidget(self.frameSystemRegionsHeader, 0, 0, 1, 5)

        self.verticalSpacerSystemRegionsEnglishButton = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayoutSystemRegions.addItem(self.verticalSpacerSystemRegionsEnglishButton, 4, 0, 1, 1)

        self.listWidgetSystemSelectedRegions = CustomListSelfDrag(self.gridSystemRegions)
        self.listWidgetSystemSelectedRegions.setObjectName(u"listWidgetSystemSelectedRegions")
        sizePolicy8.setHeightForWidth(self.listWidgetSystemSelectedRegions.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedRegions.setSizePolicy(sizePolicy8)
        self.listWidgetSystemSelectedRegions.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedRegions.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedRegions.setProperty("showDropIndicator", True)
        self.listWidgetSystemSelectedRegions.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetSystemSelectedRegions.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetSystemSelectedRegions.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedRegions.setSelectionMode(QAbstractItemView.ExtendedSelection)

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
        self.gridLayoutSystemLanguages.setContentsMargins(0, 0, 0, 0)
        self.listWidgetSystemAvailableLanguages = CustomList(self.gridSystemLanguages)
        self.listWidgetSystemAvailableLanguages.setObjectName(u"listWidgetSystemAvailableLanguages")
        sizePolicy8.setHeightForWidth(self.listWidgetSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemAvailableLanguages.setSizePolicy(sizePolicy8)
        self.listWidgetSystemAvailableLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemAvailableLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemAvailableLanguages.setProperty("showDropIndicator", True)
        self.listWidgetSystemAvailableLanguages.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetSystemAvailableLanguages.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetSystemAvailableLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemAvailableLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetSystemAvailableLanguages.setSortingEnabled(True)
        self.listWidgetSystemAvailableLanguages.setProperty("self_drag", False)

        self.gridLayoutSystemLanguages.addWidget(self.listWidgetSystemAvailableLanguages, 3, 0, 1, 1)

        self.frameSystemLanguagesHeader = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguagesHeader.setObjectName(u"frameSystemLanguagesHeader")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frameSystemLanguagesHeader.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguagesHeader.setSizePolicy(sizePolicy12)
        self.frameSystemLanguagesHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemLanguagesHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemLanguagesHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemLanguagesHeader.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frameSystemLanguagesHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByLanguages = QLabel(self.frameSystemLanguagesHeader)
        self.labelSystemFilterByLanguages.setObjectName(u"labelSystemFilterByLanguages")
        sizePolicy5.setHeightForWidth(self.labelSystemFilterByLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByLanguages.setSizePolicy(sizePolicy5)
        self.labelSystemFilterByLanguages.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterByLanguages.setFont(font3)
        self.labelSystemFilterByLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.labelSystemFilterByLanguages)

        self.checkBoxSystemOverrideLanguages = QCheckBox(self.frameSystemLanguagesHeader)
        self.checkBoxSystemOverrideLanguages.setObjectName(u"checkBoxSystemOverrideLanguages")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideLanguages.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideLanguages.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.checkBoxSystemOverrideLanguages)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguagesHeader, 0, 0, 1, 5)

        self.horizontalSpacerSystemLanguages = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSystemLanguages.addItem(self.horizontalSpacerSystemLanguages, 3, 4, 1, 1)

        self.frameSystemLanguageLeftRight = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguageLeftRight.setObjectName(u"frameSystemLanguageLeftRight")
        sizePolicy7.setHeightForWidth(self.frameSystemLanguageLeftRight.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageLeftRight.setSizePolicy(sizePolicy7)
        self.frameSystemLanguageLeftRight.setMinimumSize(QSize(60, 0))
        self.frameSystemLanguageLeftRight.setFrameShape(QFrame.NoFrame)
        self.frameSystemLanguageLeftRight.setFrameShadow(QFrame.Plain)
        self.verticalLayout_26 = QVBoxLayout(self.frameSystemLanguageLeftRight)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacerSystemLanguageLeftRightTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightTop)

        self.buttonSystemLanguageAllRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllRight.setObjectName(u"buttonSystemLanguageAllRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllRight.setFont(font4)
        self.buttonSystemLanguageAllRight.setIcon(icon8)
        self.buttonSystemLanguageAllRight.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageAllRight)

        self.buttonSystemLanguageRight = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageRight.setObjectName(u"buttonSystemLanguageRight")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageRight.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageRight.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageRight.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageRight.setFont(font4)
        self.buttonSystemLanguageRight.setIcon(icon9)
        self.buttonSystemLanguageRight.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageRight)

        self.buttonSystemLanguageLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageLeft.setObjectName(u"buttonSystemLanguageLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageLeft.setFont(font4)
        self.buttonSystemLanguageLeft.setIcon(icon10)

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageLeft)

        self.buttonSystemLanguageAllLeft = QPushButton(self.frameSystemLanguageLeftRight)
        self.buttonSystemLanguageAllLeft.setObjectName(u"buttonSystemLanguageAllLeft")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageAllLeft.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageAllLeft.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageAllLeft.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageAllLeft.setFont(font4)
        self.buttonSystemLanguageAllLeft.setIcon(icon11)
        self.buttonSystemLanguageAllLeft.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.buttonSystemLanguageAllLeft)

        self.verticalSpacerSystemLanguageLeftRightBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightBottom)

        self.verticalSpacerSystemLanguageLeftRightBuffer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacerSystemLanguageLeftRightBuffer)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguageLeftRight, 3, 1, 1, 1)

        self.lineSystemLanguageSeparator = QFrame(self.gridSystemLanguages)
        self.lineSystemLanguageSeparator.setObjectName(u"lineSystemLanguageSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemLanguageSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemLanguageSeparator.setSizePolicy(sizePolicy3)
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemLanguageSeparator.setPalette(palette13)
        self.lineSystemLanguageSeparator.setFrameShadow(QFrame.Plain)
        self.lineSystemLanguageSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemLanguages.addWidget(self.lineSystemLanguageSeparator, 1, 0, 1, 5)

        self.frameSystemLanguageUpDown = QFrame(self.gridSystemLanguages)
        self.frameSystemLanguageUpDown.setObjectName(u"frameSystemLanguageUpDown")
        sizePolicy7.setHeightForWidth(self.frameSystemLanguageUpDown.sizePolicy().hasHeightForWidth())
        self.frameSystemLanguageUpDown.setSizePolicy(sizePolicy7)
        self.frameSystemLanguageUpDown.setMinimumSize(QSize(60, 0))
        self.frameSystemLanguageUpDown.setFrameShape(QFrame.NoFrame)
        self.frameSystemLanguageUpDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_28 = QVBoxLayout(self.frameSystemLanguageUpDown)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacerSystemLanguageUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownTop)

        self.buttonSystemLanguageUp = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageUp.setObjectName(u"buttonSystemLanguageUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageUp.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageUp.setFont(font4)
        self.buttonSystemLanguageUp.setIcon(icon6)

        self.verticalLayout_28.addWidget(self.buttonSystemLanguageUp)

        self.buttonSystemLanguageDown = QPushButton(self.frameSystemLanguageUpDown)
        self.buttonSystemLanguageDown.setObjectName(u"buttonSystemLanguageDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemLanguageDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemLanguageDown.setSizePolicy(sizePolicy6)
        self.buttonSystemLanguageDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemLanguageDown.setFont(font4)
        self.buttonSystemLanguageDown.setIcon(icon7)

        self.verticalLayout_28.addWidget(self.buttonSystemLanguageDown)

        self.verticalSpacerSystemLanguageUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownBottom)

        self.verticalSpacerSystemLanguageUpDownBuffer = QSpacerItem(20, 53, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_28.addItem(self.verticalSpacerSystemLanguageUpDownBuffer)


        self.gridLayoutSystemLanguages.addWidget(self.frameSystemLanguageUpDown, 3, 3, 1, 1)

        self.listWidgetSystemSelectedLanguages = CustomListSelfDrag(self.gridSystemLanguages)
        self.listWidgetSystemSelectedLanguages.setObjectName(u"listWidgetSystemSelectedLanguages")
        sizePolicy8.setHeightForWidth(self.listWidgetSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemSelectedLanguages.setSizePolicy(sizePolicy8)
        self.listWidgetSystemSelectedLanguages.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemSelectedLanguages.setTabKeyNavigation(True)
        self.listWidgetSystemSelectedLanguages.setProperty("showDropIndicator", True)
        self.listWidgetSystemSelectedLanguages.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetSystemSelectedLanguages.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetSystemSelectedLanguages.setAlternatingRowColors(False)
        self.listWidgetSystemSelectedLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidgetSystemSelectedLanguages.setProperty("self_drag", True)

        self.gridLayoutSystemLanguages.addWidget(self.listWidgetSystemSelectedLanguages, 3, 2, 1, 1)

        self.labelSystemAvailableLanguages = QLabel(self.gridSystemLanguages)
        self.labelSystemAvailableLanguages.setObjectName(u"labelSystemAvailableLanguages")
        sizePolicy5.setHeightForWidth(self.labelSystemAvailableLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemAvailableLanguages.setSizePolicy(sizePolicy5)
        self.labelSystemAvailableLanguages.setFont(font)
        self.labelSystemAvailableLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemLanguages.addWidget(self.labelSystemAvailableLanguages, 2, 0, 1, 1)

        self.labelSystemSelectedLanguages = QLabel(self.gridSystemLanguages)
        self.labelSystemSelectedLanguages.setObjectName(u"labelSystemSelectedLanguages")
        sizePolicy5.setHeightForWidth(self.labelSystemSelectedLanguages.sizePolicy().hasHeightForWidth())
        self.labelSystemSelectedLanguages.setSizePolicy(sizePolicy5)
        self.labelSystemSelectedLanguages.setFont(font)
        self.labelSystemSelectedLanguages.setTextInteractionFlags(Qt.NoTextInteraction)

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
        self.gridLayoutSystemVideo.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerSystemVideo_3 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_3, 4, 3, 1, 1)

        self.horizontalSpacerSystemVideo_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_2, 4, 4, 1, 1)

        self.frameSystemVideoDown = QFrame(self.gridSystemVideo)
        self.frameSystemVideoDown.setObjectName(u"frameSystemVideoDown")
        sizePolicy7.setHeightForWidth(self.frameSystemVideoDown.sizePolicy().hasHeightForWidth())
        self.frameSystemVideoDown.setSizePolicy(sizePolicy7)
        self.frameSystemVideoDown.setMinimumSize(QSize(60, 0))
        self.frameSystemVideoDown.setFrameShape(QFrame.NoFrame)
        self.frameSystemVideoDown.setFrameShadow(QFrame.Plain)
        self.verticalLayout_29 = QVBoxLayout(self.frameSystemVideoDown)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacerSystemVideoUpDownTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownTop)

        self.buttonSystemVideoStandardUp = QPushButton(self.frameSystemVideoDown)
        self.buttonSystemVideoStandardUp.setObjectName(u"buttonSystemVideoStandardUp")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardUp.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardUp.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardUp.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardUp.setFont(font4)
        self.buttonSystemVideoStandardUp.setIcon(icon6)

        self.verticalLayout_29.addWidget(self.buttonSystemVideoStandardUp)

        self.buttonSystemVideoStandardDown = QPushButton(self.frameSystemVideoDown)
        self.buttonSystemVideoStandardDown.setObjectName(u"buttonSystemVideoStandardDown")
        sizePolicy6.setHeightForWidth(self.buttonSystemVideoStandardDown.sizePolicy().hasHeightForWidth())
        self.buttonSystemVideoStandardDown.setSizePolicy(sizePolicy6)
        self.buttonSystemVideoStandardDown.setMinimumSize(QSize(40, 41))
        self.buttonSystemVideoStandardDown.setFont(font4)
        self.buttonSystemVideoStandardDown.setIcon(icon7)

        self.verticalLayout_29.addWidget(self.buttonSystemVideoStandardDown)

        self.verticalSpacerSystemVideoUpDownBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownBottom)

        self.verticalSpacerSystemVideoUpDownBuffer = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_29.addItem(self.verticalSpacerSystemVideoUpDownBuffer)


        self.gridLayoutSystemVideo.addWidget(self.frameSystemVideoDown, 4, 1, 1, 1)

        self.lineSystemVideoStandardsSeparator = QFrame(self.gridSystemVideo)
        self.lineSystemVideoStandardsSeparator.setObjectName(u"lineSystemVideoStandardsSeparator")
        sizePolicy3.setHeightForWidth(self.lineSystemVideoStandardsSeparator.sizePolicy().hasHeightForWidth())
        self.lineSystemVideoStandardsSeparator.setSizePolicy(sizePolicy3)
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemVideoStandardsSeparator.setPalette(palette14)
        self.lineSystemVideoStandardsSeparator.setFrameShadow(QFrame.Plain)
        self.lineSystemVideoStandardsSeparator.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemVideo.addWidget(self.lineSystemVideoStandardsSeparator, 1, 0, 1, 5)

        self.frameSystemVideoHeader = QFrame(self.gridSystemVideo)
        self.frameSystemVideoHeader.setObjectName(u"frameSystemVideoHeader")
        self.frameSystemVideoHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemVideoHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemVideoHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemVideoHeader.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameSystemVideoHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelSystemFilterByVideo = QLabel(self.frameSystemVideoHeader)
        self.labelSystemFilterByVideo.setObjectName(u"labelSystemFilterByVideo")
        sizePolicy5.setHeightForWidth(self.labelSystemFilterByVideo.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterByVideo.setSizePolicy(sizePolicy5)
        self.labelSystemFilterByVideo.setMinimumSize(QSize(0, 20))
        self.labelSystemFilterByVideo.setFont(font3)
        self.labelSystemFilterByVideo.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.labelSystemFilterByVideo)

        self.checkBoxSystemOverrideVideo = QCheckBox(self.frameSystemVideoHeader)
        self.checkBoxSystemOverrideVideo.setObjectName(u"checkBoxSystemOverrideVideo")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideVideo.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideVideo.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.checkBoxSystemOverrideVideo)


        self.gridLayoutSystemVideo.addWidget(self.frameSystemVideoHeader, 0, 0, 1, 5)

        self.listWidgetSystemVideoStandards = CustomListSelfDrag(self.gridSystemVideo)
        self.listWidgetSystemVideoStandards.setObjectName(u"listWidgetSystemVideoStandards")
        sizePolicy8.setHeightForWidth(self.listWidgetSystemVideoStandards.sizePolicy().hasHeightForWidth())
        self.listWidgetSystemVideoStandards.setSizePolicy(sizePolicy8)
        self.listWidgetSystemVideoStandards.setMinimumSize(QSize(220, 0))
        self.listWidgetSystemVideoStandards.setTabKeyNavigation(True)
        self.listWidgetSystemVideoStandards.setProperty("showDropIndicator", True)
        self.listWidgetSystemVideoStandards.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidgetSystemVideoStandards.setDefaultDropAction(Qt.MoveAction)
        self.listWidgetSystemVideoStandards.setAlternatingRowColors(False)
        self.listWidgetSystemVideoStandards.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayoutSystemVideo.addWidget(self.listWidgetSystemVideoStandards, 4, 0, 1, 1)

        self.horizontalSpacerSystemVideo_1 = QSpacerItem(220, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemVideo.addItem(self.horizontalSpacerSystemVideo_1, 4, 2, 1, 1)

        self.labelSystemVideoStandardsOrder = QLabel(self.gridSystemVideo)
        self.labelSystemVideoStandardsOrder.setObjectName(u"labelSystemVideoStandardsOrder")
        sizePolicy5.setHeightForWidth(self.labelSystemVideoStandardsOrder.sizePolicy().hasHeightForWidth())
        self.labelSystemVideoStandardsOrder.setSizePolicy(sizePolicy5)
        self.labelSystemVideoStandardsOrder.setFont(font)
        self.labelSystemVideoStandardsOrder.setTextInteractionFlags(Qt.NoTextInteraction)

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
        self.gridLayoutSystemExclusions.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSystemExcludeEducational = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeEducational.setObjectName(u"checkBoxSystemExcludeEducational")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeEducational, 10, 0, 1, 1)

        self.frameSystemExcludeSelectButtons = QFrame(self.gridSystemExclusions)
        self.frameSystemExcludeSelectButtons.setObjectName(u"frameSystemExcludeSelectButtons")
        sizePolicy8.setHeightForWidth(self.frameSystemExcludeSelectButtons.sizePolicy().hasHeightForWidth())
        self.frameSystemExcludeSelectButtons.setSizePolicy(sizePolicy8)
        self.frameSystemExcludeSelectButtons.setMinimumSize(QSize(120, 80))
        self.frameSystemExcludeSelectButtons.setFrameShape(QFrame.NoFrame)
        self.frameSystemExcludeSelectButtons.setFrameShadow(QFrame.Plain)
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

        self.verticalSpacerSystemExclude_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacerSystemExclude_1)


        self.gridLayoutSystemExclusions.addWidget(self.frameSystemExcludeSelectButtons, 2, 4, 4, 1)

        self.checkBoxSystemExcludeBadDumps = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBadDumps.setObjectName(u"checkBoxSystemExcludeBadDumps")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBadDumps, 5, 0, 1, 1)

        self.lineSystemExclude = QFrame(self.gridSystemExclusions)
        self.lineSystemExclude.setObjectName(u"lineSystemExclude")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemExclude.setPalette(palette15)
        self.lineSystemExclude.setFrameShadow(QFrame.Plain)
        self.lineSystemExclude.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemExclusions.addWidget(self.lineSystemExclude, 1, 0, 1, 6)

        self.checkBoxSystemExcludePreproduction = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePreproduction.setObjectName(u"checkBoxSystemExcludePreproduction")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludePreproduction, 6, 2, 1, 1)

        self.horizontalSpacerSystemExclude_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_3, 6, 1, 1, 1)

        self.checkBoxSystemExcludeCoverdiscs = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeCoverdiscs.setObjectName(u"checkBoxSystemExcludeCoverdiscs")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeCoverdiscs, 8, 0, 1, 1)

        self.checkBoxSystemExcludeBonusDiscs = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBonusDiscs.setObjectName(u"checkBoxSystemExcludeBonusDiscs")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBonusDiscs, 7, 0, 1, 1)

        self.checkBoxSystemExcludeVideo = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeVideo.setObjectName(u"checkBoxSystemExcludeVideo")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeVideo, 9, 2, 1, 1)

        self.checkBoxSystemExcludeApplications = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeApplications.setObjectName(u"checkBoxSystemExcludeApplications")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeApplications, 3, 0, 1, 1)

        self.checkBoxSystemExcludeMultimedia = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeMultimedia.setObjectName(u"checkBoxSystemExcludeMultimedia")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeMultimedia, 4, 2, 1, 1)

        self.checkBoxSystemExcludeDemos = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeDemos.setObjectName(u"checkBoxSystemExcludeDemos")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeDemos, 9, 0, 1, 1)

        self.horizontalSpacerSystemExclude_1 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_1, 6, 3, 1, 1)

        self.checkBoxSystemExcludePromotional = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePromotional.setObjectName(u"checkBoxSystemExcludePromotional")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludePromotional, 7, 2, 1, 1)

        self.checkBoxSystemExcludeBIOS = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeBIOS.setObjectName(u"checkBoxSystemExcludeBIOS")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeBIOS, 6, 0, 1, 1)

        self.checkBoxSystemExcludeMIA = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeMIA.setObjectName(u"checkBoxSystemExcludeMIA")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeMIA, 3, 2, 1, 1)

        self.checkBoxSystemExcludeUnlicensed = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeUnlicensed.setObjectName(u"checkBoxSystemExcludeUnlicensed")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeUnlicensed, 8, 2, 1, 1)

        self.frameSystemExcludeHeader = QFrame(self.gridSystemExclusions)
        self.frameSystemExcludeHeader.setObjectName(u"frameSystemExcludeHeader")
        self.frameSystemExcludeHeader.setMinimumSize(QSize(0, 20))
        self.frameSystemExcludeHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemExcludeHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemExcludeHeader.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frameSystemExcludeHeader)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelGlobalExclude_2 = QLabel(self.frameSystemExcludeHeader)
        self.labelGlobalExclude_2.setObjectName(u"labelGlobalExclude_2")
        self.labelGlobalExclude_2.setMinimumSize(QSize(0, 20))
        self.labelGlobalExclude_2.setFont(font3)
        self.labelGlobalExclude_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_4.addWidget(self.labelGlobalExclude_2)

        self.checkBoxSystemOverrideExclusions = QCheckBox(self.frameSystemExcludeHeader)
        self.checkBoxSystemOverrideExclusions.setObjectName(u"checkBoxSystemOverrideExclusions")
        sizePolicy6.setHeightForWidth(self.checkBoxSystemOverrideExclusions.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOverrideExclusions.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.checkBoxSystemOverrideExclusions)


        self.gridLayoutSystemExclusions.addWidget(self.frameSystemExcludeHeader, 0, 0, 1, 6)

        self.checkBoxSystemExcludePirate = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludePirate.setObjectName(u"checkBoxSystemExcludePirate")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludePirate, 5, 2, 1, 1)

        self.checkBoxSystemExcludeAudio = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeAudio.setObjectName(u"checkBoxSystemExcludeAudio")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeAudio, 4, 0, 1, 1)

        self.verticalSpacerSystemExclude_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayoutSystemExclusions.addItem(self.verticalSpacerSystemExclude_2, 11, 0, 1, 1)

        self.horizontalSpacerSystemExclude_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutSystemExclusions.addItem(self.horizontalSpacerSystemExclude_2, 2, 5, 1, 1)

        self.checkBoxSystemExcludeManuals = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeManuals.setObjectName(u"checkBoxSystemExcludeManuals")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeManuals, 2, 2, 1, 1)

        self.checkBoxSystemExcludeAddOns = QCheckBox(self.gridSystemExclusions)
        self.checkBoxSystemExcludeAddOns.setObjectName(u"checkBoxSystemExcludeAddOns")

        self.gridLayoutSystemExclusions.addWidget(self.checkBoxSystemExcludeAddOns, 2, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.gridSystemExclusions)

        self.tabWidgetSystemSettings.addTab(self.tabSystemExclusions, "")
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
        self.frameSystemOptionsHeader.setFrameShape(QFrame.NoFrame)
        self.frameSystemOptionsHeader.setFrameShadow(QFrame.Plain)
        self.frameSystemOptionsHeader.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frameSystemOptionsHeader)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
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
        self.labelSystemOptions.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_4.addWidget(self.labelSystemOptions, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frameSystemOptionsHeader)

        self.lineSystemOptions = QFrame(self.tabSystemOptions)
        self.lineSystemOptions.setObjectName(u"lineSystemOptions")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemOptions.setPalette(palette16)
        self.lineSystemOptions.setFrameShadow(QFrame.Plain)
        self.lineSystemOptions.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.lineSystemOptions)

        self.scrollAreaSystemOptions = QScrollArea(self.tabSystemOptions)
        self.scrollAreaSystemOptions.setObjectName(u"scrollAreaSystemOptions")
        sizePolicy5.setHeightForWidth(self.scrollAreaSystemOptions.sizePolicy().hasHeightForWidth())
        self.scrollAreaSystemOptions.setSizePolicy(sizePolicy5)
        self.scrollAreaSystemOptions.setFrameShape(QFrame.NoFrame)
        self.scrollAreaSystemOptions.setFrameShadow(QFrame.Plain)
        self.scrollAreaSystemOptions.setLineWidth(0)
        self.scrollAreaSystemOptions.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaSystemOptions.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaSystemOptions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollAreaSystemOptions.setWidgetResizable(True)
        self.layoutScrollAreaSystemOptions = QWidget()
        self.layoutScrollAreaSystemOptions.setObjectName(u"layoutScrollAreaSystemOptions")
        self.layoutScrollAreaSystemOptions.setGeometry(QRect(0, 0, 422, 725))
        sizePolicy5.setHeightForWidth(self.layoutScrollAreaSystemOptions.sizePolicy().hasHeightForWidth())
        self.layoutScrollAreaSystemOptions.setSizePolicy(sizePolicy5)
        self.verticalLayout_22 = QVBoxLayout(self.layoutScrollAreaSystemOptions)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 18, 18)
        self.labelSystemOptionsTitle = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsTitle.setObjectName(u"labelSystemOptionsTitle")
        self.labelSystemOptionsTitle.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsTitle.setFont(font3)
        self.labelSystemOptionsTitle.setScaledContents(False)
        self.labelSystemOptionsTitle.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsTitle)

        self.checkBoxSystemOptionsDisable1G1R = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisable1G1R.setObjectName(u"checkBoxSystemOptionsDisable1G1R")
        self.checkBoxSystemOptionsDisable1G1R.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsDisable1G1R.setFont(font5)
        self.checkBoxSystemOptionsDisable1G1R.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisable1G1R)

        self.checkBoxSystemOptionsIncludeHashless = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsIncludeHashless.setObjectName(u"checkBoxSystemOptionsIncludeHashless")
        self.checkBoxSystemOptionsIncludeHashless.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsIncludeHashless.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsIncludeHashless)

        self.checkBoxSystemOptionsPreferRegions = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsPreferRegions.setObjectName(u"checkBoxSystemOptionsPreferRegions")
        self.checkBoxSystemOptionsPreferRegions.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsPreferRegions.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsPreferRegions)

        self.checkBoxSystemOptionsModernPlatforms = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsModernPlatforms.setObjectName(u"checkBoxSystemOptionsModernPlatforms")
        sizePolicy9.setHeightForWidth(self.checkBoxSystemOptionsModernPlatforms.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsModernPlatforms.setSizePolicy(sizePolicy9)
        self.checkBoxSystemOptionsModernPlatforms.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsModernPlatforms.setFont(font)
        self.checkBoxSystemOptionsModernPlatforms.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsModernPlatforms)

        self.checkBoxSystemOptionsDemoteUnlicensed = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDemoteUnlicensed.setObjectName(u"checkBoxSystemOptionsDemoteUnlicensed")
        self.checkBoxSystemOptionsDemoteUnlicensed.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsDemoteUnlicensed.setFont(font)
        self.checkBoxSystemOptionsDemoteUnlicensed.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDemoteUnlicensed)

        self.checkBoxSystemOptionsDisableFilters = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisableFilters.setObjectName(u"checkBoxSystemOptionsDisableFilters")
        sizePolicy9.setHeightForWidth(self.checkBoxSystemOptionsDisableFilters.sizePolicy().hasHeightForWidth())
        self.checkBoxSystemOptionsDisableFilters.setSizePolicy(sizePolicy9)
        self.checkBoxSystemOptionsDisableFilters.setMinimumSize(QSize(0, 20))
        self.checkBoxSystemOptionsDisableFilters.setMaximumSize(QSize(16777215, 20))
        self.checkBoxSystemOptionsDisableFilters.setFont(font)
        self.checkBoxSystemOptionsDisableFilters.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisableFilters)

        self.verticalSpacerSystemOptions_1 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_1)

        self.labelSystemOptionsOutput = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsOutput.setObjectName(u"labelSystemOptionsOutput")
        self.labelSystemOptionsOutput.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsOutput.setFont(font3)
        self.labelSystemOptionsOutput.setLineWidth(0)
        self.labelSystemOptionsOutput.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.labelSystemOptionsOutput)

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
        sizePolicy5.setHeightForWidth(self.frameSystemOptions1G1RPrefix.sizePolicy().hasHeightForWidth())
        self.frameSystemOptions1G1RPrefix.setSizePolicy(sizePolicy5)
        self.frameSystemOptions1G1RPrefix.setMinimumSize(QSize(0, 109))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.frameSystemOptions1G1RPrefix.setPalette(palette17)
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

        self.verticalSpacerSystemOptions_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_2)

        self.labelSystemOptionsDebug = QLabel(self.layoutScrollAreaSystemOptions)
        self.labelSystemOptionsDebug.setObjectName(u"labelSystemOptionsDebug")
        self.labelSystemOptionsDebug.setMinimumSize(QSize(0, 20))
        self.labelSystemOptionsDebug.setFont(font3)
        self.labelSystemOptionsDebug.setLineWidth(0)
        self.labelSystemOptionsDebug.setTextInteractionFlags(Qt.NoTextInteraction)

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

        self.checkBoxSystemOptionsBypassDTD = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsBypassDTD.setObjectName(u"checkBoxSystemOptionsBypassDTD")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsBypassDTD)

        self.checkBoxSystemOptionsDisableMultiCPU = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsDisableMultiCPU.setObjectName(u"checkBoxSystemOptionsDisableMultiCPU")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsDisableMultiCPU)

        self.checkBoxSystemOptionsTrace = QCheckBox(self.layoutScrollAreaSystemOptions)
        self.checkBoxSystemOptionsTrace.setObjectName(u"checkBoxSystemOptionsTrace")

        self.verticalLayout_22.addWidget(self.checkBoxSystemOptionsTrace)

        self.frameSystemOptionsTrace = QFrame(self.layoutScrollAreaSystemOptions)
        self.frameSystemOptionsTrace.setObjectName(u"frameSystemOptionsTrace")
        self.frameSystemOptionsTrace.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.frameSystemOptionsTrace.sizePolicy().hasHeightForWidth())
        self.frameSystemOptionsTrace.setSizePolicy(sizePolicy5)
        self.frameSystemOptionsTrace.setMinimumSize(QSize(0, 55))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush8)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush8)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush8)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.frameSystemOptionsTrace.setPalette(palette18)
        self.labelSystemOptionsTrace = QLabel(self.frameSystemOptionsTrace)
        self.labelSystemOptionsTrace.setObjectName(u"labelSystemOptionsTrace")
        self.labelSystemOptionsTrace.setGeometry(QRect(22, 5, 521, 20))
        self.lineEditSystemOptionsTrace = CustomLineEdit(self.frameSystemOptionsTrace)
        self.lineEditSystemOptionsTrace.setObjectName(u"lineEditSystemOptionsTrace")
        self.lineEditSystemOptionsTrace.setGeometry(QRect(20, 30, 521, 24))
        self.lineEditSystemOptionsTrace.setMinimumSize(QSize(0, 24))

        self.verticalLayout_22.addWidget(self.frameSystemOptionsTrace)

        self.verticalSpacerSystemOptions_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacerSystemOptions_3)

        self.scrollAreaSystemOptions.setWidget(self.layoutScrollAreaSystemOptions)

        self.verticalLayout_3.addWidget(self.scrollAreaSystemOptions)

        self.tabWidgetSystemSettings.addTab(self.tabSystemOptions, "")
        self.tabSystemUserFilters = QWidget()
        self.tabSystemUserFilters.setObjectName(u"tabSystemUserFilters")
        self.verticalLayout_4 = QVBoxLayout(self.tabSystemUserFilters)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollAreaSystemUserFilters = QScrollArea(self.tabSystemUserFilters)
        self.scrollAreaSystemUserFilters.setObjectName(u"scrollAreaSystemUserFilters")
        self.scrollAreaSystemUserFilters.setFrameShape(QFrame.NoFrame)
        self.scrollAreaSystemUserFilters.setFrameShadow(QFrame.Plain)
        self.scrollAreaSystemUserFilters.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaSystemUserFilters.setWidgetResizable(True)
        self.scrollAreaSystemUserFilters.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContentsSystemUserFilters = QWidget()
        self.scrollAreaWidgetContentsSystemUserFilters.setObjectName(u"scrollAreaWidgetContentsSystemUserFilters")
        self.scrollAreaWidgetContentsSystemUserFilters.setGeometry(QRect(0, 0, 182, 553))
        self.scrollAreaWidgetContentsSystemUserFilters.setMinimumSize(QSize(0, 0))
        self.gridLayoutSystemUserFilters = QGridLayout(self.scrollAreaWidgetContentsSystemUserFilters)
        self.gridLayoutSystemUserFilters.setObjectName(u"gridLayoutSystemUserFilters")
        self.gridLayoutSystemUserFilters.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayoutSystemUserFilters.setContentsMargins(0, 0, 18, 10)
        self.textEditSystemInclude = CustomTextEdit(self.scrollAreaWidgetContentsSystemUserFilters)
        self.textEditSystemInclude.setObjectName(u"textEditSystemInclude")
        sizePolicy.setHeightForWidth(self.textEditSystemInclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemInclude.setSizePolicy(sizePolicy)
        self.textEditSystemInclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemInclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemInclude.setTabChangesFocus(True)
        self.textEditSystemInclude.setAcceptRichText(False)

        self.gridLayoutSystemUserFilters.addWidget(self.textEditSystemInclude, 5, 0, 1, 1)

        self.horizontalSpacerSystemUserFilters = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayoutSystemUserFilters.addItem(self.horizontalSpacerSystemUserFilters, 5, 1, 1, 1)

        self.lineSystemFilterByText = QFrame(self.scrollAreaWidgetContentsSystemUserFilters)
        self.lineSystemFilterByText.setObjectName(u"lineSystemFilterByText")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSystemFilterByText.setPalette(palette19)
        self.lineSystemFilterByText.setFrameShadow(QFrame.Plain)
        self.lineSystemFilterByText.setFrameShape(QFrame.HLine)

        self.gridLayoutSystemUserFilters.addWidget(self.lineSystemFilterByText, 1, 0, 1, 3)

        self.verticalSpacerSystemUserFilters = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayoutSystemUserFilters.addItem(self.verticalSpacerSystemUserFilters, 3, 0, 1, 3)

        self.labelSystemFilterInclude = QLabel(self.scrollAreaWidgetContentsSystemUserFilters)
        self.labelSystemFilterInclude.setObjectName(u"labelSystemFilterInclude")
        sizePolicy5.setHeightForWidth(self.labelSystemFilterInclude.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterInclude.setSizePolicy(sizePolicy5)
        self.labelSystemFilterInclude.setFont(font6)
        self.labelSystemFilterInclude.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelSystemFilterInclude.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemFilterInclude, 4, 0, 1, 1)

        self.labelSystemFilterExclude = QLabel(self.scrollAreaWidgetContentsSystemUserFilters)
        self.labelSystemFilterExclude.setObjectName(u"labelSystemFilterExclude")
        sizePolicy3.setHeightForWidth(self.labelSystemFilterExclude.sizePolicy().hasHeightForWidth())
        self.labelSystemFilterExclude.setSizePolicy(sizePolicy3)
        self.labelSystemFilterExclude.setMinimumSize(QSize(0, 0))
        self.labelSystemFilterExclude.setFont(font6)
        self.labelSystemFilterExclude.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemFilterExclude, 4, 2, 1, 1)

        self.labelSystemFilterByText = QLabel(self.scrollAreaWidgetContentsSystemUserFilters)
        self.labelSystemFilterByText.setObjectName(u"labelSystemFilterByText")
        self.labelSystemFilterByText.setMinimumSize(QSize(0, 20))
        self.labelSystemFilterByText.setFont(font3)
        self.labelSystemFilterByText.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemFilterByText, 0, 0, 1, 3)

        self.labelSystemFilter = QLabel(self.scrollAreaWidgetContentsSystemUserFilters)
        self.labelSystemFilter.setObjectName(u"labelSystemFilter")
        self.labelSystemFilter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelSystemFilter.setWordWrap(True)
        self.labelSystemFilter.setOpenExternalLinks(True)
        self.labelSystemFilter.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.gridLayoutSystemUserFilters.addWidget(self.labelSystemFilter, 2, 0, 1, 3)

        self.textEditSystemExclude = CustomTextEdit(self.scrollAreaWidgetContentsSystemUserFilters)
        self.textEditSystemExclude.setObjectName(u"textEditSystemExclude")
        sizePolicy.setHeightForWidth(self.textEditSystemExclude.sizePolicy().hasHeightForWidth())
        self.textEditSystemExclude.setSizePolicy(sizePolicy)
        self.textEditSystemExclude.setMinimumSize(QSize(0, 100))
        self.textEditSystemExclude.setMaximumSize(QSize(16777215, 16777215))
        self.textEditSystemExclude.setTabChangesFocus(True)
        self.textEditSystemExclude.setAcceptRichText(False)

        self.gridLayoutSystemUserFilters.addWidget(self.textEditSystemExclude, 5, 2, 1, 1)

        self.scrollAreaSystemUserFilters.setWidget(self.scrollAreaWidgetContentsSystemUserFilters)

        self.verticalLayout_4.addWidget(self.scrollAreaSystemUserFilters)

        self.tabWidgetSystemSettings.addTab(self.tabSystemUserFilters, "")

        self.gridLayout_3.addWidget(self.tabWidgetSystemSettings, 1, 0, 1, 1)

        self.tabWidgetSettings.addTab(self.tabSystemSettings, "")

        self.gridLayoutRight.addWidget(self.tabWidgetSettings, 3, 0, 1, 2)

        self.labelSettingsSaved = QLabel(self.gridLayoutRight_2)
        self.labelSettingsSaved.setObjectName(u"labelSettingsSaved")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.labelSettingsSaved.setPalette(palette20)
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(9)
        self.labelSettingsSaved.setFont(font8)
        self.labelSettingsSaved.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayoutRight.addWidget(self.labelSettingsSaved, 1, 1, 1, 1)

        self.labelChooseYourSettings = QLabel(self.gridLayoutRight_2)
        self.labelChooseYourSettings.setObjectName(u"labelChooseYourSettings")
        self.labelChooseYourSettings.setFont(font3)

        self.gridLayoutRight.addWidget(self.labelChooseYourSettings, 1, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutRight_2)

        self.gridLayout.addWidget(self.splitter, 2, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frameProcessDatFile = QFrame(self.centralwidget)
        self.frameProcessDatFile.setObjectName(u"frameProcessDatFile")
        sizePolicy11.setHeightForWidth(self.frameProcessDatFile.sizePolicy().hasHeightForWidth())
        self.frameProcessDatFile.setSizePolicy(sizePolicy11)
        self.frameProcessDatFile.setMinimumSize(QSize(0, 50))
        self.frameProcessDatFile.setFrameShape(QFrame.NoFrame)
        self.frameProcessDatFile.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frameProcessDatFile)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutBottom = QWidget(self.frameProcessDatFile)
        self.horizontalLayoutBottom.setObjectName(u"horizontalLayoutBottom")
        self.horizontalLayoutOutputGo = QHBoxLayout(self.horizontalLayoutBottom)
        self.horizontalLayoutOutputGo.setObjectName(u"horizontalLayoutOutputGo")
        self.horizontalLayoutOutputGo.setContentsMargins(0, 0, 9, 0)
        self.mainProgram = QFrame(self.horizontalLayoutBottom)
        self.mainProgram.setObjectName(u"mainProgram")
        sizePolicy.setHeightForWidth(self.mainProgram.sizePolicy().hasHeightForWidth())
        self.mainProgram.setSizePolicy(sizePolicy)
        self.mainProgram.setFrameShape(QFrame.NoFrame)
        self.mainProgram.setFrameShadow(QFrame.Plain)
        self.mainProgram.setLineWidth(0)
        self.labelSelectOutput = QLabel(self.mainProgram)
        self.labelSelectOutput.setObjectName(u"labelSelectOutput")
        self.labelSelectOutput.setGeometry(QRect(60, 10, 251, 20))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(8)
        font9.setBold(True)
        self.labelSelectOutput.setFont(font9)
        self.lineSelectOutputSeparator = QFrame(self.mainProgram)
        self.lineSelectOutputSeparator.setObjectName(u"lineSelectOutputSeparator")
        self.lineSelectOutputSeparator.setGeometry(QRect(0, -5, 321, 16))
        palette21 = QPalette()
        brush11 = QBrush(QColor(153, 153, 153, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lineSelectOutputSeparator.setPalette(palette21)
        self.lineSelectOutputSeparator.setFrameShadow(QFrame.Plain)
        self.lineSelectOutputSeparator.setFrameShape(QFrame.HLine)
        self.buttonChooseOutput = QPushButton(self.mainProgram)
        self.buttonChooseOutput.setObjectName(u"buttonChooseOutput")
        self.buttonChooseOutput.setGeometry(QRect(4, 10, 44, 40))
        self.buttonChooseOutput.setFont(font1)
        self.buttonChooseOutput.setIcon(icon13)
        self.buttonChooseOutput.setIconSize(QSize(32, 32))
        self.labelOutputFolder = ElisionLabel(self.mainProgram)
        self.labelOutputFolder.setObjectName(u"labelOutputFolder")
        self.labelOutputFolder.setGeometry(QRect(60, 31, 251, 20))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.labelOutputFolder.setPalette(palette22)
        self.labelOutputFolder.setFont(font2)

        self.horizontalLayoutOutputGo.addWidget(self.mainProgram)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutOutputGo.addItem(self.horizontalSpacer)

        self.buttonGo = CustomPushButton(self.horizontalLayoutBottom)
        self.buttonGo.setObjectName(u"buttonGo")
        sizePolicy6.setHeightForWidth(self.buttonGo.sizePolicy().hasHeightForWidth())
        self.buttonGo.setSizePolicy(sizePolicy6)
        self.buttonGo.setMinimumSize(QSize(130, 41))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(10)
        font10.setBold(False)
        self.buttonGo.setFont(font10)

        self.horizontalLayoutOutputGo.addWidget(self.buttonGo)


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
        self.buttonAddDats.setToolTip(QCoreApplication.translate("MainWindow", u"Add DAT files to the list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddDats.setText("")
#if QT_CONFIG(tooltip)
        self.buttonAddFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Add a folder of DAT files to the list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddFolder.setText("")
#if QT_CONFIG(tooltip)
        self.buttonAddFolderRecursive.setToolTip(QCoreApplication.translate("MainWindow", u"Add a folder of DAT files recursively to the list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAddFolderRecursive.setText("")
#if QT_CONFIG(tooltip)
        self.buttonDeleteDats.setToolTip(QCoreApplication.translate("MainWindow", u"Remove selected DAT files from the list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonDeleteDats.setText("")
#if QT_CONFIG(tooltip)
        self.buttonClearDats.setToolTip(QCoreApplication.translate("MainWindow", u"Remove all DAT files from the list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClearDats.setText("")

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
        self.labelGlobalSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
        self.labelGlobalAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionDown.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalRegionAllLeft.setText("")
        self.labelGlobalFilterByRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalLanguageDown.setText("")
        self.labelGlobalAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelGlobalSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
        self.labelGlobalFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalVideoStandardDown.setText("")
        self.labelGlobalVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
        self.labelGlobalFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalVideo), QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Pirate)\" in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePirate.setText(QCoreApplication.translate("MainWindow", u"Pirate", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\"\n"
"\n"
"These might be used as soundtracks by games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\"\n"
"\n"
"These could be anything other than the main title content, like\n"
"patches, manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Manual)\" in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeManuals.setText(QCoreApplication.translate("MainWindow", u"Manuals", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Multimedia\"\n"
"\n"
"These might include games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMultimedia.setText(QCoreApplication.translate("MainWindow", u"Multimedia", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setToolTip(QCoreApplication.translate("MainWindow", u"Titles or ROMs declared as missing in action in the clone lists or DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeMIA.setText(QCoreApplication.translate("MainWindow", u"MIA", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles unauthorized by console manufacturers, marked by the\n"
"following text in the name:\n"
"\n"
"\u2022 (Unl)\n"
"\u2022 (Aftermarket)\n"
"\u2022 (Homebrew)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Unlicensed", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeVideo.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Video\"", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeVideo.setText(QCoreApplication.translate("MainWindow", u"Video", None))
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
        self.checkBoxGlobalExcludeDemos.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Demos\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 @barai\n"
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
        self.checkBoxGlobalExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\"\n"
"\n"
"These were discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePreproduction.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Preproduction\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Alpha [0-99])\n"
"\u2022 (Beta [0-99])\n"
"\u2022 (Pre-Production)\n"
"\u2022 (Possible Proto)\n"
"\u2022 (Proto [0-99])\n"
"\u2022 (Review Code)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludePreproduction.setText(QCoreApplication.translate("MainWindow", u"Preproduction", None))
        self.labelGlobalExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles from the output DAT", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\"", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types", None))
#endif // QT_CONFIG(tooltip)
        self.buttonGlobalDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
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
        self.checkBoxGlobalOptionsIncludeHashless.setToolTip(QCoreApplication.translate("MainWindow", u"Some DAT files don't list any hashes or sizes for some files, and Retool\n"
"filters these out by default. This option makes sure those files are kept.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsIncludeHashless.setText(QCoreApplication.translate("MainWindow", u"Include titles without hashes or sizes specified in the input DAT file", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPreferRegions.setToolTip(QCoreApplication.translate("MainWindow", u"By default, if a title from a higher priority region doesn't support\n"
"your preferred languages but a lower priority region does, Retool\n"
"selects the latter. This option disables this behavior, forcing\n"
"strict adherence to region priority regardless of language support.\n"
"\n"
"This option also overrides similar behavior in superset selection,\n"
"which means you might get a title that was released in your\n"
"preferred region that has less content, instead of one that was\n"
"released in another region that contains more content and supports\n"
"your preferred languages.", None))
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
        self.checkBoxGlobalOptionsDemoteUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Sometimes games are rereleased long after the lifespan of a console,\n"
"in regions they weren't originally available in. By default Retool\n"
"selects these titles if they match your preferred region/language\n"
"priorities.\n"
"\n"
"Enable this option to choose a production version of a title over\n"
"the unlicensed/aftermarket/homebrew title if possible. This might\n"
"select titles from a lower priority region, or with lower priority\n"
"languages, or with less features.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDemoteUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Prefer licensed versions over unlicensed, aftermarket, or homebrew titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableFilters.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore both global and system user filters", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableFilters.setText(QCoreApplication.translate("MainWindow", u"Disable global and system user filters", None))
        self.labelGlobalOptionsOutput.setText(QCoreApplication.translate("MainWindow", u"Output options", None))
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
"DAT file containing the titles Retool removed", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsRemovesDat.setText(QCoreApplication.translate("MainWindow", u"Also output a DAT file of all the removed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsKeepRemove.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file\n"
"that lists what titles have been kept, and what\n"
"titles have been removed", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsKeepRemove.setText(QCoreApplication.translate("MainWindow", u"Also output lists of what titles have been kept and removed", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptions1G1RNames.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file that lists only\n"
"the name of each title in the output DAT file, and optionally add a prefix\n"
"and suffix to each name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptions1G1RNames.setText(QCoreApplication.translate("MainWindow", u"Also output a list of just the title names from the output DAT file", None))
        self.labelGlobalOptions1G1RPrefix.setText(QCoreApplication.translate("MainWindow", u"Add text to the start of each title (start with http://, https//, or ftp:// to URL encode)", None))
        self.labelGlobalOptions1G1RSuffix.setText(QCoreApplication.translate("MainWindow", u"Add text to the end of each title", None))
        self.labelGlobalOptionsDebug.setText(QCoreApplication.translate("MainWindow", u"Debug options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsReportWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Turn on warnings when there are mismatches\n"
"between the clone list and the DAT file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsReportWarnings.setText(QCoreApplication.translate("MainWindow", u"Report clone list warnings during processing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPauseWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Pause Retool each time a clone list warning is issued", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsPauseWarnings.setText(QCoreApplication.translate("MainWindow", u"Pause on clone list warnings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsLegacy.setToolTip(QCoreApplication.translate("MainWindow", u"Not recommended unless you're debugging or comparing outputs between\n"
"DAT file versions.\n"
"\n"
"If this is disabled, it's because you've disabled 1G1R filtering or\n"
"chosen to split by region, which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsLegacy.setText(QCoreApplication.translate("MainWindow", u"Output DAT file in legacy parent/clone format", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsBypassDTD.setToolTip(QCoreApplication.translate("MainWindow", u"Skips DTD validation of DAT files, useful if validation is causing issues", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsBypassDTD.setText(QCoreApplication.translate("MainWindow", u"Bypass DTD validation", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableMultiCPU.setToolTip(QCoreApplication.translate("MainWindow", u"Forces Retool to use only a single CPU\n"
"core, at the cost of performance", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsDisableMultiCPU.setText(QCoreApplication.translate("MainWindow", u"Disable multiprocessor usage", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsTrace.setToolTip(QCoreApplication.translate("MainWindow", u"Follows a title through Retool's selection process for debugging", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGlobalOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Trace a title through Retool's process (no DAT files are created)", None))
        self.labelGlobalOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Enter a regex string to trace (case insensitive)", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.labelGlobalFilterExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.labelGlobalFilter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exclude or include specific titles by adding your own text strings to match against. Each string should be on its own line, and is case sensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui/#user-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also remove any match's related clones.</p></body></html>", None))
        self.labelGlobalFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter by text", None))
        self.labelGlobalFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.tabWidgetGlobalSettings.setTabText(self.tabWidgetGlobalSettings.indexOf(self.tabGlobalUserFilters), QCoreApplication.translate("MainWindow", u"User filters", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabGlobalSettings), QCoreApplication.translate("MainWindow", u"Global settings", None))
        self.labelSystemSettings.setText(QCoreApplication.translate("MainWindow", u"Add a DAT file, then select it in the list to enable system-specific settings.", None))
        self.labelSelectSystemCloneList.setText(QCoreApplication.translate("MainWindow", u"Select a custom clone list", None))
#if QT_CONFIG(tooltip)
        self.buttonChooseSystemMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom metadata file", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseSystemMetadataFile.setText("")
#if QT_CONFIG(tooltip)
        self.buttonClearSystemCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Use default clone list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClearSystemCloneList.setText("")
#if QT_CONFIG(tooltip)
        self.buttonChooseSystemOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseSystemOutput.setText("")
#if QT_CONFIG(tooltip)
        self.buttonClearSystemOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Use global output folder", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClearSystemOutput.setText("")
        self.labelSelectSystemMetadataFile.setText(QCoreApplication.translate("MainWindow", u"Select a custom metadata file", None))
#if QT_CONFIG(tooltip)
        self.buttonClearSystemMetadataFile.setToolTip(QCoreApplication.translate("MainWindow", u"Use default metadata file", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClearSystemMetadataFile.setText("")
        self.labelSystemCustomFilesAndFolders.setText(QCoreApplication.translate("MainWindow", u"Custom files and folders to use when processing this DAT", None))
        self.checkBoxSystemOverridePaths.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSelectSystemOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder", None))
        self.labelSystemMetadataFile.setText(QCoreApplication.translate("MainWindow", u"No custom metadata file selected, using default metadata file location", None))
#if QT_CONFIG(tooltip)
        self.buttonChooseSystemCloneList.setToolTip(QCoreApplication.translate("MainWindow", u"Choose a custom clone list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseSystemCloneList.setText("")
        self.labelSystemCloneList.setText(QCoreApplication.translate("MainWindow", u"No custom clone list selected, using default clone list location", None))
        self.labelSystemOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected, using global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemPaths), QCoreApplication.translate("MainWindow", u"Paths", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionDown.setText("")
        self.labelSystemSelectedRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by this region order", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemRegionAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemRegionAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Set a region order that prioritizes\n"
"English-speaking regions and 60Hz titles", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDefaultRegionOrder.setText(QCoreApplication.translate("MainWindow", u"Use default order for English speakers", None))
        self.labelSystemAvailableRegions.setText(QCoreApplication.translate("MainWindow", u"Available regions", None))
        self.labelSystemFilterByRegions.setText(QCoreApplication.translate("MainWindow", u"Filter by regions (you must add at least one)", None))
        self.checkBoxSystemOverrideRegions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemRegions), QCoreApplication.translate("MainWindow", u"Regions", None))
        self.labelSystemFilterByLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by languages (an empty filter list includes all languages)", None))
        self.checkBoxSystemOverrideLanguages.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the remaining available regions to the end of the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the filter list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageRight.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setToolTip(QCoreApplication.translate("MainWindow", u"Move all regions in the filter list to the available list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageAllLeft.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemLanguageDown.setText("")
        self.labelSystemAvailableLanguages.setText(QCoreApplication.translate("MainWindow", u"Available languages", None))
        self.labelSystemSelectedLanguages.setText(QCoreApplication.translate("MainWindow", u"Filter by this language order", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemLanguages), QCoreApplication.translate("MainWindow", u"Languages", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions up in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardUp.setText("")
#if QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setToolTip(QCoreApplication.translate("MainWindow", u"Move the selected regions down in priority", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemVideoStandardDown.setText("")
        self.labelSystemFilterByVideo.setText(QCoreApplication.translate("MainWindow", u"Set a video priority for titles with a video tag in their name", None))
        self.checkBoxSystemOverrideVideo.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
        self.labelSystemVideoStandardsOrder.setText(QCoreApplication.translate("MainWindow", u"Video order", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemVideo), QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeEducational.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Educational\"", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeEducational.setText(QCoreApplication.translate("MainWindow", u"Educational", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemSelectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Select all title types", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemSelectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
#if QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setToolTip(QCoreApplication.translate("MainWindow", u"Deselect all title types", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSystemDeselectAllExclude.setText(QCoreApplication.translate("MainWindow", u"Deselect all", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles marked as bad dumps with a [b] in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBadDumps.setText(QCoreApplication.translate("MainWindow", u"Bad dumps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePreproduction.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Preproduction\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Alpha [0-99])\n"
"\u2022 (Beta [0-99])\n"
"\u2022 (Pre-Production)\n"
"\u2022 (Possible Proto)\n"
"\u2022 (Proto [0-99])\n"
"\u2022 (Review Code)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePreproduction.setText(QCoreApplication.translate("MainWindow", u"Preproduction", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Coverdiscs\"\n"
"\n"
"These were discs that were attached to the front of magazines, and\n"
"could contain demos, or rarely, full games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeCoverdiscs.setText(QCoreApplication.translate("MainWindow", u"Coverdiscs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Bonus Discs\"\n"
"\n"
"These could be anything other than the main title content, like\n"
"patches, manuals, collector discs, or otherwise", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBonusDiscs.setText(QCoreApplication.translate("MainWindow", u"Bonus discs", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeVideo.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Video\"", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeVideo.setText(QCoreApplication.translate("MainWindow", u"Video", None))
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
        self.checkBoxSystemExcludeMultimedia.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Multimedia\"\n"
"\n"
"These might include games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMultimedia.setText(QCoreApplication.translate("MainWindow", u"Multimedia", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeDemos.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Demos\" or with the following\n"
"text in the name:\n"
"\n"
"\u2022 @barai\n"
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
        self.checkBoxSystemExcludePromotional.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Promotional\" or with the\n"
"following text in the name:\n"
"\n"
"\u2022 (Promo)\n"
"\u2022 EPK\n"
"\u2022 Press Kit", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePromotional.setText(QCoreApplication.translate("MainWindow", u"Promotional", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Console\" or with the following text\n"
"in the name:\n"
"\n"
"\u2022 [BIOS]\n"
"\u2022 (Enhancement Chip)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeBIOS.setText(QCoreApplication.translate("MainWindow", u"BIOS and other chips", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMIA.setToolTip(QCoreApplication.translate("MainWindow", u"Titles or ROMs declared as missing in action in the clone lists or DAT files.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeMIA.setText(QCoreApplication.translate("MainWindow", u"MIA", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles unauthorized by console manufacturers, marked by the\n"
"following text in the name:\n"
"\n"
"\u2022 (Unl)\n"
"\u2022 (Aftermarket)\n"
"\u2022 (Homebrew)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Unlicensed", None))
        self.labelGlobalExclude_2.setText(QCoreApplication.translate("MainWindow", u"Exclude these types of titles from the output DAT", None))
        self.checkBoxSystemOverrideExclusions.setText(QCoreApplication.translate("MainWindow", u"Override global settings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePirate.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Pirate)\" in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludePirate.setText(QCoreApplication.translate("MainWindow", u"Pirate", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAudio.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Audio\"\n"
"\n"
"These might be used as soundtracks by games", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAudio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeManuals.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with \"(Manual)\" in the name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeManuals.setText(QCoreApplication.translate("MainWindow", u"Manuals", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setToolTip(QCoreApplication.translate("MainWindow", u"Exclude titles with the DAT category \"Add-Ons\", which includes\n"
"expansion packs and additional materials for titles", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemExcludeAddOns.setText(QCoreApplication.translate("MainWindow", u"Add-ons", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemExclusions), QCoreApplication.translate("MainWindow", u"Exclusions", None))
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
        self.checkBoxSystemOptionsIncludeHashless.setToolTip(QCoreApplication.translate("MainWindow", u"Some DAT files don't list any hashes or sizes for some files, and Retool\n"
"filters these out by default. This option makes sure those files are kept.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsIncludeHashless.setText(QCoreApplication.translate("MainWindow", u"Include titles without hashes or sizes specified in the input DAT file", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPreferRegions.setToolTip(QCoreApplication.translate("MainWindow", u"By default, if a title from a higher priority region doesn't support\n"
"your preferred languages but a lower priority region does, Retool\n"
"selects the latter. This option disables this behavior, forcing\n"
"strict adherence to region priority regardless of language support.\n"
"\n"
"This option also overrides similar behavior in superset selection,\n"
"which means you might get a title that was released in your\n"
"preferred region that has less content, instead of one that was\n"
"released in another region that contains more content and supports\n"
"your preferred languages.", None))
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
        self.checkBoxSystemOptionsDemoteUnlicensed.setToolTip(QCoreApplication.translate("MainWindow", u"Sometimes games are rereleased long after the lifespan of a console,\n"
"in regions they weren't originally available in. By default Retool\n"
"selects these titles if they match your preferred region/language\n"
"priorities.\n"
"\n"
"Enable this option to choose a production version of a title over\n"
"the unlicensed/aftermarket/homebrew title if possible. This might\n"
"select titles from a lower priority region, or with lower priority\n"
"languages, or with less features.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDemoteUnlicensed.setText(QCoreApplication.translate("MainWindow", u"Prefer licensed versions over unlicensed, aftermarket, or homebrew titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableFilters.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore both global and system user filters", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableFilters.setText(QCoreApplication.translate("MainWindow", u"Disable global and system user filters", None))
        self.labelSystemOptionsOutput.setText(QCoreApplication.translate("MainWindow", u"Output options", None))
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
"DAT file containing the titles Retool removed", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsRemovesDat.setText(QCoreApplication.translate("MainWindow", u"Also output a DAT file of all the removed titles", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsKeepRemove.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file\n"
"that lists what titles have been kept, and what\n"
"titles have been removed", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsKeepRemove.setText(QCoreApplication.translate("MainWindow", u"Also output lists of what titles have been kept and removed", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptions1G1RNames.setToolTip(QCoreApplication.translate("MainWindow", u"In addition to the output DAT file, produce a TXT file that lists only\n"
"the name of each title in the output DAT file, and optionally add a prefix\n"
"and suffix to each name", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptions1G1RNames.setText(QCoreApplication.translate("MainWindow", u"Also output a list of just the title names from the output DAT file", None))
        self.labelSystemOptions1G1RPrefix.setText(QCoreApplication.translate("MainWindow", u"Add text to the start of each title (start with http://, https//, or ftp:// to URL encode)", None))
        self.labelSystemOptions1G1RSuffix.setText(QCoreApplication.translate("MainWindow", u"Add text to the end of each title", None))
        self.labelSystemOptionsDebug.setText(QCoreApplication.translate("MainWindow", u"Debug options", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsReportWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Turn on warnings when there are mismatches\n"
"between the clone list and the DAT file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsReportWarnings.setText(QCoreApplication.translate("MainWindow", u"Report clone list warnings during processing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPauseWarnings.setToolTip(QCoreApplication.translate("MainWindow", u"Pause Retool each time a clone list warning is issued", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsPauseWarnings.setText(QCoreApplication.translate("MainWindow", u"Pause on clone list warnings", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsLegacy.setToolTip(QCoreApplication.translate("MainWindow", u"Not recommended unless you're debugging or comparing outputs between\n"
"DAT file versions.\n"
"\n"
"If this is disabled, it's because you've disabled 1G1R filtering or\n"
"chosen to split by region, which isn't compatible with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsLegacy.setText(QCoreApplication.translate("MainWindow", u"Output DAT file in legacy parent/clone format", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsBypassDTD.setToolTip(QCoreApplication.translate("MainWindow", u"Skips DTD validation of DAT files, useful if validation is causing issues", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsBypassDTD.setText(QCoreApplication.translate("MainWindow", u"Bypass DTD validation", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableMultiCPU.setToolTip(QCoreApplication.translate("MainWindow", u"Forces Retool to use only a single CPU\n"
"core, at the cost of performance", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsDisableMultiCPU.setText(QCoreApplication.translate("MainWindow", u"Disable multiprocessor usage", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsTrace.setToolTip(QCoreApplication.translate("MainWindow", u"Follows a title through Retool's selection process for debugging", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSystemOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Trace a title through Retool's process (no DAT files are created)", None))
        self.labelSystemOptionsTrace.setText(QCoreApplication.translate("MainWindow", u"Enter a regex string to trace (case insensitive)", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.labelSystemFilterInclude.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.labelSystemFilterExclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.labelSystemFilterByText.setText(QCoreApplication.translate("MainWindow", u"Filter by text", None))
        self.labelSystemFilter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exclude or include specific titles by adding your own text strings to match against. Each string should be on its own line, and is case sensitive. See the <a href=\"https://unexpectedpanda.github.io/retool/how-to-use-retool-gui/#user-filters\"><span style=\" text-decoration: underline; color:#0000ff;\">documentation</span></a> for more information.<br/><br/>\u2022 Plain text indicates a partial string match.<br/>\u2022 A prefix of / indicates a regular expression match.<br/>\u2022 A prefix of | indicates a full string match.<br/>\u2022 Additionally, wrap a string in &lt;&gt; to also remove any match's related clones.</p></body></html>", None))
        self.tabWidgetSystemSettings.setTabText(self.tabWidgetSystemSettings.indexOf(self.tabSystemUserFilters), QCoreApplication.translate("MainWindow", u"User filters", None))
        self.tabWidgetSettings.setTabText(self.tabWidgetSettings.indexOf(self.tabSystemSettings), QCoreApplication.translate("MainWindow", u"System settings", None))
        self.labelSettingsSaved.setText(QCoreApplication.translate("MainWindow", u"Settings are saved automatically", None))
        self.labelChooseYourSettings.setText(QCoreApplication.translate("MainWindow", u"Choose your settings", None))
        self.labelSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Select an output folder for the filtered DATs", None))
#if QT_CONFIG(tooltip)
        self.buttonChooseOutput.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an output folder", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseOutput.setText("")
        self.labelOutputFolder.setText(QCoreApplication.translate("MainWindow", u"No output folder selected", None))
        self.buttonGo.setText(QCoreApplication.translate("MainWindow", u"Process DAT files", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

