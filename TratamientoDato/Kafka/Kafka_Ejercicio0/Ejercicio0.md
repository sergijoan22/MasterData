# Ejercicio 0

En un terminal, arrancamos el docker con Kafka

```sh
docker-compose up -d
```

Ver que están activos

```sh
docker-compose ps
```

Creamos un topic llamado `myTopic`, que es una especie de tabla para guardar mensajes, una partición y una réplica.

```sh
docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server host.docker.internal:9092
```

Ver la información del topic.

```sh
docker-compose exec kafka kafka-topics --describe --topic myTopic --bootstrap-server host.docker.internal:9092
```

Salen datos como el número de particiones o el factor de replicación.

Ahora apagamos el docker compose.

```sh
docker-compose down
```
