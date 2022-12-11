# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool-progress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QSizePolicy, QWidget)

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(449, 93)
        ProgressBar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        ProgressBar.setModal(False)
        self.progressBar = QProgressBar(ProgressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 40, 411, 23))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)
        self.label = QLabel(ProgressBar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 19, 81, 16))
        self.label.setFont(font)

        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ProgressBar", u"Importing files", None))
    # retranslateUi

