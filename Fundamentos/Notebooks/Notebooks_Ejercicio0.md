## Ejercicio 0 Notebooks

Descargamos una imagen de Zeppelin y corremos una imagen de esta con el comando

`docker run -p 19999:8080 --rm --name zeppelin_single apache/zeppelin:0.8.1`

Ahora validamos que es contenedor está corriendo con el comando

`docker ps`

Con el primer comando hemos conectado el puerto 19999 de nuestro ordenador al puerto del contenedor. Por tanto, entrando a http://localhost:19999/ en el navegador podemos acceder a Zeppelin.

