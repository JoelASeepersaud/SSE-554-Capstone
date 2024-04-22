from Node import Node
from DataHandle import cleanDataAll, client
import pandas as pd
from Options import getConfigurations

#Unit 10 : Trees
#Tests located in UnitTest.py

#TreeNode:  Class that is used by the BST class and inherit from the Node class
class TreeNode(Node):                
    def __init__(self, dataFrame, row):
        super().__init__(dataFrame, row)
        self.left = None
        self.right = None

#--------------------------------------------------------------------------------------------------

#BST:       Class that uses the TreeNode class to create a binary search tree
class BST:
    def __init__(self, root, sortType): 
        self.root = root
        self.sortType = sortType

    def insert(self, node): 
        def insertNodeAlph(root, node):
            if node.ticker < root.ticker:
                if root.left:
                    insertNodeAlph(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insertNodeAlph(root.right, node)
                else:
                    root.right = node

        if not type(node) is TreeNode: raise TypeError("Only TreeNodes are allowed")
        if self.sortType == 'alphabetical' and node.ticker.isalpha():
            insertNodeAlph(self.root, node)
        
    def inorderTrav(self):
        def Inorder(root):
            if root is None: return
            Inorder(root.left)
            returnList.append(root.ticker)
            Inorder(root.right) 
        returnList = list()
        Inorder(self.root)
        return returnList
    
    def __str__(self):
        return str(self.inorderTrav())
    
    def __iter__(self):
        lyst = self.inorderTrav()
        return iter(lyst)

    def __contains__(self, item):
        lyst = self.inorderTrav()
        if item.ticker in lyst:
            return True
        return False

    
#--------------------------------------------------------------------------------------------------
#Helper:    Function that moves data from API to the binary search tree    
def getDataToBST(configurations = getConfigurations(), sortType = None):
    if configurations['date'] == '':
        configurations['date'] = '2023-01-03'

    if configurations['volume_min'] == -1:
        configurations['volume_min'] = 10000000
    data = pd.DataFrame(client.get_grouped_daily_aggs(configurations['date']))
    cleanDataAll(data, configurations['volume_min'])
    root = TreeNode(data, 0)
    bst = BST(root, sortType)
    for x in range(1, len(data.index), 1):
        bst.insert(TreeNode(data, x))
    return bst
