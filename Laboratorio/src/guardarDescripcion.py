# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guardarDescripcion.ui'
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

class Ui_GuardarDescripcion(object):
    def setupUi(self, GuardarDescripcion):
        if not GuardarDescripcion.objectName():
            GuardarDescripcion.setObjectName(u"GuardarDescripcion")
        GuardarDescripcion.resize(365, 220)
        self.cancelar = QPushButton(GuardarDescripcion)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(220, 130, 83, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.si = QPushButton(GuardarDescripcion)
        self.si.setObjectName(u"si")
        self.si.setGeometry(QRect(70, 130, 83, 29))
        self.si.setFont(font)
        self.label_91 = QLabel(GuardarDescripcion)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(10, 40, 341, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)

        self.retranslateUi(GuardarDescripcion)

        QMetaObject.connectSlotsByName(GuardarDescripcion)
    # setupUi

    def retranslateUi(self, GuardarDescripcion):
        GuardarDescripcion.setWindowTitle(QCoreApplication.translate("GuardarDescripcion", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("GuardarDescripcion", u"Cancelar", None))
        self.si.setText(QCoreApplication.translate("GuardarDescripcion", u"Si", None))
        self.label_91.setText(QCoreApplication.translate("GuardarDescripcion", u"\u00bfGuardar Descripcion?", None))
    # retranslateUi

