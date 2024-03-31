#pip install polygon-api-client
#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
#api key denoted in polygonAPIkey.py
from polygonAPIkey import polygonAPIkey

# create client with API key 
client = RESTClient(polygonAPIkey)

class Node(object): #Node class that can be used or be an abstract method to extend
    def __init__(self, dataFrame, row):
        self.ticker = dataFrame.loc[row,"ticker"]
        self.open = dataFrame.loc[row,"open"]
        self.high = dataFrame.loc[row,"high"]
        self.low = dataFrame.loc[row,"low"]
        self.close = dataFrame.loc[row,"close"]
        self.volume = dataFrame.loc[row,"volume"]
        self.percent_change = (self.close - self.open)/ self.open

class TreeNode(Node): #TreeNode class that currently only will sort alphabetically
    def __init__(self, dataFrame, row, sortType):
        super().__init__(dataFrame, row)
        self.left = None
        self.right = None
        self.sortType = sortType

    def insert(self, node):
        if not type(node) is TreeNode:
            raise TypeError("Only TreeNodes are allowed")
        
        if self.sortType == 'alphabetical':
            if node.ticker < self.ticker:
                if self.left:
                    self.left.insert(node)
                else:
                    self.left = node
            else:
                if self.right:
                    self.right.insert(node)
                else:
                    self.right = node

def printInorder(root: TreeNode):
    if root is None:
        return
    printInorder(root.left)
    print(root.ticker)
    printInorder(root.right)       

def getDataToBST(configurations, sortType):
    if configurations['date'] == '':
        configurations['date'] = '2023-01-03'

    if configurations['volume_min'] == -1:
        configurations['volume_min'] = 100000

    data = pd.DataFrame(client.get_grouped_daily_aggs(configurations['date']))
    cleanDataAll(data, configurations['volume_min'])
    root = TreeNode(data, 0, sortType)

    for x in range(1, len(data.index), 1):
        root.insert(TreeNode(data, x, sortType))

    return root

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


def main():#Just for testing
    configurations ={'date': '',
                    'volume_min': -1,
                    }
    root = getDataToBST(configurations, 'alphabetical')

    printInorder(root)

if __name__ == '__main__':
    main()