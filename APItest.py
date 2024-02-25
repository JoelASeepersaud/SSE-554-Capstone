#pip install polygon-api-client
#pip install plotly

#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd

#api key denoted in polygonAPIkey.py
from polygonAPIkey import polygonAPIkey

# create client with API key 
client = RESTClient(polygonAPIkey)

stock = 'AAPL'

# daily bars
testRequest = client.get_aggs(ticker = stock, 
                              multiplier = 1,
                              timespan = 'day',
                              from_ = '2023-12-01',
                              to = '2100-01-01',
                              limit = 10)

returnedData = pd.DataFrame(testRequest)

print(returnedData)