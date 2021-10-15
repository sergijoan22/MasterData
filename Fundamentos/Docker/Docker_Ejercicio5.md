## Ejercicio 5 Docker

#### Eliminar imagen de ejercicio 3

`docker image rm third_edem_img`

No deja porque hay un contenedor usando esa imagen. 

`docker ps -a` 

Muestra los contenedores y a que imágenes están asociados. En este caso el contenedor del ejercicio 3 es el que se llama third_edem_img con ID e7a83a7779c2.

`docker rm e7a83a7779c2`

Con este comando borramos el contenedor. Como argumento se puede devolver indiferentemente el nombre en vez del ID.

`docker image rm third_edem_img`

Ahora ya podemos borrar la imagen al no tener ningún contenedor asociado.

`docker images`

Con este comando vemos que el comando borrado ya no está en la lista.

`docker rm cont_second_edem`

`docker rm jovial_dirac`

Borramos todos los contenedores menos fourth_edem_img

`docker image rm second_edem_img`

`docker image rm first_edem_img`

`docker image rm docker/getting-started`

Así borramos las demás imagenes.