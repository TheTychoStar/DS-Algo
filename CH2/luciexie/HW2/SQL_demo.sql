-- Create demo database and table
CREATE DATABASE sales;
CREATE TABLE "products"(
	"prod_id" int, 
	"prod_name" varchar(255),
	"brand" varchar(255),
	"category" varchar(255)
);
CREATE TABLE "segments"(
	"cust_id" int,
	"seg_name" varchar(255),
	"update_dt" datetime,
	"active_flag" varchar(255) 
);
CREATE TABLE "transactions"(
	"trans_id" int,
    "trans_dt" datetime,
	"cust_id" int,
	"prod_id" int,
	"item_qty" int,
	"item_price" real
);

-- Insert values 
INSERT INTO products(prod_id, prod_name, brand, category)
VALUES(218423, 'product 218423', 'S', 'Women');

INSERT INTO segments(cust_id, seg_name, update_dt, active_flag)
VALUES(504342, 'INFREQUENT', '2015-06-01 00:00:00', 'N');

INSERT INTO transactions(trans_id, trans_dt, cust_id, prod_id, item_qty, item_price)
VALUES(1, '2016-01-02 10:06:00', 9085146, 218423, 2, 32.99);

-- Create index
CREATE INDEX idx_cust 
ON segments (cust_id);

-- Alter table
ALTER TABLE segments
ADD email varchar(255);

ALTER TABLE segments
ADD dob date;

ALTER TABLE segments
DROP COLUMN dob;

/* Find the current active segment for each customer 
sorted by the segment update date */
SELECT cust_id, seg_name, update_at
FROM segments
WHERE active_flag = 'Y';

/* For each product purchased between Jan 2016 and May 2016 
(inclusive), find the number of distinct transactions */
SELECT t.prod_id, p.prod_name, count(t.item_qty) as count
FROM transactions t
INNER JOIN products p ON t.prod_id = p.prod_id
WHERE trans_dt BETWEEN '2016-01-01' AND '2016-05-31'
GROUP BY t.prod_id;

/* Find the most recent segment of each customer as of 2016-03-01. */
SELECT cust_id, seg_name, update_at
FROM segments s1
WHERE update_at = (
	SELECT MAX(update_at)
	FROM segments s2
	WHERE s1.cust_id = s2.cust_id
	) and update_at <= '2016-03-01'
ORDER BY cust_id;

/* Find the most popular category (by revenue) for each active segment. */
SELECT s.seg_name, s.category, MAX(s.revenue)
FROM (
	SELECT s.seg_name, p.category, SUM(t.item_qty * t.item_price) revenue
	FROM transactions t 
	JOIN segments s ON t.cust_id = s.cust_id
	JOIN products p ON t.prod_id = p.prod_id
	WHERE s.active_flag = 'Y'
	GROUP BY s.seg_name, p.category) AS s
GROUP BY seg_name;

/* Lock table: 
The ORDER of the lock matters!

code ref: https://docs.oracle.com/javadb/10.8.3.0/ref/rrefsqlj40506.html
To lock the entire table in share mode to avoid 
a large number of row locks, use the following statement: */
LOCK TABLE segments IN SHARE MODE;
SELECT *
FROM segments
WHERE active_flag = 'Y';

/* You have a transaction with multiple UPDATE statements. 
Since each of the individual statements acquires only a few 
row-level locks, the transaction will not automatically upgrade
the locks to a table-level lock. However, collectively the UPDATE
statements acquire and release a large number of locks, which might 
result in deadlocks. For this type of transaction, you can acquire an 
exclusive table-level lock at the beginning of the transaction. */
LOCK TABLE transactions IN EXCLUSIVE MODE;
UPDATE transactions
SET item_price = (item_price - 2)
WHERE prod_id = 223029 AND trans_dt = DATETIME('2016-06-02 10:06:00');

UPDATE transactions
SET item_price = (item_price - 5)
WHERE prod_id = 2276060 AND trans_dt = DATETIME('2016-01-02 14:19:00');

UPDATE transactions
SET item_price = (item_price - 10)
WHERE prod_id = 4980360 AND trans_dt = DATETIME('2016-01-02 13:42:00');

-- PARTITION BY
SELECT department_id, last_name, employee_id, ROW_NUMBER()
OVER (PARTITION BY department_id ORDER BY employee_id) AS emp_id
FROM employees;

