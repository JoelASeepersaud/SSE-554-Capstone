#pip install polygon-api-client
#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd

#api key denoted in polygonAPIkey.py
from polygonAPIkey import polygonAPIkey

# create client with API key 
client = RESTClient(polygonAPIkey)

def getStockData(stockTicker, _multiplier, timeWindow, _from, _to, candleLimit):
    
    """
    stockTicker: Ticker symbol for stock. ex. 'APPL'
    _multiplier: Multiplies with timeWindow. ex. multiplier = 5 & timeWindow = 'minutes' will be 5 minute candles
    timeWindow: Candle time window. Acceptable: second, minute, hour, day, week, month, quarter, year
    _from: Start date in YYYY-MM-DD or millisecond timestamp
    to: End date in YYYY-MM-DD or millisecond timestamp
    candleLimit: Max number of candles
    """
    #Bar Request
    testRequest = client.get_aggs(ticker = stockTicker,
                              multiplier = _multiplier,
                              timespan = timeWindow,
                              from_ = _from,
                              to = _to,
                              limit = candleLimit)
    returnedData = pd.DataFrame(testRequest)
    #Convert UNIX timestamps to milliseconds
    returnedData['Date'] = returnedData['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000)) 
    #Clean up dataframe
    returnedData = returnedData.set_index('Date')
    returnedData.drop(columns = ['vwap', 'otc', 'timestamp'], axis=1, inplace=True)
    return returnedData
print(getStockData('AAPL', 1, 'day', '2023-10-01', '2100-01-01', 5))