# No SQL

Guarda los datos en ficheros, que se deben procesar enteros, no parte de ellos, para acceder a ellos. También permite guardar en formato key-value, con un conjunto de keys únicas que apuntan cada uno a unos datos. Aparte, document store, que guarda documentos semiestructurados como JSON o XML. Además, otro tipo es el graph database, que es un conjunto de nodos con enlaces de varios tipos entre ellos.

En cassandra:

- Tenemos keyspaces, con tablas de datos que se trabajan conjuntamente. 
- En las tablas, se pueden hacer column family para agrupar varias tablas.
- Guarda para cada registro el nombre de la columna, el valor y también un timestamp.
- Cada registro tiene una clave primaria para identificarla.
- La clave primaria se divide en una clave de particionamiento (A que nodo va a ir cada uno de los registros de los  datos) y un claster (A partir de que ordena los datos)