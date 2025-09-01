# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subirBd.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Subir(object):
    def setupUi(self, Subir):
        if not Subir.objectName():
            Subir.setObjectName(u"Subir")
        Subir.resize(381, 249)
        self.cancelar = QPushButton(Subir)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(240, 190, 121, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.subir = QPushButton(Subir)
        self.subir.setObjectName(u"subir")
        self.subir.setGeometry(QRect(20, 190, 121, 29))
        self.subir.setFont(font)
        self.label_91 = QLabel(Subir)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(20, 30, 341, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)
        self.label = QLabel(Subir)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 321, 31))
        self.label.setFont(font)

        self.retranslateUi(Subir)

        QMetaObject.connectSlotsByName(Subir)
    # setupUi

    def retranslateUi(self, Subir):
        Subir.setWindowTitle(QCoreApplication.translate("Subir", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("Subir", u"Cancelar", None))
        self.subir.setText(QCoreApplication.translate("Subir", u"Subir", None))
        self.label_91.setText(QCoreApplication.translate("Subir", u"\u00bfSubir los datos seleccionados al servidor?", None))
        self.label.setText(QCoreApplication.translate("Subir", u"Algunos datos podrian sobreescribirse", None))
    # retranslateUi

