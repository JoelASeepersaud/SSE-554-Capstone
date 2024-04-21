import unittest
from BST import BST, getDataToBST
from Options import configurations

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
        self.unitTestBST = getDataToBST(configurations, 'alphabetical')

    def testBSTCreation(self):
        testBST = getDataToBST(configurations, 'alphabetical')
        self.assertTrue(isinstance(testBST, BST))
        self.assertIsNotNone(testBST.root)

    def testBSTInsert(self):
        pass

    def testBSTTrav(self):
        pass

    def testBSTStr(self):
        pass

#--------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()