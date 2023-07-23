
"""
    Methods to traverse a tree
"""

def preorder_iterative(root):
    stack = [root]

    while stack:
        nodo = stack.pop()

        print(nodo.name, end=" ")
        if nodo.right_subtree:
            stack.append(nodo.right_subtree)

        if nodo.left_subtree:
            stack.append(nodo.left_subtree)


def inorder_iterative(root):
    stack = []
    current = root

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




