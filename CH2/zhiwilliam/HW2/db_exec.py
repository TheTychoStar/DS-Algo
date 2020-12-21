import psycopg2 as psycopg2
import pandas as pd

def getSalesRecord(cur):
    cur.execute('SELECT * from sales order by sales_date')

    # display the PostgreSQL database server version
    data = cur.fetchall()
    df = pd.DataFrame.from_records(data, columns = ['name', 'amount', 'date'])

    daily_max = df[df.groupby('date')['amount'].transform(max) == df['amount']]

    records = daily_max.iloc[0:1].append(daily_max[daily_max['amount'] > daily_max.shift(1)['amount']])

    print(records)

if __name__ == '__main__':
    try:
        conn = psycopg2.connect("dbname=stock user=postgres password=royal1")
        cur = conn.cursor()
        getSalesRecord(cur)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')