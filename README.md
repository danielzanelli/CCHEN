# Sistema de Adquisición, Almacenamiento y Visualización de Datos Experimentales

##### Autor: Daniel Zanelli

Este sistema funciona utilizando dos programas o aplicaciones: Uno para ser usado en el laboratorio al ingresar datos manualmente y por medio de osciloscopios, y otro para ser usado en la oficina capaz de buscar y desgargar datos experimentales. Ambos se cominucan con el mismo servidor, en el cual se encuentran almacenados los datos.

## Aplicacion de Laboratorio
- Ingreso manual de datos experimentales
- Conexion de osciloscopios
- Adquisición de curvas
- Captura autmatica con trigger
- Almacenamiento de datos local
- Subida de datos a servidor

### Modo de uso

El programa puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).

\n
Para instalar las dependencias mediante el gestor de paquetes de python (pip):

`pip install paramiko pymongo pyvisa numpy pandas tkinter pyqt5 pyqtgraph`


\n
Luego para ejecutar:

`python AppLab.py`

\n
El software puede ser complilado a programa de windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/):

`pyinstaller AppLab.py --icon icon.ico --windowed`

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppLab.exe para mayor comodidad.

## Aplicacion de Oficina
- Conexion a servidor
- Busquedas de datos segun parametros
- Explorar archivos servidor

#### Modo de uso
El programa puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).

\n
Para instalar las dependencias mediante el gestor de paquetes de python (pip):

`pip install paramiko pymongo numpy pandas tkinter pyqt5 pyqtgraph`

\n
Luego para ejecutar:

`python AppOffice.py`

\n
El software puede ser complilado a programa de windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/):

`pyinstaller AppOffice.py --icon icon.ico --windowed`

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppOffice.exe para mayor comodidad.

## Servidor Local
- Base de datos MongoDB
- Servidor SFTP
- Administración usuarios
