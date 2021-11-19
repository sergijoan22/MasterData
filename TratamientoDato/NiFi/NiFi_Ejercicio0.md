# Ejercicio 0

Descrgamos la carpeta del repositorio echiner/edem-mda-data-ingestion en github.

Hay que hacer un cambio el el docker compose, añadir el puerto 8443 a la imagen de nifi.

Nos metemos en la carpeta, donde hay un docker compose, y hacemos en la terminal `docker-compose up -d` para cargar el archivo.

Podemos entrar con https://localhost:8443/nifi/login. El usuario y contraseña están en el log del contenedor, que aparece al darle click en Docker desktop:

```
Generated Username [0af99bf9-bc32-4927-a895-8dc720c8072c]
Generated Password [VHtV3YYlFXn9ohH9PMY6dsJ/7lSTNeaA]
```
