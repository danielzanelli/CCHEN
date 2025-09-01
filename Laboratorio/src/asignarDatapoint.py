# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asignarDatapoint.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_AsignarDatapoint(object):
    def setupUi(self, AsignarDatapoint):
        if not AsignarDatapoint.objectName():
            AsignarDatapoint.setObjectName(u"AsignarDatapoint")
        AsignarDatapoint.resize(733, 529)
        self.cancelar = QPushButton(AsignarDatapoint)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(450, 470, 111, 29))
        font = QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.asignar = QPushButton(AsignarDatapoint)
        self.asignar.setObjectName(u"asignar")
        self.asignar.setGeometry(QRect(170, 470, 111, 29))
        self.asignar.setFont(font)
        self.label_2 = QLabel(AsignarDatapoint)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 420, 151, 20))
        self.label_91 = QLabel(AsignarDatapoint)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(220, 10, 311, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(AsignarDatapoint)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 130, 591, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.preview_text = QTextBrowser(self.frame)
        self.preview_text.setObjectName(u"preview_text")
        self.preview_text.setGeometry(QRect(0, 0, 591, 261))
        self.preview_image = QLabel(self.frame)
        self.preview_image.setObjectName(u"preview_image")
        self.preview_image.setGeometry(QRect(0, 0, 591, 261))
        self.preview_image.setAlignment(Qt.AlignCenter)
        self.preview_graph = PlotWidget(self.frame)
        self.preview_graph.setObjectName(u"preview_graph")
        self.preview_graph.setGeometry(QRect(0, 0, 591, 261))
        self.preview_graph.setAutoFillBackground(False)
        self.archivo = QLabel(AsignarDatapoint)
        self.archivo.setObjectName(u"archivo")
        self.archivo.setGeometry(QRect(90, 70, 571, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.archivo.setFont(font2)
        self.archivo.setAlignment(Qt.AlignCenter)
        self.archivo.setWordWrap(True)
        self.datapoint = QLineEdit(AsignarDatapoint)
        self.datapoint.setObjectName(u"datapoint")
        self.datapoint.setGeometry(QRect(380, 420, 121, 21))

        self.retranslateUi(AsignarDatapoint)

        QMetaObject.connectSlotsByName(AsignarDatapoint)
    # setupUi

    def retranslateUi(self, AsignarDatapoint):
        AsignarDatapoint.setWindowTitle(QCoreApplication.translate("AsignarDatapoint", u"Dialog", None))
        self.cancelar.setText(QCoreApplication.translate("AsignarDatapoint", u"Cancelar", None))
        self.asignar.setText(QCoreApplication.translate("AsignarDatapoint", u"Asignar", None))
        self.label_2.setText(QCoreApplication.translate("AsignarDatapoint", u"Datapont", None))
        self.label_91.setText(QCoreApplication.translate("AsignarDatapoint", u"Asignar Datapoint", None))
        self.preview_text.setHtml(QCoreApplication.translate("AsignarDatapoint", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.preview_image.setText("")
        self.archivo.setText("")
        self.datapoint.setText("")
    # retranslateUi

