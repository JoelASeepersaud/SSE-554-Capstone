from DataStructures.BST import getDataToBST
from DataStructures.Stack import Stack
from DataStructures.HashTable import getDataToHash
from DataStructures.Graph import createGraph

alphBST     = getDataToBST('alphabetical')
openBST     = getDataToBST('open')
closeBST    = getDataToBST('close')
percentBST  = getDataToBST('percent')
volumeBST   = getDataToBST('volume')

watchListStack = Stack()

searchStock = getDataToHash()

correlationGraph = createGraph()
