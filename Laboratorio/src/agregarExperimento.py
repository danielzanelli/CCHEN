# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregarExperimento.ui'
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

class Ui_AgregarExperimento(object):
    def setupUi(self, AgregarExperimento):
        if not AgregarExperimento.objectName():
            AgregarExperimento.setObjectName(u"AgregarExperimento")
        AgregarExperimento.resize(353, 301)
        self.cancelar = QPushButton(AgregarExperimento)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(210, 230, 101, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.agregar = QPushButton(AgregarExperimento)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(50, 230, 91, 29))
        self.agregar.setFont(font)
        self.label_2 = QLabel(AgregarExperimento)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 151, 20))
        self.label_91 = QLabel(AgregarExperimento)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(30, 20, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.nombre = QLineEdit(AgregarExperimento)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(190, 90, 121, 21))
        self.label = QLabel(AgregarExperimento)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 140, 261, 51))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.retranslateUi(AgregarExperimento)

        QMetaObject.connectSlotsByName(AgregarExperimento)
    # setupUi

    def retranslateUi(self, AgregarExperimento):
        AgregarExperimento.setWindowTitle(QCoreApplication.translate("AgregarExperimento", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("AgregarExperimento", u"Cancelar", None))
        self.agregar.setText(QCoreApplication.translate("AgregarExperimento", u"Agregar", None))
        self.label_2.setText(QCoreApplication.translate("AgregarExperimento", u"Nombre", None))
        self.label_91.setText(QCoreApplication.translate("AgregarExperimento", u"Agregar Experimento", None))
        self.nombre.setText("")
        self.label.setText(QCoreApplication.translate("AgregarExperimento", u"Nota: Esto agregara el nuevo experimento al servidor", None))
    # retranslateUi

