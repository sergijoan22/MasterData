# Ejercicio 3 Repaso

### Siguiendo con lo anterior, debéis implementar los métodos GET, POST, DELETE mostrando un mensaje para cada uno. Construir la imagen y poner el servicio en el puerto 5000

Con un puerto, podemos hacer en el un GET (pide información y se devuelve. Por ejemplo entrar en una web). Para enviar algo es un POST y para borrar algo un DELETE.

Una vez tenemos el Dockerfile: Vamos en el terminal donde está la carpeta del Dockerfile

`cd C:\Users\sergi\OneDrive\GitHub\MasterDataEDEM\Fundamentos\Ejercicios_Repaso\Ejercicio3`

Una vez ahí creamos la imagen

`docker build -t imagen_ej3_repfun .`

Creamos el contenedor a partir de la imagen

`docker run -itd --name cont_ej3_repfun -p 5000:5000 imagen_ej3_repfun`

Si entramos en el navegador con http://localhost:5000/users/1 (1 es el usuario, que puede ser 1, 2, 3..) vemos el mensaje que devuelve el GET, que hemos especificado en el script.

