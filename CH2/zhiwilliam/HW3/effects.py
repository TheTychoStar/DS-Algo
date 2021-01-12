import os
import finnhub
import configparser
import psycopg2


class FinnhubClient():
    def __init__(self, api_key=os.environ.get("FINNHUB_API_KEY")):
        self.api_key = api_key
        self.client = None

    def __enter__(self):
        self.client = finnhub.Client(self.api_key)
        return self

    def __exit__(self, type, value, traceback):
        self.client.close()


class PostgresqlStore():
    def __init__(self, db_password=os.environ.get("DB_PASSWORD")):
        config = configparser.ConfigParser()
        config.read_file(open('application.conf'))
        db_config = config['DATABASE']
        self.db_host = db_config['host']
        self.db_port = int(db_config['port'])
        self.db_user = db_config['user']
        self.db_database = db_config['dbname']
        self.db_password = str(db_password)

    def __enter__(self):
        self.conn = psycopg2.connect(database=self.db_database, host=self.db_host,
                                     port=self.db_port, user=self.db_user, password=self.db_password)
        return self

    def __exit__(self, type, value, traceback):
        self.conn.close()
