#pip install polygon-api-client
#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
from Configurations import getPolygonAPIkey

# create client with API key 
client = RESTClient(getPolygonAPIkey())

def cleanDataSingle(dataFrame):
    #Convert UNIX timestamps to milliseconds
    dataFrame['Date'] = dataFrame['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000)) 
    #Clean up dataframe
    dataFrame = dataFrame.set_index('Date')
    dataFrame.drop(columns = ['vwap', 'otc', 'timestamp', 'transactions'], axis=1, inplace=True)
    return dataFrame
    """cleanDataSingle(pd.DataFrame(client.get_aggs("AAPL",
        1,
        "minute",
        "2022-01-01",
        "2023-02-03",
        limit=10,)))"""

def cleanDataAll(dataFrame, volumeMin):
    for x in dataFrame.index:
        if dataFrame.loc[x, "volume"] <  volumeMin:
            dataFrame.drop(x, inplace = True)
    dataFrame.drop(columns = ['vwap', 'otc', 'timestamp', 'transactions'], axis=1, inplace=True)
    dataFrame.reset_index(drop=True, inplace=True)
    """
    test = pd.DataFrame(client.get_grouped_daily_aggs("2023-03-16"))
    cleanDataAll(test, 10000)
    print (test)
    """

"""
Examples:

Single Stock:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-aggregates_bars.py

Open and Closes Single Stock:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-daily_open_close.py

Get All Stocks:
https://github.com/polygon-io/client-python/blob/master/examples/rest/stocks-grouped_daily_bars.py
"""


