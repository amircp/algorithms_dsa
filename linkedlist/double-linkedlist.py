class Node:
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoubleLinkedList:

    def __init__(self):
        self.parent = None

    def push(self, new_val):
        new_node = Node(new_val)

        if self.parent is not None:
            self.parent.prev_node = new_node
        self.parent = new_node

    def walkthough(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next_node


list = DoubleLinkedList()
list.push(1)
list.push(2)
list.push(3)

list.walkthough(list.parent)