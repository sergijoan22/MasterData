## Ejercicio 11 Docker

Añadir al docker-compose un nuevo servicio que levante un contenedor con la imagen del ejercicio 4. El servicio le llamamos por ejemplo cont_ima4 y le asignamos el puerto 8002 porqué está libre.

```
  cont_ima4:
    image: fourth_edem_img:latest
    ports:
      - "8002:80"
```

Al sobreescribir el archivo y volver a ejecutar:

`docker compose up -d`

El nuevo servicio se añade y los demás sigue igual.