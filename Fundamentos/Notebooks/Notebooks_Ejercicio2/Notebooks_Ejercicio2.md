## Ejercicio 2 Notebooks

Para este ejercicio se va a usar un archivo llamado amazon.csv[amazon.csv](amazon.csv). Para ello, hay que copiarlo dentro del contenedor para poder usarlo con Zeppelin. Primero entramos en el contenedor.

`docker exec -it zeppelin_single /bin/bash`

Una vez dentro, creamos una carpeta llamada data donde copiaremos el archivo.

`mkdir data`

Una vez creada la carpeta, salimos del contenedor.

`exit`

Una vez de vuelta al PC, vamos al directorio donde está el archivo y lo copiamos al contenedor.

`docker cp amazon.csv zeppelin_single:/zeppelin/data`

Ahora creamos un nuevo notebook llamado [Parameters](Parameters.json). En este archivo se van a realizar diferentes operaciones sobre el archivo adjunto.