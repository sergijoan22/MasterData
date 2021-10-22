# Ejercicio 1 Repaso

### Debéis conseguir generar y arrancar una imagen que imprima por pantalla la hora cada minuto. Debéis crear la imagen partiendo de una imagen de python existente.

Docker nos da una imagen de python. Ahi queremos meter nuestro script, lo hacemos con COPY (de destino a contenedor)

```dockerfile
##Aquí elegimos la imagen con la que queremos crear nuestro contenedor
FROM python  


##Copiamos el archivo de nuestro PC a la imagen
COPY main.py main.py   


##Arrancamos el script ya copiado en el contenedor
CMD ["python","main.py"]   

```

Una vez tenemos el Dockerfile: Vamos en el terminal donde está la carpeta del Dockerfile

`cd C:\Users\sergi\OneDrive\GitHub\MasterDataEDEM\Fundamentos\Ejercicios_Repaso\Ejercicio1`

Una vez ahí creamos la imagen

`docker build -t imagen_ejercicio1_repaso_fundamentos .`

Creamos el contenedor a partir de la imagen

`docker run -itd --name contenedor_ejercicio1_repaso_fundamentos  imagen_ejercicio1_repaso_fundamentos`

Entramos dentro del contenedor

`docker exec -it contenedor_ejercicio1_repaso_fundamentos bash`

Ejecutamos el script copiado

`python main.py`

