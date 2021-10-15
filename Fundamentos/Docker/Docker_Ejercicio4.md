## Ejercicio 4 Docker

Crea un archivo llamado index.html con

````html
<p>Tu primer párrafo.</p> 
<p>Tu segundo párrafo.</p> 
<p>Un enunciado.
<br> EDEM.</p> 
````

Al crear las imagenes: Importante situarse en la carpeta donde esta el Dockerfile

Crear un Dockerfile que también copie index.html en /var/www/html al hacer el docker exec.

```dockerfile
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY index.html /var/www/html/
	
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

En el terminal:

Redireccionar de un puerto distinto del 8080, porqué ya está en uso. Si queremos usar ese puerto, debemos borrar el contenedor que lo está usando.

#### `docker build -t fourth_edem_img .`

Esto crea la imagen a partir del Dockerfile, llamada fourth_edem_img.

`docker images`

Lista las imágenes que hay creadas, debe aparecer la nueva.

`docker run -itd --name cont_fourth_edem -p 8081:80 fourth_edem_img`

Crea un contenedor a partir de la imagen y redireccionar al puerto 80 del contenedor con el 8081 nuestro. Importante que de nuestros puertos no usemos el mismo en dos cosas.

`docker ps -a`

Lista los contenedores.

Al acceder en el navegador a  http://localhost:8081 nos debería la página web de index.html