

-- Simple operations :
-- select title, pages from books order by pages desc limit 1;

-- select distinct concat(title,'-', released_year) as summary from books order by released_year desc limit 3; 

-- select title, author_lname from books where author_lname like "%\ %";

-- select title, released_year, stock_quantity from books order by stock_quantity limit 3;

-- select author_lname, title from books order by author_lname, title;

-- select concat("MY FAVORITE BOOK IS"," ",Upper(author_fname)," ", UPPER(author_lname), "!") as yell from books order by author_lname;

-- Select count(distinct author_fname, author_lname) from books;

-- select count(*) from books where title like "%the%";

/* select author_fname, author_lname, count(*) from books group by author_lname, author_fname;

select  concat("In ", released_year,"  ", count(*),"  ", "book(s) released") as year from books group by released_year;

select min(released_year) from books;

select min(pages) from books; */

/* select max(pages) from books;

select * from books where pages = (select max(pages) from books);

select title, pages from books where pages = (select max(pages) from books);
-- or
select title, pages from books order by pages desc limit 1;

select author_fname, author_lname, min(released_year) from books group by author_lname, author_fname;
-- or
select concat(author_fname,' ', author_lname) as author, max(pages) as 'longest pages' from books group by author_lname, author_fname;

select author_fname, author_lname, sum(pages)
from books
group by author_lname, author_fname;

select avg(released_year) from books;

select avg(pages) from books;*/

/* select released_year, avg(stock_quantity) from books group by released_year;

select author_fname, author_lname, avg(pages) from books group by author_fname, author_lname;

select  concat("In ", released_year,"  ", count(*),"  ", "book(s) released") as year  from books group by released_year;

select concat("We're having", " ",sum(stock_quantity), " ", "in stock") as "All books in stock" from books;

select author_lname, author_fname, avg(released_year) from books group by author_lname, author_fname;

select concat(author_fname," ", author_lname) as "Full name" from books where pages=(select max(pages) from books);
-- or
select concat(author_fname," ", author_lname) as "Full name" from books order by pages desc limit 1;

select released_year as year,
count(*) as '# books', avg(pages) as 'avg pages'
from books group by released_year;*/
-- DATETIME / TIMESTAMPS
-- create table people ( name varchar(100), birthdate Date, birthtime time, birthdt Datetime);

-- insert into people(name, birthdate, birthtime, birthdt) values ('Microwave', Curdate(), curtime(), Now());

-- select name,bithydate, Day(birthdate) from people;

-- select date_format('2009-10-22 22:23:00', '%W-%M-%Y') as date;

-- select date_format(birthdt,'%m/%d/%Y at %h:%m') from people;

/* select name, birthdate, datediff(now(), birthdate) from people;

select birthdt from people;

select birthdt, date_add(birthdt, interval 1 month) from people;

select birthdt */
 -- LOGICAL OP: 
/* select title, released_year from books where released_year!=2017;
 
 select title, author_lname from books where author_lname!='Harris';
 
 Select title from books where title not like '%w%';
 
 select * from books where released_year > 2000;
 
 select title, released_year from books where released_year > 2000 order by released_year;
 
 select title, stock_quantity from books where stock_quantity >= 100;
 
 select title, author_lname, released_year from books where author_lname = 'Eggers' AND released_year >= 2010;
 
 
select title, released_year from books where released_year not between 2004 and 2015;

select name, birthdt from people where birthdt between cast('1980-01-01'as datetime) and cast('2000-01-01'as datetime);

select title, author_lname from books where author_lname not in ('Carver', 'Lahiri', 'Smith');

select title, released_year from books where released_year >=2000 and released_year %2 !=0;

select title, released_year, 
	case 
		when released_year >= 2000 then 'Modern Lit' 
        else '20th Centrury Lit'
	end as genre
from books;

select title, stock_quantity, case when stock_quantity between 0 and 50 then '*' when
stock_quantity between 51 and 100 then '**' else '***' end as STOCK from books;

select title, author_lname from books where author_lname = 'Eggers' or author_lname = 'Chabon';

select title, author_lname, released_year from books where author_lname = 'Lahiri' and released_year > 2000;

select title, pages from books where pages between 100 and 200;

select title, author_lname from books where author_lname like 'C%' or author_lname like 'S%';

select title, author_lname, case when title like '%stories%' then 'Short Stories' when
title like '%Just kids%' or title like '%heartbreaking%' then 'Memoir' else 'Novel' end as 'TYPE' from books; 

select author_lname, 
	case 
		when count(*) = 1 then'1 book' else concat(count(*), ' books') 
	end as count   
from books 
group by author_lname, author_fname;*/

-- Relaionships and JOINS
-- One to Many/1:Many(Most common)
 -- CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, 
-- first_name VARCHAR(100), last_name VARCHAR(100), email VARCHAR(100));

-- CREATE TABLE orders(id INT AUTO_INCREMENT PRIMARY KEY, order_date DATE, amount DECIMAL(8,2), customer_id INT, FOREIGN KEY(customer_id) REFERENCES customers(id));


-- INSERT INTO customers (first_name, last_name, email) VALUES ('Boy', 'George','george@gmail.com'), ('George','Michael', 'gm@gmail.com'), ('David', 'Bowie', 'david@gmail.com'),
-- ('Blue','Steele','blue@gmail.com');

-- INSERT INTO orders(order_date, amount,customer_id) VALUES ('2016/02/10', 99.99, 1),
-- ('2017/11/11', 35.50,1), ('2014/12/12',800.67,2), ('2015/01/03',12.50,2)

-- INSERT INTO orders(order_date, amount,customer_id) VALUES ('2019/04/01', 33.11, 93);

-- SELECT * FROM customers where last_name='George';
-- Select * FROM orders where customer_id =1;
-- -- IMPLICIT INNER JOIN
-- select * from orders where customer_id = (
-- select ID from customers where last_name = 'George');

-- SELECT first_name, last_name, order_date, amount FROM customers, orders where customers.id = orders.customer_id;

-- -- EXPLICIT INNER JOIN
-- Select first_name, last_name, order_date, amount FROM customers
-- JOIN orders
-- ON customers.id = orders.customer_id;
-- ON DELETE CASCADE
/* 
SELECT first_name, title, grade
FROM students
INNER JOIN papers
    ON students.id = papers.student_id
ORDER BY grade DESC;

SELECT first_name, title, grade
FROM students
RIGHT JOIN papers
    ON students.id = papers.student_id
ORDER BY grade DESC;

SELECT first_name, title, grade
FROM students
LEFT JOIN papers
    ON students.id = papers.student_id;
    
SELECT
    first_name,
    IFNULL(title, 'MISSING'),
    IFNULL(grade, 0)
FROM students
LEFT JOIN papers
    ON students.id = papers.student_id;
    
SELECT
    first_name,
    IFNULL(AVG(grade), 0) AS average
FROM students
LEFT JOIN papers
    ON students.id = papers.student_id
GROUP BY students.id
ORDER BY average DESC;

SELECT first_name, 
       Ifnull(Avg(grade), 0) AS average, 
       CASE 
         WHEN Avg(grade) IS NULL THEN 'FAILING' 
         WHEN Avg(grade) >= 75 THEN 'PASSING' 
         ELSE 'FAILING' 
       end                   AS passing_status 
FROM   students 
       LEFT JOIN papers 
              ON students.id = papers.student_id 
GROUP  BY students.id 
ORDER  BY average DESC;

-- Many to Many

-- Examples
Books <-> Authors
Blog Post <-> Tags
Stundents <-> Clases*/

-- create table series( id int auto_increment primary key, title varchar(100), released_year year(4), genre varchar(100));



-- INSERT INTO series (title, released_year, genre) VALUES
--     ('Archer', 2009, 'Animation'),
--     ('Arrested Development', 2003, 'Comedy'),
--     ("Bob's Burgers", 2011, 'Animation'),
--     ('Bojack Horseman', 2014, 'Animation'),
--     ("Breaking Bad", 2008, 'Drama'),
--     ('Curb Your Enthusiasm', 2000, 'Comedy'),
--     ("Fargo", 2014, 'Drama'),
--     ('Freaks and Geeks', 1999, 'Comedy'),
--     ('General Hospital', 1963, 'Drama'),
--     ('Halt and Catch Fire', 2014, 'Drama'),
--     ('Malcolm In The Middle', 2000, 'Comedy'),
--     ('Pushing Daisies', 2007, 'Comedy'),
--     ('Seinfeld', 1989, 'Comedy'),
--     ('Stranger Things', 2016, 'Drama');
-- CREATE TABLE reviewers (id int auto_increment primary key, first_name Varchar(100), last_name varchar(100));

-- INSERT INTO reviewers (first_name, last_name) VALUES
--     ('Thomas', 'Stoneman'),
--     ('Wyatt', 'Skaggs'),
--     ('Kimbra', 'Masters'),
--     ('Domingo', 'Cortes'),
--     ('Colt', 'Steele'),
--     ('Pinkie', 'Petit'),
--     ('Marlon', 'Crafford');    
--     
-- create table reviews ( id int auto_increment primary key, rating decimal(2,1), series_id int, reviewer_id int, foreign key(series_id) references series(id), foreign key(reviewer_id) references reviewers(id));

-- INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
--     (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
--     (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
--     (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
--     (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
--     (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
--     (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
--     (7,2,9.1),(7,5,9.7),
--     (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
--     (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
--     (10,5,9.9),
--     (13,3,8.0),(13,4,7.2),
--     (14,2,8.5),(14,3,8.9),(14,4,8.9);



select title, rating from series
JOIN reviews ON series.id =  reviews.series_id;


select title, rating from series Join reviews on series.id = reviews.series_id
group by series.id;

select series.id, title, avg(rating) as avg_rating from series join reviews on series.id = reviews.series_id group by series.id
order by avg_rating desc;

select first_name, last_name, rating from reviewers
inner join reviews on reviewers.id = reviews.reviewer_id;

Select title as unreviewed_series from series
left Join reviews on series.id = reviews.series_id
where rating IS NULL;

Select genre, ROUND(avg(rating), 2) as avg_rating from series
INNER JOIN reviews
ON series.id = reviews.series_id
group by genre;

select first_name, last_name, COUNT(rating) AS COUNT,IFNULL(MIN(rating),0) AS MIN, 
IFNULL(MAX(rating),0) AS MAX,IFNULL(AVG(rating),0) AS AVG,
-- ALTERNATIVE FOR CASE: IF (COUNT(rating) >= 1, 'ACTIVE', 'INACTIVE') AS STATUS
CASE
WHEN COUNT(rating) >= 1 THEN 'ACTIVE' ELSE 'INACTIVE'
END AS STATUS 
 from reviewers
left JOIN reviews on reviewers.id = reviews.reviewer_id
group by reviewers.id;

Select title, rating, CONCAT(first_name,' ',last_name) as Reviewer from reviewers
INNER JOIN reviews ON reviewers.id = reviews.reviewer_id
INNER JOIN series on series.id = reviews.series_id
ORDER BY title;




