import pytest
import CH2.stevenli.HW2.DB_BestPractice.FinnhubDB_practice
import psycopg2
from configparser import ConfigParser
import finnhub
from datetime import datetime


# set up connection to local db
def config(filename='database_hw2.ini', section='postgresql'):
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


def test_insertDataFrame():
    CH2.stevenli.HW2.DB_BestPractice.FinnhubDB_practice.drop_table()
    # Setup client
    finnhub_client = finnhub.Client ( api_key="bv4f2qn48v6qpatdiu3g" )

    # Stock candles
    res = finnhub_client.stock_candles ( 'AAPL', 'D', 1590988249, 1591852249 )

    # Convert to Pandas Dataframe
    import pandas as pd
    CH2.stevenli.HW2.DB_BestPractice.FinnhubDB_practice.insertDataFrameIntoTable ( pd.DataFrame ( res ) )










