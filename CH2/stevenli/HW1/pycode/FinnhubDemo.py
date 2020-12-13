import finnhub


# setup client
finnhub_client = finnhub.Client(api_key="bv4f2qn48v6qpatdiu3g")

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

#Convert to Pandas Dataframe
import pandas as pd
print(pd.DataFrame(res))

#Aggregate Indicators
#print(finnhub_client.aggregate_indicator('AAPL', 'D'))

#Basic financials
print(finnhub_client.company_basic_financials('AAPL', 'margin'))

# Earnings surprises
#print(finnhub_client.company_earnings('TSLA', limit=5))

# EPS estimates
#print(finnhub_client.company_eps_estimates('AMZN', freq='quarterly'))

# Company Executives
#print(finnhub_client.company_executive('AAPL'))

# Company News
# Need to use _form instead of form to avoid conflicit
#print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))
