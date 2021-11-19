## Ejercicio 1

**Crear un proceso en NiFi que pase los archivos del directorio /tmp/in al directorio /tmp/out**

Estamos usando NiFi en docker, por lo que hay que crear los directorios dentro del contenedor.

En el terminal, hacemos un `docker ps` para ver el ID del container de NiFi: cbae042ada6b.

Entramos en el container con `docker exec -it cbae042ada6b /bin/bash`.

Creamos los dos directorios:

`cd /tmp`

`mkdir in`

`mkdir out`

En NiFi, se usan dos procesadores, GetFile que lee del primer directorio y PutFile que lo pone en el otro directorio.

En el menu de arriba, arrastramos un procesador a la pagina. Elegimos el llamado GetFile y tambien el PutFile.

Con la flecha que sale el Getfile, la arrastramos al PutFile y en menu de la conexión, todo por defecto. En GetFile solo hay una salida, llamada success, que es la que conectamos a PutFile.

En el GetFile, hay un warnin que dice que no tiene directorio. Boton derecho, configuracion, propiedades y ponemos en input directorty, /tmp/in

En el PutFile, hay tambien un warning que dice que no tiene directorio. Boton derecho, configuracion, propiedades y ponemos en input directorty, /tmp/out

Sale otro warming, porque tiene dos salidas que no se estan usando. COnfiguracionm Settings, en Automatically Terminate Relationships darle a los dos checkboxs

Dandole al fondo, boton derecho y le damos a Start. No hace nada porque no hay nada en el directorio de entrada.

Si ahora en el terminal, en el directorio de in creamos un archivo, ese archivo desaparecera automaticamente de ahi y ira directo a out.

Ahora salimos del terminal del contenedor con `exit` y hacemos un `docker compose stop` para parar el contendor pero no perder lo que hay.