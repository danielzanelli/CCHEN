# AppOffice

#### Modo de uso
El programa puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).

<br/>

Para instalar las dependencias mediante el gestor de paquetes de python (pip):

`pip install paramiko pymongo numpy pandas tk pyqt5 pyqtgraph`

Para sistemas operativos basados en Debian (como Ubuntu) se debe instalar `tk` por separado:

`pip install paramiko pymongo numpy pandas pyqt5 pyqtgraph`
`sudo apt install python3-tk`

<br/>

Luego para ejecutar:

`python AppOffice.py`

<br/>

El software puede ser complilado a programa de windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/):

`pyinstaller AppOffice.py --icon icon.ico --windowed`

<br/>

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppOffice.exe para mayor comodidad.
