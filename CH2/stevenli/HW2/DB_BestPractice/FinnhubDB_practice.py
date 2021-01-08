import psycopg2
from configparser import ConfigParser
import finnhub
from datetime import datetime



# set up connection to local db
def config(filename='database_finnhub.ini', section='postgresql'):
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

# Set up cursor in PostgreSQL
def cursor_setup():
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # return current db connector
        return conn
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

# drop table
def drop_table():
    conn = None
    try:
        conn = cursor_setup()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS stockcandles")
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None :
            conn.close()

# Create a table called stockcandles
# column: stock_id, symbol, open,
def create_table():
    conn = None
    try:
        conn = cursor_setup()
        # Create a cursor
        cur = conn.cursor()
        # create table one by one
        sqlcommand = "CREATE TABLE IF NOT EXISTS stockcandles ( " \
                     "stock_id      SERIAL PRIMARY KEY, " \
                     "symbol        VARCHAR(50) NOT NULL, " \
                     "close         FLOAT NOT NULL, " \
                     "high          FLOAT NOT NULL, " \
                     "low           FLOAT NOT NULL, " \
                     "open          FLOAT NOT NULL, " \
                     "time          TIMESTAMPTZ NOT NULL," \
                     "volume        INT NOT NULL);"
        cur.execute (sqlcommand)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# insert single row in stockcandles table
def insertSingleRow():
    conn = None
    try :
        conn = cursor_setup ()
        # Create a cursor
        cur = conn.cursor ()
        # create table one by one
        sqlcommand = "INSERT INTO stockcandles" \
                     "(symbol, close, high, low, open, time, volume) " \
                     "VALUES " \
                     "('AAPL', 2.5, 7.5, 1.5, 5.5, '2020-06-01', 999999999);"
        cur.execute(sqlcommand)
        # close communication with the PostgreSQL database server
        cur.close ()
        # commit the changes
        conn.commit ()
    except (Exception, psycopg2.DatabaseError) as error :
        print ( error )
    finally :
        if conn is not None :
            conn.close ()

# insert dataframe into stockcandles
def insertDataFrameIntoTable(df):
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    conn = None
    try:
        conn = cursor_setup()
        # Create a cursor
        cur = conn.cursor()
        # Use for loop to write dataframe into table. There might be a performance issue if dataframe size is huge.
        for x in tuples:
            sqlcommand = "INSERT INTO stockcandles" \
                         "(symbol, close, high, low, open, time, volume) " \
                         "VALUES " \
                         "('AAPL', %s, %s, %s, %s, %s, %s);"
            val = (format(x[0], '.2f'), format(x[1], '.2f'), format(x[2], '.2f'),
                   format(x[3], '.2f'), datetime.fromtimestamp(x[5]), int(x[6]))
            cur.execute(sqlcommand, val)


        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    # drop all 4 tables if exists
    drop_table()
    create_table()
    insertSingleRow()

    # Setup client
    finnhub_client = finnhub.Client ( api_key="bv4f2qn48v6qpatdiu3g" )

    # Stock candles
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)


    # Convert to Pandas Dataframe
    import pandas as pd
    insertDataFrameIntoTable(pd.DataFrame(res))

    print("The End of finnhubdb_practice")





