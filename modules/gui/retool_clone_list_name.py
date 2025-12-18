# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool-clone-list-name.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from modules.gui.gui_widgets import CustomLineEdit
from . import resources_rc

class Ui_CloneListNameTool(object):
    def setupUi(self, CloneListNameTool):
        if not CloneListNameTool.objectName():
            CloneListNameTool.setObjectName(u"CloneListNameTool")
        CloneListNameTool.resize(680, 370)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CloneListNameTool.sizePolicy().hasHeightForWidth())
        CloneListNameTool.setSizePolicy(sizePolicy)
        CloneListNameTool.setMinimumSize(QSize(680, 370))
        CloneListNameTool.setMaximumSize(QSize(680, 370))
        font = QFont()
        CloneListNameTool.setFont(font)
        icon = QIcon()
        icon.addFile(u":/retoolIcon/images/retool.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        CloneListNameTool.setWindowIcon(icon)
        CloneListNameTool.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(CloneListNameTool)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, -1)
        self.labelContribute = QLabel(self.centralwidget)
        self.labelContribute.setObjectName(u"labelContribute")
        sizePolicy1.setHeightForWidth(self.labelContribute.sizePolicy().hasHeightForWidth())
        self.labelContribute.setSizePolicy(sizePolicy1)
        self.labelContribute.setMinimumSize(QSize(0, 36))
        self.labelContribute.setMaximumSize(QSize(16777215, 16777215))
        self.labelContribute.setFont(font)
        self.labelContribute.setLineWidth(0)
        self.labelContribute.setScaledContents(False)
        self.labelContribute.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelContribute.setWordWrap(True)
        self.labelContribute.setOpenExternalLinks(True)
        self.labelContribute.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.labelContribute)

        self.verticalSpacer_5 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.labelEnterName = QLabel(self.centralwidget)
        self.labelEnterName.setObjectName(u"labelEnterName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelEnterName.sizePolicy().hasHeightForWidth())
        self.labelEnterName.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        self.labelEnterName.setFont(font1)

        self.verticalLayout.addWidget(self.labelEnterName)

        self.lineEditEnterName = CustomLineEdit(self.centralwidget)
        self.lineEditEnterName.setObjectName(u"lineEditEnterName")
        self.lineEditEnterName.setMinimumSize(QSize(320, 24))

        self.verticalLayout.addWidget(self.lineEditEnterName)

        self.checkBoxDemos = QCheckBox(self.centralwidget)
        self.checkBoxDemos.setObjectName(u"checkBoxDemos")

        self.verticalLayout.addWidget(self.checkBoxDemos)

        self.verticalSpacer = QSpacerItem(13, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelShortName = QLabel(self.centralwidget)
        self.labelShortName.setObjectName(u"labelShortName")
        sizePolicy2.setHeightForWidth(self.labelShortName.sizePolicy().hasHeightForWidth())
        self.labelShortName.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(False)
        self.labelShortName.setFont(font2)

        self.verticalLayout.addWidget(self.labelShortName)

        self.lineEditShortName = QLineEdit(self.centralwidget)
        self.lineEditShortName.setObjectName(u"lineEditShortName")
        self.lineEditShortName.setMinimumSize(QSize(320, 24))
        palette = QPalette()
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        self.lineEditShortName.setPalette(palette)
        self.lineEditShortName.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEditShortName.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditShortName)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.labelGroupName = QLabel(self.centralwidget)
        self.labelGroupName.setObjectName(u"labelGroupName")
        sizePolicy2.setHeightForWidth(self.labelGroupName.sizePolicy().hasHeightForWidth())
        self.labelGroupName.setSizePolicy(sizePolicy2)
        self.labelGroupName.setFont(font2)

        self.verticalLayout.addWidget(self.labelGroupName)

        self.lineEditGroupName = QLineEdit(self.centralwidget)
        self.lineEditGroupName.setObjectName(u"lineEditGroupName")
        self.lineEditGroupName.setMinimumSize(QSize(320, 24))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        self.lineEditGroupName.setPalette(palette1)
        self.lineEditGroupName.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditGroupName)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.labelRegionFreeName = QLabel(self.centralwidget)
        self.labelRegionFreeName.setObjectName(u"labelRegionFreeName")
        sizePolicy2.setHeightForWidth(self.labelRegionFreeName.sizePolicy().hasHeightForWidth())
        self.labelRegionFreeName.setSizePolicy(sizePolicy2)
        self.labelRegionFreeName.setFont(font2)

        self.verticalLayout.addWidget(self.labelRegionFreeName)

        self.lineEditRegionFreeName = QLineEdit(self.centralwidget)
        self.lineEditRegionFreeName.setObjectName(u"lineEditRegionFreeName")
        self.lineEditRegionFreeName.setMinimumSize(QSize(320, 24))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        self.lineEditRegionFreeName.setPalette(palette2)
        self.lineEditRegionFreeName.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEditRegionFreeName)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        CloneListNameTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(CloneListNameTool)

        QMetaObject.connectSlotsByName(CloneListNameTool)
    # setupUi

    def retranslateUi(self, CloneListNameTool):
        CloneListNameTool.setWindowTitle(QCoreApplication.translate("CloneListNameTool", u"Title tool", None))
        self.labelContribute.setText(QCoreApplication.translate("CloneListNameTool", u"<html><head/><body><p>This tool is useful for contributing to Retool's clone lists or development. If you enter a title's full name, it shows you the other names Retool assigns to it by default as part of its matching process. <a href=\"https://unexpectedpanda.github.io/retool/naming-system/\"><span style=\" text-decoration: underline; color:#0000ff;\">Read the documentation</span></a> to learn more.</p></body></html>", None))
        self.labelEnterName.setText(QCoreApplication.translate("CloneListNameTool", u"Enter the full name as it appears in the DAT file", None))
        self.checkBoxDemos.setText(QCoreApplication.translate("CloneListNameTool", u"Title has a category of Demos in the DAT file, but is missing demo tags in the filename", None))
        self.labelShortName.setText(QCoreApplication.translate("CloneListNameTool", u"Default short name", None))
        self.lineEditShortName.setText("")
        self.labelGroupName.setText(QCoreApplication.translate("CloneListNameTool", u"Default group name", None))
        self.labelRegionFreeName.setText(QCoreApplication.translate("CloneListNameTool", u"Region-free name", None))
    # retranslateUi

