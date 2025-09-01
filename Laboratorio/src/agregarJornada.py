# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarJornada.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_AgregarJornada(object):
    def setupUi(self, AgregarJornada):
        if not AgregarJornada.objectName():
            AgregarJornada.setObjectName(u"AgregarJornada")
        AgregarJornada.resize(381, 344)
        self.cancelar = QPushButton(AgregarJornada)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(220, 290, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.agregar = QPushButton(AgregarJornada)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(58, 290, 101, 29))
        self.agregar.setFont(font)
        self.label = QLabel(AgregarJornada)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 150, 151, 20))
        self.experimento = QComboBox(AgregarJornada)
        self.experimento.setObjectName(u"experimento")
        self.experimento.setGeometry(QRect(210, 150, 121, 21))
        self.label_2 = QLabel(AgregarJornada)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 151, 20))
        self.label_91 = QLabel(AgregarJornada)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(30, 20, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.nombre = QLineEdit(AgregarJornada)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(210, 90, 121, 21))
        self.label_3 = QLabel(AgregarJornada)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 200, 261, 51))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.retranslateUi(AgregarJornada)

        QMetaObject.connectSlotsByName(AgregarJornada)
    # setupUi

    def retranslateUi(self, AgregarJornada):
        AgregarJornada.setWindowTitle(QCoreApplication.translate("AgregarJornada", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("AgregarJornada", u"Cancelar", None))
        self.agregar.setText(QCoreApplication.translate("AgregarJornada", u"Agregar", None))
        self.label.setText(QCoreApplication.translate("AgregarJornada", u"Experimento", None))
        self.label_2.setText(QCoreApplication.translate("AgregarJornada", u"Nombre", None))
        self.label_91.setText(QCoreApplication.translate("AgregarJornada", u"Agregar Jornada", None))
        self.nombre.setText("")
        self.label_3.setText(QCoreApplication.translate("AgregarJornada", u"Nota: Esto agregara la nueva jornada al servidor", None))
    # retranslateUi

