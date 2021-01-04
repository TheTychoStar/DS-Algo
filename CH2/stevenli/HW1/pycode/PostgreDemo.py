import psycopg2
from configparser import ConfigParser
import pandas as pd


# set up connection to local db
def config(filename='database.ini', section='postgresql'):
    # create a parser
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

# Create a new database table
def create_table(table_name, sqlCommand):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Drop the table if existing
        cur.execute("DROP TABLE IF EXISTS "+table_name+" ;")
        # create table one by one
        cur.execute(sqlCommand)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally :
        if conn is not None:
            conn.close()

# Execute sql command
def execute_postgresql(table_name, sqlCommand):
    print("execute_postgresql")
    conn=None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect ( **params )
        cur = conn.cursor()
        # create table one by one
        cur.execute(sqlCommand)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



# SELECT query
def Get_QueryResult(query_string):
    print(query_string)

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
        # cur = conn.cursor()
        # Execute the query
        # Covert to pandas dataframe
        row = pd.read_sql_query(string, conn)

        print(row)

        #
        # close the communication with the PostgreSQL
        # cur.close()
    except (Exception, psycopg2.DatabaseError)as error:
        print("except: ", error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # Get_QueryResult("SELECT title, description FROM film")
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

    # Get_QueryResult(queryStr)

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

    # Using PostgreSQL ORDER BY claus to
    # sort rows by multiple columns
    queryStr="SELECT " \
             "FIRST_NAME, " \
             "LAST_NAME " \
             "FROM " \
             "CUSTOMER " \
             "ORDER BY " \
             "FIRST_NAME ASC, " \
             "LAST_NAME DESC;"
    ConvertQueryToDataFrame(queryStr)

    # create a new table by passing a sql command
    table_name = "employee"
    sqlCommand = "create table if not exists "\
                 +table_name+\
                 " (employee_id INT PRIMARY KEY, " \
                 "first_name varchar(255) NOT NULL, " \
                 "last_name varchar(255) NOT NULL, " \
                 "manager_id INT, " \
                 "FOREIGN KEY(manager_id) " \
                 "REFERENCES employee (employee_id) " \
                 "ON DELETE CASCADE);"
    create_table(table_name, sqlCommand)
    # insert one row into employee table
    sqlCommand = "INSERT INTO " \
                 +table_name+\
                " (employee_id, first_name, last_name, manager_id) " \
                "VALUES (1, 'Windy', 'Hays', NULL), " \
                "(2, 'Ava', 'Christensen', 1), " \
                "(3, 'Hassan', 'Conner', 1), " \
                "(4, 'Anna', 'Reeves', 2), " \
                "(5, 'Sau', 'Norman', 2), " \
                "(6, 'Kelsie', 'Hays', 3), " \
                "(7, 'Tory', 'Goff', 3), " \
                "(8, 'Salley', 'Lester', 3);"
    execute_postgresql(table_name, sqlCommand)

    # Use self-join to find who reports to whom
    sqlCommand = "SELECT " \
                 "e.first_name || '' || e.last_name employee, " \
                 "m.first_name || '' || m.last_name manager " \
                 "FROM " \
                 "employee e " \
                 "INNER JOIN employee m ON m.employee_id=e.manager_id " \
                 "ORDER BY manager;"
    ConvertQueryToDataFrame (sqlCommand)


    conn = None
