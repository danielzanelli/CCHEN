# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desconectarDispositivo.ui'
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

class Ui_DesconectarDispositivo(object):
    def setupUi(self, DesconectarDispositivo):
        if not DesconectarDispositivo.objectName():
            DesconectarDispositivo.setObjectName(u"DesconectarDispositivo")
        DesconectarDispositivo.resize(450, 305)
        self.cancelar = QPushButton(DesconectarDispositivo)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(272, 250, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.desconectar = QPushButton(DesconectarDispositivo)
        self.desconectar.setObjectName(u"desconectar")
        self.desconectar.setGeometry(QRect(70, 250, 111, 29))
        self.desconectar.setFont(font)
        self.dispositivo = QLabel(DesconectarDispositivo)
        self.dispositivo.setObjectName(u"dispositivo")
        self.dispositivo.setGeometry(QRect(70, 150, 311, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.dispositivo.setFont(font1)
        self.dispositivo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_91 = QLabel(DesconectarDispositivo)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(60, 40, 341, 61))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_91.setFont(font2)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)

        self.retranslateUi(DesconectarDispositivo)

        QMetaObject.connectSlotsByName(DesconectarDispositivo)
    # setupUi

    def retranslateUi(self, DesconectarDispositivo):
        DesconectarDispositivo.setWindowTitle(QCoreApplication.translate("DesconectarDispositivo", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("DesconectarDispositivo", u"Cancelar", None))
        self.desconectar.setText(QCoreApplication.translate("DesconectarDispositivo", u"Desconectar", None))
        self.dispositivo.setText("")
        self.label_91.setText(QCoreApplication.translate("DesconectarDispositivo", u"\u00bfDesconectar este dispositivo?", None))
    # retranslateUi

