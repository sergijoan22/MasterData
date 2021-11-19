# ETL 13 nov

ELT es ingestión pura

ETL se usa para guardar los datos ordenados

Talend es una herramienta para ETL

NiFi es ELT

ETL sobretodo para procesos que se repiten

## Talend

Arriba a derecha ponemos las cajas

En job designs, click derecho, new folder, y en ella un new job.

Ahora en la derecha aparecen todas las cajas.

Abajo tenemos la configuración de cada caja

### Leer y guardar un csv

Para leer csv: `tFileInputDelimited`.

Para guardar el csv, ponemos un `tFileOutputDelimited`.

Coenctamos los dos con una flecha arrastrando de la entrada a la salida.

En la entrada elegimos la ruta donde está ALUMNOS.csv, cual es el separador (coma), si hay cabcera (1 ya que hay una línea)

Le damos a edit schema y ahí añadimos los nombres de las columnas y el tipo de datos. Le damos propagar cambios así que en el output se heredará la configuración. Si no se ha hecho, en el output le damos a `Sync columns`.

En la salida donde se guarda y el nombre

Luego, bajo a la derecha, en la pestaña Run le damos a Run. Si pone que el archivo ya existe, para poder sobreescribir, en advancvced settings de la output, desclikamos la opción de generar un error si el archivo ya existe.

El csv de salida no tiene salida y el separador ahora es el punto y coma, esto se puede cambiar.

## Crear plantilla de un csv

En la izquierda, metadata, file delimited, create: De nombre ALUMNOS, cargamos el ALUMNOS.csv, ponemos el separador y la línea de encabezado. Al darle a refresh preview sale el csv en forma de tabla. Ahora específicamos la estructura de las columnas otravez, poniendo también la longitudd máxima para las celdas de cada columna. Esta vez es para crear una plantilla del esquema y pode usarlo cada vez.

Ahora este archivo que se crea lo arrastramos y nos pone que acciones podemos hacer, elegimos otra vez `tFileInputDelimited`.

Ponemos también un `tFileOutputDelimited`. Los conectamos y especificamos donde cargar y guardar el csv. Nos aseguramos que el output tenga el esquema del input.



### Modificar una tabla

Se va a cambiar los campos de Portugal a Andorra del campo pais de la tabla ALUMNOS. Creamos la entrada con la plantilla ALUMNOS y la salida. Ponemos también un `tReplace` desde Processing.

En tReplace, en Search/Replace añadimos una condición y le ponemos que en PAIS cambie 'Portugal 'por 'Andorra' en doble comillas. Checkamos el Entirely para que el contenido de la celda sea 'Portugal' exactamente, si no, añadiria en el cambio carácteres que también haya junto a 'Portugal' si se da el caso. Ahora le damos a `Sync columns`

### Crear una plantilla de json

Cremos la plantilla de json igual desde donde esta la de csv, le ponemos nombre y le ponemos Input Json. Read by XPath y elegimos el json del que sacar la plantilla. Luego arrastramos todos los campos a Field to extract y data a Path loop expression. Luego podemos configurar el esquema de la tabla.

### Filtrar registros de una tabla

Se va a devolver solo las filas cuyos alumnos sean de Portugal. Junto a `tFileOutputDelimited` y `tFileOutputDelimited` conectamos un `tFilterRow` desde Processing donde ponemos: PAIS, Igual, ==, "Portugal"

### Hacer un join de varias tablas

El join se hace con `tMap` donde se conectan las tablas. Se unen los campos en común de las tablas para hacer los join. Se elige que campos sacar de las entradas.

### Leer una base de datos de postgreSQL

Se va a leer la base de datos dvdrental. En metadata -> db connection -> new. Elegimos el nombre y luego ponemos los siguientes campos:

DB Type ----> PostgreSQL
DB Version ----> v9 and later
Login ----> postgres
Password ----> Welcome01
Server ----> 35.192.88.224
Port --> 5432
Database ----> dvdrental
Schema ----> public

Sobre la base de datos creada, botón derecho en la base de datos, extraer esquema, y next hasta ponerle nombre. Entonces se crearán los esquemas de las tablas de la bbd que al arrastrarla podemos usarla como entrada.