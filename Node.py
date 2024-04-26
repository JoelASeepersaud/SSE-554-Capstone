import pandas as pd
import random

class Node(object): 
    def __init__(self, dataFrame = None, row = None):
        if  not dataFrame.empty and row != None:
            self.ticker = dataFrame.loc[row,"ticker"]
            self.open = dataFrame.loc[row,"open"]
            self.high = dataFrame.loc[row,"high"]
            self.low = dataFrame.loc[row,"low"]
            self.close = dataFrame.loc[row,"close"]
            self.volume = dataFrame.loc[row,"volume"]
            self.percentChange = (self.close - self.open)/ self.open

        else:
            self.ticker = None
            self.open = None
            self.high = None
            self.low = None
            self.close = None
            self.volume = None
            self.percent_change = None


def createTestNode():
    emptyDf = pd.DataFrame()
    returnNode1 = Node(emptyDf, None)
    returnNode2 = Node(emptyDf, None)
    returnNode3 = Node(emptyDf, None)
    returnNode4 = Node(emptyDf, None)
    returnNode5 = Node(emptyDf, None)

    nodeList = [returnNode1, returnNode2, returnNode3, returnNode4, returnNode5]

    for item in nodeList:
        item.ticker = chr(random.randint(ord('A'), ord('Z')))
        item.open = random.randint(1, 1001)
        item.high = random.randint(1, 1001)
        item.low = random.randint(1, 1001)
        item.close = random.randint(1, 1001)
        item.volume = random.randint(1, 1001)
        item.percentChange = abs((item.close - item.open)/ item.open)

    return nodeList