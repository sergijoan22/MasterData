# Ejercicio 1

Hacemos el docker compose en docker.

```docker
docker-compose up -d
```

En IntelliJ cargamos la carpeta con los archivos del ejercicio 1 usando Maven. 

En src > main > java > com.gft.dkp.kafka tenemos el archivo de Consumidor y Receptor para enviar y recibir un mensaje. 

En el icono de Maven en la derecha vamos a Lifecycle y le damos a compile para los archivos Producer y Consumer. Luego, en Producer botón derecho y run y hacemos y recibimos el mensaje.

En el archivo Consumer, la siguiente linea se encarga de mostrar lo recibido, y puede ser cambiado el mensaje que se adjunta.

```java
System.out.println(String.format("XXXXXXXXXXXXXXXXX - %s, Partition - %d, Value: %s", record.topic(), record.partition(), record.value()));
```

Por último, quitar los contenedores de docker creados.

```sh
$ docker-compose down
```
