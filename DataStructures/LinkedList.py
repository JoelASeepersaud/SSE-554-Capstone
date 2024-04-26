from Node import Node

#Unit 8 : Queues
#Tests located in UnitTest.py

#DoubleLinkedNode:  Class that is used by the DoubleLinkedList class and inherits from the Node class
class DoubleLinkedNode(Node):
    def __init__(self, dataFrame, row):
        super().init(dataFrame, row)
        self.behind = None
        self.ahead = None

#--------------------------------------------------------------------------------------------------

#DoubleLinkedList:     Class that uses the DoubleLinkedNode class to create a linked list
class DoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = None

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
        
    def push(self, node: DoubleLinkedNode):
        if self.isEmpty():
            self.head = node
            self.tail = node
        self.tail.next = node
        node.previous = self.tail
        node = self.tail
        self.size += 1

    def __contains__(self):
        #Will implement when we know how we will use this
        raise NotImplementedError()

    def remove(self, value):
        raise NotImplementedError()

    def insert(self, value, position):
        raise NotImplementedError()
    
#--------------------------------------------------------------------------------------------------

#Helper:    Function that moves data to LinkedList      *Still to be implemented   
def getDataToLL():
    pass