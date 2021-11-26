## Ejercicio 2

Se va a simular un sensor IOT con NiFi, guardar los datos en Cassandra y ver los datos con Zeppelin:

* Apache NiFi: https://localhost:8443/nifi
	* **Username**: admin
	* **Password**: ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB
* Apache Zeppelin: http://localhost:9999

En NiFi se ha simulado el sensor para cree periódicamente datos.

En Cassandra creamos un nuevo keyspace:

```cassandra
CREATE KEYSPACE exercise3 WITH  replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
```

En este, creamos una tabla para guardar los datos desde NiFi:

```cassandra
CREATE TABLE exercise3.sensor_data (
    machine_id int,
    sensor_id int,
    event_time timeuuid,
    observation_type text,
    observation_value float,
    PRIMARY KEY ((machine_id, sensor_id), event_time)
);
```