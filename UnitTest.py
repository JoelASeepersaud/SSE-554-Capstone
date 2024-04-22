import unittest
from BST import BST, TreeNode, getDataToBST
from Options import getConfigurations
import pandas as pd

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

    def testBSTCreation(self):
        self.assertTrue(isinstance(self.testBST, BST))
        self.assertIsNotNone(self.testBST.root)

    def testBSTInsert(self):
        testNode = TreeNode(self.emptyDf, None)
        self.testBST.insert(testNode)
        self.assertIn(testNode, self.testBST)

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