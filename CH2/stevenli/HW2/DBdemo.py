import psycopg2
from configparser import ConfigParser
import pandas as pd
import finnhub



# set up connection to local db
def config (filename='database_hw2.ini', section='postgresql'):
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


# Create a new database table stockcandles
def create_table(table_name, sqlCommand):

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Drop the table if existing
        cur.execute("DROP TABLE "+table_name)
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


# Insert single input row in stockcandles table
def singleInsert():
    sqlCommand = "INSERT INTO STOCKCANDLES(high, )" \
                 "VALUES(%S) "
    return 0

if __name__ == '__main__':

    # create a new table by passing a sql command
    table_name="stockcandles"
    sqlCommand = "create table if not exists "+table_name+" (id bigint primary key, symbol varchar(128), open float, close float, high float, low float, volume int );"
    create_table(table_name, sqlCommand)

    # setup client
    finnhub_client = finnhub.Client(api_key="bv4f2qn48v6qpatdiu3g")

    # Stock candles
    # retrieve AAPL daily from 06/01/2020 to 06/11/2020
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
    # print out the json response
    print (res)

    # Convert to Pandas Dataframe
    import pandas as pd

    print(pd.DataFrame(res))
