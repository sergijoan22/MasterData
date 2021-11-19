## Ejercicio 1

Devuelve los alumnos de Portugal

```sql
SELECT * FROM datos_11_nov.ALUMNOS WHERE PAIS = 'Portugal'
```

Devuelve los masters que tengan en el nombre una d minuscula.

```sql
SELECT * FROM datos_11_nov.MASTERS WHERE Nom LIKE '%d%'
```

Devuelva los alumnos con ID que esté entre 37 y 45

```sql
SELECT * FROM datos_11_nov.ALUMNOS WHERE ID BETWEEN 37 AND 45 ORDER BY ID
```

