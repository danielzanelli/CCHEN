# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminarArchivo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

from pyqtgraph import PlotWidget

class Ui_EliminarArchivo(object):
    def setupUi(self, EliminarArchivo):
        if not EliminarArchivo.objectName():
            EliminarArchivo.setObjectName(u"EliminarArchivo")
        EliminarArchivo.resize(733, 529)
        self.cancelar = QPushButton(EliminarArchivo)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(450, 470, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.eliminar = QPushButton(EliminarArchivo)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(172, 470, 111, 29))
        self.eliminar.setFont(font)
        self.archivo = QLabel(EliminarArchivo)
        self.archivo.setObjectName(u"archivo")
        self.archivo.setGeometry(QRect(80, 120, 591, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.archivo.setFont(font1)
        self.archivo.setAlignment(Qt.AlignCenter)
        self.archivo.setWordWrap(True)
        self.frame = QFrame(EliminarArchivo)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 180, 591, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.preview_image = QLabel(self.frame)
        self.preview_image.setObjectName(u"preview_image")
        self.preview_image.setGeometry(QRect(0, 0, 591, 261))
        self.preview_image.setAlignment(Qt.AlignCenter)
        self.preview_text = QTextBrowser(self.frame)
        self.preview_text.setObjectName(u"preview_text")
        self.preview_text.setGeometry(QRect(0, 0, 591, 261))
        self.preview_graph = PlotWidget(self.frame)
        self.preview_graph.setObjectName(u"preview_graph")
        self.preview_graph.setGeometry(QRect(0, 0, 591, 261))
        self.preview_graph.setAutoFillBackground(False)
        self.label_91 = QLabel(EliminarArchivo)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(190, 30, 341, 61))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_91.setFont(font2)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.label_91.setWordWrap(True)

        self.retranslateUi(EliminarArchivo)

        QMetaObject.connectSlotsByName(EliminarArchivo)
    # setupUi

    def retranslateUi(self, EliminarArchivo):
        EliminarArchivo.setWindowTitle(QCoreApplication.translate("EliminarArchivo", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("EliminarArchivo", u"Cancelar", None))
        self.eliminar.setText(QCoreApplication.translate("EliminarArchivo", u"Eliminar", None))
        self.archivo.setText("")
        self.preview_image.setText("")
        self.preview_text.setHtml(QCoreApplication.translate("EliminarArchivo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("EliminarArchivo", u"\u00bfEliminar este archivo?", None))
    # retranslateUi

