import unittest
from DataStructures.Configurations import getConfigurations
from DataStructures.Node import Node
from DataStructures.BST import BST, TreeNode, getDataToBST
from DataStructures.LinkedList import DoubleLinkedList
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue
from DataStructures.HashTable import HashTable, getDataToHash
from DataStructures.Graph import Graph, createGraph
import pandas as pd

#--------------------------------------------------------------------------------------------------

#Unit 4 : Linked List Test Cases
class TestLinkedList(unittest.TestCase): 
    def setUp(self):
        self.lLyst = DoubleLinkedList()
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]
        for item in self.text_list:
            self.lLyst.push(item)
        self.testPush = ('TEST', '2', '1', '50%', '5/2/2024')
            
    def testLLCreation(self):
        self.assertTrue(isinstance(self.lLyst, DoubleLinkedList))

    def testLLPush(self):
        self.assertFalse(self.lLyst.isEmpty())

    def testLLGet(self):
        self.assertEqual(self.lLyst.getItem(4), self.text_list[4])
        
    def testLLinsert(self):
        self.lLyst.insert(self.testPush, 4)
        self.assertEqual(self.lLyst.getItem(4), self.testPush)
        
    def testLLisEmpty(self):
        self.testEmpty = DoubleLinkedList()
        self.assertTrue(self.testEmpty.isEmpty())

#--------------------------------------------------------------------------------------------------

#Unit 7 : Stack Test Cases
class TestStack(unittest.TestCase): 
    def setUp(self):
        self.stack = Stack()
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]
        for item in self.text_list:
            self.stack.push(item)

    def testStackCreation(self):
        self.assertTrue(isinstance(self.stack, Stack))

    def testStackPushPop(self):
        passFlag = False
        testPush = ('TEST', '2', '1', '50%', '5/2/2024')
        self.stack.push(testPush)
        testPop = self.stack.pop()
        if testPush == testPop.data:
            passFlag = True
        self.assertTrue(passFlag)

    def testStackPeek(self):
        self.assertTrue(isinstance(self.stack.pop().data, tuple))

    def testStackisEmpty(self):
        self.testEmpty = Stack()
        self.assertTrue(self.testEmpty.isEmpty())

#--------------------------------------------------------------------------------------------------

#Unit 8 : Queue Test Cases
class TestQueue(unittest.TestCase): 
    def setUp(self):
        self.queue = Queue()
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]

    def testQueueCreation(self):
        self.assertTrue(isinstance(self.queue, Queue))

    def testQueueisEmpty(self):
        self.queue1 = Queue()
        self.assertTrue(self.queue1.isEmpty())

    def testQueuePushPopPeek(self):
        for item in self.text_list:
            self.queue.push(item)
        self.assertFalse(self.queue.isEmpty())
        self.assertTrue(isinstance(self.queue.pop(), tuple))
        self.assertTrue(isinstance(self.queue.peek().data, tuple))
    

#--------------------------------------------------------------------------------------------------

#Unit 10 : Tree Test Cases
class TestBST(unittest.TestCase): 
    def setUp(self):
        self.testBST = getDataToBST('alphabetical')

    def testBSTCreation(self):
        self.assertTrue(isinstance(self.testBST, BST))
        self.assertIsNotNone(self.testBST.root)

    def testBSTInsert(self):
        self.assertFalse(self.testBST.isEmpty())
        

    def testBSTTrav(self):
        lyst = self.testBST.inorderTrav()
        self.assertTrue(lyst[0].ticker <= lyst[1].ticker)
        self.assertTrue(lyst[2].ticker <= lyst[3].ticker)

    def testBSTStr(self):
        stringBST = str(self.testBST)
        self.assertIsInstance(stringBST, str)

#--------------------------------------------------------------------------------------------------

#Unit 11 : HashTable Test Cases
class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hashtable = HashTable()
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]
        for item in self.text_list:
            self.hashtable[item[0]] = item
    
    def testisEmpty(self):
        self.EmptyHash = HashTable()
        self.assertTrue(self.EmptyHash.isEmpty())
        
    def testSetItem(self):
        self.assertFalse(self.hashtable.isEmpty())
        
    def testContains(self):
        self.assertTrue(self.text_list[2][0] in self.hashtable)
        
    def testClear(self):
        self.hashtable.clear()
        self.assertTrue(self.hashtable.isEmpty())
        
    def testGetItem(self):
        self.assertEqual(self.hashtable[self.text_list[4][0]], self.text_list[4])
        
    def testResize(self):
        oldCap=self.hashtable.capacity
        self.hashtable.resize()
        self.assertEqual(oldCap*2, self.hashtable.capacity)
        self.assertEqual(self.hashtable[self.text_list[4][0]], self.text_list[4])
        
    def testGetItems(self):
        self.Search = getDataToHash()
        search = 'AA'
        result = [self.Search['AAL'], self.Search['AAPL']]
        self.assertEqual(self.Search.getItems(search), result)

#--------------------------------------------------------------------------------------------------

#Unit 11 : Graph Test Cases
class TestGraphTable(unittest.TestCase):
    def setUp(self):
        self.graph = createGraph()
    
    def testGraphCreation(self):
        self.assertTrue(isinstance(self.graph, Graph))
        self.assertTrue(self.graph.nodes)
        self.assertTrue(self.graph.edges)

    def testGetMethods(self):
        self.assertTrue(isinstance(self.graph.nodes, list))
        self.assertTrue(isinstance(self.graph.edges, list))

    def testRestMarks(self):
        for item in self.graph.edges:
            item.mark = True

        self.graph.resetMarks()

        for item in self.graph.edges:
            self.assertFalse(item.mark)

    def testCompleteGraph(self):
        self.graph.createCompleteGraph
        self.assertTrue(len(self.graph.edges) > len(self.graph.nodes))

    def testBFS(self):
        lyst = self.graph.breadthSearchCorrelation()
        self.assertTrue(isinstance(lyst, list))
        self.assertTrue(isinstance(lyst[0], tuple))
        self.assertTrue(len(lyst[0]) == 3)

if __name__ == '__main__':
    unittest.main()