# Applicacion de Oficina


<br>

## Modo de Uso

<br>


<details>
<summary> <h2> Ejecución Programa Windows </h2> </summary>

<br>

> ## Instalación
> 
> <br>
> 
> Para instalar el software, descargue el archivo `AppOffice - Windows.zip`:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177225347-93966285-0053-46ed-b54c-be1f70731c9c.png)
> 
> <br>
> 
> Y descomprima el contenido del .zip en alguna carpeta de su elección:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177225441-24567f03-3f15-4219-9dab-d31c47c69ad9.png)
> 
> <br>
> 
> Una vez descomprimido, accedemos a la carpeta `AppOffice` y ubicamos el archivo `AppOffice.exe`. Haciendo click derecho podemos crear un acceso directo, el cual podemos ubicar en el escritorio o donde más acomode:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177225510-e854df27-de6f-4845-a114-0ef7e23eb12d.png)
> 
> <br>
> 
> Finalmente, podemos cambiar el nombre del acceso directo:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177225586-bc15db1a-d39e-479d-9348-24ccaa0931c1.png)
> 
> <br>
> 
> <br>
> 
> ## Ejecución
> 
> <br>
> 
> Para ejecutar el programa compilado para windows, una vez realizada la instalación, simplemente se puede hacer doble click sobre el acceso directo.
> 
> </details>

<br>

<br>

<details>
<summary> <h2> Ejecución Código Fuente </h2> </summary>

> 
> <br>
> 
> ## Instalación
> 
> <br>
> 
> El software puede ser ejecutado directamente utilizando python 3. En caso de no tenerlo instalado, se puede descargar [aqui](https://www.python.org/downloads/).
> 
> <br>
> 
> Primero, se debe descargar el contenido de la carpeta `/src/` de este repositorio, que contiene el código fuente de este software, a alguna carpeta en la maquina local. El archivo `.py` ejecutable es el `AppOffice.py`
> 
> <br>
> 
> Antes de ejecutar, se deben instalar las dependencias. Si no cuenta con el gestor de paquetes de python (pip) instalado, puede ser instalado en sistemas operativos Windows siguiendo [esta guia](https://technetters.com/como-instalar-pip-para-python-windows/). En sistemas operativos basados en debian (como Ubuntu), se puede instalar simplemente utilizando el comando:
> 
> `sudo apt install python3-pip`
> 
> Para instalar las dependencias del software usando pip:
> 
> `pip install paramiko pymongo numpy pandas tk pyqt5 pyqtgraph`
> 
> Para sistemas operativos basados en Debian (como Ubuntu) se debe instalar `tk` (Tkinter) por separado:
> 
> `pip install paramiko pymongo numpy pandas pyqt5 pyqtgraph`
> 
> `sudo apt install python3-tk`
> 
> En caso de encontrarse con el error `qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.` en sistemas operativos Debian, este puede > solucionarse instalando la dependencia:
> 
> `sudo apt install libxcb-xinerama0`
> 
> 
> <br/>
> 
> ## Ejecución
> 
> Finalmente, una vez instaladas las dependencias del programa, este se puede ejecutar abriendo una consola en la carpeta que contiene los archivos y utilizando el comando:
> 
> `python AppOffice.py`
> 
> </details>

<br/>

## Compilacion Código Fuente a Windows

El codigo fuente en `/src/` puede ser complilado a programa de Windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/), abriendo una terminal en la carpeta y ejecutando el comando:

`pyinstaller AppOffice.py --icon icon.ico --windowed`

<br/>

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppLab.exe para mayor comodidad.

## Compilación GUI a Python

Se pueden realizar modificaciones a las ventanas de la interfaz gráfica disponibles en la carpeta `/ui/`. Estos pueden ser modificados con diseñadores de software QT, como QtCreator, para mas información sobre la plataforma Qt puede acceder [aqui](https://www.qt.io/product/development-tools). 

En caso de querer recompilar los archivos `.ui`, esto se puede realizar usando la librería python `pyuic`. Para mayor información sobre esta librería y su instalación, puede acceder [aqui](https://pypi.org/project/pyuic5-tool/). Los archivos `.ui` pueden compilarse a `.py` mediante el comando (tomando como ejemplo el archivo `ventanaPrincipal.ui`):

<br/>

`pyuic5 -x .\ventanaPrincipal.ui -o ventanaPrincipal.py`

<br/>

