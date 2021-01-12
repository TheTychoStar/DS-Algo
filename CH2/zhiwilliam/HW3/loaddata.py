from query import FinnhubQuery, OldDataQuery
from persistent import SaveData
from datetime import datetime
from datetime import timedelta
# from decimal import Decimal
import csv
import pytz
import logging


# We will retrieve latest 2 ticks data to make some overlap
delta_switcher = {
    '1': timedelta(minutes=2),
    '5': timedelta(minutes=10),
    '30': timedelta(hours=1),
    'D': timedelta(days=2),
    'W': timedelta(weeks=2)
}

logging.basicConfig(filename='etl.log', level=logging.DEBUG)
est = pytz.timezone('US/Eastern')


def tick_delta(resolution):
    return delta_switcher.get(resolution)


def getCurrentTick(symbols, resolution):
    query = FinnhubQuery()
    now = datetime.now().astimezone(est)
    try:
        return query.candles(symbols, resolution, now - tick_delta(resolution), now)
    except Exception as error:
        logging.error(error)


def load_and_etl(symbol):
    resolution = 'D'
    db_tick_index = 6
    # db_open_index = 1
    tick_index = 5
    # open_index = 0

    candles_data = getCurrentTick(symbol, resolution)
    logging.info(symbol)
    logging.debug("Check if data is valid")
    latest_candle = OldDataQuery().latest_candle(symbol)
    if(latest_candle is not None and len(latest_candle) > 0):
        # Get latest tick time, compare it with retrieved tick and detect split/merge
        latest_tick = latest_candle[0][db_tick_index]
        # same_tick_candle_data = list(filter(lambda x: (x[tick_index] == latest_tick), candles_data))
        # if(len(same_tick_candle_data) > 0):
        #     new_open = Decimal(same_tick_candle_data[0][open_index])
        #     old_open = latest_candle[0][db_open_index]
        #     if (abs(new_open - old_open) > 0.01):
        #         factor = new_open / old_open
        #         : update
        save_data = list(filter(lambda x: (x[tick_index] > latest_tick), candles_data))
        if(len(save_data) > 0):
            SaveData().candles(symbol, save_data)
    else:
        SaveData().candles(symbol, candles_data)


if __name__ == "__main__":
    logging.debug("Getting candle data")
    with open('sec_list_1000.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            load_and_etl(row[0])
