# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool-about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)
from  . import resources_rc

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.setWindowModality(Qt.NonModal)
        AboutWindow.setEnabled(True)
        AboutWindow.resize(362, 322)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QSize(362, 322))
        AboutWindow.setMaximumSize(QSize(362, 322))
        AboutWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/retoolIcon/images/retool.ico", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        AboutWindow.setModal(True)
        self.labelName = QLabel(AboutWindow)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(70, 172, 221, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.labelName.setFont(font)
        self.labelName.setTextFormat(Qt.RichText)
        self.labelName.setScaledContents(False)
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelName.setOpenExternalLinks(True)
        self.labelName.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)
        self.labelGUIVersion = QLabel(AboutWindow)
        self.labelGUIVersion.setObjectName(u"labelGUIVersion")
        self.labelGUIVersion.setGeometry(QRect(105, 222, 151, 20))
        self.labelGUIVersion.setFont(font)
        self.labelGUIVersion.setAlignment(Qt.AlignCenter)
        self.labelCLIVersion = QLabel(AboutWindow)
        self.labelCLIVersion.setObjectName(u"labelCLIVersion")
        self.labelCLIVersion.setGeometry(QRect(105, 242, 151, 20))
        self.labelCLIVersion.setFont(font)
        self.labelCLIVersion.setAlignment(Qt.AlignCenter)
        self.aboutLogo = QLabel(AboutWindow)
        self.aboutLogo.setObjectName(u"aboutLogo")
        self.aboutLogo.setGeometry(QRect(105, 15, 151, 151))
        self.aboutLogo.setPixmap(QPixmap(u":/retoolAbout/images/retool-about.png"))
        self.aboutLogo.setScaledContents(True)
        self.aboutLogo.setAlignment(Qt.AlignCenter)
        self.labelCreditIcons8 = QLabel(AboutWindow)
        self.labelCreditIcons8.setObjectName(u"labelCreditIcons8")
        self.labelCreditIcons8.setGeometry(QRect(89, 280, 181, 20))
        self.labelCreditIcons8.setFont(font)
        self.labelCreditIcons8.setTextFormat(Qt.RichText)
        self.labelCreditIcons8.setAlignment(Qt.AlignCenter)
        self.labelCreditIcons8.setOpenExternalLinks(True)
        self.labelCreditIcons8.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About Retool", None))
        self.labelName.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Retool<br/></span><a href=\"https://unexpectedpanda.github.io/retool\"><span style=\" text-decoration: underline; color:#0000ff;\">https://unexpectedpanda.github.io/retool</span></a></p></body></html>", None))
        self.labelGUIVersion.setText(QCoreApplication.translate("AboutWindow", u"Retool GUI version:", None))
        self.labelCLIVersion.setText(QCoreApplication.translate("AboutWindow", u"Retool CLI version:", None))
        self.aboutLogo.setText("")
        self.labelCreditIcons8.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>Some icons provided by <a href=\"https://icons8.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Icons8</span></a></p></body></html>", None))
    # retranslateUi

