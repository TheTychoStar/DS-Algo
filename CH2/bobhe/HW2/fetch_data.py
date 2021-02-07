import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from datetime import date
from datetime import datetime
import yfinance as yf
yf.pdr_override()


# Manual Create a data folder in your current dir to proceed to_csv function
def save_data(df, filename, index_required):
    # print (os.path.dirname(__file__))
    # C:/Users/bobgx/PycharmProjects/DS-Algo/CH2/bobhe/HW2
    if index_required:
        df.to_csv(filename)
    else:
        df.to_csv(filename, index=False)
    print('save data successfully')


def symbol_to_path(symbol, base_dir="./data/"):
    """Return CSV file path given symbol symbol."""
    # print(os.path.dirname(__file__))
    # print(os.path.join(base_dir,
    #                   "{}.csv".format(str(symbol)+'_'+str(today))))
    return os.path.join(base_dir,
                        "{}.csv".format(str(symbol)+'_'+str(today)))


def get_data(symbol):
    # more way to get data from yahoo finance
    # https://www.programcreek.com/python/example/92135/
    # + pandas_datareader.data.get_data_yahoo
    print(symbol)
    data = pdr.get_data_yahoo(symbol, start=start_date, end=today)
    print(data.head())
    # dataname= symbol+'_'+str(today)
    dataname = symbol_to_path(symbol)
    files.append(dataname)
    print(files)
    save_data(data, dataname, index_required=True)


def read_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    # This loop will iterate over symbol list,
    # pass one symbol to read data from csv into a dataframe
    """
    for symbol in symbols:
            df1= pd.read_csv(symbol_to_path(symbol))
            #print (df1.head())
    """

    for symbol in symbols:
        # Read symbol data into temporary dataframe
        # the CSV has following columns:
        #   Date / Open / High / Low / Close/ Adj Close / Volume
        # dfSPY = pd.read_csv("./data/SPY.csv", index_col="Date",
        #                     parse_dates=True, usecols=['Date', 'Adj Close'],
        #                    na_values=['nan'])
        print(symbol_to_path(symbol))
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])

        # Rename dataframe column from 'Adj Close' to symbol name,
        # avoid column name overlap during join data
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # join data for each symbol
        df = df.join(df_temp)  # use default how='left'

        # Join the two dataframes using DataFram.join()
        # df = df.join(df_temp, how='inner')

        # Handle SPY non trading date.
        # Take SPY as trading date brenchmark when using left join
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def normalize_data(df):
    """Normalize stock price using  the first row of the dataframe"""
    print('In normalize_data, show the 1st row data of dataframe')
    # must user iloc intead of loc here
    print(df.iloc[0, :].head())
    print(df/df.iloc[0, :])
    return df/df.iloc[0, :]


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range"""
    df = normalize_data(df)
    plot_data(df.loc[start_index:end_index, columns], title="Select data")


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def get_and_save_symbol_list_SPY500():
    """get the fule list of SPY 500 from wiki"""
    table = pd.read_html('https://en.wikipedia.org/wiki/' +
                         'List_of_S%26P_500_companies')
    df = table[0]
    print(df.head())
    # df.to_csv('S&P500-Info.csv')
    # df.to_csv("S&P500-Symbols.csv", columns=['Symbol'])
    dataname = symbol_to_path('S&P500')
    save_data(df, dataname, index_required=False)


def test_run():
    # Define a date range
    dates = pd.date_range('2020-01-01', '2020-12-31')

    # Choose stock symbols to read
    # SPY will be added in get_data()
    symbols = ['SPY', 'GOOG', 'IBM', 'GLD', 'AAPL', 'MSFT', 'FB', 'CRM']

    for symbol in symbols:
        get_data(symbol)

    # Read stock data from CSV
    df = read_data(symbols, dates)

    print(df.head())

    # Plot by default
    # plot_data(df)

    """
    1. loc gets rows (or columns) with particular labels from the index.
    2. iloc gets rows (or columns) at particular positions in the index
        (so it only takes integers).
    3. ix usually tries to behave like loc but falls back to
        behaving like iloc if a label is not present in the index.
    """
    # df.ix['2020-01-01':'2020-01-31']  # the month of January

    # print('from 2020-01-01 to 2020-01-31')
    # print(df.loc['2020-01-01':'2020-01-31'])  # the month of January

    # Slice by column (symbols)
    # print(df['GOOG'].head())# a single label selects a single column

    # a list of labels selects multiple columns
    # print(df[['IBM', 'GLD']].head())

    # Slice by row and column
    # print(df.ix['2010-03-01':'2010-03-15', ['SPY', 'IBM']])
    # print(df.loc['2020-03-01':'2020-03-15', ['SPY', 'IBM']])

    # Slice and plot
    plot_selected(df,
                  ['SPY', 'GOOG', 'IBM', 'GLD', 'AAPL', 'MSFT', 'FB', 'CRM'],
                  '2020-01-01', '2020-12-31')


if __name__ == "__main__":
    # symbols list
    # We can add and delete any symbol from the list
    # to get desired symbol live data
    symbol_list = ['DJIA', 'DOW', 'SPY', 'GOOG', 'IBM', 'GLD',
                   'TSLA', 'AAPL', 'MSFT', 'FB', 'CRM']

    # get today date , include this value in the CSV file name
    today = date.today()

    # get S&P 500 symbol list frmo wiki, and save to a csv file
    get_and_save_symbol_list_SPY500()

    # We can get data by our choice by giving days bracket
    # select the input date and also convert to date format
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2020, 12, 31)

    files = []

    test_run()
