# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminarParametro.ui'
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

class Ui_EliminarParametro(object):
    def setupUi(self, EliminarParametro):
        if not EliminarParametro.objectName():
            EliminarParametro.setObjectName(u"EliminarParametro")
        EliminarParametro.resize(423, 346)
        self.cancelar = QPushButton(EliminarParametro)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(272, 280, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.eliminar = QPushButton(EliminarParametro)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(50, 280, 111, 29))
        self.eliminar.setFont(font)
        self.label_91 = QLabel(EliminarParametro)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(50, 30, 341, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)
        self.label_3 = QLabel(EliminarParametro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 130, 111, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.parametro = QLabel(EliminarParametro)
        self.parametro.setObjectName(u"parametro")
        self.parametro.setGeometry(QRect(160, 130, 221, 20))
        self.parametro.setFont(font2)
        self.parametro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.valor = QLabel(EliminarParametro)
        self.valor.setObjectName(u"valor")
        self.valor.setGeometry(QRect(160, 160, 221, 20))
        self.valor.setFont(font2)
        self.valor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(EliminarParametro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 160, 111, 20))
        self.label_4.setFont(font2)
        self.unidad = QLabel(EliminarParametro)
        self.unidad.setObjectName(u"unidad")
        self.unidad.setGeometry(QRect(160, 190, 221, 20))
        self.unidad.setFont(font2)
        self.unidad.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(EliminarParametro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 190, 111, 20))
        self.label_5.setFont(font2)
        self.datapoint = QLabel(EliminarParametro)
        self.datapoint.setObjectName(u"datapoint")
        self.datapoint.setGeometry(QRect(160, 220, 221, 20))
        self.datapoint.setFont(font2)
        self.datapoint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(EliminarParametro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 220, 111, 20))
        self.label_6.setFont(font2)

        self.retranslateUi(EliminarParametro)

        QMetaObject.connectSlotsByName(EliminarParametro)
    # setupUi

    def retranslateUi(self, EliminarParametro):
        EliminarParametro.setWindowTitle(QCoreApplication.translate("EliminarParametro", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("EliminarParametro", u"Cancelar", None))
        self.eliminar.setText(QCoreApplication.translate("EliminarParametro", u"Eliminar", None))
        self.label_91.setText(QCoreApplication.translate("EliminarParametro", u"\u00bfEliminar este valor?", None))
        self.label_3.setText(QCoreApplication.translate("EliminarParametro", u"Parametro", None))
        self.parametro.setText("")
        self.valor.setText("")
        self.label_4.setText(QCoreApplication.translate("EliminarParametro", u"Valor", None))
        self.unidad.setText("")
        self.label_5.setText(QCoreApplication.translate("EliminarParametro", u"Unidad", None))
        self.datapoint.setText("")
        self.label_6.setText(QCoreApplication.translate("EliminarParametro", u"Datapoint", None))
    # retranslateUi

