# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaPrincipal.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1109, 579)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(0, 500))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(50, 50))
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_11 = QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_84 = QLabel(self.tab_10)
        self.label_84.setObjectName(u"label_84")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_84.setFont(font1)
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_84, 4, 0, 1, 1)

        self.label_91 = QLabel(self.tab_10)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_91, 6, 0, 1, 2)

        self.ingreso_crear_parametro = QPushButton(self.tab_10)
        self.ingreso_crear_parametro.setObjectName(u"ingreso_crear_parametro")
        self.ingreso_crear_parametro.setMinimumSize(QSize(0, 30))
        self.ingreso_crear_parametro.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.ingreso_crear_parametro.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_crear_parametro, 6, 2, 1, 1)

        self.ingreso_eliminar_archivo = QPushButton(self.tab_10)
        self.ingreso_eliminar_archivo.setObjectName(u"ingreso_eliminar_archivo")
        self.ingreso_eliminar_archivo.setMinimumSize(QSize(0, 30))
        self.ingreso_eliminar_archivo.setMaximumSize(QSize(16777215, 40))
        self.ingreso_eliminar_archivo.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_eliminar_archivo, 0, 2, 1, 1)

        self.ingreso_label_archivos_locales = QLabel(self.tab_10)
        self.ingreso_label_archivos_locales.setObjectName(u"ingreso_label_archivos_locales")
        sizePolicy1.setHeightForWidth(self.ingreso_label_archivos_locales.sizePolicy().hasHeightForWidth())
        self.ingreso_label_archivos_locales.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.ingreso_label_archivos_locales.setFont(font3)
        self.ingreso_label_archivos_locales.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.ingreso_label_archivos_locales, 4, 1, 1, 2)

        self.ingreso_seleccionar_carpeta = QPushButton(self.tab_10)
        self.ingreso_seleccionar_carpeta.setObjectName(u"ingreso_seleccionar_carpeta")
        self.ingreso_seleccionar_carpeta.setMinimumSize(QSize(0, 30))
        self.ingreso_seleccionar_carpeta.setMaximumSize(QSize(16777215, 40))
        self.ingreso_seleccionar_carpeta.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_seleccionar_carpeta, 0, 0, 2, 1)

        self.ingreso_refrescar = QPushButton(self.tab_10)
        self.ingreso_refrescar.setObjectName(u"ingreso_refrescar")
        self.ingreso_refrescar.setMinimumSize(QSize(0, 30))
        self.ingreso_refrescar.setMaximumSize(QSize(16777215, 40))
        self.ingreso_refrescar.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_refrescar, 0, 1, 1, 1)

        self.ingreso_archivos_locales = QTreeWidget(self.tab_10)
        self.ingreso_archivos_locales.setObjectName(u"ingreso_archivos_locales")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ingreso_archivos_locales.sizePolicy().hasHeightForWidth())
        self.ingreso_archivos_locales.setSizePolicy(sizePolicy2)
        self.ingreso_archivos_locales.setFont(font2)
        self.ingreso_archivos_locales.setSortingEnabled(True)
        self.ingreso_archivos_locales.header().setDefaultSectionSize(90)

        self.gridLayout_9.addWidget(self.ingreso_archivos_locales, 5, 0, 1, 3)

        self.ingreso_asignar_datapoint = QPushButton(self.tab_10)
        self.ingreso_asignar_datapoint.setObjectName(u"ingreso_asignar_datapoint")
        self.ingreso_asignar_datapoint.setMinimumSize(QSize(0, 30))
        self.ingreso_asignar_datapoint.setMaximumSize(QSize(16777215, 40))
        self.ingreso_asignar_datapoint.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_asignar_datapoint, 1, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ingreso_unidad_parametro_1 = QLineEdit(self.tab_10)
        self.ingreso_unidad_parametro_1.setObjectName(u"ingreso_unidad_parametro_1")
        self.ingreso_unidad_parametro_1.setMinimumSize(QSize(20, 0))
        self.ingreso_unidad_parametro_1.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_unidad_parametro_1, 1, 1, 1, 1)

        self.ingreso_parametro_parametro_1 = QComboBox(self.tab_10)
        self.ingreso_parametro_parametro_1.addItem("")
        self.ingreso_parametro_parametro_1.addItem("")
        self.ingreso_parametro_parametro_1.addItem("")
        self.ingreso_parametro_parametro_1.addItem("")
        self.ingreso_parametro_parametro_1.setObjectName(u"ingreso_parametro_parametro_1")
        self.ingreso_parametro_parametro_1.setMinimumSize(QSize(20, 0))
        self.ingreso_parametro_parametro_1.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_parametro_parametro_1, 2, 1, 1, 1)

        self.label_88 = QLabel(self.tab_10)
        self.label_88.setObjectName(u"label_88")
        sizePolicy1.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy1)
        self.label_88.setFont(font2)

        self.gridLayout_10.addWidget(self.label_88, 0, 0, 1, 1)

        self.ingreso_datapoint_parametro_3 = QLineEdit(self.tab_10)
        self.ingreso_datapoint_parametro_3.setObjectName(u"ingreso_datapoint_parametro_3")
        self.ingreso_datapoint_parametro_3.setMinimumSize(QSize(20, 0))
        self.ingreso_datapoint_parametro_3.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_datapoint_parametro_3, 0, 3, 1, 1)

        self.ingreso_datapoint_parametro_1 = QLineEdit(self.tab_10)
        self.ingreso_datapoint_parametro_1.setObjectName(u"ingreso_datapoint_parametro_1")
        self.ingreso_datapoint_parametro_1.setMinimumSize(QSize(20, 0))
        self.ingreso_datapoint_parametro_1.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_datapoint_parametro_1, 0, 1, 1, 1)

        self.label_89 = QLabel(self.tab_10)
        self.label_89.setObjectName(u"label_89")
        sizePolicy1.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy1)
        self.label_89.setFont(font2)

        self.gridLayout_10.addWidget(self.label_89, 2, 0, 1, 1)

        self.ingreso_valor_parametro_1 = QLineEdit(self.tab_10)
        self.ingreso_valor_parametro_1.setObjectName(u"ingreso_valor_parametro_1")
        self.ingreso_valor_parametro_1.setMinimumSize(QSize(20, 0))
        self.ingreso_valor_parametro_1.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_valor_parametro_1, 3, 1, 1, 1)

        self.label_87 = QLabel(self.tab_10)
        self.label_87.setObjectName(u"label_87")
        sizePolicy1.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy1)
        self.label_87.setFont(font2)

        self.gridLayout_10.addWidget(self.label_87, 3, 0, 1, 1)

        self.label_26 = QLabel(self.tab_10)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setFont(font2)

        self.gridLayout_10.addWidget(self.label_26, 1, 0, 1, 1)

        self.ingreso_agregar_parametro_1 = QPushButton(self.tab_10)
        self.ingreso_agregar_parametro_1.setObjectName(u"ingreso_agregar_parametro_1")
        self.ingreso_agregar_parametro_1.setMinimumSize(QSize(30, 20))
        self.ingreso_agregar_parametro_1.setMaximumSize(QSize(16777215, 30))
        self.ingreso_agregar_parametro_1.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_agregar_parametro_1, 4, 1, 1, 1)

        self.ingreso_datapoint_parametro_2 = QLineEdit(self.tab_10)
        self.ingreso_datapoint_parametro_2.setObjectName(u"ingreso_datapoint_parametro_2")
        self.ingreso_datapoint_parametro_2.setMinimumSize(QSize(20, 0))
        self.ingreso_datapoint_parametro_2.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_datapoint_parametro_2, 0, 2, 1, 1)

        self.ingreso_datapoint_parametro_4 = QLineEdit(self.tab_10)
        self.ingreso_datapoint_parametro_4.setObjectName(u"ingreso_datapoint_parametro_4")
        self.ingreso_datapoint_parametro_4.setMinimumSize(QSize(20, 0))
        self.ingreso_datapoint_parametro_4.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_datapoint_parametro_4, 0, 4, 1, 1)

        self.ingreso_unidad_parametro_2 = QLineEdit(self.tab_10)
        self.ingreso_unidad_parametro_2.setObjectName(u"ingreso_unidad_parametro_2")
        self.ingreso_unidad_parametro_2.setMinimumSize(QSize(20, 0))
        self.ingreso_unidad_parametro_2.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_unidad_parametro_2, 1, 2, 1, 1)

        self.ingreso_unidad_parametro_3 = QLineEdit(self.tab_10)
        self.ingreso_unidad_parametro_3.setObjectName(u"ingreso_unidad_parametro_3")
        self.ingreso_unidad_parametro_3.setMinimumSize(QSize(20, 0))
        self.ingreso_unidad_parametro_3.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_unidad_parametro_3, 1, 3, 1, 1)

        self.ingreso_unidad_parametro_4 = QLineEdit(self.tab_10)
        self.ingreso_unidad_parametro_4.setObjectName(u"ingreso_unidad_parametro_4")
        self.ingreso_unidad_parametro_4.setMinimumSize(QSize(20, 0))
        self.ingreso_unidad_parametro_4.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_unidad_parametro_4, 1, 4, 1, 1)

        self.ingreso_parametro_parametro_2 = QComboBox(self.tab_10)
        self.ingreso_parametro_parametro_2.addItem("")
        self.ingreso_parametro_parametro_2.addItem("")
        self.ingreso_parametro_parametro_2.addItem("")
        self.ingreso_parametro_parametro_2.addItem("")
        self.ingreso_parametro_parametro_2.setObjectName(u"ingreso_parametro_parametro_2")
        self.ingreso_parametro_parametro_2.setMinimumSize(QSize(20, 0))
        self.ingreso_parametro_parametro_2.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_parametro_parametro_2, 2, 2, 1, 1)

        self.ingreso_parametro_parametro_3 = QComboBox(self.tab_10)
        self.ingreso_parametro_parametro_3.addItem("")
        self.ingreso_parametro_parametro_3.addItem("")
        self.ingreso_parametro_parametro_3.addItem("")
        self.ingreso_parametro_parametro_3.addItem("")
        self.ingreso_parametro_parametro_3.setObjectName(u"ingreso_parametro_parametro_3")
        self.ingreso_parametro_parametro_3.setMinimumSize(QSize(20, 0))
        self.ingreso_parametro_parametro_3.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_parametro_parametro_3, 2, 3, 1, 1)

        self.ingreso_parametro_parametro_4 = QComboBox(self.tab_10)
        self.ingreso_parametro_parametro_4.addItem("")
        self.ingreso_parametro_parametro_4.addItem("")
        self.ingreso_parametro_parametro_4.addItem("")
        self.ingreso_parametro_parametro_4.addItem("")
        self.ingreso_parametro_parametro_4.setObjectName(u"ingreso_parametro_parametro_4")
        self.ingreso_parametro_parametro_4.setMinimumSize(QSize(20, 0))
        self.ingreso_parametro_parametro_4.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_parametro_parametro_4, 2, 4, 1, 1)

        self.ingreso_valor_parametro_2 = QLineEdit(self.tab_10)
        self.ingreso_valor_parametro_2.setObjectName(u"ingreso_valor_parametro_2")
        self.ingreso_valor_parametro_2.setMinimumSize(QSize(20, 0))
        self.ingreso_valor_parametro_2.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_valor_parametro_2, 3, 2, 1, 1)

        self.ingreso_valor_parametro_3 = QLineEdit(self.tab_10)
        self.ingreso_valor_parametro_3.setObjectName(u"ingreso_valor_parametro_3")
        self.ingreso_valor_parametro_3.setMinimumSize(QSize(20, 0))
        self.ingreso_valor_parametro_3.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_valor_parametro_3, 3, 3, 1, 1)

        self.ingreso_valor_parametro_4 = QLineEdit(self.tab_10)
        self.ingreso_valor_parametro_4.setObjectName(u"ingreso_valor_parametro_4")
        self.ingreso_valor_parametro_4.setMinimumSize(QSize(20, 0))
        self.ingreso_valor_parametro_4.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_valor_parametro_4, 3, 4, 1, 1)

        self.ingreso_agregar_parametro_2 = QPushButton(self.tab_10)
        self.ingreso_agregar_parametro_2.setObjectName(u"ingreso_agregar_parametro_2")
        self.ingreso_agregar_parametro_2.setMinimumSize(QSize(30, 20))
        self.ingreso_agregar_parametro_2.setMaximumSize(QSize(16777215, 30))
        self.ingreso_agregar_parametro_2.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_agregar_parametro_2, 4, 2, 1, 1)

        self.ingreso_agregar_parametro_3 = QPushButton(self.tab_10)
        self.ingreso_agregar_parametro_3.setObjectName(u"ingreso_agregar_parametro_3")
        self.ingreso_agregar_parametro_3.setMinimumSize(QSize(30, 20))
        self.ingreso_agregar_parametro_3.setMaximumSize(QSize(16777215, 30))
        self.ingreso_agregar_parametro_3.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_agregar_parametro_3, 4, 3, 1, 1)

        self.ingreso_agregar_parametro_4 = QPushButton(self.tab_10)
        self.ingreso_agregar_parametro_4.setObjectName(u"ingreso_agregar_parametro_4")
        self.ingreso_agregar_parametro_4.setMinimumSize(QSize(30, 20))
        self.ingreso_agregar_parametro_4.setMaximumSize(QSize(16777215, 30))
        self.ingreso_agregar_parametro_4.setFont(font2)

        self.gridLayout_10.addWidget(self.ingreso_agregar_parametro_4, 4, 4, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 7, 0, 1, 3)

        self.ingreso_agregar_archivo = QPushButton(self.tab_10)
        self.ingreso_agregar_archivo.setObjectName(u"ingreso_agregar_archivo")
        self.ingreso_agregar_archivo.setMinimumSize(QSize(0, 30))
        self.ingreso_agregar_archivo.setMaximumSize(QSize(16777215, 40))
        self.ingreso_agregar_archivo.setFont(font2)

        self.gridLayout_9.addWidget(self.ingreso_agregar_archivo, 1, 2, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ingreso_descripcion = QPlainTextEdit(self.tab_10)
        self.ingreso_descripcion.setObjectName(u"ingreso_descripcion")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ingreso_descripcion.sizePolicy().hasHeightForWidth())
        self.ingreso_descripcion.setSizePolicy(sizePolicy3)
        self.ingreso_descripcion.setMaximumSize(QSize(16777215, 100))
        self.ingreso_descripcion.setFont(font2)

        self.gridLayout_7.addWidget(self.ingreso_descripcion, 5, 1, 1, 2)

        self.ingreso_label_preview = QLabel(self.tab_10)
        self.ingreso_label_preview.setObjectName(u"ingreso_label_preview")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ingreso_label_preview.sizePolicy().hasHeightForWidth())
        self.ingreso_label_preview.setSizePolicy(sizePolicy4)
        self.ingreso_label_preview.setFont(font3)
        self.ingreso_label_preview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.ingreso_label_preview, 0, 2, 1, 1)

        self.ingreso_parametros = QTreeWidget(self.tab_10)
        self.ingreso_parametros.setObjectName(u"ingreso_parametros")
        self.ingreso_parametros.setMaximumSize(QSize(16777215, 150))
        self.ingreso_parametros.setFont(font2)
        self.ingreso_parametros.setSortingEnabled(True)
        self.ingreso_parametros.header().setCascadingSectionResizes(False)
        self.ingreso_parametros.header().setDefaultSectionSize(110)

        self.gridLayout_7.addWidget(self.ingreso_parametros, 11, 1, 1, 2)

        self.label_17 = QLabel(self.tab_10)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font1)

        self.gridLayout_7.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_29 = QLabel(self.tab_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_7.addWidget(self.label_29, 4, 1, 1, 1)

        self.ingreso_guardar_descripcion = QPushButton(self.tab_10)
        self.ingreso_guardar_descripcion.setObjectName(u"ingreso_guardar_descripcion")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ingreso_guardar_descripcion.sizePolicy().hasHeightForWidth())
        self.ingreso_guardar_descripcion.setSizePolicy(sizePolicy5)
        self.ingreso_guardar_descripcion.setMinimumSize(QSize(0, 30))
        self.ingreso_guardar_descripcion.setMaximumSize(QSize(16777215, 40))
        self.ingreso_guardar_descripcion.setFont(font2)

        self.gridLayout_7.addWidget(self.ingreso_guardar_descripcion, 4, 2, 1, 1)

        self.frame_2 = QFrame(self.tab_10)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 600))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ingreso_preview_text = QTextBrowser(self.frame_2)
        self.ingreso_preview_text.setObjectName(u"ingreso_preview_text")
        self.ingreso_preview_text.setFont(font2)

        self.gridLayout_8.addWidget(self.ingreso_preview_text, 0, 1, 1, 1)

        self.ingreso_preview_graph = PlotWidget(self.frame_2)
        self.ingreso_preview_graph.setObjectName(u"ingreso_preview_graph")
        sizePolicy6.setHeightForWidth(self.ingreso_preview_graph.sizePolicy().hasHeightForWidth())
        self.ingreso_preview_graph.setSizePolicy(sizePolicy6)
        self.ingreso_preview_graph.setFont(font2)
        self.ingreso_preview_graph.setAutoFillBackground(False)

        self.gridLayout_8.addWidget(self.ingreso_preview_graph, 0, 2, 1, 1)

        self.ingreso_preview_image = QLabel(self.frame_2)
        self.ingreso_preview_image.setObjectName(u"ingreso_preview_image")
        sizePolicy6.setHeightForWidth(self.ingreso_preview_image.sizePolicy().hasHeightForWidth())
        self.ingreso_preview_image.setSizePolicy(sizePolicy6)
        self.ingreso_preview_image.setFont(font2)
        self.ingreso_preview_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.ingreso_preview_image, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_2, 1, 1, 3, 2)

        self.label_28 = QLabel(self.tab_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_7.addWidget(self.label_28, 10, 1, 1, 1)

        self.ingreso_eliminar_parametro = QPushButton(self.tab_10)
        self.ingreso_eliminar_parametro.setObjectName(u"ingreso_eliminar_parametro")
        sizePolicy5.setHeightForWidth(self.ingreso_eliminar_parametro.sizePolicy().hasHeightForWidth())
        self.ingreso_eliminar_parametro.setSizePolicy(sizePolicy5)
        self.ingreso_eliminar_parametro.setMinimumSize(QSize(0, 30))
        self.ingreso_eliminar_parametro.setMaximumSize(QSize(16777215, 40))
        self.ingreso_eliminar_parametro.setFont(font2)

        self.gridLayout_7.addWidget(self.ingreso_eliminar_parametro, 10, 2, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 1, 1, 2)

        self.tabWidget.addTab(self.tab_10, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.status_2 = QLabel(self.tab)
        self.status_2.setObjectName(u"status_2")

        self.gridLayout_6.addWidget(self.status_2, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dispositivos_buscar = QPushButton(self.tab)
        self.dispositivos_buscar.setObjectName(u"dispositivos_buscar")
        self.dispositivos_buscar.setMinimumSize(QSize(0, 30))
        self.dispositivos_buscar.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_buscar.setFont(font2)

        self.gridLayout.addWidget(self.dispositivos_buscar, 1, 1, 1, 1)

        self.dispositivos_conectar = QPushButton(self.tab)
        self.dispositivos_conectar.setObjectName(u"dispositivos_conectar")
        self.dispositivos_conectar.setMinimumSize(QSize(0, 30))
        self.dispositivos_conectar.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_conectar.setFont(font2)

        self.gridLayout.addWidget(self.dispositivos_conectar, 1, 0, 1, 1)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 2)

        self.dispositivos_dispositivos_disponibles = QTreeWidget(self.tab)
        self.dispositivos_dispositivos_disponibles.setObjectName(u"dispositivos_dispositivos_disponibles")
        self.dispositivos_dispositivos_disponibles.setFont(font2)
        self.dispositivos_dispositivos_disponibles.setSortingEnabled(True)

        self.gridLayout.addWidget(self.dispositivos_dispositivos_disponibles, 2, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 2)

        self.dispositivos_agregar_canal = QPushButton(self.tab)
        self.dispositivos_agregar_canal.setObjectName(u"dispositivos_agregar_canal")
        self.dispositivos_agregar_canal.setMinimumSize(QSize(0, 30))
        self.dispositivos_agregar_canal.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_agregar_canal.setFont(font2)

        self.gridLayout_3.addWidget(self.dispositivos_agregar_canal, 1, 1, 1, 1)

        self.dispositivos_eliminar_canal = QPushButton(self.tab)
        self.dispositivos_eliminar_canal.setObjectName(u"dispositivos_eliminar_canal")
        self.dispositivos_eliminar_canal.setMinimumSize(QSize(0, 30))
        self.dispositivos_eliminar_canal.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_eliminar_canal.setFont(font2)

        self.gridLayout_3.addWidget(self.dispositivos_eliminar_canal, 1, 0, 1, 1)

        self.dispositivos_canales = QTreeWidget(self.tab)
        self.dispositivos_canales.setObjectName(u"dispositivos_canales")
        self.dispositivos_canales.setFont(font2)
        self.dispositivos_canales.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.dispositivos_canales, 2, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dispositivos_desconectar = QPushButton(self.tab)
        self.dispositivos_desconectar.setObjectName(u"dispositivos_desconectar")
        self.dispositivos_desconectar.setMinimumSize(QSize(0, 30))
        self.dispositivos_desconectar.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_desconectar.setFont(font2)

        self.gridLayout_2.addWidget(self.dispositivos_desconectar, 1, 1, 1, 1)

        self.dispositivos_agregar_ip = QPushButton(self.tab)
        self.dispositivos_agregar_ip.setObjectName(u"dispositivos_agregar_ip")
        self.dispositivos_agregar_ip.setMinimumSize(QSize(0, 30))
        self.dispositivos_agregar_ip.setMaximumSize(QSize(16777215, 40))
        self.dispositivos_agregar_ip.setFont(font2)

        self.gridLayout_2.addWidget(self.dispositivos_agregar_ip, 1, 0, 1, 1)

        self.dispositivos_dispositivos_conectados = QTreeWidget(self.tab)
        self.dispositivos_dispositivos_conectados.setObjectName(u"dispositivos_dispositivos_conectados")
        self.dispositivos_dispositivos_conectados.setFont(font2)
        self.dispositivos_dispositivos_conectados.setSortingEnabled(True)
        self.dispositivos_dispositivos_conectados.header().setDefaultSectionSize(110)

        self.gridLayout_2.addWidget(self.dispositivos_dispositivos_conectados, 2, 0, 1, 2)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 3, 1)

        self.dispositivos_cargar_perfil = QPushButton(self.tab)
        self.dispositivos_cargar_perfil.setObjectName(u"dispositivos_cargar_perfil")
        self.dispositivos_cargar_perfil.setMinimumSize(QSize(0, 30))
        self.dispositivos_cargar_perfil.setMaximumSize(QSize(200, 40))
        self.dispositivos_cargar_perfil.setFont(font2)

        self.gridLayout_4.addWidget(self.dispositivos_cargar_perfil, 3, 1, 1, 1)

        self.dispositivos_guardar_perfil = QPushButton(self.tab)
        self.dispositivos_guardar_perfil.setObjectName(u"dispositivos_guardar_perfil")
        self.dispositivos_guardar_perfil.setMinimumSize(QSize(0, 30))
        self.dispositivos_guardar_perfil.setMaximumSize(QSize(200, 40))
        self.dispositivos_guardar_perfil.setFont(font2)

        self.gridLayout_4.addWidget(self.dispositivos_guardar_perfil, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 3, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_16 = QGridLayout(self.tab_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_22, 1, 0, 1, 1)

        self.adquisicion_seleccionar_carpeta = QPushButton(self.tab_2)
        self.adquisicion_seleccionar_carpeta.setObjectName(u"adquisicion_seleccionar_carpeta")
        self.adquisicion_seleccionar_carpeta.setMinimumSize(QSize(0, 30))
        self.adquisicion_seleccionar_carpeta.setMaximumSize(QSize(16777215, 40))
        self.adquisicion_seleccionar_carpeta.setFont(font2)

        self.gridLayout_12.addWidget(self.adquisicion_seleccionar_carpeta, 0, 0, 1, 1)

        self.adquisicion_archivos_locales = QTreeWidget(self.tab_2)
        self.adquisicion_archivos_locales.setObjectName(u"adquisicion_archivos_locales")
        self.adquisicion_archivos_locales.setFont(font2)

        self.gridLayout_12.addWidget(self.adquisicion_archivos_locales, 2, 0, 1, 2)

        self.adquisicion_label_archivos_locales = QLabel(self.tab_2)
        self.adquisicion_label_archivos_locales.setObjectName(u"adquisicion_label_archivos_locales")
        self.adquisicion_label_archivos_locales.setFont(font2)
        self.adquisicion_label_archivos_locales.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_12.addWidget(self.adquisicion_label_archivos_locales, 1, 1, 1, 1)

        self.adquisicion_refrescar = QPushButton(self.tab_2)
        self.adquisicion_refrescar.setObjectName(u"adquisicion_refrescar")
        self.adquisicion_refrescar.setMinimumSize(QSize(0, 30))
        self.adquisicion_refrescar.setMaximumSize(QSize(16777215, 40))
        self.adquisicion_refrescar.setFont(font2)

        self.gridLayout_12.addWidget(self.adquisicion_refrescar, 0, 1, 1, 1)

        self.adquisicion_origen_datos = QTreeWidget(self.tab_2)
        self.adquisicion_origen_datos.setObjectName(u"adquisicion_origen_datos")
        self.adquisicion_origen_datos.setFont(font2)

        self.gridLayout_12.addWidget(self.adquisicion_origen_datos, 4, 0, 1, 2)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_12.addWidget(self.label_10, 3, 0, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_12, 0, 0, 2, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.adquisicion_auto_guardar = QCheckBox(self.tab_2)
        self.adquisicion_auto_guardar.setObjectName(u"adquisicion_auto_guardar")
        self.adquisicion_auto_guardar.setFont(font2)

        self.gridLayout_15.addWidget(self.adquisicion_auto_guardar, 6, 1, 1, 3)

        self.adquisicion_seleccionar_carpeta_imagenes = QPushButton(self.tab_2)
        self.adquisicion_seleccionar_carpeta_imagenes.setObjectName(u"adquisicion_seleccionar_carpeta_imagenes")
        sizePolicy3.setHeightForWidth(self.adquisicion_seleccionar_carpeta_imagenes.sizePolicy().hasHeightForWidth())
        self.adquisicion_seleccionar_carpeta_imagenes.setSizePolicy(sizePolicy3)
        self.adquisicion_seleccionar_carpeta_imagenes.setMinimumSize(QSize(0, 30))
        self.adquisicion_seleccionar_carpeta_imagenes.setMaximumSize(QSize(300, 40))
        self.adquisicion_seleccionar_carpeta_imagenes.setFont(font2)

        self.gridLayout_15.addWidget(self.adquisicion_seleccionar_carpeta_imagenes, 8, 3, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_15.addWidget(self.label, 0, 1, 1, 2)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_15.addWidget(self.label_9, 7, 2, 1, 1)

        self.adquisicion_auto_imagenes = QCheckBox(self.tab_2)
        self.adquisicion_auto_imagenes.setObjectName(u"adquisicion_auto_imagenes")
        self.adquisicion_auto_imagenes.setFont(font2)

        self.gridLayout_15.addWidget(self.adquisicion_auto_imagenes, 7, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.adquisicion_auto = QPushButton(self.tab_2)
        self.adquisicion_auto.setObjectName(u"adquisicion_auto")
        sizePolicy3.setHeightForWidth(self.adquisicion_auto.sizePolicy().hasHeightForWidth())
        self.adquisicion_auto.setSizePolicy(sizePolicy3)
        self.adquisicion_auto.setMinimumSize(QSize(0, 30))
        self.adquisicion_auto.setMaximumSize(QSize(300, 40))
        self.adquisicion_auto.setFont(font2)
        self.adquisicion_auto.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_15.addWidget(self.adquisicion_auto, 0, 3, 1, 1)

        self.adquisicion_label_carpeta_imagenes = QLabel(self.tab_2)
        self.adquisicion_label_carpeta_imagenes.setObjectName(u"adquisicion_label_carpeta_imagenes")
        sizePolicy3.setHeightForWidth(self.adquisicion_label_carpeta_imagenes.sizePolicy().hasHeightForWidth())
        self.adquisicion_label_carpeta_imagenes.setSizePolicy(sizePolicy3)
        self.adquisicion_label_carpeta_imagenes.setFont(font2)

        self.gridLayout_15.addWidget(self.adquisicion_label_carpeta_imagenes, 7, 3, 1, 2)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_15.addWidget(self.label_11, 5, 1, 1, 2)

        self.adquisicion_fuente_trigger = QComboBox(self.tab_2)
        self.adquisicion_fuente_trigger.setObjectName(u"adquisicion_fuente_trigger")
        self.adquisicion_fuente_trigger.setFont(font2)

        self.gridLayout_15.addWidget(self.adquisicion_fuente_trigger, 5, 3, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 1, 1, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.adquisicion_adquirir = QPushButton(self.tab_2)
        self.adquisicion_adquirir.setObjectName(u"adquisicion_adquirir")
        sizePolicy3.setHeightForWidth(self.adquisicion_adquirir.sizePolicy().hasHeightForWidth())
        self.adquisicion_adquirir.setSizePolicy(sizePolicy3)
        self.adquisicion_adquirir.setMinimumSize(QSize(0, 30))
        self.adquisicion_adquirir.setMaximumSize(QSize(200, 40))
        self.adquisicion_adquirir.setFont(font2)

        self.gridLayout_13.addWidget(self.adquisicion_adquirir, 5, 1, 1, 1)

        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_13.addWidget(self.label_19, 6, 0, 1, 1)

        self.adquisicion_guardar = QPushButton(self.tab_2)
        self.adquisicion_guardar.setObjectName(u"adquisicion_guardar")
        sizePolicy3.setHeightForWidth(self.adquisicion_guardar.sizePolicy().hasHeightForWidth())
        self.adquisicion_guardar.setSizePolicy(sizePolicy3)
        self.adquisicion_guardar.setMinimumSize(QSize(0, 30))
        self.adquisicion_guardar.setMaximumSize(QSize(200, 40))
        self.adquisicion_guardar.setFont(font2)

        self.gridLayout_13.addWidget(self.adquisicion_guardar, 5, 2, 1, 1)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 500))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.adquisicion_preview_text = QTextBrowser(self.frame)
        self.adquisicion_preview_text.setObjectName(u"adquisicion_preview_text")
        self.adquisicion_preview_text.setFont(font2)

        self.gridLayout_14.addWidget(self.adquisicion_preview_text, 0, 1, 1, 1)

        self.adquisicion_preview_image = QLabel(self.frame)
        self.adquisicion_preview_image.setObjectName(u"adquisicion_preview_image")
        sizePolicy6.setHeightForWidth(self.adquisicion_preview_image.sizePolicy().hasHeightForWidth())
        self.adquisicion_preview_image.setSizePolicy(sizePolicy6)
        self.adquisicion_preview_image.setFont(font2)
        self.adquisicion_preview_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.adquisicion_preview_image, 0, 2, 1, 1)

        self.adquisicion_preview_graph = PlotWidget(self.frame)
        self.adquisicion_preview_graph.setObjectName(u"adquisicion_preview_graph")
        sizePolicy6.setHeightForWidth(self.adquisicion_preview_graph.sizePolicy().hasHeightForWidth())
        self.adquisicion_preview_graph.setSizePolicy(sizePolicy6)
        self.adquisicion_preview_graph.setFont(font2)
        self.adquisicion_preview_graph.setAutoFillBackground(False)

        self.gridLayout_14.addWidget(self.adquisicion_preview_graph, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame, 4, 0, 1, 4)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 4)

        self.adquisicion_label_preview = QLabel(self.tab_2)
        self.adquisicion_label_preview.setObjectName(u"adquisicion_label_preview")
        self.adquisicion_label_preview.setFont(font3)
        self.adquisicion_label_preview.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_13.addWidget(self.adquisicion_label_preview, 6, 1, 1, 3)

        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setFont(font)

        self.gridLayout_13.addWidget(self.label_23, 7, 1, 1, 1)

        self.adquisicion_prefijo = QLineEdit(self.tab_2)
        self.adquisicion_prefijo.setObjectName(u"adquisicion_prefijo")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.adquisicion_prefijo.sizePolicy().hasHeightForWidth())
        self.adquisicion_prefijo.setSizePolicy(sizePolicy7)
        self.adquisicion_prefijo.setFont(font2)

        self.gridLayout_13.addWidget(self.adquisicion_prefijo, 7, 2, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_13, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_20 = QGridLayout(self.tab_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.bd_agregar_experimento = QPushButton(self.tab_3)
        self.bd_agregar_experimento.setObjectName(u"bd_agregar_experimento")
        self.bd_agregar_experimento.setMinimumSize(QSize(0, 30))
        self.bd_agregar_experimento.setMaximumSize(QSize(16777215, 40))
        self.bd_agregar_experimento.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_agregar_experimento, 7, 3, 1, 1)

        self.bd_experimento = QComboBox(self.tab_3)
        self.bd_experimento.addItem("")
        self.bd_experimento.setObjectName(u"bd_experimento")
        sizePolicy7.setHeightForWidth(self.bd_experimento.sizePolicy().hasHeightForWidth())
        self.bd_experimento.setSizePolicy(sizePolicy7)
        self.bd_experimento.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_experimento, 7, 2, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.gridLayout_18.addWidget(self.label_3, 7, 1, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)

        self.gridLayout_18.addWidget(self.label_4, 8, 1, 1, 1)

        self.bd_jornada = QComboBox(self.tab_3)
        self.bd_jornada.addItem("")
        self.bd_jornada.addItem("")
        self.bd_jornada.addItem("")
        self.bd_jornada.setObjectName(u"bd_jornada")
        sizePolicy7.setHeightForWidth(self.bd_jornada.sizePolicy().hasHeightForWidth())
        self.bd_jornada.setSizePolicy(sizePolicy7)
        self.bd_jornada.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_jornada, 8, 2, 1, 1)

        self.bd_agregar_jornada = QPushButton(self.tab_3)
        self.bd_agregar_jornada.setObjectName(u"bd_agregar_jornada")
        self.bd_agregar_jornada.setMinimumSize(QSize(0, 30))
        self.bd_agregar_jornada.setMaximumSize(QSize(16777215, 40))
        self.bd_agregar_jornada.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_agregar_jornada, 8, 3, 1, 1)

        self.bd_subir = QPushButton(self.tab_3)
        self.bd_subir.setObjectName(u"bd_subir")
        sizePolicy5.setHeightForWidth(self.bd_subir.sizePolicy().hasHeightForWidth())
        self.bd_subir.setSizePolicy(sizePolicy5)
        self.bd_subir.setMinimumSize(QSize(0, 30))
        self.bd_subir.setMaximumSize(QSize(16777215, 40))
        self.bd_subir.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_subir, 7, 0, 2, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 5, 1, 1, 2)

        self.bd_usuario = QLineEdit(self.tab_3)
        self.bd_usuario.setObjectName(u"bd_usuario")
        sizePolicy7.setHeightForWidth(self.bd_usuario.sizePolicy().hasHeightForWidth())
        self.bd_usuario.setSizePolicy(sizePolicy7)
        self.bd_usuario.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_usuario, 2, 3, 1, 1)

        self.bd_password = QLineEdit(self.tab_3)
        self.bd_password.setObjectName(u"bd_password")
        sizePolicy7.setHeightForWidth(self.bd_password.sizePolicy().hasHeightForWidth())
        self.bd_password.setSizePolicy(sizePolicy7)
        self.bd_password.setFont(font2)
        self.bd_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_18.addWidget(self.bd_password, 3, 3, 1, 1)

        self.bd_ip = QLineEdit(self.tab_3)
        self.bd_ip.setObjectName(u"bd_ip")
        sizePolicy7.setHeightForWidth(self.bd_ip.sizePolicy().hasHeightForWidth())
        self.bd_ip.setSizePolicy(sizePolicy7)
        self.bd_ip.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_ip, 4, 3, 1, 1)

        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font)

        self.gridLayout_18.addWidget(self.label_16, 4, 2, 1, 1)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setFont(font)

        self.gridLayout_18.addWidget(self.label_15, 3, 2, 1, 1)

        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)

        self.gridLayout_18.addWidget(self.label_5, 2, 2, 1, 1)

        self.bd_refrescar_servidor = QPushButton(self.tab_3)
        self.bd_refrescar_servidor.setObjectName(u"bd_refrescar_servidor")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.bd_refrescar_servidor.sizePolicy().hasHeightForWidth())
        self.bd_refrescar_servidor.setSizePolicy(sizePolicy8)
        self.bd_refrescar_servidor.setMinimumSize(QSize(0, 30))
        self.bd_refrescar_servidor.setMaximumSize(QSize(16777215, 40))
        self.bd_refrescar_servidor.setFont(font2)

        self.gridLayout_18.addWidget(self.bd_refrescar_servidor, 2, 0, 3, 2)


        self.gridLayout_20.addLayout(self.gridLayout_18, 0, 1, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font1)

        self.gridLayout_19.addWidget(self.label_6, 0, 0, 1, 1)

        self.bd_archivos_servidor = QTreeWidget(self.tab_3)
        self.bd_archivos_servidor.setObjectName(u"bd_archivos_servidor")
        sizePolicy2.setHeightForWidth(self.bd_archivos_servidor.sizePolicy().hasHeightForWidth())
        self.bd_archivos_servidor.setSizePolicy(sizePolicy2)
        self.bd_archivos_servidor.setFont(font2)
        self.bd_archivos_servidor.setSortingEnabled(True)

        self.gridLayout_19.addWidget(self.bd_archivos_servidor, 1, 0, 1, 1)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        self.label_24.setFont(font1)

        self.gridLayout_19.addWidget(self.label_24, 2, 0, 1, 1)

        self.bd_parametros_servidor = QTreeWidget(self.tab_3)
        self.bd_parametros_servidor.setObjectName(u"bd_parametros_servidor")
        sizePolicy2.setHeightForWidth(self.bd_parametros_servidor.sizePolicy().hasHeightForWidth())
        self.bd_parametros_servidor.setSizePolicy(sizePolicy2)
        self.bd_parametros_servidor.setFont(font2)
        self.bd_parametros_servidor.setSortingEnabled(True)
        self.bd_parametros_servidor.header().setDefaultSectionSize(100)

        self.gridLayout_19.addWidget(self.bd_parametros_servidor, 3, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 2, 1, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.bd_label_archivos_locales = QLabel(self.tab_3)
        self.bd_label_archivos_locales.setObjectName(u"bd_label_archivos_locales")
        self.bd_label_archivos_locales.setFont(font3)
        self.bd_label_archivos_locales.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_17.addWidget(self.bd_label_archivos_locales, 3, 2, 1, 2)

        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_21, 3, 0, 1, 2)

        self.bd_archivos_locales = QTreeWidget(self.tab_3)
        self.bd_archivos_locales.setObjectName(u"bd_archivos_locales")
        self.bd_archivos_locales.setEnabled(True)
        self.bd_archivos_locales.setFont(font2)
        self.bd_archivos_locales.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.bd_archivos_locales.setIndentation(25)
        self.bd_archivos_locales.setRootIsDecorated(True)
        self.bd_archivos_locales.setSortingEnabled(True)
        self.bd_archivos_locales.setAnimated(False)
        self.bd_archivos_locales.setWordWrap(False)
        self.bd_archivos_locales.header().setCascadingSectionResizes(False)
        self.bd_archivos_locales.header().setProperty(u"showSortIndicator", True)
        self.bd_archivos_locales.header().setStretchLastSection(True)

        self.gridLayout_17.addWidget(self.bd_archivos_locales, 4, 0, 1, 4)

        self.bd_descripcion = QTextBrowser(self.tab_3)
        self.bd_descripcion.setObjectName(u"bd_descripcion")
        self.bd_descripcion.setFont(font2)

        self.gridLayout_17.addWidget(self.bd_descripcion, 6, 0, 1, 4)

        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_17.addWidget(self.label_18, 5, 0, 1, 4)

        self.bd_parametros_locales = QTreeWidget(self.tab_3)
        self.bd_parametros_locales.setObjectName(u"bd_parametros_locales")
        self.bd_parametros_locales.setFont(font2)
        self.bd_parametros_locales.setSortingEnabled(True)
        self.bd_parametros_locales.header().setDefaultSectionSize(100)

        self.gridLayout_17.addWidget(self.bd_parametros_locales, 8, 0, 1, 4)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_17.addWidget(self.label_20, 7, 0, 1, 4)

        self.bd_seleccionar_carpeta = QPushButton(self.tab_3)
        self.bd_seleccionar_carpeta.setObjectName(u"bd_seleccionar_carpeta")
        self.bd_seleccionar_carpeta.setMinimumSize(QSize(0, 30))
        self.bd_seleccionar_carpeta.setMaximumSize(QSize(16777215, 40))
        self.bd_seleccionar_carpeta.setFont(font2)

        self.gridLayout_17.addWidget(self.bd_seleccionar_carpeta, 2, 2, 1, 1)

        self.bd_refrescar = QPushButton(self.tab_3)
        self.bd_refrescar.setObjectName(u"bd_refrescar")
        self.bd_refrescar.setMinimumSize(QSize(0, 30))
        self.bd_refrescar.setMaximumSize(QSize(16777215, 40))
        self.bd_refrescar.setFont(font2)

        self.gridLayout_17.addWidget(self.bd_refrescar, 2, 1, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_17, 0, 0, 3, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_2 = QVBoxLayout(self.tab_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_92 = QLabel(self.tab_6)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font)
        self.label_92.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_92)

        self.log = QTextBrowser(self.tab_6)
        self.log.setObjectName(u"log")
        self.log.setFont(font2)

        self.verticalLayout_2.addWidget(self.log)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.status = QLabel(Widget)
        self.status.setObjectName(u"status")
        sizePolicy3.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setBold(True)
        self.status.setFont(font4)

        self.horizontalLayout_2.addWidget(self.status)

        self.darkmode_button = QPushButton(Widget)
        self.darkmode_button.setObjectName(u"darkmode_button")
        sizePolicy5.setHeightForWidth(self.darkmode_button.sizePolicy().hasHeightForWidth())
        self.darkmode_button.setSizePolicy(sizePolicy5)
        self.darkmode_button.setMinimumSize(QSize(0, 30))
        self.darkmode_button.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.darkmode_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_84.setText(QCoreApplication.translate("Widget", u"Carpeta Local", None))
        self.label_91.setText(QCoreApplication.translate("Widget", u"Ingreso de Parametros", None))
        self.ingreso_crear_parametro.setText(QCoreApplication.translate("Widget", u"Crear Nuevo Parametro", None))
        self.ingreso_eliminar_archivo.setText(QCoreApplication.translate("Widget", u"Eliminar Archivo Seleccionado", None))
        self.ingreso_label_archivos_locales.setText("")
        self.ingreso_seleccionar_carpeta.setText(QCoreApplication.translate("Widget", u"Cambiar Carpeta Local", None))
        self.ingreso_refrescar.setText(QCoreApplication.translate("Widget", u"Refrescar", None))
        ___qtreewidgetitem = self.ingreso_archivos_locales.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Widget", u"Filename", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.ingreso_asignar_datapoint.setText(QCoreApplication.translate("Widget", u"Asignar Datapoint a Archivo", None))
        self.ingreso_unidad_parametro_1.setText("")
        self.ingreso_parametro_parametro_1.setItemText(0, QCoreApplication.translate("Widget", u"Presion", None))
        self.ingreso_parametro_parametro_1.setItemText(1, QCoreApplication.translate("Widget", u"-", None))
        self.ingreso_parametro_parametro_1.setItemText(2, QCoreApplication.translate("Widget", u"Voltaje Descarga", None))
        self.ingreso_parametro_parametro_1.setItemText(3, QCoreApplication.translate("Widget", u"Gas", None))

        self.label_88.setText(QCoreApplication.translate("Widget", u"Datapoint", None))
        self.ingreso_datapoint_parametro_3.setText("")
        self.ingreso_datapoint_parametro_1.setText("")
        self.label_89.setText(QCoreApplication.translate("Widget", u"Parametro", None))
        self.ingreso_valor_parametro_1.setText("")
        self.label_87.setText(QCoreApplication.translate("Widget", u"Valor", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"Unidad", None))
        self.ingreso_agregar_parametro_1.setText(QCoreApplication.translate("Widget", u"Agregar", None))
        self.ingreso_datapoint_parametro_2.setText("")
        self.ingreso_datapoint_parametro_4.setText("")
        self.ingreso_unidad_parametro_2.setText("")
        self.ingreso_unidad_parametro_3.setText("")
        self.ingreso_unidad_parametro_4.setText("")
        self.ingreso_parametro_parametro_2.setItemText(0, QCoreApplication.translate("Widget", u"Voltaje Descarga", None))
        self.ingreso_parametro_parametro_2.setItemText(1, QCoreApplication.translate("Widget", u"-", None))
        self.ingreso_parametro_parametro_2.setItemText(2, QCoreApplication.translate("Widget", u"Presion", None))
        self.ingreso_parametro_parametro_2.setItemText(3, QCoreApplication.translate("Widget", u"Gas", None))

        self.ingreso_parametro_parametro_3.setItemText(0, QCoreApplication.translate("Widget", u"Gas", None))
        self.ingreso_parametro_parametro_3.setItemText(1, QCoreApplication.translate("Widget", u"-", None))
        self.ingreso_parametro_parametro_3.setItemText(2, QCoreApplication.translate("Widget", u"Presion", None))
        self.ingreso_parametro_parametro_3.setItemText(3, QCoreApplication.translate("Widget", u"Voltaje Descarga", None))

        self.ingreso_parametro_parametro_4.setItemText(0, QCoreApplication.translate("Widget", u"-", None))
        self.ingreso_parametro_parametro_4.setItemText(1, QCoreApplication.translate("Widget", u"Presion", None))
        self.ingreso_parametro_parametro_4.setItemText(2, QCoreApplication.translate("Widget", u"Voltaje Descarga", None))
        self.ingreso_parametro_parametro_4.setItemText(3, QCoreApplication.translate("Widget", u"Gas", None))

        self.ingreso_valor_parametro_2.setText("")
        self.ingreso_valor_parametro_3.setText("")
        self.ingreso_valor_parametro_4.setText("")
        self.ingreso_agregar_parametro_2.setText(QCoreApplication.translate("Widget", u"Agregar", None))
        self.ingreso_agregar_parametro_3.setText(QCoreApplication.translate("Widget", u"Agregar", None))
        self.ingreso_agregar_parametro_4.setText(QCoreApplication.translate("Widget", u"Agregar", None))
        self.ingreso_agregar_archivo.setText(QCoreApplication.translate("Widget", u"Agregar Archivo a Carpeta", None))
        self.ingreso_descripcion.setPlainText("")
        self.ingreso_label_preview.setText("")
        ___qtreewidgetitem1 = self.ingreso_parametros.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("Widget", u"Tipo", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("Widget", u"Unidad", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Widget", u"Valor", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Widget", u"Par\u00e1metro", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.label_17.setText(QCoreApplication.translate("Widget", u"Preview", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"Descripcion", None))
        self.ingreso_guardar_descripcion.setText(QCoreApplication.translate("Widget", u"Guardar Descripcion", None))
        self.ingreso_preview_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ingreso_preview_image.setText("")
        self.label_28.setText(QCoreApplication.translate("Widget", u"Parametros Guardados", None))
        self.ingreso_eliminar_parametro.setText(QCoreApplication.translate("Widget", u"Eliminar Parametro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("Widget", u"Ingreso Manual", None))
        self.status_2.setText("")
        self.dispositivos_buscar.setText(QCoreApplication.translate("Widget", u"Buscar Dispositivos", None))
        self.dispositivos_conectar.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Osciloscopios Disponibles", None))
        ___qtreewidgetitem2 = self.dispositivos_dispositivos_disponibles.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Widget", u"id", None));
        self.label_14.setText(QCoreApplication.translate("Widget", u"Canales", None))
        self.dispositivos_agregar_canal.setText(QCoreApplication.translate("Widget", u"Agregar Canal", None))
        self.dispositivos_eliminar_canal.setText(QCoreApplication.translate("Widget", u"Eliminar Canal", None))
        ___qtreewidgetitem3 = self.dispositivos_canales.headerItem()
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("Widget", u"Datapoints", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("Widget", u"Dispositivo", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("Widget", u"Canal", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Widget", u"Nombre", None));
        self.dispositivos_desconectar.setText(QCoreApplication.translate("Widget", u"Desconectar Osciloscopio", None))
        self.dispositivos_agregar_ip.setText(QCoreApplication.translate("Widget", u"Conectar por IP", None))
        ___qtreewidgetitem4 = self.dispositivos_dispositivos_conectados.headerItem()
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("Widget", u"Conexion", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("Widget", u"Canales", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("Widget", u"Modelo", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Widget", u"id", None));
        self.label_13.setText(QCoreApplication.translate("Widget", u"Osciloscopios Conectados", None))
        self.dispositivos_cargar_perfil.setText(QCoreApplication.translate("Widget", u"Cargar Configuracion", None))
        self.dispositivos_guardar_perfil.setText(QCoreApplication.translate("Widget", u"Guardar Configuracion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Osciloscopios", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Carpeta Local", None))
        self.adquisicion_seleccionar_carpeta.setText(QCoreApplication.translate("Widget", u"Cambiar Carpeta Local", None))
        ___qtreewidgetitem5 = self.adquisicion_archivos_locales.headerItem()
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("Widget", u"Filename", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.adquisicion_label_archivos_locales.setText("")
        self.adquisicion_refrescar.setText(QCoreApplication.translate("Widget", u"Refrescar", None))
        ___qtreewidgetitem6 = self.adquisicion_origen_datos.headerItem()
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("Widget", u"Dispositivo", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("Widget", u"Canal", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Widget", u"Nombre", None));
        self.label_10.setText(QCoreApplication.translate("Widget", u"Canales", None))
        self.adquisicion_auto_guardar.setText(QCoreApplication.translate("Widget", u"Auto Guardar en Carpeta Local", None))
        self.adquisicion_seleccionar_carpeta_imagenes.setText(QCoreApplication.translate("Widget", u"Seleccionar Carpeta Imagenes", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Adquisicion Automatica en Cada Disparo", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Carpeta Origen Imagenes:", None))
        self.adquisicion_auto_imagenes.setText(QCoreApplication.translate("Widget", u"Auto Ingresar Imagenes", None))
        self.adquisicion_auto.setText(QCoreApplication.translate("Widget", u"Auto Adquirir ", None))
        self.adquisicion_label_carpeta_imagenes.setText("")
        self.label_11.setText(QCoreApplication.translate("Widget", u"Se\u00f1al de Trigger:", None))
        self.adquisicion_adquirir.setText(QCoreApplication.translate("Widget", u"Adquirir", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"Nombre Archivo:", None))
        self.adquisicion_guardar.setText(QCoreApplication.translate("Widget", u"Guardar", None))
        self.adquisicion_preview_text.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.adquisicion_preview_image.setText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"Preview", None))
        self.adquisicion_label_preview.setText("")
        self.label_23.setText(QCoreApplication.translate("Widget", u"Prefijo :", None))
        self.adquisicion_prefijo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Adquisicion", None))
        self.bd_agregar_experimento.setText(QCoreApplication.translate("Widget", u"Nuevo Experimento", None))
        self.bd_experimento.setItemText(0, QCoreApplication.translate("Widget", u"PF2J - Desgaste", None))

        self.label_3.setText(QCoreApplication.translate("Widget", u"Experimento", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Jornada", None))
        self.bd_jornada.setItemText(0, QCoreApplication.translate("Widget", u"25 Enero", None))
        self.bd_jornada.setItemText(1, QCoreApplication.translate("Widget", u"27 Abril", None))
        self.bd_jornada.setItemText(2, QCoreApplication.translate("Widget", u"03 Mayo", None))

        self.bd_agregar_jornada.setText(QCoreApplication.translate("Widget", u"Nueva Jornada", None))
        self.bd_subir.setText(QCoreApplication.translate("Widget", u"Subir Datos", None))
        self.bd_usuario.setText("")
        self.bd_password.setText("")
        self.bd_ip.setText(QCoreApplication.translate("Widget", u"200.28.103.190", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"IP Servidor", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.bd_refrescar_servidor.setText(QCoreApplication.translate("Widget", u"Conectar / Refrescar Servidor", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Archivos Servidor", None))
        ___qtreewidgetitem7 = self.bd_archivos_servidor.headerItem()
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("Widget", u"Filename", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.label_24.setText(QCoreApplication.translate("Widget", u"Parametros Servidor", None))
        ___qtreewidgetitem8 = self.bd_parametros_servidor.headerItem()
        ___qtreewidgetitem8.setText(3, QCoreApplication.translate("Widget", u"Unidad", None));
        ___qtreewidgetitem8.setText(2, QCoreApplication.translate("Widget", u"Valor", None));
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("Widget", u"Par\u00e1metro", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.bd_label_archivos_locales.setText("")
        self.label_21.setText(QCoreApplication.translate("Widget", u"Archivos Locales", None))
        ___qtreewidgetitem9 = self.bd_archivos_locales.headerItem()
        ___qtreewidgetitem9.setText(3, QCoreApplication.translate("Widget", u"Subir", None));
        ___qtreewidgetitem9.setText(2, QCoreApplication.translate("Widget", u"En Servidor", None));
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("Widget", u"Filename", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.bd_descripcion.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"Descripcion", None))
        ___qtreewidgetitem10 = self.bd_parametros_locales.headerItem()
        ___qtreewidgetitem10.setText(4, QCoreApplication.translate("Widget", u"Subir", None));
        ___qtreewidgetitem10.setText(3, QCoreApplication.translate("Widget", u"Unidad", None));
        ___qtreewidgetitem10.setText(2, QCoreApplication.translate("Widget", u"Valor", None));
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("Widget", u"Par\u00e1metro", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("Widget", u"Datapoint", None));
        self.label_20.setText(QCoreApplication.translate("Widget", u"Parametros Locales", None))
        self.bd_seleccionar_carpeta.setText(QCoreApplication.translate("Widget", u"Cambiar Carpeta Local", None))
        self.bd_refrescar.setText(QCoreApplication.translate("Widget", u"Refrescar Carpeta Local", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Base de Datos", None))
        self.label_92.setText(QCoreApplication.translate("Widget", u"Registro de Eventos", None))
        self.log.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Widget", u"Registro", None))
        self.status.setText(QCoreApplication.translate("Widget", u"Status: OK", None))
        self.darkmode_button.setText(QCoreApplication.translate("Widget", u"Darkmode", None))
    # retranslateUi

