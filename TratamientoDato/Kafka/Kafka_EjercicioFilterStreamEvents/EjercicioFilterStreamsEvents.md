# Ejercicio Filter Streams Events

En el directorio a usar se crean las carpetas src y test. Luego se arranca un docker compose con varios contenedores.

```bash
docker-compose up -d
```

Ahora abrimos el ksqlDB CLI.

```bash
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```

Se crea un topic de Kafka llamado publication_events y un stream llamado all_publications.

```bash
CREATE STREAM all_publications (bookid BIGINT KEY, author VARCHAR, title VARCHAR)
    WITH (kafka_topic = 'publication_events', partitions = 1, value_format = 'avro');
```

Ahora se producen varios eventos en el stream.

```bash
INSERT INTO all_publications (bookid, author, title) VALUES (1, 'C.S. Lewis', 'The Silver Chair');
INSERT INTO all_publications (bookid, author, title) VALUES (2, 'George R. R. Martin', 'A Song of Ice and Fire');
INSERT INTO all_publications (bookid, author, title) VALUES (3, 'C.S. Lewis', 'Perelandra');
INSERT INTO all_publications (bookid, author, title) VALUES (4, 'George R. R. Martin', 'Fire & Blood');
INSERT INTO all_publications (bookid, author, title) VALUES (5, 'J. R. R. Tolkien', 'The Hobbit');
INSERT INTO all_publications (bookid, author, title) VALUES (6, 'J. R. R. Tolkien', 'The Lord of the Rings');
INSERT INTO all_publications (bookid, author, title) VALUES (7, 'George R. R. Martin', 'A Dream of Spring');
INSERT INTO all_publications (bookid, author, title) VALUES (8, 'J. R. R. Tolkien', 'The Fellowship of the Ring');
INSERT INTO all_publications (bookid, author, title) VALUES (9, 'George R. R. Martin', 'The Ice Dragon');
```

Ahora vamos a leer los eventos en el stream, asegurandose leer desde el principio.

```bash
SET 'auto.offset.reset' = 'earliest';
```

De los mensajes, se va a buscar solo los libros escritos por George R. R. Martin.

```bash
SELECT * FROM all_publications WHERE author = 'George R. R. Martin' EMIT CHANGES LIMIT 4;
```

Obtenemos de salida todos los mensajes que incluian libros del autor, de entre todos los mensajes con libros de varios autores.

Ahora se va a hacer que la query hecha antes se haga continuamente.

```bash
CREATE STREAM george_martin WITH (kafka_topic = 'george_martin_books') AS
    SELECT *
      FROM all_publications
      WHERE author = 'George R. R. Martin';
```

Podemos obtener en cualquier momento el resultado de la query, que nos devuelve los libros de George R. R. Martin otra vez.

```bash
PRINT george_martin_books FROM BEGINNING LIMIT 4;
```

Una vez creados los statements que funcionan correctamente, se ponen en un archivo para poder usarlos fuera de la sesion de CLI. En la carpeta src se crea un archivo llamado `statements.sql` con los statements para consultar:

```bash
CREATE STREAM all_publications (bookid BIGINT KEY, author VARCHAR, title VARCHAR)
    WITH (kafka_topic = 'publication_events', partitions = 1, value_format = 'avro');

CREATE STREAM george_martin WITH (kafka_topic = 'george_martin_books') AS
    SELECT *
      FROM all_publications
      WHERE author = 'George R. R. Martin';
```

Y en la carpeta test, se crea un archivo `input.json` con las entradas de los mensajes para hacer la prueba. Se crea en el mismo sitio otro archivo llamado `output.json` con las salidas que podríamos esperar al hacer las consultas de antes.

Por último, se hacen los test en el terminal con los archivos creados.

```bash
docker exec ksqldb-cli ksql-test-runner -i /opt/app/test/input.json -s /opt/app/src/statements.sql -o /opt/app/test/output.json
```

Si es todo correcto, si el archivo `output.json` tiene el contenido esperado luego de hacer la consulta en `statements.sql` sobre el archivo `input.json`, obtenemos un mensaje de éxito al hacer la prueba.

```bash
docker exec ksqldb-cli ksql-test-runner -i /opt/app/test/input.json -s /opt/app/src/statements.sql -o /opt/app/test/output.json
```