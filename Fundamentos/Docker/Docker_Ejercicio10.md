## Ejercicio 10 Docker

### Crear un Docker compose desde https://docs.docker.com/samples/wordpress/

```yaml
version: "3.9"
    
services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    
  wordpress:
    depends_on:
      - db // Nombre que usan los demás contenedores para refernciarlo
    image: wordpress:latest
    volumes:
      - wordpress_data:/var/www/html
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
volumes:
  db_data: {}
  wordpress_data: {}
```

Lo copiamos en un fichero llamado docker-compose.yml

Vamos en el terminal a la carpeta donde está el archivo, en la carpeta del ejercicio.

Ejecutamos el archivo con

`docker compose up -d`



Crea un contenedor db: A partir de una imagen, crea un volumen, Crea 4 variables de entorno

Crea un contenedor wordpress: Depende de el contenedor db (debe estar arrancada antes), a partir de una imagen, crea un volumen, redirecciona los puertos.