import unittest
from Node import createTestNode
from BST import BST, TreeNode, getDataToBST
from Options import getConfigurations
import pandas as pd

#--------------------------------------------------------------------------------------------------

#Unit 4 : Linked List Test Cases
class TestLinkedList(unittest.TestCase): 
    def setUp(self):
        pass

    def testLLCreation(self):
        pass

    def testLLPush(self):
        pass

    def testLLisEmpty(self):
        pass

    def testLLContains(self):
        pass

    def testLLinsert(Self):
        pass

    def testLLremove(self):
        pass

#--------------------------------------------------------------------------------------------------

#Unit 7 : Stack Test Cases
class TestStack(unittest.TestCase): 
    def setUp(self):
        pass

    def testStackCreation(self):
        pass

    def testStackPush(self):
        pass

    def testStackPop(self):
        pass

    def testStackPeek(self):
        pass

    def testStackisEmpty(self):
        pass

#--------------------------------------------------------------------------------------------------

#Unit 8 : Queue Test Cases
class TestQueue(unittest.TestCase): 
    def setUp(self):
        pass

    def testQueueCreation(self):
        pass

    def testQueuePush(self):
        pass

    def testQueuePop(self):
        pass

    def testQueuePeek(self):
        pass

    def testQueueisEmpty(self):
        pass

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


if __name__ == '__main__':
    unittest.main()