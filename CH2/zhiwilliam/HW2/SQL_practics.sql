CREATE DATABASE demo
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE salesperson
(
    id SERIAL PRIMARY KEY,
    name character varying(20)
)

CREATE TABLE public.sales
(
    salesperson_id INT not null,
    sales_amount numeric not null,
    sales_date date not null,
	CONSTRAINT fk_sales_person
      FOREIGN KEY(salesperson_id) 
	  REFERENCES salesperson(id)
)

CREATE INDEX index_sales_date
ON sales (sales_date);

INSERT INTO salesperson (name) VALUES ('William');
INSERT INTO salesperson (name) VALUES ('Neo');
INSERT INTO salesperson (name) VALUES ('Harry');


INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('1',23.4,'2020-01-01');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('2',23.2,'2020-01-01');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('3',24.2,'2020-01-01');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('1',23.4,'2020-01-02');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('2',24.3,'2020-01-02');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('3',22.4,'2020-01-02');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('1',23.4,'2020-01-03');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('2',23.4,'2020-01-03');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('3',23.4,'2020-01-03');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('1',25.3,'2020-01-04');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('2',23.2,'2020-01-04');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('3',26.7,'2020-01-04');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('1',25.3,'2020-01-05');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('2',23.2,'2020-01-05');
INSERT INTO SALES (salesperson_id,sales_amount,sales_date) VALUES ('3',26.7,'2020-01-05');

-- Find all dates having total sale amount over 70.5
SELECT sales_date AS total_sale FROM sales GROUP BY sales_date
HAVING SUM(sales_amount) > 70.5


-- Find all sales name and date that creates a sale record.
WITH all_record AS 
 (SELECT DISTINCT 
  sales_date,
  max(sales_amount) OVER (ORDER BY sales_date ) latest_record
 FROM sales ORDER BY sales_date),
 new_record AS (
	SELECT latest_record, MIN(sales_date) AS create_date FROM all_record 
 	GROUP BY latest_record
 )

SELECT P.name, sales_date FROM sales INNER JOIN new_record 
ON sales_amount = latest_record and sales_date = create_date
INNER JOIN salesperson P ON P.id = salesperson_id;