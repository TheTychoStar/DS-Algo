import os
import psycopg2

# Create a database connection
db_password = os.environ.get('DB_PASSWORD')  # Set to your own password
#engine = create_engine('postgresql://postgres:{}@localhost/demo'.format(db_password))
#conn = psycopg2.connect("host=localhost dbname=demo user=postgres password=Hzh821105$")
conn = psycopg2.connect('host=localhost dbname=demo user=postgres password={}'.format(db_password))
cur = conn.cursor()


#cur.execute('SELECT * FROM sales')
sql = """select sales_name, date, sales_amount  from sales s1
   where sales_amount=
    (select max(sales_amount) from sales s2 where s1.date>=s2.date)"""


cur.execute(sql)

one = cur.fetchone()
print (one)
all = cur.fetchall()
print (all)

#https://www.dataquest.io/blog/loading-data-into-postgres/
