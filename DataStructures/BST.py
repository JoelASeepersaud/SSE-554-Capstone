from DataStructures.Node import Node
from DataHandle import cleanDataAll, client
import pandas as pd
from Options import getConfigurations

#Unit 10 : Trees
#Tests located in UnitTest.py

#TreeNode:  Class that is used by the BST class and inherits from the Node class
class TreeNode(Node):                
    def __init__(self, dataFrame, row):
        super().__init__(dataFrame, row)
        self.left = None
        self.right = None

    def nodeHandle(self):
        thisTuple = (self.ticker, self.open, self.close, self.percentChange, self.volume)
        return thisTuple

#--------------------------------------------------------------------------------------------------

#BST:       Class that uses the TreeNode class to create a binary search tree
class BST:

    data = pd.DataFrame(client.get_grouped_daily_aggs(getConfigurations()['date']))
    cleanDataAll(data, getConfigurations()['volume_min'])

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

        def insertNodeOpen(root, node):
            if node.open < root.open:
                if root.left:
                    insertNodeOpen(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insertNodeOpen(root.right, node)
                else:
                    root.right = node

        def insertNodeClose(root, node):
            if node.close < root.close:
                if root.left:
                    insertNodeClose(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insertNodeClose(root.right, node)
                else:
                    root.right = node
        
        def insertNodePercentChange(root, node):
            if node.percentChange > root.percentChange:
                if root.left:
                    insertNodePercentChange(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insertNodePercentChange(root.right, node)
                else:
                    root.right = node

        def insertNodeVolume(root, node):
            if node.volume < root.volume:
                if root.left:
                    insertNodeVolume(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insertNodeVolume(root.right, node)
                else:
                    root.right = node

        if not type(node) is TreeNode: raise TypeError("Only TreeNodes are allowed")
        if self.sortType == 'alphabetical' and node.ticker.isalpha():
            insertNodeAlph(self.root, node)
        elif self.sortType == 'open':
            insertNodeOpen(self.root, node)
        elif self.sortType == 'close':
            insertNodeClose(self.root, node)
        elif self.sortType == 'percent':
            insertNodePercentChange(self.root, node)
        elif self.sortType == 'volume':
            insertNodeVolume(self.root, node)
        
    def inorderTrav(self):
        def Inorder(root):
            if root is None: return
            Inorder(root.left)
            returnList.append(root)
            Inorder(root.right) 
        returnList = list()
        Inorder(self.root)
        return returnList
    
    def __str__(self):
        returnSTR = ""
        lyst = self.inorderTrav()
        for item in lyst:
            returnSTR += f"\n{item.ticker}, {item.open}, {item.close}"
        return returnSTR
        
    
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
def getDataToBST(sortType):
    root = TreeNode(BST.data, 0)
    bst = BST(root, sortType)
    for x in range(1, len(BST.data.index), 1):
        bst.insert(TreeNode(BST.data, x))
    return bst
