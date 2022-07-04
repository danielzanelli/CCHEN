# Aplicación de Laboratorio


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
> Para instalar el software, descargue el archivo `AppLab - Windows.zip`:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177222815-e8f19e10-f6fd-4a3c-8b0a-3967ef846594.png)
> 
> <br>
> 
> Y descomprima el contenido del .zip en alguna carpeta de su elección:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177222963-c8b3874b-b801-498d-af6b-d608404bce3e.png)
> 
> <br>
> 
> Una vez descomprimido, accedemos a la carpeta `AppLab` y ubicamos el archivo `AppLab.exe`. Haciendo click derecho podemos crear un acceso directo, el cual podemos ubicar en el escritorio o donde más acomode:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177223171-90405739-dc9a-4f9f-b813-d7a5b8a68864.png)
> 
> <br>
> 
> Finalmente, podemos cambiar el nombre del acceso directo:
> 
> ![image](https://user-images.githubusercontent.com/83187517/177223270-46d0f4b6-b065-4814-b6a1-4c8906e3c131.png)
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
> Primero, se debe descargar el contenido de la carpeta `/src/` de este repositorio, que contiene el código fuente de este software, a alguna carpeta en la maquina local. El archivo `.py` ejecutable es el `AppLab.py`
> 
> <br>
> 
> Antes de ejecutar, se deben instalar las dependencias. Si no cuenta con el gestor de paquetes de python (pip) instalado, puede ser instalado en sistemas operativos Windows siguiendo [esta guia](https://technetters.com/como-instalar-pip-para-python-windows/). En sistemas operativos basados en debian (como Ubuntu), se puede instalar simplemente utilizando el comando:
> 
> `sudo apt install python3-pip`
> 
> Para instalar las dependencias del software usando pip:
> 
> `pip install paramiko pymongo pyvisa numpy pandas tk pyqt5 pyqtgraph`
> 
> Para sistemas operativos basados en Debian (como Ubuntu) se debe instalar `tk` (Tkinter) por separado:
> 
> `pip install paramiko pymongo pyvisa numpy pandas pyqt5 pyqtgraph`
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
> `python AppLab.py`
> 
> </details>

<br/>

## Drivers Osciloscopios

Este software requiere que estén instalados los drivers para reconocer y comunicarse con los osciloscopios. El software fue desarrollado específicamente para ser compatible con osciloscopios `Tektronix`, cuyos drivers pueden encontrarse en [este enlace](https://www.tek.com/en/support/software/driver/tekvisa-connectivity-software-v411). 

Sin embargo, el software es compatible con osciloscopios que operen usando el protocolo `VISA`, por lo que es posible instalar drivers de otros proveedores, como [NI-VISA](https://www.ni.com/es-cl/support/downloads/drivers/download.ni-visa.html).  Para mayor información respecto a los drivers y la compatibilidad con su osciloscopio contacte su proveedor.

<br/>

## Compilacion Código Fuente a Programa Windows

El codigo fuente en `/src/` puede ser complilado a programa de Windows (.exe) utilizando [pyinstaller](https://pyinstaller.org/en/stable/), abriendo una terminal en la carpeta y ejecutando el comando:

`pyinstaller AppLab.py --icon icon.ico --windowed`

<br/>

Posteriormente se puede agregar el archivo 'icon.ico' a la carpeta generada y crear un acceso directo a AppLab.exe para mayor comodidad.

## Compilación GUI a Python

Se pueden realizar modificaciones a las ventanas de la interfaz gráfica disponibles en la carpeta `/ui/`. Estos pueden ser modificados con diseñadores de software QT, como QtCreator, para mas información sobre la plataforma Qt puede acceder [aqui](https://www.qt.io/product/development-tools). 

En caso de querer recompilar los archivos `.ui`, esto se puede realizar usando la librería python `pyuic`. Para mayor información sobre esta librería y su instalación, puede acceder [aqui](https://pypi.org/project/pyuic5-tool/). Los archivos `.ui` pueden compilarse a `.py` mediante el comando (tomando como ejemplo el archivo `ventanaPrincipal.ui`):

<br/>

`pyuic5 -x .\ventanaPrincipal.ui -o ventanaPrincipal.py`

<br/>

