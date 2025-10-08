-- Mostrar actor y customer

SELECT * FROM actor;
SELECT * FROM customer;

-- @block 
-- Mostrar solo algunas columnas de actor

SELECT first_name FROM actor;

-- @block 
-- Cambiar el nombre de una columna o alias

SELECT first_name AS "cliente" FROM actor;
SELECT email AS "correo clientes" FROM customer;
SELECT first_name AS "empleado", email AS "Correo empleados" FROM staff;

--@BLOCK
-- Aplicación de filtros
-- Busca un cliente con apellido Crawford 
SELECT * FROM customer
WHERE last_name = "CRAWFORD" AND active = 1;

-- @block 
-- Selecciona los payment que sean menor a 11.0 o mayor a 9.0
SELECT * FROM payment
WHERE amount < 11.0 AND amount > 9.0;

-- @blocK
-- Selecciona clientes que los  nombres que comience con A y el apellido con C, muestra
-- los 3 primeros resultados
SELECT * FROM customer
WHERE first_name LIKE "A%" AND last_name LIKE "C%"
LIMIT 3;

-- @blocK
-- Cuenta la cantidad total de clientes 
SELECT COUNT(*) AS total_clientes FROM customer;

-- @blocK
-- Cuenta la cantidad total de staff 
SELECT COUNT(*) as total_staff FROM staff;