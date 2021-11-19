## Ejercicio 3 Docker

### Crear un Dockerfile

Creamos un archivo llamado Dockerfile sin extensión que contiene:

```dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 80

CMD ["ngnix", "-g", "daemon off;"]
```

Importante guardarlo en otro directorio que el anterior Dockerfile. El comando se debe ejecutar en el mismo directorio. Lo vamos a guardar en C:\Users\sergi\Archivos\Master\Docker\Ejercicio3.

### Ejecutar en terminal

#### `docker build -t third_edem_img .`

Esto crea la imagen a partir del Dockerfile, llamada second_edem_img.

`docker images`

Lista las imágenes que hay creadas, debe aparecer la nueva.

`docker run -itd --name cont_third_edem -p 8080:80
third_edem_img`

Crea un contenedor a partir de la imagen y redireccionar al puerto 80 del contenedor con el 8080 nuestro. Importante que de nuestros puertos no usemos el mismo en dos cosas.

`docker ps -a`

Lista los contenedores.

Al acceder en el navegador a  http://localhost:8080 nos debería abrir una página.

QUE HACE

`FROM ubuntu:16.04`

`RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*`

Hemos descargado el puerto 80

`EXPOSE 80`

Abre el puerto 80

`CMD ["ngnix", "-g", "daemon off;"]`

ngnix es un servidor web

