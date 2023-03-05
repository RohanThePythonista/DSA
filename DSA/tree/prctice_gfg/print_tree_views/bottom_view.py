"""
TC: O(n) --->n in no of nodes in tree
SC: O(w)/Theta(n) --->w is width of tree --max leaf nodes in a level

"""

import queue


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_bottom_view(root):
    # recursive method and printing leaf nodes
    if not root:
        return
    if not root.left and not root.right:
        # leaf node check for for bottom view
        print(f"{root.data}", end=" ")
    print_bottom_view(root.left)
    print_bottom_view(root.right)


def print_bottom_view_iterative(root):
    # order is not maintained from left to right
    if not root:
        print(f"tree is empty")
        return
    aux_queue = queue.Queue()
    aux_queue.put(root)
    while not aux_queue.empty():
        curr = aux_queue.get()
        if not curr.left and not curr.right:
            print(f"{curr.data}", end=' ')
        if curr.left:
            aux_queue.put(curr.left)
        if curr.right:
            aux_queue.put(curr.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    root.left.left.left = Node(70)
    print_bottom_view(root)
    print('')
    print_bottom_view_iterative(root)
