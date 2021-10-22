# Notebooks

El notebook se divide en celdas, donde en cada una va código. Lo que hace correr la notebook se llama kernel. Las variables se comparten en todas las celdas. Las celdas se pueden ejecutar en cualquier orden, obteniendo diferentes resultados, aunque es recomendable hacerlo en orden. Hay notebooks multilenguaje donde cada celda puede ser de un lenguaje.

Se recomienda:

- Un notebook para cada foco
- Tener en cuenta que se pueda usar en otros notebooks. Especificar al principio todas las librerías que se deben descargar
- No es un IDE, gran parte del notebook debe ser texto
- Limpiar el código y no meter en una única celda grandes bloques de código
- Etiquetar los diagramas

## Google Colab

Para ejecutar: Mayus + Intro

Se pueden hacer celdas de texto o colaborativas

Entorno de ejecución -> Reiniciar entorno de ejecución: Por si hay problema de memoria, se reinicia

Entorno de ejecución -> Ejecutat todas: Ejecuta en orden

Debajo hay kernel de linux, por lo que poniendo una exclamación primero, podemos usar comandos de linux

En la izquierda, el símbolo de carpetas muestra el directorio de archivos del proyecto

En la izquierda, el símbolo <> ofrece trozos de código

La primera celda deberían ser los import.

Crear uno: Archivo -> Nuevo Cuaderno

Podemos cambiar el tipo de entrono de ejecución para que sea con GPU.

## Jupyter

Frente a Google Colab, tiene también versión local.

## Apache zeppelin

Es solo local. Es multilenguaje.

Creamos una nueva nota, y decimos que queremos el interprete de python.

En el menú podemos: Ejecutar todo, ocultar código, esconder la salida, borrar las salidas (las variables no se reinician).

Permite organizar las celdas en horizontal.

Para escribir en una celda python por ejemplo: Poner %python en la primera línea.

Para escribir texto, ponemos %md para escribir en markdown

Al estar usando Zeppelin en el contenedor, hay que guardar antes lo usado en el ordenador, si no se borrará.

Usa una extensión propia, frente a Jupyter que usa una general.



## Prueba 1

Crear un contenedor de docker con jupyter

Usamos elpuerto 8888 para poder ver el contenido

Descargamos la imagen de Jupyter de internet

`docker pull jupyter/minimal-notebook:latest`

Creamos el contenedor a partir de la imagen, conectando nuestro puerto 8888 al 8888 de dentro. El puerto nuestro es el que queramos, pero el de la imagen ya está definido.

`docker run -p 8888:8888 jupyter/minimal-notebook`

## Ejercicio 0

Creamos un contenedor de Zeppelin

`docker run -p 19999:8080 --rm --name zeppelin_single apache/zeppelin:0.8.1`

Comprobamos que esté el contenedor

`docker ps`

Abrimos http://localhost:19999/ y accedemos a Zeppelin

Creamos una nueva nota, y decimos que queremos el interprete de python.

## Ejercicio 1

Creamos el archivo pedido

## Ejercicio 2

Entramos en el contenedor con

`docker exec -it zeppelin_single /bin/bash`

Creamos la carpeta data 

`mkdir data`

Salimos del contenedor

`exit`

Copiamos el archivo amazon.csv en la carpeta del contenedor creada. Podemos poner la ruta absoluta o ir al directorio donde tenemos el archivo.

`docker cp amazon.csv zeppelin_single:/zeppelin/data`

En Zeppelin, creamos una notebook llamada Parameters y en la primera celda ponemos

```SPARQL
%spark 

spark
.read
.option("header", "true")
.option("delimiter", ",")
.option("inferSchema", "true")
.csv("data/amazon.csv")
.registerTempTable("amazon")
```

Con esto cargamos los datos de ejemplo. Ahora hacemos una query para sacar productos con "hobby"

```sql
%spark.sql
select * from amazon where product_name like  '%hobby%'
```

Para comprobar que está bien, en otra celda

```sql
%spark
println(z.angular("numberReviews"))
```

## Ejercicio 3

Nos metemos en el contenedor

`docker exec -it zeppelin_single /bin/bash`

Ejecutamos los siguientes comandos

`apt-get update`

`apt-get upgrade`

`apt install python3-pip`

`apt install python3-pip`

`pip3 install --upgrade pip`

`pip3 install seaborn`

`pip3 install pandas`







[Usar argumento -d al hacer docker run para que al cerrar la ventana no se quite]