# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dispositivoIp.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DispositivoIp(object):
    def setupUi(self, DispositivoIp):
        if not DispositivoIp.objectName():
            DispositivoIp.setObjectName(u"DispositivoIp")
        DispositivoIp.resize(381, 213)
        self.cancelar = QPushButton(DispositivoIp)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(222, 150, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.conectar = QPushButton(DispositivoIp)
        self.conectar.setObjectName(u"conectar")
        self.conectar.setGeometry(QRect(50, 150, 101, 29))
        self.conectar.setFont(font)
        self.label_2 = QLabel(DispositivoIp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 121, 20))
        self.label_91 = QLabel(DispositivoIp)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(30, 20, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.ip = QLineEdit(DispositivoIp)
        self.ip.setObjectName(u"ip")
        self.ip.setGeometry(QRect(210, 90, 121, 21))

        self.retranslateUi(DispositivoIp)

        QMetaObject.connectSlotsByName(DispositivoIp)
    # setupUi

    def retranslateUi(self, DispositivoIp):
        DispositivoIp.setWindowTitle(QCoreApplication.translate("DispositivoIp", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("DispositivoIp", u"Cancelar", None))
        self.conectar.setText(QCoreApplication.translate("DispositivoIp", u"Conectar", None))
        self.label_2.setText(QCoreApplication.translate("DispositivoIp", u"IP", None))
        self.label_91.setText(QCoreApplication.translate("DispositivoIp", u"Conectar Osciloscopio en LAN", None))
        self.ip.setText("")
    # retranslateUi

