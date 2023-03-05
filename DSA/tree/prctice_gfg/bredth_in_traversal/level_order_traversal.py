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


def level_order_traversal(root):
    if not root:
        print(f"tree in empty")
        return
    aux_queue = queue.Queue()
    aux_queue.put(root)
    while not aux_queue.empty():
        curr = aux_queue.get()
        print(f"{curr.data}", end=' ')
        if curr.left:
            aux_queue.put(curr.left)
        if curr.right:
            aux_queue.put(curr.right)


def level_order_line_by_line_traversal(root):
    if not root:
        print(f"tree in empty")
        return
    aux_queue = queue.Queue()
    aux_queue.put(root)
    while not aux_queue.empty():
        count = aux_queue.qsize()
        for _ in range(count):
            curr = aux_queue.get()
            print(f"{curr.data}", end=' ')
            if curr.left:
                aux_queue.put(curr.left)
            if curr.right:
                aux_queue.put(curr.right)
        print('')


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    level_order_traversal(root)
    print('')
    level_order_line_by_line_traversal(root)
    print('')
