## Ejercicio 8 Docker

Creamos un contenedor llamado my-vol

`docker volume create my-vol`

Listamos los volumenes que tenemos

`docker volume ls`

Vemos las características del volumen

`docker volume inspect my-vol`

Arranca el volumen

`docker run -d --name volume_test --mount source=my-vol,target=/app sergijoan22/myfirstimage`

Entramos en el volumen

`docker exec -it volume_test bash`