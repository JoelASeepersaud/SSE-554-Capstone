#pip install polygon-api-client
#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
from DataStructures.Configurations import getPolygonAPIkey

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

def cleanDataAll(dataFrame, volumeMin):
    for x in dataFrame.index:
        if dataFrame.loc[x, "volume"] <  volumeMin:
            dataFrame.drop(x, inplace = True)
    dataFrame.drop(columns = ['vwap', 'otc', 'timestamp', 'transactions'], axis=1, inplace=True)
    dataFrame.reset_index(drop=True, inplace=True)



