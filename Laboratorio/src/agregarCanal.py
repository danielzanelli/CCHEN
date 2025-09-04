# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarCanal.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_AgregarCanal(object):
    def setupUi(self, AgregarCanal):
        if not AgregarCanal.objectName():
            AgregarCanal.setObjectName(u"AgregarCanal")
        AgregarCanal.resize(380, 331)
        self.cancelar = QPushButton(AgregarCanal)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(240, 270, 83, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.agregar = QPushButton(AgregarCanal)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(60, 270, 83, 29))
        self.agregar.setFont(font)
        self.label = QLabel(AgregarCanal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 130, 151, 20))
        self.osciloscopio = QComboBox(AgregarCanal)
        self.osciloscopio.setObjectName(u"osciloscopio")
        self.osciloscopio.setGeometry(QRect(210, 130, 121, 21))
        self.label_2 = QLabel(AgregarCanal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 90, 151, 20))
        self.label_3 = QLabel(AgregarCanal)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 170, 151, 20))
        self.canal = QComboBox(AgregarCanal)
        self.canal.setObjectName(u"canal")
        self.canal.setGeometry(QRect(210, 170, 121, 21))
        self.label_91 = QLabel(AgregarCanal)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(30, 20, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nombre_variable = QLineEdit(AgregarCanal)
        self.nombre_variable.setObjectName(u"nombre_variable")
        self.nombre_variable.setGeometry(QRect(210, 90, 121, 21))
        self.label_4 = QLabel(AgregarCanal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 210, 151, 20))
        self.datapoints = QSpinBox(AgregarCanal)
        self.datapoints.setObjectName(u"datapoints")
        self.datapoints.setGeometry(QRect(210, 210, 121, 21))
        self.datapoints.setMinimum(10)
        self.datapoints.setMaximum(20000)
        self.datapoints.setSingleStep(1000)
        self.datapoints.setValue(10000)

        self.retranslateUi(AgregarCanal)

        QMetaObject.connectSlotsByName(AgregarCanal)
    # setupUi

    def retranslateUi(self, AgregarCanal):
        AgregarCanal.setWindowTitle(QCoreApplication.translate("AgregarCanal", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("AgregarCanal", u"Cancelar", None))
        self.agregar.setText(QCoreApplication.translate("AgregarCanal", u"Agregar", None))
        self.label.setText(QCoreApplication.translate("AgregarCanal", u"Osciloscopio", None))
        self.label_2.setText(QCoreApplication.translate("AgregarCanal", u"Nombre Curva", None))
        self.label_3.setText(QCoreApplication.translate("AgregarCanal", u"Canal", None))
        self.label_91.setText(QCoreApplication.translate("AgregarCanal", u"Agregar Nuevo Canal", None))
        self.nombre_variable.setText("")
        self.label_4.setText(QCoreApplication.translate("AgregarCanal", u"Datapoints", None))
    # retranslateUi

