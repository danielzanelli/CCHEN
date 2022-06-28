# AppOffice

### Instalación
El programa puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).

<br/>

Para instalar las dependencias mediante el gestor de paquetes de python (pip):

`pip install paramiko pymongo numpy pandas tk pyqt5 pyqtgraph`

Para sistemas operativos basados en Debian (como Ubuntu) se debe instalar `tk` (Tkinter) por separado:

`pip install paramiko pymongo numpy pandas pyqt5 pyqtgraph`

`sudo apt install python3-tk`

En caso de encontrarse con el error `qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.` en sistemas operativos Debian, este puede solucionarse instalando la dependencia:

`sudo apt install libxcb-xinerama0`

<br/>

### Modo de uso

Finalmente, una vez instaladas las dependencias del programa, este se puede ejecutar utilizando:

`python AppOffice.py`

<br/>

### Compilacion a Windows


El software puede ser complilado a programa de windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/):

`pyinstaller AppOffice.py --icon icon.ico --windowed`

<br/>

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppOffice.exe para mayor comodidad.
