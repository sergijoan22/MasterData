## Ejercicio 3

### Cambia tu país a Mexico

Sabiendo que somos el ID 153,

```sql
UPDATE datos_11_nov.ALUMNOS SET PAIS="Mexico" WHERE ID = 153
```

### Insertar fila con nuestra asistencia al master de MDA

Primero comprobamos que existe el master MDA

```sql
SELECT * FROM datos_11_nov.MASTERS WHERE Nom = 'MDA'
```

No existe el master, por lo que primero insertamos el master llamado MDA en la tabla de master. Para ello, primero vemos cual es el último ID.

```sql
SELECT COUNT(*) FROM datos_11_nov.MASTERS
```

Como el último ID es 100, creamos el próximo con ID 101.

```sql
INSERT INTO datos_11_nov.MASTERS (id, Nom) VALUES (101, 'MDA')
```

Por último, ver también el último ID de la tabla ALU_MASTERS

```sql
INSERT INTO datos_11_nov.ALU_MASTER (id, ALU_ID, MAS_ID) VALUES (289, 153, 101);

```
