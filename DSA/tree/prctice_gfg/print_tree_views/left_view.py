import queue

max_level = 0


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


"""
TC: Theta(n) --->n in no of nodes in tree
SC: O(w)/Theta(n) --->w is width of tree --max leaf nodes in a level

"""


# idea is to use pre_order traversal as it visits left side first always
# maintain two extra variables max_level and level
# when max_level is less than curr level then only print value of that node
def print_left_view_recursive(root, level=1):
    global max_level
    if not root:
        return
    if max_level < level:
        print(f"{root.data}", end=" ")
        max_level = level  # update printed curr level to max level
    print_left_view_recursive(root.left, level + 1)
    print_left_view_recursive(root.right, level + 1)


"""
TC: Theta(n) --->n in no of nodes in tree
SC: O(h) --->h is height of tree

"""


# based on line by line level order traversal using queue and its size for iteration
def print_left_view(root):
    if not root:
        print(f"tree is empty")
        return
    aux_queue = queue.Queue()
    aux_queue.put(root)
    while not aux_queue.empty():
        size = aux_queue.qsize()
        for i in range(size):
            curr = aux_queue.get()
            if i == 0:
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
    print_left_view(root)
    print('')
    print_left_view_recursive(root)
