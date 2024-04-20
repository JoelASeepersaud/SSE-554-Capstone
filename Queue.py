from Node import Node

class QueueNode(Node):
    def __init__(self, dataFrame, row):
        super().init(dataFrame, row)
        self.ahead = None
        self.behind = None

class Queue():
    def __init__(self, head : QueueNode = None):
        self.head = head
        self.tail = head
        self.is_empty = False

    def _push(self, Node : QueueNode):
        if self.is_empty == False:
            self.tail.behind = Node
            Node.ahead = self.tail
            self.tail = Node
        else:
            self.head, self.tail = Node
            self.is_empty = False

    def _pop(self):
        if self.is_empty: raise KeyError("The Queue is empty!")
        pop_node = self.head
        self.head = self.head.behind
        self.head.ahead = None
        return pop_node

    def _peek(self):
        if self.is_empty: raise KeyError("The Queue is empty!")
        return self.head        




def main():#Just for testing
    pass

if __name__ == '__main__':
    main()