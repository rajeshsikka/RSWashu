 # 1a
use sakila;

select first_name, last_name from actor; 

#1b
select concat(first_name, ' ', last_name) AS 'Actor Name' from actor;

#2a
select actor_id, first_name, last_name from actor where first_name = "Joe";

#2b
select first_name, last_name from actor where last_name like "%GEN%";

#2c
select last_name, first_name from actor where last_name like "%LI%" order by last_name, first_name;

#2d
select country_id, country from country where country IN  ('Afghanistan', 'Bangladesh', 'China');

#3a
alter table actor
add column description blob NOT NULL ;

#3b
alter table actor
drop column description;

#4a
select last_name, count(*)
  from actor
group
    by last_name
having count(*) > 1;

#4b

select last_name, count(*)
  from actor
group
    by last_name
having count(*) > 2;

#4c
select first_name, last_name from actor where first_name = 'GROUCHO' and last_name = 'Williams';
UPDATE actor SET first_name ='HARPO' WHERE first_name ='GROUCHO' and last_name = 'WILLIAMS';
select first_name, last_name from actor where first_name = 'GROUCHO' and last_name = 'Williams';
select first_name, last_name from actor where first_name = 'HARPO' and last_name = 'Williams';

#4d
UPDATE actor SET first_name ='GROUCHO' WHERE first_name ='HARPO' and last_name = 'WILLIAMS';
select first_name, last_name from actor where first_name = 'GROUCHO' and last_name = 'Williams';

#5a (schema was already present. Ran the following 2 queries to check it)
SELECT table_name FROM information_schema.tables where table_schema='sakila';
DESCRIBE address; 

#6a 
select staff.first_name, staff.last_name, address.address 
  from staff, address
  where staff.address_id = address.address_id;

#6b
SELECT staff.first_name, staff.last_name, SUM(payment.amount)
  FROM staff join payment on 
	staff.staff_id = payment.staff_id 
	where Month(payment_date)='08' && YEAR(payment_date)='2005'
	group by staff.first_name,staff.last_name;
    
#6c
SELECT film.title, count(film_actor.actor_id)
  FROM film join film_actor on 
	film.film_id = film_actor.film_id
	group by film.title;
    
#6d
SELECT film.title, count(inventory.film_id)
  FROM film join inventory on 
	film.film_id = inventory.film_id
    where film.title = "Hunchback Impossible"; 

#6e
SELECT customer.last_name as 'Customer Last Name', SUM(payment.amount) as 'Total Amount paid by Customer'
  FROM customer join payment on 
	 customer.customer_id = payment.customer_id
	 group by customer.last_name;

#7a
SELECT film.title, language.name FROM film, language WHERE 
 (title LIKE ("K%") OR title LIKE ("Q%")) AND
 (language.name = (select name from language where name = 'English'));    
 
#7b
select actor.actor_id, actor.first_name, actor.last_name, film.title from actor, film, film_actor where 
 (actor.actor_id = film_actor.actor_id) AND
 (film_actor.film_id = film.film_id) AND
 (film.title = 'Alone Trip');
 
#7c
select customer_list.name, customer_list.country, customer.email from customer_list, customer where
 (customer_list.ID = customer.customer_id) and
 (customer_list.country = "Canada");
 
 #7d
 SELECT film.title as 'Film Name', category.name as 'Film Category' from film, film_category, category WHERE
  film.film_id = film_category.film_id AND
  film_category.category_id = category.category_id AND
  category.name = 'Family';
 
 #7e
 select film.title, count(inventory.inventory_id) from film, inventory, rental where
    film.film_id = inventory.film_id AND
    rental.inventory_id = inventory.inventory_id
    group by film.title 
    order by count(inventory.inventory_id) desc;
    
#7f
select store.store_id, sum(payment.amount) from store, payment, inventory, rental where 
  store.store_id = inventory.store_id AND
  rental.inventory_id = inventory.inventory_id AND
  payment.rental_id = rental.rental_id 
  group by store.store_id;

#7g
Select store.store_id, address.address, city.city, country.country from store, address, city, country where
  store.address_id = address.address_id AND
  address.city_id = city.city_id AND
  city.country_id = country.country_id; 
  
#7h
select category.name AS 'GENRES', sum(payment.amount) AS 'Total Amt Sales' from category, film_category, inventory, payment, rental where
  category.category_id = film_category.category_id AND
  inventory.inventory_id = rental.inventory_id AND
  inventory.film_id = film_category.film_id AND
  payment.rental_id = rental.rental_id   
  group by category.name
  order by sum(payment.amount) desc;
  
  #8a
  CREATE VIEW exec_review AS select category.name AS 'GENRES', sum(payment.amount) AS 'Total Amt Sales' 
   from category, film_category, inventory, payment, rental where
   category.category_id = film_category.category_id AND
   inventory.inventory_id = rental.inventory_id AND
   inventory.film_id = film_category.film_id AND
   payment.rental_id = rental.rental_id   
   group by category.name
   order by sum(payment.amount) desc
   LIMIT 5;
   
   #8b
   select * from exec_review;
   
   #8c
   DROP VIEW exec_review;