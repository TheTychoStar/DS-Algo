import effects
import logging
from datetime import datetime


class FinnhubQuery:
    def __init__(self):
        self.base_time = datetime(1970, 1, 1)

    def candles(self, symbol: str, resolution: str, start: datetime, end: datetime):
        start_seconds = int((start - self.base_time).total_seconds())
        end_seconds = int((end - self.base_time).total_seconds())

        with effects.FinnhubClient() as finnhub:
            # 1, 5, 15, 30, 60, D, W, M
            data = finnhub.client.stock_candles(symbol, resolution, start_seconds, end_seconds)
            if(data["s"] == "ok"):
                return list(zip(data['o'], data['c'], data['h'], data['l'], data['v'], data['t']))
            elif(data["s"] == "no_data"):
                return []
            else:
                raise Exception("Failed to load candles" + data["s"])


class OldDataQuery:
    def __init__(self):
        self.base_time = datetime(1970, 1, 1)
        self.cadnles_foramt = """SELECT symbol, open, close, high, low, volume, \
            tick FROM candles_tick_daily WHERE symbol = '{symbol}' ORDER BY tick DESC limit 1"""

    def latest_candle(self, symbol: str):
        with effects.PostgresqlStore('Like1hate_') as db:
            cur = db.conn.cursor()
            sql = self.cadnles_foramt.format(symbol=symbol)
            try:
                cur.execute(sql)
                data = cur.fetchall()
                return data
            except Exception as error:
                logging.error(error)
            cur.close()


if __name__ == "__main__":
    data = OldDataQuery().latest_candle('GOOG')
    print(data)
