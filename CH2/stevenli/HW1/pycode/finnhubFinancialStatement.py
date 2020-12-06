import requests

r = requests.get('https://finnhub.io/api/v1/stock/financials?symbol=AAPL'
                 '&statement=bs&freq=annual&token=bv4f2qn48v6qpatdiu3g')

print(r)