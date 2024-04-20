import Node
from DataHandle import cleanDataAll, client
import pandas as pd

class TreeNode(Node): #TreeNode class that currently only will sort alphabetically
    def __init__(self, dataFrame, row, sortType):
        super().__init__(dataFrame, row)
        self.left = None
        self.right = None
        self.sortType = sortType

    def insert(self, node):
        if not type(node) is TreeNode:
            raise TypeError("Only TreeNodes are allowed")
        
        if self.sortType == 'alphabetical':
            if node.ticker < self.ticker:
                if self.left:
                    self.left.insert(node)
                else:
                    self.left = node
            else:
                if self.right:
                    self.right.insert(node)
                else:
                    self.right = node

def printInorder(root: TreeNode):
    if root is None:
        return
    printInorder(root.left)
    print(root.ticker)
    printInorder(root.right)       

def getDataToBST(configurations, sortType):
    if configurations['date'] == '':
        configurations['date'] = '2023-01-03'

    if configurations['volume_min'] == -1:
        configurations['volume_min'] = 100000

    data = pd.DataFrame(client.get_grouped_daily_aggs(configurations['date']))
    cleanDataAll(data, configurations['volume_min'])
    root = TreeNode(data, 0, sortType)

    for x in range(1, len(data.index), 1):
        root.insert(TreeNode(data, x, sortType))

    return root

def main():#Just for testing
    configurations ={'date': '',
                    'volume_min': -1,
                    }
    root = getDataToBST(configurations, 'alphabetical')

    printInorder(root)

if __name__ == '__main__':
    main()