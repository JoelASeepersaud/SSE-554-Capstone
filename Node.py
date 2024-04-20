#Node class that can be used or be an abstract method to extend
class Node(object): 
    def __init__(self, dataFrame, row):
        self.ticker = dataFrame.loc[row,"ticker"]
        self.open = dataFrame.loc[row,"open"]
        self.high = dataFrame.loc[row,"high"]
        self.low = dataFrame.loc[row,"low"]
        self.close = dataFrame.loc[row,"close"]
        self.volume = dataFrame.loc[row,"volume"]
        self.percent_change = (self.close - self.open)/ self.open