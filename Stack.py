from Node import Node
from DataHandle import cleanDataAll, client
import pandas as pd
from Options import getConfigurations

#Unit 7 : Stacks
#Tests located in UnitTest.py

#StackNode:  Class that is used by the Stack class and inherit from the Node class
class StackNode(Node):
    def __init__(self, dataFrame, row):
        super().__init__(dataFrame, row)
        self.next = None

#--------------------------------------------------------------------------------------------------

#Stack:     Class that uses the StackNode class to create a linked stack
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, node: StackNode):
        if self.isEmpty():
            self.head = node
        else:
            self.head.next = node
            self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty(): raise KeyError("Queue is Empty")
        returnNode= self.head
        self.head = self.head.next
        return returnNode
    
    def peek(self):
        if self.isEmpty(): raise KeyError("Queue is Empty")
        return self.head

    def isEmpty(self):
        if self.size != 0: return False
        return True

#--------------------------------------------------------------------------------------------------

#Helper:    Function that moves data to Stack       *Still to be implemented   
def getDataToStack():
    pass