## Ejercicio 6 Docker

#### Descargar imagen de https://hub.docker.com/_/wordpress

`docker pull wordpress`

Descargamos la imagen.

#### Crear un contenedor a partir de esa imagen, accediendo con el puerto 8080

`docker run -itd --name sixth_edem_img -p 8080:80 wordpress`

Creamos el contenedor, llamado sixth_edem_img, en el puerto 8080 y a partir de la imagen wordpress.

`docker ps -a`

Vemos que se ha creado el contenedor. Entrando en  http://localhost:8080 podemos acceder a la página web que hay en el contenedor.