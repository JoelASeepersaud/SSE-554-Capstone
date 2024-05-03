import unittest
from Configurations import getConfigurations
from Node import createTestNode
from BST import BST, getDataToBST
from LinkedList import DoubleLinkedList
from Stack import Stack
from Queue import Queue
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
        self.text_list = [('1 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024'), ('6 S&P500', '2', '1', '50%', '5/2/2024'), ('7 S&P500', '2', '1', '50%', '5/2/2024'), ('8 S&P500', '2', '1', '50%', '5/2/2024'), ('9 S&P500', '2', '1', '50%', '5/2/2024'), ('2 S&P500', '2', '1', '50%', '5/2/2024'), ('3 S&P500', '2', '1', '50%', '5/2/2024'), ('4 S&P500', '2', '1', '50%', '5/2/2024'), ('5 S&P500', '2', '1', '50%', '5/2/2024')]

    def testQueueCreation(self):
        self.assertTrue(isinstance(self.queue, TestQueue))

    def testQueueisEmpty(self):
        self.assertTrue(self.queue.isEmpty())

    def testQueuePush(self):
        for item in self.text_list:
            self.stack.push(item)
        self.assertFalse(self.queue.isEmpty())

    def testQueuePop(self):
        self.assertTrue(isinstance(self.queue.pop(), tuple))

    def testQueuePeek(self):
        self.assertTrue(isinstance(self.queue.peek(), tuple))

    
"""
#--------------------------------------------------------------------------------------------------

#Unit 10 : Tree Test Cases
class TestBST(unittest.TestCase): 
    def setUp(self):
        self.testBST = getDataToBST(getConfigurations(), 'alphabetical')
        self.emptyDf = pd.DataFrame()
        self.testNodeList = createTestNode()

    def testBSTCreation(self):
        self.assertTrue(isinstance(self.testBST, BST))
        self.assertIsNotNone(self.testBST.root)

    def testBSTInsert(self):
        for item in self.testNodeList:
            self.testBST.insert(item)
        for item in self.testNodeList:
            self.assertIn(item, self.testBST)

    def testBSTTrav(self):
        lyst = self.testBST.inorderTrav()
        self.assertTrue(lyst[0] <= lyst[1])
        self.assertTrue(lyst[2] <= lyst[3])

    def testBSTStr(self):
        stringBST = str(self.testBST)
        self.assertIsInstance(stringBST, str)

#--------------------------------------------------------------------------------------------------

"""
if __name__ == '__main__':
    unittest.main()