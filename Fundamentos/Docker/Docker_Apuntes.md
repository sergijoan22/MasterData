# Docker

## Arquitectura de microservicios

Al darle a comprar una cosaen amazon hay que hacer varias cosas: comprobar stock, reservar el producto, llamar al pago...

Antes se usaban funciones de código que se llamaban una a una. Ahora, se crean unidades de código que se llaman. A los desarrolladores se le asigna una tarea específica y una potencia de hardware mayor o menor. Esto se llama microservicios. Bueno para virtualización, ya que puedes hacerlo en alguna parte solo. Bueno para cosas complejas.

La architectura de microservicios: Se separa la aplicación en diferentes bloques separados pero conectados. El problema de esta estructura dividida: La coordinación entre los bloques, por ejemplo: El microservicio de pago podría fallar pero el de enviar el producto no.

## Containers

Paquete de software estandarizado, que permite aislar unos de otros. Comparten el mismo OS kernel. Los contenedores no tienen dentro un SO completo, ya que el core de este (el kernel) está fuera y lo permite compartir con todos los contenedores.

La diferencia entre un contenedor y una maquina virtual es que no hay un SO completo, como si en una MV. Por tanto, los contenedores son muy livianos, ya que la parte de SO de cada contenedor es muy liviana. En un contenedor podemos poner Alpine, que es un SO muy ligero, para aplicaciones que no requieran más. Así, se ahorra recursos. Los contendores pemiten usar más SO a la vez en una máquina.

Al hacer una MV en Google Cloud hace esto al hacer una instancia, crea solo la parte de arriba.

Docker es una plataforma abierta para generar, enviar y correr contenedores.

### Docker engine

Aplicación cliente-servidor compuesto por:

- Servidor: El que crea el contenedor
- API rest: Servicio en internet que devuelve una funcionalidad.
- Command line interface

### Prueba con Docker

Vamos a la consola de Google Cloud con nuestra cuenta. Vamos a compue engine -> instancias de vm.

Vamos a crear una MV, y dentro ejecutar docker y un contenedor. Vamos a crear uno predefinido para hacer pruebas.

Para docker no vale cualquier MV.

Le damos a crear instancia: la zona la que sea mas barata. De máquina elegimos la e2-small, ya que 2gb de ram son suficientes. Le tenemos que clickar a permitir tráfico HTTP y HTTPS (así permitimos tráfico entrante por el puerto 80, que es el de http). (Los cloud bloquean todo por defecto así que es importante marcar que queremos permitir).

Hay que cambiar el disco de arranque porque el de defecto no tiene docker. En las opciones, de las imágenes públicas ponemos en el SO el Container Optimized OS. En la versión, ponemos de LTS (long time support) la última versión, la 89.

Truco para pagar menos: Activar interrumpibilidad en el menú de crear la máquina. Son más baratas pero solo duran 24 horas y se pueden interrumpir derepente por demanda. Por ello, ni en este ni tampoco en otro caso es recomendable guardar datos dentro de la máquina.

Ahora ya podemos crear la máquina. En SSH le damos a abrir en otra ventana y ya entramos en el terminal. En esta tenemos docker porque hemos elegido una ya preparado, en la defecto no lo tiene pero se podria descargar.

Escribimos 

`docker version` 

para ver la versión de docker. 

Luego `docker run -dp 80:80 docker/getting-started`. 

Esto crea un contenedor. -d permite que no se bloquee y aparezca otra vez lo de comandos. -p especifica el puerto, 80:80 mapea el puerto 80 del contendor con el puerto 80 de la máquina anfitriona. Luego docker/getting-started es la imagen elegida para crear el contenedor.

En la respuesta dice que no puede encontrar la imagen en local, por lo que la busca en internet.

En la pagina de GCloud y buscamos la IP externa de la instancia. Si por está Ip entramos en el puerto 80 nos rideccionará al puerto 80 del contenedor. Pegamos esta ip externa en el navegador. Se abre una página web. Ahora ya podemos cerrar la instancia.



#### Ahora vamos a hacer lo mismo en local en nuestro PC

En el terminal de windows escribimos

`docker run -d -p 80:80 docker/getting-started`

Una vez creado el contenedor, vamos a Docker desktop y nos saldrá llamado jovial_dirac. Este nombre es aleatorio al no haber especificado uno. Al darle al contenedor, una opción es abrirlo en el navegador, y nos saldrá la misma página que en el caso con Google Cloud. Otra opción para verla es poner en el navegador localhost.

De las dos, la diferencia es que el de la máquina se puede ver en cualquier sitio y el local solo en nuestro PC.



El ciclo normal es crear un Docker file, con el que construye una imagen. Y a partir de esta imagen se construye el contenedor. En nuestra prueba, directamente hemos cogido una imagen ya existente y con ella hemos creado el contenedor.

Al descargar la imagen de internet, va descargando los diferentes fotogramas hasta tener todos que forman la imagen. Partiendo de un contenedor, para crear una imagen a partir de este, se añaden fotogramas a los que ya hay.

Los fotogramas descargados se guardan en la caché  y docker cachea para ver si ya se encuentran en la máquina.

### Docker file 

Es una secuencia de instrucciones. Cada instrucción crea una capa. Archivo sin extensión que se debe llamar Dockerfile. Se pueden subir o descargar a Docker hub, que es un repositorio. Tiene 3 tipos de instrucciones: Fundamentales, de configuración y de ejecución.

### Docker image

Se reconocen por un nombre o una ID (lo que salia al descargar las capas de la imagen desde el terminal).

### Docker terminal

Exponiendo el puerto, el contenedor lo puede ver la máquina anfitriona o los demás contenedores.

## Docker desktop

Para borrar un contenedor o una imagen, desde el menú principal de Docker desktop.

Para entrar a Docker se puede poner el comando docker exec o bien el icono de docker desktop.

En la lista de imágenes muestra cuales están en uso.

Al usar docker, el kernel es el propio de macos. En windows, una de las dos opciones es usar hyper-v, que crea una maquina virtual con Linux de la que se usa su kernel. 

## Docker Hub

Nos creamos una cuenta en Docker Hub para poder guardar ahí imágenes.

[Orientation and setup | Docker Documentation](https://docs.docker.com/get-started/?utm_source=mailgun&utm_medium=email&utm_campaign=confirm-verify-email-address)

En docker registry podemos subir las imágenes.

`docker push` para subirla y `docker pull` para bajarla.

Antes de hacer un push hay que registrarse.

Cluster de servidores: Conjunto de servidores interconectados.

Los contenedores podrían contener virus, pero lo que hay dentro del cotnenedor no tiene protestad para ejecutar programas en la máquina. Por tanto, oferece mucha mejor seguridad.

## Docker volume

Hacer que datos en el contenedor se guarden en una unidad fuera, en una parte del disco duro. Al eliminar el contenedor, esos datos no se borran. También permite añadir datos en la unidad y que queden reflejados dentro del contenedor.

## Docker compose

Para ejecutar aplicaciones complejas, con varios componentes. Permite definir varios contenedores a la vez.  

Usa ficheros yaml (con extensión .yaml o .yml)

En un fichero:

En el apartado servicios: App, influxdb y grafana.

![image-20210925123049844](../Assets/image-20210925123049844.png)

En este archivo creamos 3 contenedores. En el segundo se crea a partir de una imagen y en los otros a a partir de un Dockerfile. Para cada contenedor se crea un volumen, se redireccionan los puertos, y en el primero se hace que dependa del contenedor influxdb.

## Kubernetes

Organiza cuando hay muchos contenedores.

Permite copiar archivos de la máquina anfritirona al contenedor y viceversa.

