# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearParametro.ui'
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

class Ui_CrearParametro(object):
    def setupUi(self, CrearParametro):
        if not CrearParametro.objectName():
            CrearParametro.setObjectName(u"CrearParametro")
        CrearParametro.resize(381, 281)
        self.cancelar = QPushButton(CrearParametro)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(222, 230, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.crear = QPushButton(CrearParametro)
        self.crear.setObjectName(u"crear")
        self.crear.setGeometry(QRect(50, 230, 111, 29))
        self.crear.setFont(font)
        self.label_2 = QLabel(CrearParametro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 81, 20))
        self.label_3 = QLabel(CrearParametro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 61, 20))
        self.tipo = QComboBox(CrearParametro)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(170, 150, 161, 21))
        self.label_91 = QLabel(CrearParametro)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(30, 20, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.nombre = QLineEdit(CrearParametro)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(170, 90, 161, 21))

        self.retranslateUi(CrearParametro)

        QMetaObject.connectSlotsByName(CrearParametro)
    # setupUi

    def retranslateUi(self, CrearParametro):
        CrearParametro.setWindowTitle(QCoreApplication.translate("CrearParametro", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("CrearParametro", u"Cancelar", None))
        self.crear.setText(QCoreApplication.translate("CrearParametro", u"Crear", None))
        self.label_2.setText(QCoreApplication.translate("CrearParametro", u"Nombre ", None))
        self.label_3.setText(QCoreApplication.translate("CrearParametro", u"Tipo", None))
        self.tipo.setItemText(0, QCoreApplication.translate("CrearParametro", u"Entero", None))
        self.tipo.setItemText(1, QCoreApplication.translate("CrearParametro", u"Real", None))
        self.tipo.setItemText(2, QCoreApplication.translate("CrearParametro", u"Texto", None))
        self.tipo.setItemText(3, QCoreApplication.translate("CrearParametro", u"Boolean", None))

        self.label_91.setText(QCoreApplication.translate("CrearParametro", u"Crear Nuevo Parametro", None))
        self.nombre.setText("")
    # retranslateUi

