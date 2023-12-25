"""
Linked List
"""


class Node:
    """
    Create Nodes.
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
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
            return True

        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        return True

    def prepend(self):
        pass

    def insert(self, index, value):
        pass

    def __str__(self):
        """
        Prints content of Linked List created.
        :return: String of Linked List values
        """
        ll_str = ""
        temp = self.head
        while temp is not None:
            ll_str += str(temp.value) + "-->"
            temp = temp.next

        return ll_str


ll = LinkedList(4)
print(f"Head: {ll.head.value}, Tail: {ll.tail.value}, Next node: {ll.head.next}, Length: {ll.length}")
print(f"Linked List: {ll}")
print("Adding new nodes...")
ll.append(1)
ll.append(2)
print(f"After appending new nodes: {ll}")
print("Removing all items from LL...")
ll.pop()
print(f"After 1st pop: {ll}")
ll.pop()
print(f"After 2nd pop: {ll}")
ll.pop()
print(f"After final pop: {ll}")
