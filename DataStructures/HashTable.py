from DataStructures.Node import Node
from DataStructures.dataHandle import cleanDataAll, client
import pandas as pd
from Options import getConfigurations

#Unit 10 : HashTable
#Tests located in UnitTest.py

#HashTableNode:  Class that is used by the HashTable class and inherits from the Node class
class HashTableNode(Node):
    def __init__(self, dataFrame, row):
        super().__init__(dataFrame, row)
        
    def nodeHandle(self):
        thisTuple = (self.ticker, self.open, self.close, self.percentChange, self.volume)
        return thisTuple

class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#--------------------------------------------------------------------------------------------------       
#dictionary entry
class Entry(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key

#--------------------------------------------------------------------------------------------------
#HashTable using keys in a dictionary 
class HashTable:
    
    data = pd.DataFrame(client.get_grouped_daily_aggs(getConfigurations()[0][1]))
    cleanDataAll(data, getConfigurations()[1][1])
    HashCap = 160
    
    def __init__(self, capacity = HashCap):
        self.keys = []
        self.capacity = capacity
        self.table=[]
        for i in range(self.capacity):
            self.table.append(None)
        self.foundNode = self.priorNode = None
        self.index = -1
        self.size = 0

    # Accessors
    def __contains__(self, key):
        self.index = abs(hash(key)) % len(self.table)
        self.priorNode = None
        self.foundNode = self.table[self.index]
        while self.foundNode != None:
            if self.foundNode.data.key == key: 
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False
    
    def clear(self):
        self.foundNode = self.priorNode = None
        self.index = -1
        self.table=[]
        for i in range(self.capacity):
            self.table.append(None)
        self.size = 0
        self.keys = []

    def __setitem__(self, key, value):
        while self.size == len(self.table):
            self.resize()
        if key in self: 
            self.foundNode.data.value = value
        else:
            newNode = node(Entry(key, value), self.table[self.index])
            self.table[self.index] = newNode
            self.size += 1
            self.keys.append(key)
            
    def resize(self):
        temp = self.table
        cap = len(self.table)
        self.capacity = cap * 2
        self.clear()
        self.table = []
        for i in range(self.capacity):
            self.table.append(None)
        
        for i in range(len(temp)):
            if temp[i]!=None:
                self.__setitem__(temp[i].data.key, temp[i].data.value)
    
    def __getitem__(self, key):
        if not key in self: return None
        return self.foundNode.data.value
    
    def getItems(self, key):
        similarKeys = []
        items = []
        for item in self.keys:
            if key in item[:len(key)]:
                similarKeys.append(item)
                
        if len(similarKeys) == 0: return None
        
        similarKeys.sort()
        for item in similarKeys:
            items.append(self.__getitem__(item))
        return items

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
        
#--------------------------------------------------------------------------------------------------
#create and fill hashtable
def getDataToHash():
    hashtable = HashTable()
    for x in range(0, len(hashtable.data.index), 1):
        temp = HashTableNode(hashtable.data, x)
        temp.nodeHandle()
        hashtable[temp.ticker] = HashTableNode(hashtable.data, x)
    return hashtable