# Ejercicios SQL

## Sergi Joan Sastre Antequera

La base de datos es dvdrental de postgreSQL. 

- URL: 35.192.88.224:5050/login?next=%2Fbrowser%2F
- Usuario: pgadmin4@pgadmin.org
- Password: admin y luego Welcome01

### 1. Nombre Actor, Apellido Actor

```sql
select first_name, last_name from actor
```

### 2. Nombre Actor, Titulo de la Película

```sql
select actor.first_name, film.title
from actor
inner join film_actor
on actor.actor_id = film_actor.actor_id
inner join film
on film_actor.film_id = film.film_id
```

### 3. Nombre Actor, Número de películas, Ordenar de mayor a menor

```sql
select actor.first_name, count(*) as movies_starring
from actor
inner join film_actor
on actor.actor_id = film_actor.actor_id
inner join film
on film_actor.film_id = film.film_id
group by actor.actor_id
order by movies_starring desc
```

### 4. Película, Número de veces alquilada

```sql
select film.title, count(*) as times_rented
from film
inner join inventory
on film.film_id = inventory.film_id
inner join rental
on inventory.inventory_id = rental.inventory_id
group by film.film_id
```

### 5. Película, Dinero recaudado por película

```sql
select film.title, sum(amount) as money_collected
from film
inner join inventory
on film.film_id = inventory.film_id
inner join rental
on inventory.inventory_id = rental.inventory_id
inner join payment
on rental.rental_id = payment.rental_id
group by film.film_id
```

### 6. Nombre del mejor cliente (mayor gasto)

```sql
select customer.first_name, sum(payment.amount) as money_spent
from customer
inner join payment
on customer.customer_id = payment.customer_id
group by customer.first_name
order by money_spent desc
limit 1
```

### 7. Nombre del mejor cliente (mayor num alquileres)

```sql
select customer.first_name, count(*) as times_rented 
from customer
inner join payment
on customer.customer_id = payment.customer_id
group by customer.first_name
order by times_rented desc
limit 1
```

