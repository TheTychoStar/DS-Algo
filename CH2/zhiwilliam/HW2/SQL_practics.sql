CREATE DATABASE demo
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE public.sales
(
    sales_name character varying(20) COLLATE pg_catalog."default",
    sales_amount numeric,
    sales_date date
)

CREATE INDEX index_sales_date
ON sales (sales_date);


INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("William",23.4,"2020-01-01")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Neo",23.2,"2020-01-01")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Harry",24.2,"2020-01-01")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("William",23.4,"2020-01-02")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Neo",24.3,"2020-01-02")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Harry",22.4,"2020-01-02")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("William",23.4,"2020-01-03")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Neo",23.4,"2020-01-03")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Harry",23.4,"2020-01-03")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("William",25.3,"2020-01-04")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Neo",23.2,"2020-01-04")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Harry",26.7,"2020-01-04")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("William",25.3,"2020-01-05")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Neo",23.2,"2020-01-05")
INSERT INTO SALES ("sales_name","sales_amount","sales_date") VALUES ("Harry",26.7,"2020-01-05")

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

SELECT sales_name, sales_date FROM sales INNER JOIN new_record 
ON sales_amount = latest_record and sales_date = create_date