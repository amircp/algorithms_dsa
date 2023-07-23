"""
    Practicing Linked Lists
"""


class Node:

    def __init__(self, name, next_node=None):
        self.name = name
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.parent_node = None

    def walk_trough(self):
        next_val = self.parent_node

        while next_val is not None:
            print(next_val.name)
            next_val = next_val.next_node

    def insert_new_head(self, name):
        new_node = Node(name)
        new_node.next_node = self.parent_node
        self.parent_node = new_node

    def insert_new_element(self, name):
        new_node = Node(name)
        if self.parent_node is None:
            self.parent_node = new_node

        element_node = self.parent_node
        while element_node.next_node:
            element_node = element_node.next_node
        element_node.next_node = new_node

    def insert_between(self, middle_node, new_node):
        if middle_node is None:
            print("Next node doesn't exists")
            return

        new_node = Node(new_node)
        new_node.next_node = middle_node.next_node
        middle_node.next_node = new_node


node1 = Node('Monday')
node2 = Node('Tuesday')
node3 = Node('Wednesday')
node4 = Node('Tuesday')
node5 = Node('Friday')

list = LinkedList()
list.parent_node = node1
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5

list.insert_new_element('Saturday')
list.insert_between(node4.next_node, "A break will be fine")

list.walk_trough()
