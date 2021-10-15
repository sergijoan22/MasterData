## Ejercicio 7 Docker

#### Al contenedor del ejercicio 4, añadir una línea de código, con nuestro nombre, al archivo html.

Arrancamos el contenedor del ejercicio 4, llamado cont_fourth_edem, ya que está parado.

`docker start cont_fourth_edem`

Entramos en el contenedor

`docker exec -it cont_fourth_edem bash`

Ahora estamos dentro del contenedor, y vamos a la ruta

`cd /var/www/html`

`echo "<p>Sergi Sastre</p>" >> ./index.html`

`cat index.html`

`exit`

#### Una vez modificado el contenedor con la nueva línea, crear una imagen a partir del contenedor modificado.

Convierte cont en imagen llamada cont_fourth_edem_img_newline

`docker commit cont_fourth_edem cont_fourth_edem_img_newline:latest`

### Subir la imagen a DockerHub

Vemos el id de la imagen, d5c2d0295402, con:

`docker images`

Subir la imagen a DockerHub. Antes de subir la imagen hay que crear un repositorio en DockerHub: En repositorios -> Create repository. Lo llamamos por ejemplo myfirstimage

Nos logeamos en la cuenta de Docker Hub

`docker login --username=sergijoan22`

Ponemos la contraseña de la cuenta

Definimos la imagen como la última versión en el repositorio creado.

`docker tag d5c2d0295402 sergijoan22/myfirstimage:latest`

Subimos al repositorio de DockerHub la imagen. Por defecto el push sube la última versión, que es lo que hemos definido en el anterior comando.

`docker push sergijoan22/myfirstimage`