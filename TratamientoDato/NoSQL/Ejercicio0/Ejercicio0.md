## Ejercicio 0

Preparación del entorno Cassandra. Cargamos los componentes necesarios a partir del archivo Docker compose.

```shell
docker-compose up -d
```

 Falta el CQL Shell, que se lanza interactivamente.

```shell
# Start the CQL container, which points to the Cassandra database
docker-compose run cqlsh
```

Dentro de cqlsh, veemos la configuracion.

```bash
# In the CQL prompt, check the config
cqlsh> SELECT cluster_name, listen_address, release_version FROM system.local;
```

Nos muestra:

```
 cluster_name | listen_address | release_version
--------------+----------------+-----------------
 Test Cluster |     172.19.0.6 |           4.0.1

```

Se lanzan los siguientes componentes:

* **Apache Cassandra**: NOSQL columnar database
* **CQL Shell**: Command line interface for CQL (Cassandra Query Language)
* **Apache NiFi**: Web-based data ingestion tool
* **Apache Zeppelin**:  Web-based notebooks

Cada uno tiene sus detalles:

| Component            | Ports | URL                         | Credentials                              |
| -------------------- | ----- | --------------------------- | ---------------------------------------- |
| **Apache Cassandra** | 9042  | N/A                         | N/A                                      |
| **CQL Shell**        | N/A   | N/A                         | N/A                                      |
| **Apache NiFi**      | 8443  | https://localhost:8443/nifi | admin / ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB |
| **Apache Zeppelin**  | 9999  | http://localhost:9999/      | N/A                                      |
