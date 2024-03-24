#pip install polygon-api-client
#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd

#api key denoted in polygonAPIkey.py
from polygonAPIkey import polygonAPIkey

# create client with API key 
client = RESTClient(polygonAPIkey)

def cleanDataSingle(dataFrame):
    #Convert UNIX timestamps to milliseconds
    dataFrame['Date'] = dataFrame['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000)) 
    #Clean up dataframe
    dataFrame = dataFrame.set_index('Date')
    dataFrame.drop(columns = ['vwap', 'otc', 'timestamp', 'transactions'], axis=1, inplace=True)
    return dataFrame

"""
print(cleanDataSingle(client.get_aggs("AAPL",
    1,
    "minute",
    "2022-01-01",
    "2023-02-03",
    limit=10,)))

Examples:

Single Stock:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-aggregates_bars.py

Open and Closes Single Stock:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-daily_open_close.py

Get All Stocks:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-grouped_daily_bars.py
"""

