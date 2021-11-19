# 11 nov

## Operaciones de SQL

### DDL

Crear y modificar estructura base de datos: Crear tablas, añadir columnas

Drop, elimina tabla

Truncate, elimina datos de tabla, conserva estructura

### DML

Modificar datos de las tablas

SELECT, recuperar datos

INSERT, añadir registros

UPDATE, modificar registros

DELTE, eliminar registros

MERGE, hacer select y a a partir de los datos hacer otra select

### DCL

Dar y quitar permisos sobre los datos.

### TCL

Administrar transcacciones. Los cambios hechos con querys no son definitivos hasta confirmarlo.

COMMIT, para confirmar que las querys se guarden definitivamente

ROLLBACK, para hacer que las querys no se guarden



## SELECT

De la tabla ALUMNOS:

\* para referirse a todos los alumnos

```sql
SELECT * FROM ALUMNOS
```

En bigquery hay de especificar en que conjunto esta la tabla, en nuestro caso se llama datos_11_nov.

```sql
SELECT * FROM datos_11_nov.ALUMNOS
```

Ahora se ordena

```sql
SELECT * FROM ALUMNOS ORDER BY ID
```

Sacar solo algunas columnas de las tablas

```sql
SELECT nom, email FROM ALUMNOS ORDER BY ID
```

Where para definir que registros devolver

```sql
SELECT nom, email FROM ALUMNOS WHERE PAIS='Indonesia' ORDER BY ID
```

```sql
SELECT nom, email FROM ALUMNOS WHERE PAIS='Indonesia' or PAIS='Portugal' ORDER BY ID
```

También se puede crear una lista de paises, por ejemplo y poner IN o NOT IN.

Para devolver si el país empieza por P. Para ello, el metacarácter `%`. Si ponemos `%`, que contenga una P, que puede estar al principio o al final.

```sql
SELECT nom, email FROM ALUMNOS WHERE PAIS like 'P%' ORDER BY ID
```

Ahora pero cambiando el orden de sentido

```sql
SELECT nom, email FROM ALUMNOS WHERE PAIS='Indonesia' ORDER BY ID DESC
```

Para saber el total de registos de una consulta

```sql
SELECT COUNT(*) FROM ALUMNOS WHERE PAIS='Indonesia' 
```

## INSERT

```SQL
INSERT INTO ALUMNOS VALUES (<>,<>,<>)
```

Insertar solo algunos valores del registro, y lo demás vacío

```sql
INSERT INTO ALUMNOS VALUES (<>,<>,<>)
```

## UPDATE

Modificar un registro existente. Si no ponemos WHERE, cambia todos los registros

```sql
UPDATE datos_11_nov.ALUMNOS SET <cambio> WHERE <condicion_de_los_registros>
```

```sql
UPDATE datos_11_nov.ALUMNOS SET NOM = 'Sergi' WHERE ID = 1
```

```sql
UPDATE EDEM.ALUMNOS SET NOM="ESTEBAN" WHERE NOM="PEDRO"
```

Cambiar Los Pedro por Esteban

En WHERE podemos poner una consulta. En este caso, cambiar el nombre 

```sql
UPDATE EDEM.ALUMNOS SET NOM="ESTEBAN" WHERE ID IN (SELECT ID FROM
EDEM.ALUMNOS WHERE NOM="PEDRO")
```

## SELECT EN VARIAS TABLAS

Podemos ponerle un alias a las tablas para usarlo en la consulta.

```sql
SELECT * FROM datos_11_nov.ALUMNOS AL, datos_11_nov.ALU_MASTER AM, datos_11_nov.MASTERS M WHERE AL.ID = AM.ALU_ID AND AM.MAS_ID = M.ID
```

## JOIN

[Visual JOIN (spathon.com)](https://joins.spathon.com/)

[SQL Joins Visualizer (leopard.in.ua)](https://sql-joins.leopard.in.ua/)

### 



