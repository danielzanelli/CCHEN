from ventanaPrincipal import Ui_Widget
from agregarFiltro import Ui_AgregarFiltro
from eliminarFiltro import Ui_EliminarFiltro

import stat
import paramiko
import pymongo
import datetime
import sys
import os
import json
import numpy as np
import pandas as pd
from PySide6.QtGui import QPixmap, QTextCursor, QIcon
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from tkinter import Tk
from tkinter.filedialog import askdirectory


class Office_Wigdet(Ui_Widget):
    def __init__(self, Widget) -> None:
        super().__init__()
        self.setupUi(Widget)

        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        self.color_palette = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        
        self.usuario = ''
        self.password = ''
        self.ip = ''
        
        self.filtros = []
        self.resultados_globales = {}
        
        self.busqueda_preview_graph.setBackground('white')    
        self.explorar_preview_graph.setBackground('white')        

        self.conexion_conectar.clicked.connect(self.conectar)
        self.busqueda_buscar.clicked.connect(self.buscar)
        
        self.explorar_archivos.itemDoubleClicked.connect(self.visualizar_archivo_explorar)
        self.busqueda_archivos.itemDoubleClicked.connect(self.visualizar_archivo_busqueda)
        self.busqueda_resultados.itemDoubleClicked.connect(self.visualizar_resultados)

        self.busqueda_descargar.clicked.connect(self.busqueda_descargar_seleccion)
        self.explorar_descargar.clicked.connect(self.explorar_descargar_seleccion)
        
        self.busqueda_agregar_filtro.clicked.connect(self.popup_agregar_filtro)
        self.busqueda_eliminar_filtro.clicked.connect(self.popup_eliminar_filtro)        

        self.print('Programa inicializado - ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    def refrescar_filtros(self):
        items = []
        i=0
        for filtro in self.filtros:
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, filtro['parametro'])
            item.setText(1, filtro['condicion'])
            item.setText(2, filtro['valor'])
            items.append(item)
            i+=1
        self.busqueda_filtros.clear()
        self.busqueda_filtros.addTopLevelItems(items)

    def popup_agregar_filtro(self):
        
        if self.ip == '' or self.usuario == '' or self.password == '':
            self.print('Error al agregar filtro: Servidor desconectado')
            self.status.setText('Status: Error')
            return
        
        self.dialog_agregar_filtro = QtWidgets.QDialog()
        self.ui_agregar_filtro = Ui_AgregarFiltro()
        self.ui_agregar_filtro.setupUi(self.dialog_agregar_filtro)

        self.ui_agregar_filtro.cancelar.clicked.connect(self.dialog_agregar_filtro.done)
        self.ui_agregar_filtro.agregar.clicked.connect(self.agregar_filtro)

        self.ui_agregar_filtro.parametro.clear()
        self.ui_agregar_filtro.parametro.addItems([x for x in self.nombres_parametros] + ['Experimento'])

        self.ui_agregar_filtro.parametro.currentIndexChanged.connect(self.refrescar_popup_agregar_filtro)
        self.refrescar_popup_agregar_filtro()

        self.dialog_agregar_filtro.exec()
        
    def refrescar_popup_agregar_filtro(self):
        
        parametro = self.ui_agregar_filtro.parametro.currentText()

        if parametro == 'Experimento':
            tipo = 'string'
        elif parametro in self.nombres_parametros:
            tipo = self.nombres_parametros[parametro]
        else:
            return
        
        if tipo == 'int' or tipo == 'float':
            self.ui_agregar_filtro.condicion.clear()
            self.ui_agregar_filtro.condicion.addItems([ 'Mayor que', 'Menor que', 'Igual a', 'Mayor o Igual que', 'Menor o Igual que' ])
            self.ui_agregar_filtro.valor.clear()
            self.ui_agregar_filtro.valor.setEnabled(True)
        elif tipo == 'string':
            self.ui_agregar_filtro.condicion.clear()
            self.ui_agregar_filtro.condicion.addItems([ 'Contiene', 'Contiene (case sensitive)', 'Igual a', 'Igual a (case sensitive)'])
            self.ui_agregar_filtro.valor.clear()
            self.ui_agregar_filtro.valor.setEnabled(True)
        elif tipo == 'boolean':
            self.ui_agregar_filtro.condicion.clear()
            self.ui_agregar_filtro.condicion.addItems([ 'Verdadero', 'Falso'])
            self.ui_agregar_filtro.valor.clear()
            self.ui_agregar_filtro.valor.setEnabled(False)
            
    def agregar_filtro(self):
        
        parametro = self.ui_agregar_filtro.parametro.currentText()
        condicion = self.ui_agregar_filtro.condicion.currentText()
        valor = self.ui_agregar_filtro.valor.text()

        if parametro == 'Experimento':
            tipo = 'string'
        elif parametro in self.nombres_parametros:
            tipo = self.nombres_parametros[parametro]
        else:
            self.status.setText('Status: Error')
            self.print('Error agregando filtro: Tipo invalido')
            return
        
        if tipo in [ 'int', 'float']:
            if valor.replace('.','').replace(' ', '').isdigit():
                self.filtros.append({'parametro':parametro,'condicion':condicion,'valor':valor.replace(' ' , '')})
                self.print('Filtro agregado: ' + str({'parametro':parametro,'condicion':condicion,'valor':valor.replace(' ' , '')}))
                self.status.setText('Status: OK')
            else:
                self.print('Error agregando filtro: Valor invalido')
                self.status.setText('Status: Error')
        elif tipo == 'string':
                self.filtros.append({'parametro':parametro,'condicion':condicion,'valor':valor.replace(' ' , '')})
                self.print('Filtro agregado: ' + str({'parametro':parametro,'condicion':condicion,'valor':valor.replace(' ' , '')}))
                self.status.setText('Status: OK')
            
        elif tipo == 'boolean':
            self.filtros.append({'parametro':parametro,'condicion':condicion,'valor':''})
            self.print('Filtro agregado: ' + str({'parametro':parametro,'condicion':condicion}))
            self.status.setText('Status: OK')
            
        self.refrescar_filtros()        
        self.dialog_agregar_filtro.done(1)
        
    def popup_eliminar_filtro(self):
        
        if self.ip == '' or self.usuario == '' or self.password == '':
            self.print('Error al eliminar filtro: Servidor desconectado')
            self.status.setText('Status: Error')
            return
        if len(self.busqueda_filtros.selectedItems()) == 0:
            self.print('Error al eliminar filtro: Ninguno seleccionado')
            self.status.setText('Status: Error')
            return

        parametro = self.busqueda_filtros.selectedItems()[0].text(0)
        condicion = self.busqueda_filtros.selectedItems()[0].text(1)
        valor = self.busqueda_filtros.selectedItems()[0].text(2)
        
        self.dialog_eliminar_filtro = QtWidgets.QDialog()
        self.ui_eliminar_filtro = Ui_EliminarFiltro()
        self.ui_eliminar_filtro.setupUi(self.dialog_eliminar_filtro)

        self.ui_eliminar_filtro.cancelar.clicked.connect(self.dialog_eliminar_filtro.done)
        self.ui_eliminar_filtro.eliminar.clicked.connect(self.eliminar_filtro)

        self.ui_eliminar_filtro.parametro.setText(parametro)
        self.ui_eliminar_filtro.condicion.setText(condicion)
        self.ui_eliminar_filtro.valor.setText(valor)

        self.dialog_eliminar_filtro.exec()
        
    def eliminar_filtro(self):
        parametro = self.ui_eliminar_filtro.parametro.text()
        condicion = self.ui_eliminar_filtro.condicion.text()
        valor = self.ui_eliminar_filtro.valor.text()
        
        for filtro in self.filtros:
            if filtro['parametro'] == parametro and filtro['condicion'] == condicion and filtro['valor'] == valor:
                self.filtros.remove(filtro)
                self.print('Filtro eliminado: ' + str(filtro))
                break
        self.status.setText('Status: OK')
        self.refrescar_filtros()
        self.dialog_eliminar_filtro.done(1)

    def buscar(self):
    
        if self.ip == '' or self.usuario == '' or self.password == '':
            self.print('Error al realizar busqueda: Servidor desconectado')
            self.status.setText('Status: Error')
            return

        if len(self.filtros) == 0:
            self.print('Error al realizar busqueda: Busqueda vacia')
            self.status.setText('Status: Error')
            return

        try:
            self.print('Realizando busqueda...')
            resultados = {}
            resultados_parametros = {}
            i=0
            for filtro in self.filtros:

                busqueda = {}
                resultados[i] = {}            
                busqueda['parametro'] = filtro['parametro']

                if filtro['parametro'] == 'Experimento':

                    del busqueda['parametro']

                    if filtro['condicion'] == 'Contiene':
                        busqueda['experimento'] = {'$regex':filtro['valor'], '$options':'i'}
                        
                    elif filtro['condicion'] == 'Contiene (case sensitive)':
                        busqueda['experimento'] = {'$regex':filtro['valor']}
                                            
                    elif filtro['condicion'] == 'Igual a':
                        busqueda['experimento'] = {'$regex': '^' + filtro['valor'] + '$', '$options':'i'}
                                            
                    elif filtro['condicion'] == 'Igual a (case sensitive)':
                        busqueda['experimento'] = {'$regex': '^' + filtro['valor'] + '$'}

            
                elif filtro['condicion'] == 'Mayor que':
                    busqueda['valor'] = {'$gt': float(filtro['valor'])}
                    
                elif filtro['condicion'] == 'Mayor o Igual que':
                    busqueda['valor'] = {'$gte': float(filtro['valor'])}
                    
                elif filtro['condicion'] == 'Menor que':
                    busqueda['valor'] = {'$lt': float(filtro['valor'])}
                    
                elif filtro['condicion'] == 'Menor o Igual que':
                    busqueda['valor'] = {'$lte': float(filtro['valor'])}
                    
                elif filtro['condicion'] == 'Igual a':

                    if filtro['parametro'] in self.nombres_parametros:
                        
                        if self.nombres_parametros[filtro['parametro']] in ['float', 'int']:
                            busqueda['valor'] = float(filtro['valor'])
                        elif self.nombres_parametros[filtro['parametro']] == 'string':
                            busqueda['valor'] = {'$regex': '^' + filtro['valor'] + '$', '$options':'i'}
                        else:
                            busqueda['valor'] = filtro['valor']

                    else:
                        self.print('Error realizando busqueda: Parametro no encontrado')
                        self.status.setText('Status: Error')
                        return
                    
                elif filtro['condicion'] == 'Contiene':
                    busqueda['valor'] = {'$regex':filtro['valor'], '$options':'i'}
                    
                elif filtro['condicion'] == 'Contiene (case sensitive)':
                    busqueda['valor'] = {'$regex':filtro['valor']}
                                        
                elif filtro['condicion'] == 'Igual a (case sensitive)':
                  busqueda['valor'] = {'$regex': '^' + filtro['valor'] + '$'}

                elif filtro['condicion'] == 'Verdadero':
                  busqueda['valor'] = {'$regex': '^True$', '$options':'i'}

                elif filtro['condicion'] == 'Falso':
                  busqueda['valor'] = {'$regex': '^False$', '$options':'i'}

                else:
                    self.print('Error realizando busqueda: Condicion no encontrada')
                    self.status.setText('Status: Error')
                    return
                
                for res in self.mongo_client.db.parametros.find(busqueda):
                    experimento = res['experimento']
                    jornada = res['jornada']
                    if not experimento in resultados[i]:
                        resultados[i][experimento] = {}
                    if not jornada in resultados[i][experimento]:
                        resultados[i][experimento][jornada] = []
                        
                    if '*' in resultados[i][experimento][jornada]:
                        continue

                    if res['datapoint'] == '*':
                        resultados[i][experimento][jornada] = ['*']
                    else:
                        resultados[i][experimento][jornada].append(res['datapoint'])

                resultados_parametros = resultados[i]
                i+=1

            for i in resultados:
                for experimento_filtro in resultados[i]:
                    if experimento_filtro in resultados_parametros:
                        for jornada_filtro in resultados[i][experimento_filtro]:
                            if jornada_filtro in resultados_parametros[experimento_filtro]:
                                datapoints_filtro = resultados[i][experimento_filtro][jornada_filtro]
                                datapoints_globales = resultados_parametros[experimento_filtro][jornada_filtro]
                                if '*' in datapoints_filtro:
                                    continue
                                if '*' in datapoints_globales:
                                    resultados_parametros[experimento_filtro][jornada_filtro] = datapoints_filtro
                                else:
                                    for datapoint in resultados_parametros[experimento_filtro][jornada_filtro]:
                                        if not datapoint in datapoints_filtro:
                                            resultados_parametros[experimento_filtro][jornada_filtro].remove(datapoint)


            self.resultados_globales = {}
            for experimento in resultados_parametros:
                self.resultados_globales[experimento] = {}
                for jornada in resultados_parametros[experimento]:
                    resultados_set = {}
                    if '*' in resultados_parametros[experimento][jornada]:
                        resultados_set['parametros'] = [elem for elem in self.mongo_client.db.parametros.find({'experimento':experimento,'jornada':jornada})]
                        resultados_set['archivos'] = [elem for elem in self.mongo_client.db.indice.find({'experimento':experimento,'jornada':jornada})]
                    else:
                        resultados_set['parametros'] = [elem for elem in self.mongo_client.db.parametros.find({'experimento':experimento,'jornada':jornada,'$or':[{'datapoint':'*'}] + [{'datapoint':x} for x in resultados_parametros[experimento][jornada]]})]
                        resultados_set['archivos'] = [elem for elem in self.mongo_client.db.indice.find({'experimento':experimento,'jornada':jornada,'$or':[{'datapoint':'*'}] + [{'datapoint':x} for x in resultados_parametros[experimento][jornada]]})]
                    
                    self.resultados_globales[experimento][jornada] = resultados_set

            self.refrescar_resultados()
            self.print('Busqueda exitosa')
        
        except Exception as e:
            self.print('Error realizando busqueda:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def refrescar_resultados(self):

        items = []
        i = 0
        for experimento in self.resultados_globales:
            for jornada in self.resultados_globales[experimento]:
                
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, experimento)
                item.setText(1, jornada)
                item.setText(2, str(len(self.resultados_globales[experimento][jornada]['parametros'])))
                item.setText(3, str(len(self.resultados_globales[experimento][jornada]['archivos'])))
                item.setCheckState(4, 0)
                items.append(item)
                i+=1
        self.busqueda_resultados.clear()
        self.busqueda_resultados.addTopLevelItems(items)

    def busqueda_descargar_seleccion(self):

        if self.ip == '' or self.usuario == '' or self.password == '':
            self.print('Error al descargar: Servidor desconectado')
            self.status.setText('Status: Error')
            return

        seleccion = {}
        root = self.busqueda_resultados.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if item.checkState(4) == 2:
                experimento = item.text(0)
                jornada = item.text(1)
                if experimento not in seleccion:
                    seleccion[experimento] = {}
                seleccion[experimento][jornada] = self.resultados_globales[experimento][jornada]

        try:

            parent = Tk()
            parent.overrideredirect(1)
            parent.withdraw()
            carpeta = askdirectory(title = 'Seleccionar Carpeta Descarga')

            if carpeta == '':
                return            

            transport = paramiko.Transport((self.ip,22))
            transport.connect(username = self.usuario, password = self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            if not os.path.exists(carpeta + '/Descargas'):
                os.mkdir(carpeta + '/Descargas')

            for experimento in seleccion:
                if not os.path.exists(carpeta + '/Descargas/' + experimento):
                    os.mkdir(carpeta + '/Descargas/' + experimento)
                    os.mkdir(carpeta + '/Descargas/' + experimento + '/Jornadas')
                for jornada in seleccion[experimento]:
                    if not os.path.exists(carpeta + '/Descargas/' + experimento + '/Jornadas/' + jornada):
                        os.mkdir(carpeta + '/Descargas/' + experimento + '/Jornadas/' + jornada)
                    parametros = {}
                    for parametro in seleccion[experimento][jornada]['parametros']:
                        if parametro['parametro'] not in parametros:
                            parametros[parametro['parametro']] = []
                        parametros[parametro['parametro']].append({'datapoint':parametro['datapoint'], 'valor':parametro['valor'], 'unidad':parametro['unidad']})
                        
                    with open(carpeta + '/Descargas/' + experimento + '/Jornadas/' + jornada +'/parametros.txt', 'w') as archivo:
                        json.dump(parametros, archivo, indent = 4)

                    indice = {}
                    for archivo in seleccion[experimento][jornada]['archivos']:
                        if archivo['nombre'] in ['parametros.txt','indice.txt']:
                            continue
                        indice[archivo['nombre']] = archivo['datapoint']
                        sftp.get('usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada + '/' + archivo['nombre'], carpeta + '/Descargas/' + experimento + '/Jornadas/' + jornada + '/' + archivo['nombre'])

                    with open(carpeta + '/Descargas/' + experimento + '/Jornadas/' + jornada +'/indice.txt', 'w') as archivo:
                        json.dump(indice, archivo, indent = 4)

            self.print('Resultados de busqueda descargados exitosamente en ' + carpeta + '/Descargas')
            self.status.setText('Status: OK')
            
        except Exception as e:
            self.print('Error descargando archivos:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def obtener_seleccion_arbol(self, arbol):
        seleccion = {}
        for i in range(arbol.childCount()):
            item = arbol.child(i)
            if item.checkState(2) == 2:
                seleccion[item.text(0)] = '*'
            else:
                interior = self.obtener_seleccion_arbol(item)
                if interior != {}:
                    seleccion[item.text(0)] = interior
        return seleccion

    def explorar_descargar_seleccion(self):

        
        if self.ip == '' or self.usuario == '' or self.password == '':
            self.print('Error al descargar: Servidor desconectado')
            self.status.setText('Status: Error')
            return

        try:

            root = self.explorar_archivos.invisibleRootItem()
            arbol = self.obtener_seleccion_arbol(root)
            
            parent = Tk()
            parent.overrideredirect(1)
            parent.withdraw()
            carpeta = askdirectory(title = 'Seleccionar Carpeta Descarga')

            if carpeta == '':
                return            

            transport = paramiko.Transport((self.ip,22))
            transport.connect(username = self.usuario, password = self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)

            if not os.path.exists(carpeta + '/Descargas'):
                os.mkdir(carpeta + '/Descargas')

            self.descargar_archivos_desde_arbol(arbol, carpeta + '/Descargas', 'usuario_sftp/Experimentos', sftp)

            self.print('Archivos seleccionados descargados exitosamente en ' + carpeta + '/Descargas')

            self.status.setText('Status: OK')
            
        except Exception as e:
            self.print('Error descargando archivos:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def descargar_archivos_desde_arbol(self, arbol, carpeta_local, carpeta_remota, sftp):

        for elemento in sftp.listdir_attr(carpeta_remota):
            if elemento.filename in arbol:
                if stat.S_ISDIR(elemento.st_mode):
                    if not os.path.exists(carpeta_local + '/' + elemento.filename):
                        os.mkdir(carpeta_local + '/' + elemento.filename)
                    if arbol[elemento.filename] == '*':
                        arbol_nuevo = {}
                        for x in sftp.listdir_attr(carpeta_remota + '/' + elemento.filename):
                            arbol_nuevo [x.filename] = '*'
                        self.descargar_archivos_desde_arbol(arbol_nuevo, carpeta_local + '/' + elemento.filename, carpeta_remota + '/' + elemento.filename, sftp)
                    else:
                        self.descargar_archivos_desde_arbol(arbol[elemento.filename], carpeta_local + '/' + elemento.filename, carpeta_remota + '/' + elemento.filename, sftp)
                else:
                    sftp.get(carpeta_remota + '/' + elemento.filename, carpeta_local + '/' + elemento.filename)

    def visualizar_resultados(self):
        try:

            if len(self.busqueda_resultados.selectedItems()) == 0:
                return
            
            experimento = self.busqueda_resultados.selectedItems()[0].text(0)
            jornada = self.busqueda_resultados.selectedItems()[0].text(1)

            self.busqueda_label_experimento.setText(experimento)
            self.busqueda_label_jornada.setText(jornada)

            parametros = self.resultados_globales[experimento][jornada]['parametros']
            items_parametros = []
            i=0
            for parametro in parametros:
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0,parametro['datapoint'])
                item.setText(1,parametro['parametro'])
                item.setText(2,str(parametro['valor']))
                item.setText(3,parametro['unidad'])
                items_parametros.append(item)
                i+=1
            self.busqueda_parametros.clear()     
            self.busqueda_parametros.addTopLevelItems(items_parametros)

            archivos = self.resultados_globales[experimento][jornada]['archivos']
            items_archivos = []
            i=0
            for archivo in archivos:
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0,archivo['datapoint'])
                item.setText(1,archivo['nombre'])
                items_archivos.append(item)
                i+=1
            self.busqueda_archivos.clear()
            self.busqueda_archivos.addTopLevelItems(items_archivos)
            


        except Exception as e:
            self.print('Error visualizando archivo:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def visualizar_archivo_busqueda(self):

        if len(self.busqueda_archivos.selectedItems()) == 0:
            return

        try:

            archivo = self.busqueda_archivos.selectedItems()[0].text(1)
            jornada = self.busqueda_label_jornada.text()
            experimento = self.busqueda_label_experimento.text()

            if jornada == '-' or experimento == '-':
                return

            filepath = 'usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada + '/' + archivo
            
            if filepath[-4:].lower() == '.csv':
                self.visualizar_csv(filepath, self.busqueda_preview_graph, self.busqueda_preview_image, self.busqueda_preview_text, self.busqueda_preview_label)

            elif filepath[-4:].lower() == '.png' or filepath[-4:].lower() == '.jpg' or filepath[-5:].lower() == '.jpeg' or filepath[-5:].lower() == '.gif':
                self.visualizar_imagen(filepath, self.busqueda_preview_graph, self.busqueda_preview_image, self.busqueda_preview_text, self.busqueda_preview_label)

            elif filepath[-4:].lower() == '.txt' or filepath[-5:].lower() == '.json' or filepath[-7:].lower() == '.config' or filepath[-3:].lower() == '.py':
                self.visualizar_texto(filepath, self.busqueda_preview_graph, self.busqueda_preview_image, self.busqueda_preview_text, self.busqueda_preview_label)

            else:
                self.busqueda_preview_graph.setVisible(False)
                self.busqueda_preview_image.setVisible(False)
                self.busqueda_preview_text.setVisible(False)

            self.status.setText('Status: OK')

        except Exception as e:
            self.print('Error visualizando archivo:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def visualizar_archivo_explorar(self):
        try:
           
            if self.explorar_archivos.selectedItems()[0].parent() == None:
                return
            if self.explorar_archivos.selectedItems()[0].parent().parent() == None:
                return
            if self.explorar_archivos.selectedItems()[0].parent().parent().parent() == None:
                jornada = self.explorar_archivos.selectedItems()[0].text(0)
                experimento = self.explorar_archivos.selectedItems()[0].parent().parent().text(0)
                self.visualizar_parametros_explorar( experimento, jornada )
                return

            archivo = self.explorar_archivos.selectedItems()[0].text(0)
            jornada = self.explorar_archivos.selectedItems()[0].parent().text(0)
            experimento = self.explorar_archivos.selectedItems()[0].parent().parent().parent().text(0)
            filepath = 'usuario_sftp/Experimentos/' + experimento + '/Jornadas/' + jornada + '/' + archivo
            
            self.visualizar_parametros_explorar( experimento, jornada )
            
            if filepath[-4:].lower() == '.csv':
                self.visualizar_csv(filepath, self.explorar_preview_graph, self.explorar_preview_image, self.explorar_preview_text, self.explorar_preview_label)

            elif filepath[-4:].lower() == '.png' or filepath[-4:].lower() == '.jpg' or filepath[-5:].lower() == '.jpeg' or filepath[-5:].lower() == '.gif':
                self.visualizar_imagen(filepath, self.explorar_preview_graph, self.explorar_preview_image, self.explorar_preview_text, self.explorar_preview_label)

            elif filepath[-4:].lower() == '.txt' or filepath[-5:].lower() == '.json' or filepath[-7:].lower() == '.config' or filepath[-3:].lower() == '.py':
                self.visualizar_texto(filepath, self.explorar_preview_graph, self.explorar_preview_image, self.explorar_preview_text, self.explorar_preview_label)

            else:
                self.explorar_preview_graph.setVisible(False)
                self.explorar_preview_image.setVisible(False)
                self.explorar_preview_text.setVisible(False)

            self.status.setText('Status: OK')

        except Exception as e:
            self.print('Error visualizando archivo:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def visualizar_parametros_explorar(self, experimento, jornada):
        try:
            items = []
            i=0
            for parametro in self.mongo_client.db.parametros.find({'experimento':experimento,'jornada':jornada}):
                item = QtWidgets.QTreeWidgetItem(i)
                item.setText(0, parametro['datapoint'])
                item.setText(1, parametro['parametro'])
                item.setText(2, str(parametro['valor']))
                item.setText(3, parametro['unidad'])
                items.append(item)
                i+=1
            self.explorar_parametros.clear()
            self.explorar_parametros.addTopLevelItems(items)
            self.status.setText('Status: OK')

        except Exception as e:
            self.print('Error visualizando parametros:')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')

    def visualizar_csv(self, filepath, graph_frame, image_frame, text_frame, preview_label):

        transport = paramiko.Transport((self.ip,22))
        transport.connect(username = self.usuario, password = self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        with sftp.open(filepath, mode = 'r') as file:
            dataframe = pd.read_csv(file)
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

        transport = paramiko.Transport((self.ip,22))
        transport.connect(username = self.usuario, password = self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        
        dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        sftp.get(filepath, dir_path + '/imagen_temp.' + filepath.split('.')[-1])

        self.pixmap = QPixmap(dir_path + '/imagen_temp.' + filepath.split('.')[-1]).scaled(651,231, aspectRatioMode = Qt.AspectRatioMode.KeepAspectRatio)            
        graph_frame.setVisible(False)
        image_frame.setVisible(True)
        text_frame.setVisible(False)
        preview_label.setText(filepath.split('/')[-1])
        image_frame.setPixmap(self.pixmap)
        image_frame.show()

        os.remove(dir_path + '/imagen_temp.' + filepath.split('.')[-1])

    def visualizar_texto(self, filepath, graph_frame, image_frame, text_frame, preview_label):
                
        transport = paramiko.Transport((self.ip,22))
        transport.connect(username = self.usuario, password = self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        with sftp.open(filepath, mode = 'r') as file:
                text_frame.clear()
                lineas = file.readlines()
                for linea in lineas:
                    text_frame.append(linea)
                
                graph_frame.setVisible(False)
                image_frame.setVisible(False)
                text_frame.setVisible(True)
                preview_label.setText(filepath.split('/')[-1])

    def generar_arbol(self, sftp, root, folder):
        i=0
        for elemento in sftp.listdir_attr(folder):
            item = QtWidgets.QTreeWidgetItem(i)
            item.setText(0, elemento.filename)
            item.setCheckState(2, 0)
            if folder + '/' + elemento.filename in self.indice:
                item.setText(1, self.indice[folder + '/' + elemento.filename])
            else:
                item.setText(1, '-')
            root.addChild(item)
            if stat.S_ISDIR(elemento.st_mode):
                self.generar_arbol(sftp, item, folder + '/' + elemento.filename)
            i+=1

    def refrescar_checkbox_arbol(self,item):
        
        for i in range(item.childCount()):
            item.child(i).setCheckState(2,item.checkState(2))

    def conectar(self):
        self.print('Conectando a servidor...')
        self.status.setText('Status: Conectando')

        try:
            self.mongo_client = pymongo.MongoClient(self.conexion_ip.text(), username=self.conexion_usuario.text(), password=self.conexion_password.text(), serverSelectionTimeoutMS = 2000)
            self.nombres_parametros = {}
            for parametro in self.mongo_client.db.nombres_parametros.find({}):
                self.nombres_parametros[parametro['nombre']] = parametro['tipo']
            self.indice = {}
            for item in self.mongo_client.db.indice.find({}):
                self.indice['usuario_sftp/Experimentos/' + item['experimento'] + '/Jornadas/' + item['jornada'] + '/' + item['nombre']] = item['datapoint']


            transport = paramiko.Transport((self.conexion_ip.text(),22))
            transport.connect(username = self.conexion_usuario.text(), password = self.conexion_password.text())
            sftp = paramiko.SFTPClient.from_transport(transport)

            if not 'usuario_sftp' in sftp.listdir('./'):
                sftp.mkdir('usuario_sftp')
            if not 'Experimentos' in sftp.listdir('usuario_sftp'):
                sftp.mkdir('usuario_sftp/Experimentos')
            self.explorar_archivos.clear()
            self.generar_arbol(sftp, self.explorar_archivos.invisibleRootItem(), 'usuario_sftp/Experimentos')
            self.explorar_archivos.itemChanged.connect(self.refrescar_checkbox_arbol)

            self.usuario = self.conexion_usuario.text()
            self.password = self.conexion_password.text()
            self.ip = self.conexion_ip.text()        

            self.print('Conexion exitosa al servidor')
            self.status.setText('Status: OK')

        except Exception as e:
            self.print('Error conectando al servidor')
            self.print(str(e) + '\n')
            self.status.setText('Status: Error')
            self.nombres_parametros = {}

    def print(self, text):
        self.log.append( datetime.datetime.now().strftime('%H:%M:%S - ') + str(text))
        self.log.moveCursor(QTextCursor.End)
        self.log.ensureCursorVisible()

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QIcon('icon.ico'))
Widget = QtWidgets.QWidget()
ui = Office_Wigdet(Widget)
Widget.show()
Widget.setWindowTitle('Applicacion de Oficina')
sys.exit(app.exec())
