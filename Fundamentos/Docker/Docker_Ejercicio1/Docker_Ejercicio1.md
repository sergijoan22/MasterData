## Ejercicio 1 Docker

### Crear un Dockerfile

Creamos un archivo llamado Dockerfile sin extensión que contiene:

```dockerfile
ARG CODE_VERSION=16.04

FROM ubuntu:${CODE_VERSION}

RUN apt-get update -y
```

Se puede guardar en el directorio que queramos. El comando se debe ejecutar en el mismo directorio. Lo vamos a guardar en C:\Users\sergi\Archivos\Master\Docker\Ejercicio1.

### Ejecutar el archivo

Vamos en el terminal a la carpeta donde está el archivo y ejecutamos:

○ `$ docker build -t first_edem_img .`

Esto crea una imagen con nombre first_edem_img. El punto final busca el archivo Dockerfile.

### Comprobar que se ha creado la imagen

Ahora ejecutamos en el terminal:

`docker images`

Este comando muestra la lista de imágenes que tenemos, siendo una de ellas la que hemos creado. Nos indica si ID, el tamaño y cuando se creó. Independientemente de donde se creen las imágenes, estas se guardan todas en un mismo sitio.

### Que hace cada uno de las líneas del fichero 

`ARG CODE_VERSION=16.04`

Crea una variable donde guardamos en número de versión de ubuntu que vamos a querer.

`FROM ubuntu:${CODE_VERSION}`

Descarga la imagen de ubuntu versión 16.04 del Docker Hub.

`RUN apt-get update -y`

Ejecuta el comando en la imagen descargada arriba. Lo que hace es actualizar el sistema. Esto añade una capa a la imagen de ubuntu, siendo la suma de ambos la imagen que hemos creado.