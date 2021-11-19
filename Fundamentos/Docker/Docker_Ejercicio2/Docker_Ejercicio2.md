## Ejercicio 2 Docker

### Crear un Dockerfile

Creamos un archivo llamado Dockerfile sin extensión que contiene:

```dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /home/edem

ENV USER masfworld
ENV SHELL /bin/bash
ENV LONGNAME masfworld

CMD ["bash"]
```

Importante guardarlo en otro directorio que el anterior Dockerfile. El comando se debe ejecutar en el mismo directorio. Lo vamos a guardar en C:\Users\sergi\Archivos\Master\Docker\Ejercicio2.

### Ejecutar en terminal

#### `docker build -t second_edem_img .`

Esto crea la imagen a partir del Dockerfile, llamada second_edem_img.

`docker images`

Lista las imágenes que hay creadas, debe aparecer la nueva.

`docker run -itd --name cont_second_edem second_edem_img`

Crea un contenedor a partir de la imagen

`docker ps -a`

Lista los contenedores.

![image-20210924194948769](../Assets/image-20210924194948769.png)

`docker exec -it cont_second_edem bash`

Ejecuta en el contenedor la instrucción bash. Nos metemos dentro de la MV.

![image-20210924195024717](../Assets/image-20210924195024717.png)

Ahora, al poner

`echo $SUPER`

Devuelve masfworld

Para salir del contenedor ponemos:

`exit`

### Que hace cada uno de las líneas del fichero

`FROM ubuntu:16.04`

Crea una variable donde guardamos en número de versión de ubuntu que vamos a querer.

`RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists`

Instala curl (utilidad para peticiones web), borra los ficheros temporales, y borra un directorio.

`RUN mkdir /home/edem`

Ejecuta un comando que crea un directorio

`ENV USER masfworld`

Definiendo una variable de entorno llamada USER que tiene de valor masfworld

`ENV SHELL /bin/bash`

Definiendo una variable de entorno llamada SHELL que tiene de valor /bin/bash

`ENV LONGNAME masfworld`

Definiendo una variable de entorno llamada LONGNAME que tiene de valor masfworld

`CMD ["bash"]`

Deja el bash dentro del contenedor.