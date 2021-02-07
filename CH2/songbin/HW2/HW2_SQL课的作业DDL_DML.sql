create table sales(
sales_name char(10), 
sales_amount number, 
busi_date date
)

INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('William', 23.4,TO_DATE( '2020-01-01','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Neo',     23.2, TO_DATE('2020-01-01','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Harry',   24.2, TO_DATE('2020-01-01','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('William', 23.4, TO_DATE('2020-01-02','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Neo',     24.3, TO_DATE('2020-01-02','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Harry',   22.4, TO_DATE('2020-01-02','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('William', 23.4, TO_DATE('2020-01-03','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Neo',     23.4,TO_DATE('2020-01-03','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Harry',   23.4, TO_DATE('2020-01-03','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('William', 25.3,TO_DATE('2020-01-04','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Neo',     23.2, TO_DATE('2020-01-04','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Harry',   26.7,TO_DATE('2020-01-04','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('William', 25.3,TO_DATE('2020-01-05','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Neo',     23.2, TO_DATE('2020-01-05','yyyy-mm-dd'));
INSERT INTO sales(sales_name, sales_amount, busi_date) VALUES ('Harry',   26.7, TO_DATE('2020-01-05','yyyy-mm-dd'));



with c1 as 
(select busi_date, max(sales_amount) as m  from sales group by busi_date) 
,c2_all as 
(select busi_date , max(m) over (order by busi_date) as n  from c1)
,c2_old as
(select busi_date, lag(n,1,-1000) over (order by busi_date) as n  from c2_all)
,c_result as
(select c1.busi_date,c1.m as m ,c2_old.n as n from c1 inner join c2_old on c1.busi_date=c2_old.busi_date where m>n)
select sales.busi_date,sales.sales_name,sales.sales_amount from sales inner join c_result
on sales.busi_date=c_result.busi_date and sales.sales_amount=c_result.m
