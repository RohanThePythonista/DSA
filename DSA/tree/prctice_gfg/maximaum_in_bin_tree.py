"""
recursive result
TC: O(n) --->n in no of nodes in tree
SC: O(h) --->h is height of tree

iterative using queue level order traversal --> if perfect bin tree is there it will take more space
if it is skewed tree then it will take O(1) space
TC: O(n) --->n in no of nodes in tree
SC: O(w) --->w is width of tree

"""
import sys

curr_max = - sys.maxsize


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def get_max(root):
    global curr_max
    if not root:
        return
    if root.data > curr_max:
        curr_max = root.data
    get_max(root.left)
    get_max(root.right)


def get_max_2(root):
    if not root:
        return - sys.maxsize
    return max(root.data, max(get_max_2(root.left), get_max_2(root.right)))


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    get_max(root)
    print(f"{curr_max}")
    print(f"{get_max_2(root)}")
