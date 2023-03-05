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


# based on line by line level order traversal using queue and its size for iteration
def print_top_view(root):
    # left and right view combination
    if not root:
        print(f"tree is empty")
        return
    aux_queue = queue.Queue()
    aux_queue.put(root)
    while not aux_queue.empty():
        size = aux_queue.qsize()
        for i in range(size):
            curr = aux_queue.get()
            if i == 0 or i == size - 1:
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
    print_top_view(root)
