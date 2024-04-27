from DataStructures.Node import Node
from DataHandle import cleanDataAll, client
import pandas as pd
from Options import getConfigurations

#Unit 8 : Queues
#Tests located in UnitTest.py

#QueueNode:  Class that is used by the Queue class and inherits from the Node class
class QueueNode(Node):
    def __init__(self, dataFrame, row):
        super().init(dataFrame, row)
        self.next = None

#--------------------------------------------------------------------------------------------------

#Queue:     Class that uses the QueueNode class to create a linked queue
class Queue():

    data = pd.DataFrame(client.get_grouped_daily_aggs(getConfigurations()['date']))
    cleanDataAll(data, getConfigurations()['volume_min'])

    def __init__(self):
        self.head, self.tail = None
        self.size = 0

    def __iter__(self):
        cursor = self.head
        while not cursor is None:
            yield cursor
            cursor = cursor.next

    def push(self, node : QueueNode):
        if self.is_empty(): self.head = node
        else: self.tail.next = node
        self.tail = node
        self.size += 1

    def pop(self):
        if self.isEmpty(): raise KeyError("The Queue is empty!")
        popNode = self.head
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty(): self.tail = None
        return popNode

    def peek(self):
        if self.isEmpty: raise KeyError("The Queue is empty!")
        return self.head        
    
    def isEmpty(self):
        if self.size != 0: return False
        return True

#--------------------------------------------------------------------------------------------------

#Helper:    Function that sorts data then moves to Queue
def sort():
    pass

def getDataToQueue():
    pass