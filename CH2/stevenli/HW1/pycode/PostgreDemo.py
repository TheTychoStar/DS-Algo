import psycopg2
from configparser import ConfigParser


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

# Query file title and description
def query_filmTitleAndDescription():

    conn = None

    try:
        # read connetion parameters
        params = config()
        # connect to PostgreSQL server
        conn = psycopg2.connect(**params)
        print("connecting to database")
        # create a cursor
        cur = conn.cursor()
        # Query title and description from file table
        cur.execute("SELECT title, description FROM film")
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        #
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError)as error:
        print("except")
    finally:
        conn.close()
        print("Database connection closed")


# Query first name and last name from customer table
def query_firstnameAndlastnameFromCustomerTable(query_string):
    print (query_string)

    try:
        # read connetion parameters
        params = config()
        # connect to PostgreSQL server
        conn = psycopg2.connect(**params)
        print("connecting to database")
        # create a cursor
        cur = conn.cursor()
        # Query title and description from file table
        cur.execute(query_string)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        #
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError)as error:
        print("except")
    finally:
        conn.close()

if __name__=='__main__':
    query_filmTitleAndDescription()

    query_firstnameAndlastnameFromCustomerTable("SELECT first_name,last_name FROM customer")

    conn = None

