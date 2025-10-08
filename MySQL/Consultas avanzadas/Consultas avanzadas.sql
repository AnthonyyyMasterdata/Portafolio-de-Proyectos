-- Selecciona a los clientes que hayan pagado una cantidad mayor a 11$ 

SELECT p.payment_id, c.first_name AS "client", c.last_name AS "last name", amount, payment_date
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
WHERE amount > 11.0
ORDER BY c.first_name;

-- @blocK
-- Selecciona el actor "Zero Cage" que haya realizado peliculas  con un rental_rate mayor a 4.0

SELECT f.title, a.first_name, a.last_name, f.rental_rate
FROM film_actor fa
JOIN film f ON fa.film_id = f.film_id
JOIN actor a on fa.actor_id = a.actor_id
WHERE f.rental_rate > 4.0 AND a.first_name = "Zero"
ORDER BY a.first_name; 

-- @blocK
-- Suma la venta total por categoría de peliculas

SELECT c.name, SUM(p.amount) AS total_ventas
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_ventas DESC;


-- @blocK
-- Selecciona a los clientes por pais y ciudad

SELECT first_name as "Nombre", last_name AS "Apellido",  ci.city as "Ciudad", coun.country as "Pais"
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country coun ON ci.country_id = coun.country_id
GROUP BY first_name, last_name, ci.city, coun.country
ORDER BY first_name DESC;

-- @blocK
-- Suma la venta total de peliculas por cada staff 
SELECT s.first_name, s.last_name, SUM(amount) AS total_ventas 
FROM payment p
JOIN staff s ON p.staff_id = s.staff_id
GROUP BY s.first_name, s.last_name
ORDER BY total_ventas DESC;


-- @blocK
SELECT * FROM rental;
SELECT * FROM inventory;
SELECT * FROM film;
SELECT * FROM film_category;
SELECT * FROM category;