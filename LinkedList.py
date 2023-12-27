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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True

        # If length is more than 1
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return True

    def get(self, index):

        # Check if index is valid
        if index < 0 or index >= self.length:
            return "None"

        # At last index
        if index == self.length - 1:
            return self.tail

        # Between 0th and last index
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):

        # Check if index is valid
        if index < 0 or index >= self.length:
            return "None"

        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return self.__str__()

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "None"

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):

        if index < 0 or index >= self.length:
            return "None"

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return True

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
print("Prepending nodes...")
add_value = 1
ll.prepend(add_value)
print(f"After prepending {add_value}: {ll}")
add_value = 11
ll.prepend(add_value)
print(f"After prepending {add_value}: {ll}")
print(f"Checking pop-first...")
ll.pop_first()
print(ll)
ll.append(123)
ll.append(234)
print("Checking get() call...")
print("List before get() call:", ll)
print(f"At 0th index: {ll.get(0)}")
print(f"When index equals length: {ll.get(ll.length)}")
print(f"At 2nd index: {ll.get(2)}")
print("Checking set_value() call..")
print(ll.set_value(1, 23))
print("Checking insert() call...")
ll.insert(3, 333)
print("After inserting 333 at 3:", ll)
ll.insert(2, 222)
print("After inserting 222 at 2:", ll)
ll.insert(4, 444)
print("After inserting 444 at 4:", ll)
print("Checking remove() call...")
print("Removing from 0th index:", ll.remove(0), ll)
print("Removing from Linked List length:", ll.remove(ll.length), ll)
print("Removing from last:", ll.remove(ll.length - 1), ll)
print("Removing from 2nd index:", ll.remove(1), ll)
print("Checking reverse() call...")
print("Before reverse:", ll)
print("After reverse:", ll.reverse(), ll)
