#Node class that can be used or be an abstract method to extend
class Node(object): 
    def __init__(self, dataFrame = None, row = None):
        if  not dataFrame.empty and row != None:
            self.ticker = dataFrame.loc[row,"ticker"]
            self.open = dataFrame.loc[row,"open"]
            self.high = dataFrame.loc[row,"high"]
            self.low = dataFrame.loc[row,"low"]
            self.close = dataFrame.loc[row,"close"]
            self.volume = dataFrame.loc[row,"volume"]
            self.percent_change = (self.close - self.open)/ self.open

        else:
            self.ticker = 'abc'
            self.open = 1234
            self.high = 12345
            self.low = 123
            self.close = 1245
            self.volume = 1000000
            self.percent_change = (self.close - self.open)/ self.open