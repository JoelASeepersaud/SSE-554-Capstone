from Node import Node

class GraphNode(Node):
    def __init__(self, dataFrame, row):
        super().init(dataFrame, row)
        self.key = self.ticker

    def __str__(self):
        return self.key

class GraphEdge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
        self.mark = False

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def addNode(self, node):
        if node.key not in self.nodes:
            self.nodes[node.key] = node

    def addEdge(self, startNode, endNode):
        if startNode.key in self.nodes and endNode.key in self.nodes:
            start = startNode
            end = endNode
            weight = abs(start.percentChange - end.percentChange) 
            newEdge = GraphEdge(start, end, weight)
            self.edges.append(newEdge)
        else:
            print("At least one node is not in the graph.")

    def getAllNode(self):
        return list(self.nodes.values)
    
    def getAllEdges(self):
        return self.edges