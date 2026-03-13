from ventanaPrincipal import Ui_Widget
from agregarCanal import Ui_AgregarCanal
from agregarExperimento import Ui_AgregarExperimento
from agregarJornada import Ui_AgregarJornada
from asignarDatapoint import Ui_AsignarDatapoint
from crearParametro import Ui_CrearParametro
from desconectarDispositivo import Ui_DesconectarDispositivo
from guardarDescripcion import Ui_GuardarDescripcion
from dispositivoIp import Ui_DispositivoIp
from eliminarArchivo import Ui_EliminarArchivo
from eliminarParametro import Ui_EliminarParametro
from eliminarCanal import Ui_EliminarCanal
from subirBd import Ui_Subir

import sys
import os
import shutil
import paramiko
import pymongo
import datetime
import unicodedata
import re
import time
import json
import pyvisa
import pyvisa_py
import zeroconf

# Backends for pyvisa-py (ensure these are included in the PyInstaller spec file)
import usb.core
import usb.util
import serial
import serial.tools.list_ports
import gpib_ctypes

import numpy as np
import pandas as pd
from PySide6.QtGui import QPixmap, QTextCursor, QIcon, QShortcut, QPalette, QColor
from PySide6.QtCore import Qt, QObject, Signal, QThread
from PySide6 import QtWidgets
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


# File type constants for cleaner extension checking
CSV_EXTENSIONS = ('.csv',)
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
TEXT_EXTENSIONS = ('.txt', '.json', '.config', '.py')

# Global VISA backend state
_visa_backend = None  # Will be 'native', 'pyvisa-py', or None
_resource_manager = None  # Cached ResourceManager instance

def get_resource_manager(force_new=False):
    """Get working VISA ResourceManager with automatic backend fallback.
    
    Tries native VISA first (TekVisa, NI-VISA) which supports GPIB/USB/Serial.
    Falls back to pyvisa-py for machines without vendor drivers (TCPIP/Serial only).
    
    Args:
        force_new: If True, create a new ResourceManager instead of using cached one.
        
    Returns:
        tuple: (ResourceManager, backend_name) or (None, None) if no backend works
    """
    global _visa_backend, _resource_manager
    
    # Return cached manager if available and not forcing new
    if not force_new and _resource_manager is not None:
        return _resource_manager, _visa_backend
    
    # Try native VISA first (supports GPIB, USB, everything)
    try:
        rm = pyvisa.ResourceManager()
        rm.list_resources()  # Test if it actually works
        _resource_manager = rm
        _visa_backend = 'native'
        return rm, 'native'
    except Exception:
        pass
    
    # Fall back to pyvisa-py (TCPIP/Serial only, but no drivers needed)
    try:
        rm = pyvisa.ResourceManager('@py')
        rm.list_resources()  # Test if it works
        _resource_manager = rm
        _visa_backend = 'pyvisa-py'
        return rm, 'pyvisa-py'
    except Exception:
        pass
    
    _visa_backend = None
    _resource_manager = None
    return None, None

def get_visa_backend():
    """Return the currently active VISA backend name."""
    return _visa_backend


class TriggerWorker(QObject):

    finished = Signal()
    trigger = Signal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.pause = False

    def set_source(self, source):
        rm, _ = get_resource_manager()
        self.device = rm.open_resource(source)
        self.device.timeout = 10 * 1000
        self.current_count = self.device.query('ACQuire:NUMACq?')
        self.source = source
    
    def count(self):
        try:
            count = self.device.query('ACQuire:NUMACq?')
            if count != self.current_count:
                self.current_count = count
                return True
            else:
                return False
        except Exception:
            return False

    def run(self):
        self.running = True
        while self.running:
            if not self.pause:
                if self.count():
                    self.trigger.emit(self.current_count)
                    self.pause = True
                time.sleep(1)
            else:
                time.sleep(0.1)  # Sleep when paused to avoid busy-looping
        self.finished.emit()

class ImageWorker(QObject):

    finished = Signal()
    msg = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.new_files = []
        self.files = []

    def set_folder(self, folder):
        self.folder = folder
        self.files = set(os.listdir(folder))  # Use set for O(1) lookup
    
    def check(self):
        current_files = set(os.listdir(self.folder))
        self.new_files = list(current_files - self.files)  # Set difference is O(n) vs O(n²)
        self.files = current_files
        return len(self.new_files) > 0

    def run(self):
        self.running = True
        while self.running:
            time.sleep(0.5)
            if self.check():
                message = ''
                for file in self.new_files:
                    if file == self.new_files[-1]:
                        message += file
                    else:
                        message += file + '*'
                self.msg.emit(message)
        self.finished.emit()

class DataWorker(QObject):

    finished = Signal()
    response = Signal(object)

    def __init__(self):
        super().__init__()

    def set_device(self, device_name, channels, existing_device=None): 
        """Set up device for acquisition.
        
        Args:
            device_name: VISA resource name
            channels: dict like {'CH1':{'nombre': 'ch1', 'datapoints':10000}}
            existing_device: Reuse existing pyvisa device connection if provided
        """
        self.device_name = device_name
        self.channels = channels
        # Reuse existing connection if available (faster than creating new ResourceManager)
        if existing_device is not None:
            self.device = existing_device
        else:
            rm, _ = get_resource_manager()
            self.device = rm.open_resource(device_name)
        self.device.timeout = 10 * 1000
        self.done = False

    def get_data(self):
        """
        Acquire waveform data from oscilloscope using binary encoding for optimal performance.
        Binary transfer is 3-5x faster than ASCII due to smaller data size and faster parsing.
        """
        i = 0

        for chan_id in self.channels:

            channel = self.channels[chan_id]
            i += 1
        
            try:
                ti = time.time()
                
                # Configure for binary transfer using single combined command (reduces USB/GPIB overhead)
                # SRIbinary = signed little-endian (native for x86, fastest)
                config_cmd = (
                    f':DATA:ENCDG SRIbinary;'
                    f':DATA:WIDTH 2;'
                    f':DATA:START 1;'
                    f':DATA:STOP {channel["datapoints"]};'
                    f':HEADER 0;'
                    f':DATA:SOURCE {chan_id}'
                )
                self.device.write(config_cmd)
                
                # Get waveform preamble (scaling info) separately
                preamble = self.device.query(':WFMPRE?')
                
                # Parse scaling parameters from preamble
                # Tektronix oscilloscopes return preamble in positional format:
                # BYT_Nr;BIT_Nr;ENCDG;BN_Fmt;BYT_Or;NR_Pt;"WFID";PT_Fmt;XINCR;PT_Off;XZERO;XUNIT;YMULT;YZERO;YOFF;YUNIT
                # Positions: 8=XINCR, 10=XZERO, 12=YMULT, 13=YZERO, 14=YOFF
                
                y_zero = 0.0
                y_mult = 1.0
                y_off = 0.0
                x_zero = 0.0
                x_incr = 1.0
                
                try:
                    # Split preamble by semicolon
                    parts = preamble.strip().split(';')
                    
                    # Helper to safely parse float from preamble part
                    def safe_float(s):
                        s = s.strip().strip('"')
                        try:
                            return float(s)
                        except ValueError:
                            return None
                    
                    # Extract values by position (Tektronix standard positions)
                    if len(parts) >= 15:
                        x_incr = safe_float(parts[8]) or 1.0   # XINCR - time per point
                        x_zero = safe_float(parts[10]) or 0.0  # XZERO - time of first point
                        y_mult = safe_float(parts[12]) or 1.0  # YMULT - voltage scale
                        y_zero = safe_float(parts[13]) or 0.0  # YZERO - voltage offset
                        y_off = safe_float(parts[14]) or 0.0   # YOFF - ADC offset
                        
                except Exception as e:
                    print(f'Error parsing preamble: {e}')
                    print(f'Preamble was: {repr(preamble)}')
                
                # Query binary curve data
                self.device.write(':CURVE?')
                
                # Read binary block data with IEEE 488.2 format: #<n><length><data>
                raw_data = self.device.read_raw()
                
                # Parse IEEE 488.2 binary block header
                # Format: #<digit_count><byte_count><binary_data>
                if raw_data[0:1] == b'#':
                    digit_count = int(raw_data[1:2])
                    byte_count = int(raw_data[2:2+digit_count])
                    data_start = 2 + digit_count
                    binary_data = raw_data[data_start:data_start + byte_count]
                else:
                    raise ValueError('Invalid binary block header')
                
                # Convert binary data to numpy array (signed 16-bit little-endian)
                y_raw = np.frombuffer(binary_data, dtype='<i2')  # Little-endian signed 16-bit
                
                # Apply scaling: voltage = (raw - yoff) * ymult + yzero
                # Use in-place operations where possible for memory efficiency
                y = y_raw.astype(np.float64)
                if y_off != 0:
                    y -= y_off
                if y_mult != 1:
                    y *= y_mult
                if y_zero != 0:
                    y += y_zero
                
                # Generate x (time) array - use float64 multiplication for precision
                n_points = len(y)
                x = np.arange(n_points, dtype=np.float64) * x_incr + x_zero

                datos = {'x': x, 'y': y, 'header': preamble}    
                
                self.response.emit({
                    'exito': True, 
                    'datos': datos, 
                    'dispositivo': self.device_name, 
                    'canal': chan_id, 
                    'tiempo': time.time() - ti, 
                    'ultimo': i == len(self.channels)
                })
                
            except Exception as e:
                print('Error adquiriendo datos:')
                print(str(e) + '\n')
                self.response.emit({'exito' : False, 'dispositivo' : self.device_name, 'canal' : chan_id, 'tiempo': time.time()-ti, 'ultimo':i==len(self.channels)})

        self.done = True
        self.finished.emit()

class Lab_Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Lab_Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.carpeta_local = ''
        self.carpeta_imagenes = ''
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        self.color_palette = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        
        # Initialize VISA with auto-detect backend
        self.manager, backend = get_resource_manager()
        if self.manager is None:
            self.print('Error inicializando ResourceManager de PyVISA. No se encontro ningun backend funcional.')
            self.print('Algunas funciones de adquisicion pueden no estar disponibles.')
        elif backend == 'pyvisa-py':
            self.print('Usando backend pyvisa-py (soporte limitado: TCPIP y Serial solamente)')
            self.print('Para soporte GPIB/USB, instale TekVisa o NI-VISA')
        else:
            self.print('Usando backend VISA nativo (soporte completo: GPIB, USB, TCPIP, Serial)')
        
        self.dispositivos_disponibles = []
        self.dispositivos_conectados = {}
        self.datos = {}
        self.parametros = {}
        self.indice = {}
        self.contador_trigger = {}
        self.nombres_parametros = {}
        self.archivos_servidor = {}

        self.data_workers = []
        self.data_threads = []
        
        self.trigger_worker = TriggerWorker()
        self.trigger_thread = QThread()
        self.image_thread = QThread()
        self.image_worker = ImageWorker()

        self.darkmode = None  # Will be set during apply_initial_theme
        self.adquisicion_en_progreso = False  # Lock flag to prevent concurrent acquisitions


        self.cargar_parametros()
        self.cargar_indice()
        self.cargar_descripcion()
        self.refrescar_archivos_locales()

        
        self.ui.adquisicion_auto.setCheckable(True)


        self.ui.bd_refrescar.clicked.connect(self.refrescar_archivos_locales)
        self.ui.ingreso_refrescar.clicked.connect(self.refrescar_archivos_locales)
        self.ui.adquisicion_refrescar.clicked.connect(self.refrescar_archivos_locales)
        self.ui.bd_seleccionar_carpeta.clicked.connect(self.seleccionar_carpeta)
        self.ui.ingreso_seleccionar_carpeta.clicked.connect(self.seleccionar_carpeta)
        self.ui.adquisicion_seleccionar_carpeta.clicked.connect(self.seleccionar_carpeta)

        self.ui.adquisicion_archivos_locales.itemDoubleClicked.connect(self.adquisicion_visualizar_archivo)
        self.ui.ingreso_archivos_locales.itemDoubleClicked.connect(self.ingreso_visualizar_archivo)
        
        # Set background color to transparent for all preview widgets
        self.ui.adquisicion_preview_graph.setBackground((0,0,0,0))
        self.ui.adquisicion_preview_image.setStyleSheet("background-color: transparent;")
        self.ui.adquisicion_preview_text.setStyleSheet("background-color: transparent;")
        self.ui.ingreso_preview_graph.setBackground((0,0,0,0))
        self.ui.ingreso_preview_image.setStyleSheet("background-color: transparent;")
        self.ui.ingreso_preview_text.setStyleSheet("background-color: transparent;")
        self.ui.frame.setStyleSheet("background-color: transparent;")
        self.ui.frame_2.setStyleSheet("background-color: transparent;")


        # Disable the text, image and graph widgets until a file is selected
        self.ui.adquisicion_preview_graph.setVisible(False)
        self.ui.adquisicion_preview_image.setVisible(False)
        self.ui.adquisicion_preview_text.setVisible(False)
        self.ui.ingreso_preview_graph.setVisible(False)
        self.ui.ingreso_preview_image.setVisible(False)
        self.ui.ingreso_preview_text.setVisible(False)



        self.ui.dispositivos_conectar.clicked.connect(self.conectar)
        self.ui.dispositivos_buscar.clicked.connect(self.buscar_dispositivos)

        self.ui.dispositivos_agregar_canal.clicked.connect(self.popup_agregar_canal)
        self.ui.dispositivos_agregar_ip.clicked.connect(self.popup_conectar_dispositivo_ip)
        self.ui.ingreso_asignar_datapoint.clicked.connect(self.popup_asignar_datapoint)
        self.ui.ingreso_eliminar_archivo.clicked.connect(self.popup_eliminar_archivo)
        self.ui.ingreso_eliminar_parametro.clicked.connect(self.popup_eliminar_parametro)
        self.ui.bd_subir.clicked.connect(self.popup_subir)
        self.ui.ingreso_guardar_descripcion.clicked.connect(self.popup_guardar_descripcion)
        self.ui.dispositivos_desconectar.clicked.connect(self.popup_desconectar_dispositivo)
        self.ui.dispositivos_eliminar_canal.clicked.connect(self.popup_eliminar_canal)
        self.ui.bd_agregar_experimento.clicked.connect(self.popup_agregar_experimento)
        self.ui.bd_agregar_jornada.clicked.connect(self.popup_agregar_jornada)


        self.ui.dispositivos_guardar_perfil.clicked.connect(self.guardar_perfil)
        self.ui.dispositivos_cargar_perfil.clicked.connect(self.cargar_perfil)

        self.ui.adquisicion_adquirir.clicked.connect(self.adquirir_datos)
        self.ui.adquisicion_auto.clicked.connect(self.auto)
        self.ui.adquisicion_guardar.clicked.connect(self.guardar_datos)

        self.ui.adquisicion_seleccionar_carpeta_imagenes.clicked.connect(self.seleccionar_carpeta_imagenes)
        self.ui.ingreso_agregar_archivo.clicked.connect(self.agregar_archivo)
        self.ui.ingreso_agregar_parametro_1.clicked.connect(self.agregar_valor_parametro_1)
        self.ui.ingreso_agregar_parametro_2.clicked.connect(self.agregar_valor_parametro_2)
        self.ui.ingreso_agregar_parametro_3.clicked.connect(self.agregar_valor_parametro_3)
        self.ui.ingreso_agregar_parametro_4.clicked.connect(self.agregar_valor_parametro_4)

        self.ui.ingreso_crear_parametro.clicked.connect(self.popup_crear_parametro)

        self.ui.darkmode_button.clicked.connect(self.toggle_darkmode)

        self.ui.bd_refrescar_servidor.clicked.connect(self.refrescar_servidor)

        self.ui.bd_experimento.currentIndexChanged.connect(self.refrescar_jornadas)
        self.ui.bd_jornada.currentIndexChanged.connect(self.refrescar_archivos_servidor)

        self.print('Programa inicializado - ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

        self.refrescar_servidor()

    def refrescar_jornadas(self):
        
        experimento = self.ui.bd_experimento.currentText()

        self.ui.bd_jornada.currentIndexChanged.disconnect()

        self.ui.bd_jornada.clear()
        if self.mongo_client is not None:
            self.ui.bd_jornada.addItems([x['nombre'] for x in self.mongo_client.db.jornadas.find({'experimento':experimento})])

        self.ui.bd_jornada.currentIndexChanged.connect(self.refrescar_archivos_servidor)
        self.refrescar_archivos_servidor()

    def refrescar_archivos_servidor(self):        
        
        experimento = self.ui.bd_experimento.currentText()
        jornada = self.ui.bd_jornada.currentText()

        self.archivos_servidor = {}
        self.parametros_servidor = []
        
        if self.mongo_client is None:
            self.print('Error refrezcando archivos del servidor: Servidor desconectado')
            self.ui.status.setText('Status: Error')
            return
        
        for archivo in self.mongo_client.db.indice.find({'experimento':experimento, 'jornada':jornada}):
            self.archivos_servidor[archivo['nombre']] = archivo['datapoint']

        for parametro in self.mongo_client.db.parametros.find({'experimento':experimento, 'jornada':jornada}):
            self.parametros_servidor.append({'parametro':parametro['parametro'],  'datapoint':parametro['datapoint'],  'valor':str(parametro['valor']),  'unidad':parametro['unidad']})

        items = []
        i=0
        for archivo in self.archivos_servidor:
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, self.archivos_servidor[archivo])
            item.setText(1, archivo)
            items.append(item)
            i+=1

        self.ui.bd_archivos_servidor.clear()
        self.ui.bd_archivos_servidor.addTopLevelItems(items)

        items = []
        i=0
        for parametro in self.parametros_servidor:
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, parametro['datapoint'])
            item.setText(1, parametro['parametro'])
            item.setText(2, parametro['valor'])
            item.setText(3, parametro['unidad'])
            items.append(item)
            i+=1

        self.ui.bd_parametros_servidor.clear()
        self.ui.bd_parametros_servidor.addTopLevelItems(items)

        self.refrescar_archivos_locales()
        self.refrescar_parametros()

    def refrescar_servidor(self):

        try:
            self.mongo_client = pymongo.MongoClient(self.ui.bd_ip.text(), username=self.ui.bd_usuario.text(), password=self.ui.bd_password.text(), serverSelectionTimeoutMS = 3000)
            self.nombres_parametros = {}
            for parametro in self.mongo_client.db.nombres_parametros.find({}):
                self.nombres_parametros[parametro['nombre']] = parametro['tipo']
            self.print('Conexion a base de datos exitosa')
            self.print('Guardando nombres de parametros localmente')
            dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')           
            with open(dir_path + '/nombres_parametros.txt', 'w') as archivo_nombres_parametros:
                json.dump(self.nombres_parametros, archivo_nombres_parametros, indent = 4)
            self.ui.status.setText('Status: OK')

        except Exception as e:
            self.mongo_client = None
            self.print('Error conectando a base de datos del servidor')
            self.print(str(e) + '\n')
            self.print('Operando en modo offline')
            self.ui.status.setText('Status: Error')
            dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
            if 'nombres_parametros.txt' in os.listdir(dir_path):
                with open(dir_path + '/nombres_parametros.txt', 'r') as archivo_nombres_parametros:
                    self.nombres_parametros = json.load(archivo_nombres_parametros)
            else:
                self.nombres_parametros = {}
                
        self.refrescar_nombres_parametros()

        
        self.ui.bd_experimento.currentIndexChanged.disconnect()
        
        self.ui.bd_experimento.clear()
        if self.mongo_client is not None:
            self.ui.bd_experimento.addItems([x['nombre'] for x in self.mongo_client.db.experimentos.find({})])

        self.ui.bd_experimento.currentIndexChanged.connect(self.refrescar_jornadas)

        self.refrescar_jornadas()

    def refrescar_nombres_parametros(self):
        
        self.ui.ingreso_parametro_parametro_1.clear()
        self.ui.ingreso_parametro_parametro_1.addItems([x for x in self.nombres_parametros])
        
        self.ui.ingreso_parametro_parametro_2.clear()
        self.ui.ingreso_parametro_parametro_2.addItems([x for x in self.nombres_parametros])
        
        self.ui.ingreso_parametro_parametro_3.clear()
        self.ui.ingreso_parametro_parametro_3.addItems([x for x in self.nombres_parametros])
        
        self.ui.ingreso_parametro_parametro_4.clear()
        self.ui.ingreso_parametro_parametro_4.addItems([x for x in self.nombres_parametros])

    def buscar_dispositivos(self):

        try:
            self.dispositivos_disponibles = [x for x in self.manager.list_resources()]
        except Exception as e:
            self.print('Error buscando dispositivos:\n' + str(e))
            self.dispositivos_disponibles = []

        items = []
        i=0
        for dispositivo in self.dispositivos_disponibles:
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, dispositivo)
            items.append(item)

        self.ui.dispositivos_dispositivos_disponibles.clear()
        self.ui.dispositivos_dispositivos_disponibles.addTopLevelItems(items)

    def conectar(self):
        try:
            nombre = self.ui.dispositivos_dispositivos_disponibles.selectedItems()[0].text(0)
            dispositivo = self.manager.open_resource(nombre)
            
            try:
                dispositivo.timeout = 3 * 1000
                modelo = dispositivo.query('*IDN?')
                if len(modelo.split(',')) > 1:
                    modelo = modelo.split(',')[1]
                dispositivo.timeout = 10 * 1000
            except Exception as e:
                self.print('Error conectando dispositivo, modelo no identificado:')
                self.print(str(e) + '\n')
                self.ui.status.setText('Status: Error')
                return
            self.dispositivos_conectados [nombre] = {'dispositivo':dispositivo, 'canales':{}, 'conexion':'USB', 'modelo':modelo} #canales = {'ch1': 'canal 1', 'ch2': 'canal 2'  }
            self.datos[nombre] = {}
            self.print('Dispositivo conectado: ' + nombre + ' - ' + modelo)
            self.ui.status.setText('Status: OK')
            items = []
            i=0
            for id_dispositivo in self.dispositivos_conectados:
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, id_dispositivo)
                item.setText(1, self.dispositivos_conectados[id_dispositivo]['modelo'])
                item.setText(2, str(len(self.dispositivos_conectados[id_dispositivo]['canales'])))
                item.setText(3, self.dispositivos_conectados[id_dispositivo]['conexion'])
                items.append(item)

            self.ui.dispositivos_dispositivos_conectados.clear()
            self.ui.dispositivos_dispositivos_conectados.addTopLevelItems(items)

            self.ui.adquisicion_fuente_trigger.clear()
            self.ui.adquisicion_fuente_trigger.addItems([x + ' - ' + self.dispositivos_conectados[x]['modelo'] for x in self.dispositivos_conectados])
        except Exception as e:
            self.print('Error conectando dispositivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
 
    def conectar_dispositivo_ip(self):
        try:
            ip = self.ui_conectar_dispositivo_ip.ip.text()
            nombre = 'TCPIP0::' + str(ip).replace(' ','') + '::INSTR'
            dispositivo = self.manager.open_resource(nombre)
            try:
                dispositivo.timeout = 3 * 1000
                modelo = dispositivo.query('*IDN?')
                if len(modelo.split(',')) > 1:
                    modelo = modelo.split(',')[1]
                dispositivo.timeout = 10 * 1000
            except Exception as e:
                self.print('Error conectando dispositivo, modelo no identificado:')
                self.print(str(e) + '\n')
                self.ui.status.setText('Status: Error')
                self.dialog_conectar_dispositivo_ip.done(1)
                return
            self.dispositivos_conectados [nombre] = {'dispositivo':dispositivo, 'canales':{}, 'conexion':'TCP/IP', 'modelo':modelo} #canales = {'ch1': 'canal 1', 'ch2': 'canal 2'  }
            self.datos[nombre] = {}
            self.print('Dispositivo conectado: ' + nombre + ' - ' + modelo)
            self.ui.status.setText('Status: OK')
            items = []
            i=0
            for nombre_dispositivo in self.dispositivos_conectados:
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, nombre_dispositivo)
                item.setText(1, self.dispositivos_conectados[nombre_dispositivo]['modelo'])
                item.setText(2, str(len(self.dispositivos_conectados[nombre_dispositivo]['canales'])))
                item.setText(3, self.dispositivos_conectados[nombre_dispositivo]['conexion'])
                items.append(item)

            self.ui.dispositivos_dispositivos_conectados.clear()
            self.ui.dispositivos_dispositivos_conectados.addTopLevelItems(items)

            self.ui.adquisicion_fuente_trigger.clear()
            self.ui.adquisicion_fuente_trigger.addItems([x + ' - ' + self.dispositivos_conectados[x]['modelo'] for x in self.dispositivos_conectados])
            self.dialog_conectar_dispositivo_ip.done(1)

        except Exception as e:
            self.print('Error conectando dispositivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
            self.dialog_conectar_dispositivo_ip.done(1)

    def desconectar_dispositivo(self):
        try:
            nombre = self.ui.dispositivos_dispositivos_conectados.selectedItems()[0].text(0)
            if nombre in self.dispositivos_conectados:
                del self.dispositivos_conectados[nombre]
                del self.datos[nombre]
                self.print('Dispositivo desconectado: '+ nombre)     
                self.ui.status.setText('Status: OK')       
                self.ui.adquisicion_fuente_trigger.clear()
                self.ui.adquisicion_fuente_trigger.addItems([x + ' - ' + self.dispositivos_conectados[x]['modelo'] for x in self.dispositivos_conectados])
                self.actualizar_canales()
                self.dialog_desconectar_dispositivo.done(1)
        except Exception as e:
            self.print('Error desconectando dispositivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def agregar_jornada(self):

        nombre = self.ui_agregar_jornada.nombre.text()
        experimento = self.ui_agregar_jornada.experimento.currentText()

        if self.mongo_client is None:
            self.print('Error agregando jornada: Servidor desconectado')
            self.ui.status.setText('Status: Error')
            return
        if self.mongo_client.db.jornadas.count_documents({'nombre':nombre, 'experimento':experimento}) < 1:
            self.mongo_client.db.jornadas.insert_one({'nombre':nombre, 'experimento':experimento})
            self.refrescar_servidor()
            self.ui.status.setText('Status: OK')
            self.dialog_agregar_jornada.done(1)
        else:
            self.print('Jornada ' + nombre + ' ya existe en experimento ' + experimento)
            self.ui.status.setText('Status: Error')
            self.dialog_agregar_jornada.done(1)

    def agregar_experimento(self):

        nombre = self.ui_agregar_experimento.nombre.text()

        if self.mongo_client is None:
            self.print('Error agregando experimento: Servidor desconectado')
            self.ui.status.setText('Status: Error')
            return
        if self.mongo_client.db.experimentos.count_documents({'nombre':nombre}) < 1:
            self.mongo_client.db.experimentos.insert_one({'nombre':nombre})
            self.refrescar_servidor()
            self.ui.status.setText('Status: OK')
            self.dialog_agregar_experimento.done(1)
        else:
            self.print('Experimento ' + nombre + ' ya existe')
            self.ui.status.setText('Status: Error')
            self.dialog_agregar_experimento.done(1)

    def popup_agregar_experimento(self):
        self.dialog_agregar_experimento = QtWidgets.QDialog()
        self.ui_agregar_experimento = Ui_AgregarExperimento()
        self.ui_agregar_experimento.setupUi(self.dialog_agregar_experimento)

        self.ui_agregar_experimento.cancelar.clicked.connect(lambda: self.dialog_agregar_experimento.done(1))
        self.ui_agregar_experimento.agregar.clicked.connect(self.agregar_experimento)

        self.dialog_agregar_experimento.exec()

    def popup_agregar_jornada(self):
        self.dialog_agregar_jornada = QtWidgets.QDialog()
        self.ui_agregar_jornada = Ui_AgregarJornada()
        self.ui_agregar_jornada.setupUi(self.dialog_agregar_jornada)

        self.ui_agregar_jornada.experimento.clear()
        
        if self.mongo_client is not None:            
            self.ui_agregar_jornada.experimento.addItems([x['nombre'] for x in self.mongo_client.db.experimentos.find({})])

        self.ui_agregar_jornada.cancelar.clicked.connect(lambda: self.dialog_agregar_jornada.done(1))
        self.ui_agregar_jornada.agregar.clicked.connect(self.agregar_jornada)

        self.dialog_agregar_jornada.exec()

    def popup_conectar_dispositivo_ip(self):
        self.dialog_conectar_dispositivo_ip = QtWidgets.QDialog()
        self.ui_conectar_dispositivo_ip = Ui_DispositivoIp()
        self.ui_conectar_dispositivo_ip.setupUi(self.dialog_conectar_dispositivo_ip)

        self.ui_conectar_dispositivo_ip.cancelar.clicked.connect(lambda: self.dialog_conectar_dispositivo_ip.done(1))
        self.ui_conectar_dispositivo_ip.conectar.clicked.connect(self.conectar_dispositivo_ip)

        self.dialog_conectar_dispositivo_ip.exec()

    def actualizar_canales_popup(self):
        
        canales_disponibles = ['CH1', 'CH2', 'CH3', 'CH4', 'MATH']

        nombre_osc = self.ui_agregar_canal.osciloscopio.currentText().split(' - ')[0]
        if nombre_osc == '':
            return        
            
        for chan_id in self.dispositivos_conectados[nombre_osc]['canales']:
            if chan_id in canales_disponibles:
                canales_disponibles.remove(chan_id)

        self.ui_agregar_canal.canal.clear()
        self.ui_agregar_canal.canal.addItems(canales_disponibles)

    def popup_agregar_canal(self):        
        
        self.dialog_agregar_canal = QtWidgets.QDialog()
        self.ui_agregar_canal = Ui_AgregarCanal()
        self.ui_agregar_canal.setupUi(self.dialog_agregar_canal)


        self.ui_agregar_canal.cancelar.clicked.connect(lambda: self.dialog_agregar_canal.done(1))
        self.ui_agregar_canal.agregar.clicked.connect(self.agregar_canal)

        self.ui_agregar_canal.osciloscopio.addItems([x + ' - ' + self.dispositivos_conectados[x]['modelo'] for x in self.dispositivos_conectados])
        self.ui_agregar_canal.osciloscopio.currentIndexChanged.connect(self.actualizar_canales_popup)
        self.actualizar_canales_popup()

        self.dialog_agregar_canal.exec()

    def popup_asignar_datapoint(self):        
        
        self.dialog_asignar_datapoint = QtWidgets.QDialog()
        self.ui_asignar_datapoint = Ui_AsignarDatapoint()
        self.ui_asignar_datapoint.setupUi(self.dialog_asignar_datapoint)
        
        self.ui_asignar_datapoint.preview_graph.setBackground('white')
        
        self.ui_asignar_datapoint.datapoint.setText(self.ui.ingreso_archivos_locales.selectedItems()[0].text(0))

        self.ui_asignar_datapoint.cancelar.clicked.connect(lambda: self.dialog_asignar_datapoint.done(1))
        self.ui_asignar_datapoint.asignar.clicked.connect(self.asignar_datapoint)

        
        try:

            archivo = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)        
            filepath = self.carpeta_local + '/' + archivo
            filepath_lower = filepath.lower()
            
            if filepath_lower.endswith(CSV_EXTENSIONS):
                self.visualizar_csv(filepath, self.ui_asignar_datapoint.preview_graph, self.ui_asignar_datapoint.preview_image, self.ui_asignar_datapoint.preview_text, self.ui_asignar_datapoint.archivo)

            elif filepath_lower.endswith(IMAGE_EXTENSIONS):
                self.visualizar_imagen(filepath, self.ui_asignar_datapoint.preview_graph, self.ui_asignar_datapoint.preview_image, self.ui_asignar_datapoint.preview_text, self.ui_asignar_datapoint.archivo)

            elif filepath_lower.endswith(TEXT_EXTENSIONS):
                self.visualizar_texto(filepath, self.ui_asignar_datapoint.preview_graph, self.ui_asignar_datapoint.preview_image, self.ui_asignar_datapoint.preview_text, self.ui_asignar_datapoint.archivo)

            else:
                self.ui_asignar_datapoint.preview_graph.setVisible(False)
                self.ui_asignar_datapoint.preview_image.setVisible(False)
                self.ui_asignar_datapoint.preview_text.setVisible(False)

        except Exception as e:
            self.print('Error asignando datapoint:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

        self.dialog_asignar_datapoint.exec()

    def popup_eliminar_archivo(self):        
        
        self.dialog_eliminar_archivo = QtWidgets.QDialog()
        self.ui_eliminar_archivo = Ui_EliminarArchivo()
        self.ui_eliminar_archivo.setupUi(self.dialog_eliminar_archivo)
        
        self.ui_eliminar_archivo.preview_graph.setBackground('white')

        self.ui_eliminar_archivo.cancelar.clicked.connect(lambda: self.dialog_eliminar_archivo.done(1))
        self.ui_eliminar_archivo.eliminar.clicked.connect(self.eliminar_archivo)


        try:

            archivo = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)        
            filepath = self.carpeta_local + '/' + archivo
            filepath_lower = filepath.lower()

            if filepath_lower.endswith(CSV_EXTENSIONS):
                self.visualizar_csv(filepath, self.ui_eliminar_archivo.preview_graph, self.ui_eliminar_archivo.preview_image, self.ui_eliminar_archivo.preview_text, self.ui_eliminar_archivo.archivo)

            elif filepath_lower.endswith(IMAGE_EXTENSIONS):
                self.visualizar_imagen(filepath, self.ui_eliminar_archivo.preview_graph, self.ui_eliminar_archivo.preview_image, self.ui_eliminar_archivo.preview_text, self.ui_eliminar_archivo.archivo)

            elif filepath_lower.endswith(TEXT_EXTENSIONS):
                self.visualizar_texto(filepath, self.ui_eliminar_archivo.preview_graph, self.ui_eliminar_archivo.preview_image, self.ui_eliminar_archivo.preview_text, self.ui_eliminar_archivo.archivo)

            else:
                self.ui_eliminar_archivo.preview_graph.setVisible(False)
                self.ui_eliminar_archivo.preview_image.setVisible(False)
                self.ui_eliminar_archivo.preview_text.setVisible(False)

        except Exception as e:
            self.print('Error eliminando archivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

        self.dialog_eliminar_archivo.exec()

    def popup_eliminar_parametro(self):        
        
        self.dialog_eliminar_parametro = QtWidgets.QDialog()
        self.ui_eliminar_parametro = Ui_EliminarParametro()
        self.ui_eliminar_parametro.setupUi(self.dialog_eliminar_parametro)
        

        self.ui_eliminar_parametro.cancelar.clicked.connect(lambda: self.dialog_eliminar_parametro.done(1))
        self.ui_eliminar_parametro.eliminar.clicked.connect(self.eliminar_parametro)

        datapoint = self.ui.ingreso_parametros.selectedItems()[0].text(0)
        parametro = self.ui.ingreso_parametros.selectedItems()[0].text(1)
        valor = self.ui.ingreso_parametros.selectedItems()[0].text(2)
        unidad = self.ui.ingreso_parametros.selectedItems()[0].text(3)

        self.ui_eliminar_parametro.parametro.setText(parametro)
        self.ui_eliminar_parametro.valor.setText(valor)
        self.ui_eliminar_parametro.unidad.setText(unidad)
        self.ui_eliminar_parametro.datapoint.setText(datapoint)

        self.dialog_eliminar_parametro.exec()

    def popup_crear_parametro(self):        
        
        self.dialog_crear_parametro = QtWidgets.QDialog()
        self.ui_crear_parametro = Ui_CrearParametro()
        self.ui_crear_parametro.setupUi(self.dialog_crear_parametro)        

        self.ui_crear_parametro.cancelar.clicked.connect(lambda: self.dialog_crear_parametro.done(1))
        self.ui_crear_parametro.crear.clicked.connect(self.crear_parametro)

        self.dialog_crear_parametro.exec()

    def popup_subir(self):        
        
        self.dialog_subir = QtWidgets.QDialog()
        self.ui_subir = Ui_Subir()
        self.ui_subir.setupUi(self.dialog_subir)        

        self.ui_subir.cancelar.clicked.connect(lambda: self.dialog_subir.done(1))
        self.ui_subir.subir.clicked.connect(self.subir)

        self.dialog_subir.exec()

    def popup_guardar_descripcion(self):        
        
        self.dialog_guardar_descripcion = QtWidgets.QDialog()
        self.ui_guardar_descripcion = Ui_GuardarDescripcion()
        self.ui_guardar_descripcion.setupUi(self.dialog_guardar_descripcion)        

        self.ui_guardar_descripcion.cancelar.clicked.connect(lambda: self.dialog_guardar_descripcion.done(1))
        self.ui_guardar_descripcion.si.clicked.connect(self.guardar_descripcion)

        self.dialog_guardar_descripcion.exec()
        
    def popup_desconectar_dispositivo(self):
        try:
            nombre = self.ui.dispositivos_dispositivos_conectados.selectedItems()[0].text(0)
        except (IndexError, AttributeError):
            return
        self.dialog_desconectar_dispositivo = QtWidgets.QDialog()
        self.ui_desconectar_dispositivo = Ui_DesconectarDispositivo()
        self.ui_desconectar_dispositivo.setupUi(self.dialog_desconectar_dispositivo)
        self.ui_desconectar_dispositivo.dispositivo.setText(nombre + ' - ' + self.dispositivos_conectados[nombre]['modelo'])
        self.ui_desconectar_dispositivo.cancelar.clicked.connect(lambda: self.dialog_desconectar_dispositivo.done(1))
        self.ui_desconectar_dispositivo.desconectar.clicked.connect(self.desconectar_dispositivo)

        self.dialog_desconectar_dispositivo.exec()

    def popup_eliminar_canal(self):
        try:
            nombre = self.ui.dispositivos_canales.selectedItems()[0].text(0)
            canal = self.ui.dispositivos_canales.selectedItems()[0].text(1)
            osciloscopio = self.ui.dispositivos_canales.selectedItems()[0].text(2)
            datapoints = self.ui.dispositivos_canales.selectedItems()[0].text(3)
        except (IndexError, AttributeError):
            return

        self.dialog_eliminar_canal = QtWidgets.QDialog()
        self.ui_eliminar_canal = Ui_EliminarCanal()
        self.ui_eliminar_canal.setupUi(self.dialog_eliminar_canal)

        self.ui_eliminar_canal.nombre.setText(nombre)
        self.ui_eliminar_canal.canal.setText(canal)
        self.ui_eliminar_canal.osciloscopio.setText(osciloscopio)
        self.ui_eliminar_canal.datapoints.setText(datapoints)

        self.ui_eliminar_canal.cancelar.clicked.connect(lambda: self.dialog_eliminar_canal.done(1))
        self.ui_eliminar_canal.eliminar.clicked.connect(self.eliminar_canal)

        self.dialog_eliminar_canal.exec()

    def agregar_canal(self):

        try:        
            nombre = self.ui_agregar_canal.nombre_variable.text()
            osciloscopio = self.ui_agregar_canal.osciloscopio.currentText().split(' - ')[0]
            canal = self.ui_agregar_canal.canal.currentText()
            datapoints = self.ui_agregar_canal.datapoints.value()

            self.print('Canal agregado:')
            self.print('Nombre:' + nombre + '\t Osciloscopio: ' + osciloscopio + '\t Canal: ' + canal + '\t Datapoints: ' + str(datapoints))
            self.ui.status.setText('Status: OK')

            self.dispositivos_conectados[osciloscopio]['canales'][canal] = {'nombre':nombre, 'datapoints':datapoints}
            
            self.actualizar_canales()

            self.dialog_agregar_canal.done(1)
        
        except Exception as e:
            self.print('Error agregando canal:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def actualizar_canales(self):
        items = []
        i=0
        for nombre_dispositivo in self.dispositivos_conectados:
            for id_canal in self.dispositivos_conectados[nombre_dispositivo]['canales']:
                canal = self.dispositivos_conectados[nombre_dispositivo]['canales'][id_canal]
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, canal['nombre'])
                item.setText(1, id_canal)
                item.setText(2, nombre_dispositivo + ' - ' + self.dispositivos_conectados[nombre_dispositivo]['modelo'])
                item.setText(3, str(canal['datapoints']))
                items.append(item)
        self.ui.dispositivos_canales.clear()
        self.ui.dispositivos_canales.addTopLevelItems(items)

        items = []
        i=0
        for nombre_dispositivo in self.dispositivos_conectados:
            for id_canal in self.dispositivos_conectados[nombre_dispositivo]['canales']:
                canal = self.dispositivos_conectados[nombre_dispositivo]['canales'][id_canal]
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, canal['nombre'])
                item.setText(1, id_canal)
                item.setText(2, nombre_dispositivo + ' - ' + self.dispositivos_conectados[nombre_dispositivo]['modelo'])
                item.setText(3, str(canal['datapoints']))
                items.append(item)
        self.ui.adquisicion_origen_datos.clear()
        self.ui.adquisicion_origen_datos.addTopLevelItems(items)

        items = []
        i=0
        for nombre_dispositivo in self.dispositivos_conectados:
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, nombre_dispositivo)
            item.setText(1, self.dispositivos_conectados[nombre_dispositivo]['modelo'])
            item.setText(2, str(len(self.dispositivos_conectados[nombre_dispositivo]['canales'])))
            item.setText(3, self.dispositivos_conectados[nombre_dispositivo]['conexion'])
            items.append(item)

        self.ui.dispositivos_dispositivos_conectados.clear()
        self.ui.dispositivos_dispositivos_conectados.addTopLevelItems(items)

    def eliminar_canal(self):
        try:
            osciloscopio = self.ui.dispositivos_canales.selectedItems()[0].text(2).split(' - ')[0]
            id_canal = self.ui.dispositivos_canales.selectedItems()[0].text(1)

            canal = None
            for chan_id in self.dispositivos_conectados[osciloscopio]['canales']:
                if chan_id == id_canal:
                    canal = self.dispositivos_conectados[osciloscopio]['canales'][chan_id]
                    break
            if canal is None:
                self.print('Error eliminando canal: Canal no encontrado')
                self.ui.status.setText('Status: Error')
                self.dialog_eliminar_canal.done(1)
                return
            
            del self.dispositivos_conectados[osciloscopio]['canales'][chan_id]

            if chan_id in self.datos[osciloscopio]:
                del self.datos[osciloscopio][chan_id]

            self.actualizar_canales()
            self.dialog_eliminar_canal.done(1)

        except Exception as e:
            self.print('Error eliminando canal:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def actualizar_status(self, ultimo):
        if len(self.data_workers) <=1 and ultimo:
            # Acquisition complete - release lock and re-enable button
            self.adquisicion_en_progreso = False
            self.ui.adquisicion_adquirir.setEnabled(True)
            
            if self.ui.adquisicion_auto_guardar.checkState() == Qt.CheckState.Checked:
                self.ui.status.setText('Status: Guardando datos')
                self.guardar_datos()
            else:
                self.ui.status.setText('Status: OK')
            
            # Only resume trigger after everything is complete (small delay to prevent immediate re-trigger)
            QThread.msleep(100)
            self.trigger_worker.pause = False
        else:
            if len(self.data_workers)>1:
                self.ui.status.setText('Status: Adquiriendo datos de ' + str(len(self.data_workers)) + ' dispositivos')
            else:
                self.ui.status.setText('Status: Adquiriendo datos de 1 dispositivo')

    def eliminar_workers(self):

        for worker in self.data_workers[:]:
            try:
                if worker.done:
                    self.data_workers.remove(worker)
            except RuntimeError:
                # Worker might have been deleted already
                if worker in self.data_workers:
                    self.data_workers.remove(worker)
                
        for thread in self.data_threads[:]:
            try:
                if not thread.isRunning():
                    self.data_threads.remove(thread)
            except RuntimeError:
                pass

    def adquirir_datos(self):

        # Check if acquisition is already in progress
        if self.adquisicion_en_progreso:
            self.print('Adquisicion ya en progreso, ignorando solicitud')
            return False
        
        self.adquisicion_en_progreso = True
        self.ui.adquisicion_adquirir.setEnabled(False)  # Disable button during acquisition
        
        # Pause trigger worker to prevent VISA query conflicts
        self.trigger_worker.pause = True
        time.sleep(0.2)  # Wait for any pending trigger queries to complete

        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        self.print('Adquiriendo datos \t-\t' + self.timestamp)
        self.ui.status.setText('Status: Adquiriendo datos de ' + str(len(self.dispositivos_conectados)) + ' dispositivos')

        try:
            # Clean up any stale workers before starting
            self.eliminar_workers()

            self.datos = {}
            self.ui.adquisicion_preview_graph.clear()
            self.ui.adquisicion_preview_graph.addLegend()

            canales_solicitados = 0

            for nombre_dispositivo in self.dispositivos_conectados:
                self.datos[nombre_dispositivo] = {}
                canales = self.dispositivos_conectados[nombre_dispositivo]['canales']
                
                canales_solicitados += len(canales)
                existe = False
                for data_worker in self.data_workers:
                    if data_worker.device_name == nombre_dispositivo:
                        existe = True
                        break
                if existe:
                    self.print('No se pueden adquirir datos de ' + nombre_dispositivo  + ':\t Esperando respuesta de solicitud anterior')
                    self.print(str(self.data_workers))
                    self.ui.status.setText('Status: Error')
                    continue
                
                worker = DataWorker()
                thread = QThread()
                # Reuse existing device connection for faster acquisition
                existing_device = self.dispositivos_conectados[nombre_dispositivo].get('dispositivo')
                worker.set_device(nombre_dispositivo, canales, existing_device)

                worker.moveToThread(thread)
                thread.started.connect(worker.get_data)
                worker.finished.connect(thread.quit)
                worker.finished.connect(worker.deleteLater)
                thread.finished.connect(thread.deleteLater)
                worker.finished.connect(self.eliminar_workers)
                
                worker.response.connect(self.get_data_event, Qt.QueuedConnection)

                self.data_workers.append(worker)
                self.data_threads.append(thread)
                
                thread.start()

            if canales_solicitados == 0:
                self.print('No hay canales por adquirir')
                self.ui.status.setText('Status: Error')
                self.adquisicion_en_progreso = False
                self.ui.adquisicion_adquirir.setEnabled(True)


            return True

        except Exception as e:
            self.print('Error adquiriendo datos:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
            self.adquisicion_en_progreso = False
            self.ui.adquisicion_adquirir.setEnabled(True)

    def guardar_datos(self):
        if self.carpeta_local == '':
            self.print('Error al guardar datos: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
        try:
            last = 0
            archivos_locales = os.listdir(self.carpeta_local)
            for archivo in self.indice:
                if archivo not in archivos_locales:
                    continue
                datapoint = self.indice[archivo]
                if datapoint.isdigit():
                    if int(datapoint) > last:
                        last = int(datapoint)
            maxdatalength = 0
            for nombre_dispositivo in self.datos:
                for chan in self.datos[nombre_dispositivo]:
                    length = len(self.datos[nombre_dispositivo][chan]['x'])
                    if length > maxdatalength:
                        maxdatalength = length
            # Build DataFrame more efficiently using dict comprehension
            data_dict = {}
            col_order = []
            for nombre_dispositivo in self.datos:
                for chan in self.datos[nombre_dispositivo]:
                    nombre = self.dispositivos_conectados[nombre_dispositivo]['canales'][chan]['nombre']
                    x_data = self.datos[nombre_dispositivo][chan]['x']
                    y_data = self.datos[nombre_dispositivo][chan]['y']
                    
                    # Pad with NaN instead of empty string (more efficient, proper numeric type)
                    if len(x_data) < maxdatalength:
                        pad_length = maxdatalength - len(x_data)
                        x_data = np.concatenate([x_data, np.full(pad_length, np.nan)])
                        y_data = np.concatenate([y_data, np.full(pad_length, np.nan)])
                    
                    data_dict['t_' + nombre] = x_data
                    data_dict[nombre] = y_data
                    col_order.extend(['t_' + nombre, nombre])
            
            # Create DataFrame in one operation (much faster than repeated insert)
            df = pd.DataFrame(data_dict, columns=col_order)
            if len(df.columns) > 0:

                prefijo = self.ui.adquisicion_prefijo.text()
                prefijo = unicodedata.normalize('NFKD', prefijo).encode('ascii', 'ignore').decode('ascii')
                prefijo = re.sub(r'[^\w\s-]', '', prefijo.lower())
                
                
                if prefijo == '':
                    nombre_archivo = self.carpeta_local + '/' + self.timestamp + '.csv'
                    if self.timestamp + '.csv' not in self.indice:
                        self.indice[self.timestamp + '.csv'] = str(last + 1)
                else:
                    nombre_archivo = self.carpeta_local + '/' + prefijo + '_' + self.timestamp + '.csv'
                    if prefijo + '_' + self.timestamp + '.csv' not in self.indice:
                        self.indice[prefijo + '_' + self.timestamp + '.csv'] = str(last + 1)



                df.to_csv(nombre_archivo, index = False)
                self.print('Datos guardados en:' + nombre_archivo)
                self.guardar_indice()
                self.refrescar_archivos_locales()
                self.ui.status.setText('Status: OK')

            else:
                self.print('Error al guardar datos: No hay datos para guardar')
                self.ui.status.setText('Status: Error guardando datos')
        except Exception as e:
            self.print('Error al guardar datos:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def trigger_event(self, count):
        self.print('Evento de Trigger')
        # Skip if acquisition is already in progress
        if self.adquisicion_en_progreso:
            self.print('Adquisicion en progreso, ignorando trigger')
            return
        self.adquirir_datos()

    def get_data_event(self, response):
        nombre_dispositivo = response['dispositivo']
        canal = response['canal']

        if not response['exito']:
            self.print('Error adquiriendo datos de ' + nombre_dispositivo + '  ' + canal)
            self.actualizar_status(response['ultimo'])
            return

        self.datos[nombre_dispositivo][canal] = response['datos']
        
        self.ui.adquisicion_preview_graph.clear()
        self.ui.adquisicion_preview_graph.addLegend()

        i=0
        for dispositivo in self.datos:
            for chan in self.datos[dispositivo]:
                # Data is already numpy arrays, no need to convert again
                x = self.datos[dispositivo][chan]['x']
                y = self.datos[dispositivo][chan]['y']
                self.ui.adquisicion_preview_graph.plot(x, y, name = self.dispositivos_conectados[dispositivo]['canales'][chan]['nombre'], pen = self.color_palette[i%len(self.color_palette)])
                i+=1

        prefijo = self.ui.adquisicion_prefijo.text()
        prefijo = unicodedata.normalize('NFKD', prefijo).encode('ascii', 'ignore').decode('ascii')
        prefijo = re.sub(r'[^\w\s-]', '', prefijo.lower())
                
        if prefijo == '':
            self.ui.adquisicion_label_preview.setText(self.timestamp + '.csv')
        else:
            self.ui.adquisicion_label_preview.setText(prefijo + '_' + self.timestamp + '.csv')

        self.print('Datos adquiridos de ' + nombre_dispositivo + ' ' + canal + ' en ' + str(int(response['tiempo']*1000)) + ' ms')

        self.actualizar_status(response['ultimo'])
        
        self.ui.adquisicion_preview_graph.setVisible(True)
        self.ui.adquisicion_preview_image.setVisible(False)
        self.ui.adquisicion_preview_text.setVisible(False)

    def new_image_event(self, msg):
        if '*' in msg:
            files = msg.split('*')
        else:
            files = [msg]
        try:
            last = 0
            archivos_locales = os.listdir(self.carpeta_local)
            for archivo in self.indice:
                if archivo not in archivos_locales:
                    continue
                datapoint = self.indice[archivo]
                if datapoint.isdigit():
                    if int(datapoint) > last:
                        last = int(datapoint)
            for file in files:
                if os.path.exists(self.carpeta_local + '/' + file):
                    i=1
                    while True:
                        if not os.path.exists(self.carpeta_local + '/' + file.split('.')[0] + '(' + str(i) + ').' + file.split('.')[-1]):
                            shutil.copyfile(self.carpeta_imagenes + '/' + file, self.carpeta_local + '/' + file.split('.')[0] + '(' + str(i) + ').' + file.split('.')[-1])

                            self.indice[file.split('.')[0] + '(' + str(i) + ').' + file.split('.')[-1]] = str(last + 1)
                            self.print('Se ha agregado un nuevo archio de imagen:\t' + file.split('.')[0] + '(' + str(i) + ').' + file.split('.')[-1])
                            self.ui.status.setText('Status: OK')
                            break
                        i+=1
                else:
                    shutil.copyfile(self.carpeta_imagenes + '/' + file, self.carpeta_local + '/' + file)

                    self.indice[file] = str(last + 1)
                    self.print('Se ha agregado un nuevo archio de imagen:\t' + file)
                    self.ui.status.setText('Status: OK')
                self.refrescar_archivos_locales()
        except Exception as e:
            self.print('Error al guardar imagen:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def auto(self):
        if self.ui.adquisicion_auto.text() == 'Auto Adquirir':
            self.print('Adquisicion automatica iniciada')
            self.ui.adquisicion_auto.setText('Stop')
            self.ui.adquisicion_auto_guardar.setEnabled(False)
            self.ui.adquisicion_auto_imagenes.setEnabled(False)
            self.ui.adquisicion_seleccionar_carpeta_imagenes.setEnabled(False)
            self.ui.adquisicion_fuente_trigger.setEnabled(False)
            
            self.trigger_worker = TriggerWorker()
            self.trigger_thread = QThread()
            self.image_thread = QThread()
            self.image_worker = ImageWorker()

            self.trigger_worker.moveToThread(self.trigger_thread)
            self.trigger_thread.started.connect(self.trigger_worker.run)
            self.trigger_worker.finished.connect(self.trigger_thread.quit)
            self.trigger_worker.finished.connect(self.trigger_worker.deleteLater)
            self.trigger_thread.finished.connect(self.trigger_thread.deleteLater)
            self.trigger_worker.trigger.connect(self.trigger_event, Qt.QueuedConnection)

            self.image_worker.moveToThread(self.image_thread)
            self.image_thread.started.connect(self.image_worker.run)
            self.image_worker.finished.connect(self.image_thread.quit)
            self.image_worker.finished.connect(self.image_worker.deleteLater)
            self.image_thread.finished.connect(self.image_thread.deleteLater)
            self.image_worker.msg.connect(self.new_image_event, Qt.QueuedConnection)
            try:
                self.trigger_worker.set_source(str(self.ui.adquisicion_fuente_trigger.currentText()).split(' - ')[0])
                self.trigger_thread.start()
            except Exception as e:
                self.print('Error al conectar a fuente de trigger: ' + str(self.ui.adquisicion_fuente_trigger.currentText()))
                self.print(str(e) + '\n')
                self.ui.status.setText('Status: Error')

            if self.ui.adquisicion_auto_imagenes.checkState() == Qt.CheckState.Checked:
                if self.carpeta_imagenes == '':
                    self.print('Carpeta de imaganes no especificada')
                else:
                    try:
                        self.image_worker.set_folder(self.carpeta_imagenes)
                        self.image_thread.start()
                    except Exception as e:
                        self.print('Error al buscar imagenes en: ' + self.carpeta_imagenes)
                        self.print(str(e) + '\n')
                        self.ui.status.setText('Status: Error')

        elif self.ui.adquisicion_auto.text() == 'Stop':
            self.print('Adquisicion automatica detenida')
            self.ui.adquisicion_auto.setText('Auto Adquirir')
            self.ui.adquisicion_auto_guardar.setEnabled(True)
            self.ui.adquisicion_auto_imagenes.setEnabled(True)
            self.ui.adquisicion_seleccionar_carpeta_imagenes.setEnabled(True)
            self.ui.adquisicion_fuente_trigger.setEnabled(True)
            
            self.trigger_worker.running = False
            self.trigger_thread.quit()
            self.image_worker.running = False
            self.image_thread.quit()
            
            # Reset acquisition state
            self.adquisicion_en_progreso = False
            self.ui.adquisicion_adquirir.setEnabled(True)
            self.eliminar_workers()
 
    def seleccionar_carpeta_imagenes(self):
        parent = Tk()
        parent.overrideredirect(1)
        parent.withdraw()
        carpeta = askdirectory(title = 'Seleccionar Carpeta de Imagenes')

        if carpeta == '':
            return
        elif carpeta == self.carpeta_local:
            self.print('Carpeta de imaganes no puede ser la misma que la carpeta local')
            return

        self.carpeta_imagenes = carpeta
        self.ui.adquisicion_label_carpeta_imagenes.setText(self.carpeta_imagenes)

    def refrescar_archivos_locales(self):

        self.ui.bd_label_archivos_locales.setText(self.carpeta_local)
        self.ui.ingreso_label_archivos_locales.setText(self.carpeta_local)
        self.ui.adquisicion_label_archivos_locales.setText(self.carpeta_local)

        if self.carpeta_local == '':
            return
        try:
            items_bd= []
            items_ingreso= []
            items_adqusicion= []
            i=0
            for archivo in os.listdir(self.carpeta_local):
                item_bd = QtWidgets.QTreeWidgetItem(i)
                if archivo in self.indice:
                    item_bd.setText(0, str(self.indice[archivo]))
                else:
                    item_bd.setText(0, '-')
                item_bd.setText(1, archivo)
                if archivo in self.archivos_servidor:
                    item_bd.setText(2, 'Si')
                    item_bd.setCheckState(3, Qt.CheckState.Unchecked)
                else:
                    item_bd.setText(2, 'No')
                    item_bd.setCheckState(3, Qt.CheckState.Checked)
                items_bd.append(item_bd)
                
                item_ingreso = QtWidgets.QTreeWidgetItem(i)
                if archivo in self.indice:
                    item_ingreso.setText(0, str(self.indice[archivo]))
                else:
                    item_ingreso.setText(0, '-')
                item_ingreso.setText(1, archivo)
                items_ingreso.append(item_ingreso)
                
                item_adqusicion = QtWidgets.QTreeWidgetItem(i)
                if archivo in self.indice:
                    item_adqusicion.setText(0, str(self.indice[archivo]))
                else:
                    item_adqusicion.setText(0, '-')
                item_adqusicion.setText(1, archivo)
                items_adqusicion.append(item_adqusicion)
                i+=1

            self.ui.bd_archivos_locales.clear()
            self.ui.bd_archivos_locales.addTopLevelItems(items_bd)

            self.ui.ingreso_archivos_locales.clear()
            self.ui.ingreso_archivos_locales.addTopLevelItems(items_ingreso)

            self.ui.adquisicion_archivos_locales.clear()
            self.ui.adquisicion_archivos_locales.addTopLevelItems(items_adqusicion)
        
        except Exception as e:
            self.print('Error al refrescar archivos locales:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def seleccionar_carpeta(self):
        parent = Tk()
        parent.overrideredirect(1)
        parent.withdraw()
        path = askdirectory(title = 'Seleccionar Carpeta de Trabajo')
        if path != '':
            self.carpeta_local = path
            self.cargar_parametros()
            self.cargar_indice()
            self.cargar_descripcion()
            self.refrescar_archivos_locales()
            self.print('Carpeta de trabajo seleccionada: ' + path)
            self.ui.status.setText('Status: OK')

    def adquisicion_visualizar_archivo(self):

        try:
            file = self.ui.adquisicion_archivos_locales.selectedItems()[0].text(1)
            filepath = self.carpeta_local + '/' + file
            filepath_lower = filepath.lower()

            if filepath_lower.endswith(CSV_EXTENSIONS):
                self.visualizar_csv(filepath, self.ui.adquisicion_preview_graph, self.ui.adquisicion_preview_image, self.ui.adquisicion_preview_text, self.ui.adquisicion_label_preview)

            elif filepath_lower.endswith(IMAGE_EXTENSIONS):
                self.visualizar_imagen(filepath, self.ui.adquisicion_preview_graph, self.ui.adquisicion_preview_image, self.ui.adquisicion_preview_text, self.ui.adquisicion_label_preview)

            elif filepath_lower.endswith(TEXT_EXTENSIONS):
                self.visualizar_texto(filepath, self.ui.adquisicion_preview_graph, self.ui.adquisicion_preview_image, self.ui.adquisicion_preview_text, self.ui.adquisicion_label_preview)

            else:
                self.ui.adquisicion_preview_graph.setVisible(False)
                self.ui.adquisicion_preview_image.setVisible(False)
                self.ui.adquisicion_preview_text.setVisible(False)

        except Exception as e:
            self.print('Error al visualizar archivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def ingreso_visualizar_archivo(self):

        try:
            file = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)
            filepath = self.carpeta_local + '/' + file
            filepath_lower = filepath.lower()

            if filepath_lower.endswith(CSV_EXTENSIONS):
                self.visualizar_csv(filepath, self.ui.ingreso_preview_graph, self.ui.ingreso_preview_image, self.ui.ingreso_preview_text, self.ui.ingreso_label_preview)

            elif filepath_lower.endswith(IMAGE_EXTENSIONS):
                self.visualizar_imagen(filepath, self.ui.ingreso_preview_graph, self.ui.ingreso_preview_image, self.ui.ingreso_preview_text, self.ui.ingreso_label_preview)

            elif filepath_lower.endswith(TEXT_EXTENSIONS):
                self.visualizar_texto(filepath, self.ui.ingreso_preview_graph, self.ui.ingreso_preview_image, self.ui.ingreso_preview_text, self.ui.ingreso_label_preview)

            else:
                self.ui.ingreso_preview_graph.setVisible(False)
                self.ui.ingreso_preview_image.setVisible(False)
                self.ui.ingreso_preview_text.setVisible(False)

        except Exception as e:
            self.print('Error al visualizar archivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def cargar_parametros(self):
        if self.carpeta_local == '':
            return
        try:
            if os.path.exists(self.carpeta_local+'/parametros.txt'):
                with open(self.carpeta_local+'/parametros.txt', 'r') as archivo:
                    self.parametros = json.load(archivo)
                    self.refrescar_parametros()
            else:
                self.parametros = {}
                self.refrescar_parametros()
                    
        except Exception as e:
            self.print('Error al cargar archivo parametros.txt:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def guardar_parametros(self):
        if self.carpeta_local == '':
            self.print('Error al guardar parametros: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
            return
        try:
            with open(self.carpeta_local+'/parametros.txt', 'w') as archivo:
                json.dump(self.parametros, archivo, indent = 4)
            self.print('Parametros guardados en parametros.txt en la carpeta:\t'+self.carpeta_local)
            self.ui.status.setText('Status: OK')
                    
        except Exception as e:
            self.print('Error al guardar parametros:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def refrescar_parametros(self):
        try:
            parametros_bd= []
            parametros_ingreso= []            
            i=0
            for nombre in self.parametros:
                for datos in self.parametros[nombre]:
                    item_bd = QtWidgets.QTreeWidgetItem(i)
                    item_bd.setText(0, datos['datapoint'])
                    item_bd.setText(1, nombre)
                    item_bd.setText(2, str(datos['valor']))
                    item_bd.setText(3, datos['unidad'])
                    # if nombre in self.nombres_parametros:
                    #     item_bd.setText(4, self.nombres_parametros[nombre])
                    # else:
                    #     item_bd.setText(4, '-')

                    existe = False
                    for parametro in self.parametros_servidor:
                        if parametro['datapoint'] == datos['datapoint'] and parametro['parametro'] == nombre:
                            existe = True
                            break
                    if existe:
                        item_bd.setCheckState(4, Qt.CheckState.Unchecked)
                    else:
                        item_bd.setCheckState(4, Qt.CheckState.Checked)
                            

                    parametros_bd.append(item_bd)

                    item_ingreso = QtWidgets.QTreeWidgetItem(i)
                    item_ingreso.setText(0, datos['datapoint'])
                    item_ingreso.setText(1, nombre)
                    item_ingreso.setText(2, str(datos['valor']))
                    item_ingreso.setText(3, datos['unidad'])
                    if nombre in self.nombres_parametros:
                        item_ingreso.setText(4, self.nombres_parametros[nombre])
                    else:
                        item_ingreso.setText(4, '-')
                    parametros_ingreso.append(item_ingreso)
                    i+=1

            self.ui.ingreso_parametros.clear()
            self.ui.ingreso_parametros.addTopLevelItems(parametros_ingreso)
            self.ui.bd_parametros_locales.clear()
            self.ui.bd_parametros_locales.addTopLevelItems(parametros_bd)
                    
        except Exception as e:
            self.print('Error al refrescar parametros:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def cargar_indice(self):
        if self.carpeta_local == '':
            return
        try:
            if os.path.exists(self.carpeta_local+'/indice.txt'):
                with open(self.carpeta_local+'/indice.txt', 'r') as archivo:
                    self.indice = json.load(archivo)
            else:
                self.indice = {}
                    
        except Exception as e:
            self.print('Error al refrescar indice:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def guardar_indice(self):
        if self.carpeta_local == '':
            self.print('Error al guardar indice: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
            return
        try:
            with open(self.carpeta_local+'/indice.txt', 'w') as archivo:
                json.dump(self.indice, archivo, indent = 4)
            self.print('Indice guardado en la carpeta:\t'+self.carpeta_local)
            self.ui.status.setText('Status: OK')
                    
        except Exception as e:
            self.print('Error al guardar indice:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def cargar_descripcion(self):
        if self.carpeta_local == '':
            return
        try:
            if os.path.exists(self.carpeta_local+'/descripcion.txt'):
                with open(self.carpeta_local+'/descripcion.txt', 'r') as archivo:
                    self.descripcion = ''
                    for linea in archivo.readlines():
                        self.descripcion += linea +'\n'

                self.ui.bd_descripcion.setPlainText(self.descripcion)
                self.ui.ingreso_descripcion.setPlainText(self.descripcion)
            else:
                self.descripcion = ''
                self.ui.bd_descripcion.setPlainText(self.descripcion)
                self.ui.ingreso_descripcion.setPlainText(self.descripcion)
                    
        except Exception as e:
            self.print('Error al refrescar indice:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def agregar_archivo(self):
        if self.carpeta_local == '':
            self.print('Error al agregar archivo: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
            return
        try:
            parent = Tk()
            parent.overrideredirect(1)
            parent.withdraw()
            path = askopenfilename(title = 'Seleccionar Archivo')
            if path != '':
                shutil.copyfile(path, self.carpeta_local + '/' + path.split('/')[-1])
                self.refrescar_archivos_locales()
                self.print('Archivo agregado a carpeta de trabajo: '+ path.split('/')[-1])
                self.ui.status.setText('Status: OK')
        except Exception as e:
            self.print('Error al agregar archivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
    
    def asignar_datapoint(self):
        try:
            datapoint = self.ui_asignar_datapoint.datapoint.text().replace(" ", "")
            if datapoint.isdigit() or datapoint == '*':
                archivo = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)
                self.indice[archivo] = datapoint
                self.print('Datapoint\t' + datapoint + '\tasignado a archivo\t' + archivo)
                self.ui.status.setText('Status: OK')
                self.refrescar_archivos_locales()
                self.guardar_indice()
            elif datapoint.replace(" ", "") == ''  or datapoint.replace(" ", "") == '-':
                archivo = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)
                if archivo in self.indice:
                    del self.indice[archivo]
                    self.print('Datapoint eliminado de archivo\t' + archivo)
                self.refrescar_archivos_locales()
                self.guardar_indice()
            else:
                self.print('Error al asignar datapoint: Datapoint invalido')
                self.ui.status.setText('Status: Error')
            self.dialog_asignar_datapoint.done(1)
        except Exception as e:
            self.print('Error al asignar datapoint:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def eliminar_archivo(self):
        try:
            archivo = self.ui.ingreso_archivos_locales.selectedItems()[0].text(1)    

            if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Archivos Eliminados')):
                os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Archivos Eliminados'))                
            if not os.path.exists(os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Archivos Eliminados\\' + self.carpeta_local.split('/')[-1])):
                os.mkdir(os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Archivos Eliminados\\' + self.carpeta_local.split('/')[-1]))

            shutil.move(self.carpeta_local + '/' + archivo,   os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), 'Archivos Eliminados\\' + self.carpeta_local.split('/')[-1]), archivo))

            # os.remove(self.carpeta_local + '/' + archivo)
            if archivo in self.indice:
                del self.indice[archivo]
                self.guardar_indice()
            self.refrescar_archivos_locales()
            self.print('Se ha borrado el archivo:\t' + archivo + '\tde la carpeta:\t'+self.carpeta_local)
            self.ui.status.setText('Status: OK')
            self.dialog_eliminar_archivo.done(1)
        except Exception as e:
            self.print('Error al eliminar archivo:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
    
    def guardar_descripcion(self):
        if self.carpeta_local == '':
            self.print('Error al guardar descripcion: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
            return
        try:
            self.descripcion = self.ui.ingreso_descripcion.toPlainText()
            with open(self.carpeta_local + '/descripcion.txt', 'w') as archivo:
                archivo.write(self.descripcion)
            self.print('Descripcion guardada en la carpeta:\t'+self.carpeta_local)
            self.ui.status.setText('Status: OK')
            self.ui.bd_descripcion.setPlainText(self.descripcion)
            self.dialog_guardar_descripcion.done(1)

        except Exception as e:
            self.print('Error al guardar descripcion:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')
    
    def eliminar_parametro(self):
        try:
            datapoint = self.ui.ingreso_parametros.selectedItems()[0].text(0)
            parametro = self.ui.ingreso_parametros.selectedItems()[0].text(1)
            valor = self.ui.ingreso_parametros.selectedItems()[0].text(2)
            unidad = self.ui.ingreso_parametros.selectedItems()[0].text(3)
            
            for punto in self.parametros[parametro]:
                if punto['datapoint'] == datapoint and str(punto['valor']) == valor:
                    self.parametros[parametro].remove(punto)
                    self.print('Parametro eliminado:\t nombre: ' + parametro + '\tdatapoint: '+ datapoint + '\tvalor: ' + valor + unidad)
                    self.ui.status.setText('Status: OK')
                    break
            if self.parametros[parametro] == []:
                del self.parametros[parametro]

            self.refrescar_parametros()
            self.guardar_parametros()
            self.dialog_eliminar_parametro.done(1)
        except Exception as e:
            self.print('Error al eliminar parametro:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def agregar_valor_parametro(self, datapoint, unidad, parametro, valor):
        if parametro not in self.nombres_parametros:
            self.print('No se puede agregar parametro: Parametro no existe')
            self.ui.status.setText('Status: Error')
            return False
        if self.carpeta_local == '':
            self.print('No se puede agregar parametro: Carpeta de trabajo no especificada')
            self.ui.status.setText('Status: Error')
            return False
        if parametro not in self.parametros:
            self.parametros[parametro] = []
            
        if datapoint.isdigit() or datapoint == '*':
            try:
                if self.nombres_parametros[parametro] == 'int':
                    valor = int(valor)
                elif self.nombres_parametros[parametro] == 'float':
                    valor = float(valor)
                elif self.nombres_parametros[parametro] == 'string':
                    valor = str(valor)
                    unidad = ''
                elif self.nombres_parametros[parametro] == 'boolean':
                    if str(valor).lower().replace(' ','') in ['true','verdadero','si','sí','yes','1','t','v']:
                        valor = True
                        unidad = ''
                    elif str(valor).lower().replace(' ','')  in ['false','falso','no','0','f']:
                        valor = False
                        unidad = ''
                    else:
                        self.print('No se puede agregar parametro: Tipo invalido')
                        self.ui.status.setText('Status: Error')
                        return False
                else:
                    self.print('No se puede agregar parametro: Tipo invalido')
                    self.ui.status.setText('Status: Error')
                    return False


                for elemento in self.parametros[parametro]:
                    if elemento['datapoint'] == datapoint:
                        self.parametros[parametro].remove(elemento)

                self.parametros[parametro].append({'datapoint':datapoint,'valor':valor,'unidad':unidad})
                self.refrescar_parametros()
                self.guardar_parametros()
                self.refrescar_archivos_locales()
                self.print('Se ha ingresado el valor:\t'+str(valor)+' '+str(unidad)+'\t al parametro:\t'+str(parametro))
                self.ui.status.setText('Status: OK')
                return True

            except Exception as e:
                self.print('No se puede agregar parametro: Valor invalido')
                self.ui.status.setText('Status: Error')
                return False
        else:
            self.print('No se puede agregar parametro: Datapoint invalido')
            self.ui.status.setText('Status: Error')
            return False
       
    def agregar_valor_parametro_1(self):
        datapoint = self.ui.ingreso_datapoint_parametro_1.text().replace(" ", "")
        unidad = self.ui.ingreso_unidad_parametro_1.text()
        parametro = self.ui.ingreso_parametro_parametro_1.currentText()
        valor = self.ui.ingreso_valor_parametro_1.text()
        res = self.agregar_valor_parametro(datapoint, unidad, parametro, valor)
        if res:
            try:
                datapoint = int(datapoint)
                self.ui.ingreso_datapoint_parametro_1.setText(str(datapoint + 1))
            except ValueError:
                pass

    def agregar_valor_parametro_2(self):
        datapoint = self.ui.ingreso_datapoint_parametro_2.text().replace(" ", "")
        unidad = self.ui.ingreso_unidad_parametro_2.text()
        parametro = self.ui.ingreso_parametro_parametro_2.currentText()
        valor = self.ui.ingreso_valor_parametro_2.text()
        res = self.agregar_valor_parametro(datapoint, unidad, parametro, valor)
        if res:
            try:
                datapoint = int(datapoint)
                self.ui.ingreso_datapoint_parametro_2.setText(str(datapoint + 1))
            except ValueError:
                pass

    def agregar_valor_parametro_3(self):
        datapoint = self.ui.ingreso_datapoint_parametro_3.text().replace(" ", "")
        unidad = self.ui.ingreso_unidad_parametro_3.text()
        parametro = self.ui.ingreso_parametro_parametro_3.currentText()
        valor = self.ui.ingreso_valor_parametro_3.text()
        res = self.agregar_valor_parametro(datapoint, unidad, parametro, valor)
        if res:
            try:
                datapoint = int(datapoint)
                self.ui.ingreso_datapoint_parametro_3.setText(str(datapoint + 1))
            except ValueError:
                pass

    def agregar_valor_parametro_4(self):
        datapoint = self.ui.ingreso_datapoint_parametro_4.text().replace(" ", "")
        unidad = self.ui.ingreso_unidad_parametro_4.text()
        parametro = self.ui.ingreso_parametro_parametro_4.currentText()
        valor = self.ui.ingreso_valor_parametro_4.text()
        res = self.agregar_valor_parametro(datapoint, unidad, parametro, valor)
        if res:
            try:
                datapoint = int(datapoint)
                self.ui.ingreso_datapoint_parametro_4.setText(str(datapoint + 1))
            except ValueError:
                pass
    
    def crear_parametro(self):
        
        if self.mongo_client is None:
            self.print('Error creando parametro: Servidor desconectado')
            self.ui.status.setText('Status: Error')
            return
        
        nombre = self.ui_crear_parametro.nombre.text()
        tipo = self.ui_crear_parametro.tipo.currentText()
        if nombre not in self.nombres_parametros:
            tipo_map = {'Entero': 'int', 'Real': 'float', 'Texto': 'string', 'Boolean': 'boolean'}
            if tipo not in tipo_map:
                self.print('Error al crear parametro: Tipo invalido')
                self.ui.status.setText('Status: Error')
                self.refrescar_nombres_parametros()
                self.dialog_crear_parametro.done(1)
                return
            
            tipo_db = tipo_map[tipo]
            self.nombres_parametros[nombre] = tipo_db
            try:
                if self.mongo_client.db.nombres_parametros.count_documents({'nombre': nombre}) < 1:
                    self.mongo_client.db.nombres_parametros.insert_one({'nombre': nombre, 'tipo': tipo_db})
                    self.ui.status.setText('Status: OK')
            except Exception:
                self.print('Error al crear parametro: Parametro ya existe')
                self.ui.status.setText('Status: Error')

        else:
            self.print('Error al crear parametro: Parametro ya existe')
            self.ui.status.setText('Status: Error')
        self.refrescar_nombres_parametros()
        self.dialog_crear_parametro.done(1)

    def visualizar_csv(self, filepath, graph_frame, image_frame, text_frame, preview_label):        
                dataframe = pd.read_csv(filepath)
                graph_frame.clear()
                graph_frame.addLegend()
                cols = []
                for col in dataframe.columns:
                    cols.append(col)
                i=0
                for col in cols:
                    if i%2 == 1:
                        graph_frame.plot(np.array(dataframe[cols[i-1]]),np.array(dataframe[cols[i]]), name = col, pen = self.color_palette[int(i/2)%len(self.color_palette)])
                    i+=1                
                graph_frame.setVisible(True)
                image_frame.setVisible(False)
                text_frame.setVisible(False)
                preview_label.setText(filepath.split('/')[-1])

    def visualizar_imagen(self, filepath, graph_frame, image_frame, text_frame, preview_label):

                self.pixmap = QPixmap(filepath).scaled(651, 231, Qt.AspectRatioMode.KeepAspectRatio)
                time.sleep(0.1)
                
                graph_frame.setVisible(False)
                image_frame.setVisible(True)
                text_frame.setVisible(False)
                preview_label.setText(filepath.split('/')[-1])
                image_frame.setPixmap(self.pixmap)
                image_frame.show()    

    def visualizar_texto(self, filepath, graph_frame, image_frame, text_frame, preview_label):
                
                text_frame.clear()
                with open(filepath, 'r') as archivo:
                    lineas = archivo.readlines()
                    for linea in lineas:
                        text_frame.append(linea)
                
                graph_frame.setVisible(False)
                image_frame.setVisible(False)
                text_frame.setVisible(True)
                preview_label.setText(filepath.split('/')[-1])
    
    def guardar_perfil(self):

        try:
            parent = Tk()
            parent.overrideredirect(1)
            parent.withdraw()
            filename = asksaveasfilename(title = 'Guardar Perfil')

            resumen = {}

            for nombre_dispositivo in self.dispositivos_conectados:
                resumen[nombre_dispositivo] = {'canales':self.dispositivos_conectados[nombre_dispositivo]['canales'],'conexion':self.dispositivos_conectados[nombre_dispositivo]['conexion']}

                
            with open(filename, 'w') as archivo:
                json.dump(resumen, archivo, indent = 4)
            self.print('Parametros guardados en parametros.txt en la carpeta:\t'+self.carpeta_local)
            self.ui.status.setText('Status: OK')

        except Exception as e:
            self.print('Error guardando perfil:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def cargar_perfil(self):

        filename = ''

        try:
            parent = Tk()
            parent.overrideredirect(1)
            parent.withdraw()
            filename = askopenfilename(title = 'Cargar Perfil')

            if filename == '':
                return

            with open(filename, 'r') as archivo:
                resumen = json.load(archivo)
            
            for nombre_dispositivo in resumen:

                dispositivo = self.manager.open_resource(nombre_dispositivo)
                try:
                    dispositivo.timeout = 3 * 1000
                    modelo = dispositivo.query('*IDN?')
                    if len(modelo.split(',')) > 1:
                        modelo = modelo.split(',')[1]
                    dispositivo.timeout = 10 * 1000
                except Exception as e:
                    self.print('Error conectando dispositivo, modelo no identificado:')
                    self.print(str(e) + '\n')
                    self.ui.status.setText('Status: Error')
                    return

                self.dispositivos_conectados [nombre_dispositivo] = {'dispositivo':dispositivo, 'canales':resumen[nombre_dispositivo]['canales'], 'conexion':resumen[nombre_dispositivo]['conexion'], 'modelo':modelo}
                self.datos[nombre_dispositivo] = {}
                self.print('Dispositivo conectado: ' + nombre_dispositivo + ' - ' + modelo)
            
            self.ui.adquisicion_fuente_trigger.clear()
            self.ui.adquisicion_fuente_trigger.addItems([x + ' - ' + self.dispositivos_conectados[x]['modelo'] for x in self.dispositivos_conectados])
            self.actualizar_canales()
            self.print('Perfil de canales cargado exitosamente')
            self.ui.status.setText('Status: OK')
                

        except Exception as e:
            self.print('Error cargando perfil desde ' + filename + ' :')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')

    def print(self, text):
        self.ui.log.append( datetime.datetime.now().strftime('%H:%M:%S - ') + str(text))
        self.ui.log.moveCursor(QTextCursor.End)
        self.ui.log.ensureCursorVisible()

    def is_os_dark_mode(self):
        """Detect if OS is in dark mode. Supports Windows, macOS, and Linux."""
        import platform
        system = platform.system()
        
        try:
            if system == 'Windows':
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                     r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                winreg.CloseKey(key)
                return value == 0  # 0 means dark mode, 1 means light mode
            
            elif system == 'Darwin':  # macOS
                import subprocess
                result = subprocess.run(
                    ['defaults', 'read', '-g', 'AppleInterfaceStyle'],
                    capture_output=True, text=True
                )
                return result.returncode == 0 and 'Dark' in result.stdout
            
            elif system == 'Linux':
                import subprocess
                # Try GTK settings first (works for GNOME, Cinnamon, etc.)
                result = subprocess.run(
                    ['gsettings', 'get', 'org.gnome.desktop.interface', 'color-scheme'],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    return 'dark' in result.stdout.lower()
                
                # Fallback: check gtk-theme-name for 'dark' keyword
                result = subprocess.run(
                    ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    return 'dark' in result.stdout.lower()
                
                return False
            
            else:
                return False  # Unknown platform, default to light mode
                
        except Exception:
            return False  # Default to light mode if detection fails

    def apply_initial_theme(self):
        """Apply theme based on OS setting at startup."""
        os_dark = self.is_os_dark_mode()
        # Set darkmode to opposite so toggle_darkmode switches to correct mode
        self.darkmode = not os_dark
        self.toggle_darkmode()

    def toggle_darkmode(self):        
        self.darkmode = not self.darkmode
        app = QtWidgets.QApplication.instance()
        
        if self.darkmode:
            # Use Fusion style for consistent cross-platform dark theme
            app.setStyle('Fusion')
            
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
            dark_palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
            dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(66, 66, 66))
            dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
            dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
            dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
            dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
            dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
            dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
            dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))
            dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
            dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
            dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))
            dark_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
            
            app.setPalette(dark_palette)
            self.ui.darkmode_button.setText('Lightmode')
            self.print('Modo oscuro activado')
        else:
            # Use Fusion style with explicit light palette (ignores OS dark mode)
            app.setStyle('Fusion')
            
            light_palette = QPalette()
            light_palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
            light_palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
            light_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(245, 245, 245))
            light_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
            light_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
            light_palette.setColor(QPalette.ColorRole.Text, QColor(0, 0, 0))
            light_palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ColorRole.ButtonText, QColor(0, 0, 0))
            light_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
            light_palette.setColor(QPalette.ColorRole.Link, QColor(0, 0, 255))
            light_palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 120, 215))
            light_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
            light_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(120, 120, 120))
            light_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(120, 120, 120))
            light_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(120, 120, 120))
            light_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(180, 180, 180))
            light_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(120, 120, 120))
            
            app.setPalette(light_palette)
            self.ui.darkmode_button.setText('Darkmode')
            self.print('Modo claro activado')

    def subir(self):        
        if self.mongo_client is None:
            self.print('Error subiendo datos al servidor: Servidor desconectado')
            self.ui.status.setText('Status: Error')
            self.dialog_subir.done(1)
            return

        self.print('Subiendo datos al servidor')

        experimento = self.ui.bd_experimento.currentText()
        jornada = self.ui.bd_jornada.currentText()

        try:
            transport = paramiko.Transport((self.ui.bd_ip.text(),22))
            transport.connect(username = self.ui.bd_usuario.text(), password = self.ui.bd_password.text())
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            root = self.ui.bd_archivos_locales.invisibleRootItem()
                
            if not 'Experimentos' in sftp.listdir('usuario_sftp'):
                sftp.mkdir('usuario_sftp/Experimentos')
            if not experimento in sftp.listdir('usuario_sftp/Experimentos'):
                sftp.mkdir('usuario_sftp/Experimentos/'+ experimento)
            if not 'Jornadas' in sftp.listdir('usuario_sftp/Experimentos/'+ experimento):
                sftp.mkdir('usuario_sftp/Experimentos/'+ experimento + '/Jornadas')
            if not jornada in sftp.listdir('usuario_sftp/Experimentos/'+ experimento + '/Jornadas'):
                sftp.mkdir('usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada)

            archivos_agregados = 0
            for i in range(root.childCount()):
                item = root.child(i)
                if item.checkState(3) != Qt.CheckState.Checked:
                    continue
                
                if item.text(1) in sftp.listdir('usuario_sftp/Experimentos/'+ experimento + '/Jornadas/' + jornada):
                    sftp.remove('usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada + '/' +  item.text(1))
                    self.print('Archivo sobreescrito: ' + item.text(1))
                sftp.put(self.carpeta_local + '/' + item.text(1), 'usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada + '/' +  item.text(1))

                payload = {'jornada':jornada,'experimento':experimento,'datapoint':item.text(0),'nombre':item.text(1)}
                self.mongo_client.db.indice.update_one(payload, {'$set':payload}, upsert = True)
                archivos_agregados += 1

            self.print('Se han subido '+str(archivos_agregados) + ' archivos')
                  
        
            root = self.ui.bd_parametros_locales.invisibleRootItem()

            params_agregados = 0
            for i in range(root.childCount()):
                item = root.child(i)
                if item.checkState(4) != Qt.CheckState.Checked:
                    continue
                datapoint = item.text(0)
                parametro = item.text(1)
                valor = item.text(2)
                unidad = item.text(3)
                if datapoint == '-':
                    datapoint = ''
                if parametro in self.nombres_parametros:
                    if self.nombres_parametros[parametro] == 'float':
                        valor = float(valor)
                    elif self.nombres_parametros[parametro] == 'int':
                        valor = int(valor)
                payload = {'jornada':jornada,'experimento':experimento,'datapoint':datapoint,'parametro':parametro, 'valor':valor, 'unidad':unidad}
                self.mongo_client.db.parametros.update_one({'jornada':jornada,'experimento':experimento,'datapoint':datapoint,'parametro':parametro}, {'$set':payload}, upsert = True)
                params_agregados += 1

            self.print('Se han subido '+str(params_agregados) + ' datapoints de parametros')



            self.refrescar_servidor()
            self.refrescar_parametros()
            self.ui.status.setText('Status: OK')
        
        except Exception as e:
            self.print('Error subiendo datos al servidor:')
            self.print(str(e) + '\n')
            self.ui.status.setText('Status: Error')


        self.dialog_subir.done(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('icon.ico')))
    window = Lab_Widget()
    window.setWindowTitle('Applicacion de Laboratorio')

    def toggle_fullscreen():
        if window.isFullScreen():
            window.showNormal()
        else:
            window.showFullScreen()
    shortcut = QShortcut(Qt.Key.Key_F11, window)
    shortcut.activated.connect(toggle_fullscreen)

    # Apply initial theme based on OS setting
    window.apply_initial_theme()
    
    window.show()
    window.seleccionar_carpeta()


    sys.exit(app.exec())
