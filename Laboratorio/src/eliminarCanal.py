# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminarCanal.ui'
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

class Ui_EliminarCanal(object):
    def setupUi(self, EliminarCanal):
        if not EliminarCanal.objectName():
            EliminarCanal.setObjectName(u"EliminarCanal")
        EliminarCanal.resize(422, 352)
        self.cancelar = QPushButton(EliminarCanal)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(272, 280, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.eliminar = QPushButton(EliminarCanal)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(50, 280, 111, 29))
        self.eliminar.setFont(font)
        self.label_91 = QLabel(EliminarCanal)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(50, 30, 341, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)
        self.label_3 = QLabel(EliminarCanal)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 130, 111, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.nombre = QLabel(EliminarCanal)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(160, 130, 221, 20))
        self.nombre.setFont(font2)
        self.nombre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.osciloscopio = QLabel(EliminarCanal)
        self.osciloscopio.setObjectName(u"osciloscopio")
        self.osciloscopio.setGeometry(QRect(160, 160, 221, 20))
        self.osciloscopio.setFont(font2)
        self.osciloscopio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(EliminarCanal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 160, 111, 20))
        self.label_4.setFont(font2)
        self.canal = QLabel(EliminarCanal)
        self.canal.setObjectName(u"canal")
        self.canal.setGeometry(QRect(160, 190, 221, 20))
        self.canal.setFont(font2)
        self.canal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(EliminarCanal)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 190, 111, 20))
        self.label_5.setFont(font2)

        self.retranslateUi(EliminarCanal)

        QMetaObject.connectSlotsByName(EliminarCanal)
    # setupUi

    def retranslateUi(self, EliminarCanal):
        EliminarCanal.setWindowTitle(QCoreApplication.translate("EliminarCanal", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("EliminarCanal", u"Cancelar", None))
        self.eliminar.setText(QCoreApplication.translate("EliminarCanal", u"Eliminar", None))
        self.label_91.setText(QCoreApplication.translate("EliminarCanal", u"\u00bfEliminar este canal?", None))
        self.label_3.setText(QCoreApplication.translate("EliminarCanal", u"Nombre", None))
        self.nombre.setText("")
        self.osciloscopio.setText("")
        self.label_4.setText(QCoreApplication.translate("EliminarCanal", u"Osciloscopio", None))
        self.canal.setText("")
        self.label_5.setText(QCoreApplication.translate("EliminarCanal", u"Canal", None))
    # retranslateUi

