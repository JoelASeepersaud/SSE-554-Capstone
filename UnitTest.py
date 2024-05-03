import unittest
from DataStructures.Configurations import getConfigurations
from DataStructures.Node import Node
from DataStructures.BST import BST, TreeNode, getDataToBST
from DataStructures.LinkedList import DoubleLinkedList
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue
import pandas as pd

#--------------------------------------------------------------------------------------------------

#Unit 4 : Linked List Test Cases
"""class TestLinkedList(unittest.TestCase): 
    def setUp(self):
        self.lLyst = DoubleLinkedList()
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]

    def testLLCreation(self):
        self.assertTrue(isinstance(self.lLyst, DoubleLinkedList))

    def testLLisEmpty(self):
        self.assertTrue(self.lLyst.isEmpty())

    def testLLPush(self):
        for item in self.text_list:
            self.lLyst.push(item)
        self.assertFalse(self.lLyst.isEmpty())

    def testLLinsert(self):
        self.testPush = ('TEST', '2', '1', '50%', '5/2/2024')
        self.lLyst.insert(self.testPush, 4)

    def testLLGet(self):
        self.assertEqual(self.lLyst.getItem(3), self.testPush)"""

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
        self.assertTrue(isinstance(self.queue.pop().data, tuple))
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

if __name__ == '__main__':
    unittest.main()