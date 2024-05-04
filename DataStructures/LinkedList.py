
#Unit 4 and 9: LinkedList
#Tests located in UnitTest.py

#DoubleLinkedNode:  Class that is used by the DoubleLinkedList class
class DoubleLinkedNode():
    def __init__(self, data, next=None, previous=None):
        self.previous = previous
        self.next = next
        self.data = data

#--------------------------------------------------------------------------------------------------

#DoubleLinkedList:     Class that uses the DoubleLinkedNode class to create a linked list
class DoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
        
    def push(self, item):
        if self.isEmpty():
            self.head = DoubleLinkedNode(item)
            self.tail = self.head
        else:
            self.tail.next = DoubleLinkedNode(item, None, self.tail)
            self.tail=self.tail.next
        self.size += 1

    def insert(self, value, position):
        if self.isEmpty():
            self.push(value)
            
        elif position == 0:
            self.head = None
            self.size = 0
            self.push(value)
        else:
            cursor=self.head
            self.size=1
            for _ in range(position-1):
                cursor = cursor.next
                self.size+=1
            self.tail=cursor
            self.push(value)
            
    def getItem(self, position):
        cursor=self.head
        for _ in range(position):
            if cursor!= None:
                cursor=cursor.next
        return cursor.data
