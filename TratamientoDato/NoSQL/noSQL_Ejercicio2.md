## Ejercicio 2

Se va a usar Zeppelin en vez de la consola CQL. Lo abrimos con la URL http://localhost:9999. Se le indica que debe apuntar a Cassandra:

1. Abrir la configuracióm de "Interpreter" (Arriba a la derecha, dentro de "anonymous")
2. Buscar "cassandra"
3. En "Edit", cambiar "cassandra.hosts" a "cassandra" (antes "localhost"), darle a "Save", y darle a "Restart"
4. Crear una nota ("Notebook" menu arriba --> "+ Create new note"). Elegir "cassandra" como intérprete por defecto.

Ahora se pueden usar los comandos de cassandra como en el ejercicio 1. Pedir ayuda:

```cassandra
help;
```

Se van a crear dos tablas para el uso en un sistema de mensajería:

- Guardar todos los mensajes.
- El usuario puede crear grupos.
- Patrones de acceso:
	* Enviar un mensaje en una conversación o grupo.
	* Recuperar todos los mensajes de una conversación.
	* Recuperar todos los mensajes de un grupo.
	* Recuperar todos los grupos y conversaciones.
	* Eliminar un mensaje.

Se crear un keyspace para el ejercicio.

```cassandra
CREATE KEYSPACE messagingsystem WITH  replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};
```

Vemos que se ha creado.

```cassandra
describe keyspaces;
```

Ahora creamos una tabla para guardar los mensajes.

```cassandra
CREATE TABLE messagingsystem.messages (
    messageid uuid,
    content text,
    groupid int,
    senderid text,
    receiverid text,
    fecha timestamp,
    PRIMARY KEY (userid, fecha)
);
```

Y también creamos una tabla para los grupos.

```cassandra
CREATE TABLE messagingsystem.groups (
    groupid uuid,
    members <text>,
    fechaCreacion timestamp,
    PRIMARY KEY (groupid, fechaCreacion)
);
```