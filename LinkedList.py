"""
Linked List
"""


class Node:
    """
    Create Nodes
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Creates a Linked List.
    Performs operations such as append, prepend, insert.
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = None
        self.length = 1

    def append(self):
        pass

    def prepend(self):
        pass

    def insert(self, index, value):
        pass


ll = LinkedList(4)
print(f"Head: {ll.head.value}, Tail: {ll.tail}, Next node: {ll.head.next}, Length: {ll.length}")
