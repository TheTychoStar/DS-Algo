# This is my first python module for finnhub, websocket
# Follow the sample code of Trades _ Last Price updates

import requests

r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bv4f2qn48v6qpatdiu3g')

print(r.json())