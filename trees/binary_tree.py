"""
    Practicing Tree's Data structure.

"""

# Creating a node

class Node:

    def __init__(self, value):
        self.left_subtree = None
        self.right_subtree = None
        self.name = value


subtree_1 = Node('b')
subtree_2 = Node('c')
subtree_3 = Node('d')
subtree_4 = Node('e')
subtree_5 = Node('f')

root = Node('a')
root.left_subtree = subtree_1
root.right_subtree = subtree_2
subtree_2.left_subtree = subtree_3
subtree_2.right_subtree = subtree_4
subtree_4.left_subtree = subtree_5


def in_order(node):
    # InOrder: left, root, right
    if node:
        in_order(node.left_subtree)

        print(node.name,end=" ")

        in_order(node.right_subtree)

# print(f"InOrder search:")
# in_order(root)
# print("\r\n")

def pre_order(node):
    # InOrder: root, left, right
    if node:

        print(node.name, end=" ")
        pre_order(node.left_subtree)
        pre_order(node.right_subtree)

# print(f"PreOrder search:")
# pre_order(root)
# print("\r\n")



def post_order(node):
    # InOrder: left, right, root
    if node:

        post_order(node.left_subtree)
        post_order(node.right_subtree)
        print(node.name,end=" ")

# print(f"PostOrder search:")
# post_order(root)
# print("\r\n")


def preorder_iterative(root):
    stack = [root]
    while stack:

        current = stack.pop()
        print(current.name, end=" ")

        if current.right_subtree:
            stack.append(current.right_subtree)

        if current.left_subtree:
            stack.append(current.left_subtree)



print(f"Preorder iterative:")
preorder_iterative(root)
print("\r\n")


def inorder_iterative(root):
    current = root
    stack = []

    while True:
        if current:
            stack.append(current)
            current = current.left_subtree
        elif stack:
            current = stack.pop()
            print(current.name, end=" ")
            current = current.right_subtree
        else:
            break

#
#
print(f"Inorder iterative:")
inorder_iterative(root)
print("\r\n")
#


def postorder_iterative(root):
    stack1 = [root]
    stack2 = []

    while stack1:
        nodo = stack1.pop()
        stack2.append(nodo)

        if nodo.left_subtree:
            stack1.append(nodo.left_subtree)

        if nodo.right_subtree:
            stack1.append(nodo.right_subtree)

    while stack2:
        nodo = stack2.pop()
        print(nodo.name, end=" ")

print(f"Postorder iterative:")
postorder_iterative(root)
print("\r\n")
