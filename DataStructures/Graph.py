from DataStructures.Node import Node
from DataStructures.Queue import Queue
from DataStructures.dataHandle import cleanDataAll, client
from DataStructures.Configurations import getConfigurations
import pandas as pd

class GraphNode(Node):
    def __init__(self, dataFrame, row):
        super().__init__(dataFrame, row)

    def __str__(self):
        return self.ticker
    
    def nodeHandle(self):
        thisTuple = (self.ticker, self.open, self.close, self.percentChange, self.volume)
        return thisTuple

class GraphEdge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.positive = True
        self.mark = False
        if weight < 0: self.postive = False
        self.weight = round(abs(weight), 3)

    def edgeHandle(self):
        return (self.start.ticker, self.end.ticker, self.weight)
    


class Graph:

    data = pd.DataFrame(client.get_grouped_daily_aggs(getConfigurations()[0][1]))
    configurations = getConfigurations()[1][1]
    if configurations > 10000000:
        configurations = 100000000
    cleanDataAll(data, configurations)

    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def addEdge(self, startNode, endNode):
        if startNode in self.nodes and endNode in self.nodes:
            start = startNode
            end = endNode
            weight = start.percentChange - end.percentChange
            newEdge = GraphEdge(start, end, weight)
            self.edges.append(newEdge)
        else:
            print("At least one node is not in the graph.")

    def getAllNodes(self):
        return self.nodes
    
    def getAllEdges(self):
        return self.edges
    
    def resetMarks(self):
        for item in self.edges:
            item.mark = False
    
    def createCompleteGraph(self):
        if self.edges: self.edges = []
        for outerIndex in range(len(self.nodes)):
            for innerIndex in range(outerIndex + 1, len(self.nodes), 1):
                self.addEdge(self.nodes[outerIndex], self.nodes[innerIndex])

    #Will only show 2 correlations
    def breadthSearchCorrelation(self):
        CORRELATIONS = 2
        queue= Queue()
        returnList = list()
        self.itemCount = {}
        self.resetMarks()
        
        for item in self.nodes:
            self.itemCount[item.ticker] = 0
        queue.push(self.nodes[0])

        while not queue.isEmpty():
            currentNode = queue.pop()
            for item in self.edges:
                if item.start.ticker == currentNode.ticker or item.end.ticker == currentNode.ticker:
                    if item.mark is False:
                        if item.start.ticker == currentNode.ticker:
                            queue.push(item.end)
                            if self.itemCount[currentNode.ticker] < CORRELATIONS:
                                if item.weight <= .01:
                                    returnList.append(item.edgeHandle())
                                    self.itemCount[currentNode.ticker] += 1
                        else:
                            queue.push(item.start)
                        item.mark = True

        return returnList

def createGraph():
    graph = Graph()
    for x in range(1, len(Graph.data.index), 1):
        graph.addNode(GraphNode(Graph.data, x))
    graph.createCompleteGraph()
    return graph



                            

        




