import effects
import logging


class SaveData():
    def __init__(self):
        self.insert_candle_foramt = """INSERT INTO candles_tick \
                (symbol, open, close, high, low, volume, tick) \
                VALUES ('{symbol}', %s, %s, %s, %s, %s, %s)"""

    def candles(self, symbol, data):
        with effects.PostgresqlStore('Like1hate_') as db:
            cur = db.conn.cursor()
            sql = self.insert_candle_foramt.format(symbol=symbol)
            try:
                cur.fast_executemany = True
                cur.executemany(sql, data)
                db.conn.commit()
            except Exception as error:
                db.conn.rollback()
                logging.error(error)
