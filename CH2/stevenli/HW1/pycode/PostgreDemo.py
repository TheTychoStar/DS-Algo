import psycopg2
from configparser import ConfigParser
import pandas as pd


# set up connection to local db
def config(filename='database.ini', section='postgresql'):
    # create a parset
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# Query first name and last name from customer table
def Get_QueryResult(query_string):
    print (query_string)

    try:
        # read connetion parameters
        params = config()
        # connect to PostgreSQL server
        conn = psycopg2.connect(**params)

        print("connecting to database")
        # create a cursor
        cur = conn.cursor()
        # Execute the query
        cur.execute(query_string)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        #
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError)as error:
        print("except: ", error)
    finally:
        if conn is not None:
            conn.close()


# Covert sql query result to pandas dataframe
def ConvertQueryToDataFrame(string):
    print(string)


    # read connetion parameters
    params = config()

    try:
        # connect to PostgreSQL server
        conn = psycopg2.connect(**params)
        print("connecting to database")
        # create a cursor
        #cur = conn.cursor()
        # Execute the query
        # Covert to pandas dataframe
        row = pd.read_sql_query(string, conn)

        print(row)




        #
        # close the communication with the PostgreSQL
        #cur.close()
    except (Exception, psycopg2.DatabaseError)as error:
        print("except: ", error)
    finally:
        if conn is not None:
            conn.close()






if __name__=='__main__':
    #Get_QueryResult("SELECT title, description FROM film")
    # Query first name and last name from customer table
    ConvertQueryToDataFrame("SELECT first_name,last_name FROM customer")
    # Inner Join customer and payment table
    queryStr = "SELECT " \
               "CUSTOMER.CUSTOMER_ID, " \
               "FIRST_NAME, " \
               "LAST_NAME, " \
               "AMOUNT, " \
               "PAYMENT_DATE " \
               "FROM " \
               "CUSTOMER " \
               "INNER JOIN PAYMENT " \
               "ON PAYMENT.CUSTOMER_ID=CUSTOMER.CUSTOMER_ID " \
               "ORDER BY PAYMENT_DATE"

    #Get_QueryResult(queryStr)

    ConvertQueryToDataFrame(queryStr)

    # Group By with SUM() function
    queryStr = "SELECT " \
               "CUSTOMER_ID, " \
               "SUM(amount) " \
               "FROM " \
               "PAYMENT " \
               "GROUP BY " \
               "CUSTOMER_ID;"
    ConvertQueryToDataFrame(queryStr)

    # Left Join to join film table with the inventory table
    queryStr = "SELECT " \
               "FILM.FILM_ID, " \
               "TITLE, " \
               "INVENTORY_ID " \
               "FROM " \
               "FILM " \
               "LEFT JOIN INVENTORY " \
               "ON INVENTORY.FILM_ID = FILM.FILM_ID " \
               "ORDER BY TITLE;"
    ConvertQueryToDataFrame(queryStr)


    conn = None

