#Unit 7 : Stacks
#Tests located in UnitTest.py

#StackNode:  Class that is used by the Stack class
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#--------------------------------------------------------------------------------------------------

#Stack:     Class that uses the StackNode class to create a linked stack
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = StackNode(data)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty(): raise KeyError("Queue is Empty")
        returnNode= self.head
        self.head = self.head.next
        self.size -= 1
        return returnNode
    
    def peek(self):
        if self.isEmpty(): raise KeyError("Queue is Empty")
        return self.head.data[0]

    def isEmpty(self):
        if self.size != 0: return False
        return True

