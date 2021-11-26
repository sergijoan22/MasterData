# Ejercicio 1

Ya en la consola CQL, se pueden usar comandos en cassandra.

Ver ayuda:

```cassandra
cqlsh> help;
```

Ver keyspaces existentes:

```cassandra
cqlsh> describe keyspaces;
```

Ver tablas existentes:

```cassandra
cqlsh> describe tables;
```

Query básica (De la tabla system.local):

```cassandra
cqlsh> SELECT cluster_name, listen_address, release_version FROM system.local;
```

Crear un keyspace (Replication factor es la veces de copias que hace de sus datos):

```cassandra
cqlsh> CREATE KEYSPACE edem WITH  replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
```

Crear una tabla:

```cassandra
cqlsh> CREATE TABLE edem.students (
    studentid uuid,
    name text,
    age int,
    PRIMARY KEY (studentid)
);
```

Hacer una query a la tabla:

```cassandra
cqlsh> select * from edem.students;
```

Insertar datos en la tabla (USING TTL define los segundos que va a durar el dato antes de borrarse):

```cassandra
cqlsh> insert into edem.students (studentid, name, age) values (now(), 'John Doe', 25);
cqlsh> insert into edem.students (studentid, name, age) values (now(), 'Alice', 22);
cqlsh> insert into edem.students (studentid, name, age) values (now(), 'Bob', 22) USING TTL 30;
```

Volver a ver la tabla para ver los datos puestos:

```cassandra
cqlsh> select * from edem.students;
```

### Extra

Take a look at the documentation (http://cassandra.apache.org/doc/3.11/cql/index.html) and understand what we are doing.
We are specially interested in the following:

* **Data Types**: http://cassandra.apache.org/doc/3.11/cql/types.html#native-types
* **Keyspace creation**: http://cassandra.apache.org/doc/3.11/cql/ddl.html#create-keyspace
* **Table creation**: http://cassandra.apache.org/doc/3.11/cql/ddl.html#create-table
* **Insert data**: http://cassandra.apache.org/doc/3.11/cql/dml.html#insert