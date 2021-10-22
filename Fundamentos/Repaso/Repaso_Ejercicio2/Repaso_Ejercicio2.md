# Ejercicio 2 Repaso

### Basándose en lo conseguido en el ejercicio 1 debéis arrancar el docker siguiente como una api en el puerto 5000. Una vez levantado, deberíais ver el mensaje de Bienvenida en la url http://localhost:5000

Una vez tenemos el Dockerfile vamos en el terminal donde está la carpeta del Dockerfile

`cd C:\Users\sergi\OneDrive\GitHub\MasterDataEDEM\Fundamentos\Ejercicios_Repaso\Ejercicio2`

Una vez ahí creamos la imagen

`docker build -t imagen_ejercicio2_repaso_fundamentos .`

Creamos el contenedor a partir de la imagen

`docker run -p 5000:5000 contenedor_ejercicio2_repaso_fundamentos  imagen_ejercicio2_repaso_fundamentos`

