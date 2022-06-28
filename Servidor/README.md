## Configuracion del Servidor

Para el uso del sistema, se requiere de la implementación de un servidor que sea capaz de correr un servicio de SFTP y MongoDB. 
En esta implementación se cosidera un servidor corriendo en un sistema operativo Ubuntu 20.04.

<br/>

### Configuración sistema operativo

Al contar con el equipo destinado como servidor, se procede a instalar el sistema operativo:

![image](https://user-images.githubusercontent.com/83187517/176061639-15ef249c-8d3d-4091-b310-304d7ff9b589.png)

Se pueden descargar versiones del sistema operativo Ubuntu [aqui](https://releases.ubuntu.com/).

<br/>

### Configuración usuarios

Una vez instalado el sistema operativo, se deben crear los usuarios. Para esta implementación se considera un usuario Admin, con permisos de administrador sobre el equipo; un usuario 'usuario_sftp', quien almacenará todos los archivos de datos en su carpeta local; y usuarios específicos para cada usuario real del sistema.
Los usuarios personales deben ser creados con claves únicas personales por razones de seguridad. 

Estos usuarios se pueden agregar al servidor usando el comando:

`sudo adduser nombre_usuario`

Estos usuarios deben pertenecer al grupo 'sftp', el cual puede ser creado utilizando el comando:

`sudo groupadd sftp`

El usuario se agrega al grupo mediante:

`sudo usermod -a -G sftp nombre_usuario`

Esto debe realizarse para cada usuario que utilice el sistema.

Finalmente, agregaremos el usuario 'usuario_sftp' y configuraremos su carpeta base para que sea accesible por todos los usuarios, utilizando los siguientes comandos:

`sudo adduser usuario_sftp`

`sudo groupadd sftp`

`sudo chmod 777 /home/sftp_user/`

<br/>

### Configuración SFTP

Para instalar el servicio de SFTP (Secure File Transfer Protocol) se pueden seguir los siguientes pasos, para mayor detalle revisar [esta guia](https://linuxhint.com/setup-sftp-server-ubuntu/).

Primero, se debe instalar el servicio ssh:

`sudo apt install ssh`

Una vez instalado, se debe modificar el archivo de configuración mediante el comando:

`sudo nano /etc/ssh/sshd_config`

Al final del archivo, se deben agregar las siguientes líneas:

<code>
  Match group sftp <br/>
  ChrootDirectory /home <br/>
  ForceCommand internal-sftp <br/>
<code/>

Finalmente, se debe reinicar el servicio ssh:
  
`sudo systemctl restart ssh`

<br/>

### Configuración MongoDB

Para instalar la base de datos MongoDB en el servidor Ubuntu 20.04 se pueden seguir los siguientes pasos. Para mayor detalle favor de revisar [esta guia](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04-es).

Para descargar e instalar MongoDB se pueden ejecutar los siguientes comandos:

`sudo apt install curl`
  
`curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -`

`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`

`sudo apt update`

`sudo apt install mongodb-org`

Tras instalada la base de datos, se puede inicializar usando:

`sudo systemctl start mongod.service`

Finalmente, para que la base de datos se inicie al arrancar el sistema operativo:

`sudo systemctl enable mongod`
  
Ahora que tenemos la base de datos activa, podemos administrar los usuarios para que accedan a esta utilizando sus usuarios y contraseñas. Cabe destacar que estos usuarios y contrseñas deben coincidir con los usuarios y contraseñas utilizadas en la reación de usuarios en el servidor.
Esto puede realizarse con mayor facilidad utilizando una GUI capaz de administrar las bases de datos Mongo, como Robo3T. Las ultimas versiones de este software se pueden encontrar [aqui](https://github.com/Studio3T/robomongo/releases).

Tras instalar y ejecutar el software, nos debemos conectar al servicio MongoDB del servidor. Para agregar una nueva conexón se puede presionar el enlace `Create`:
  
![image](https://user-images.githubusercontent.com/83187517/176067090-bc91775c-28bb-41a2-945f-85b8d5a24ceb.png)

Desde el mismo servidor, se puede conectar directamente a `localhost`. En caso de estar accediendo desde otro equipo desde la red, se debe especificar la IP del servidor.

![image](https://user-images.githubusercontent.com/83187517/176067303-f963b31c-ef81-4e54-b204-b543f44c83b7.png)

Una vez realizada la conexion exitosamente, se pueden agregar los usuarios desde el panel de la izquierda, accediendo a `System`, luego a `admin` y finalmente haciendo click derecho en `Users` para eleccionar la opción `Add User`:
  
![image](https://user-images.githubusercontent.com/83187517/176068269-e6986a09-5be3-4445-8e11-923afc9bd15a.png)

Aqui se deben ingresar los datos delos usuarios. Notar que estos deben coincidir con los usuarios y contraseñas de los usuarios agregados al sistema mediante `sudo adduser usuario_sftp`.

![image](https://user-images.githubusercontent.com/83187517/176068593-6cdad4ff-7d13-4206-acf6-3f890b2e9b39.png)


  
  
