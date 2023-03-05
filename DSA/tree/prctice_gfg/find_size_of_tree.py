"""
TC: O(n) --->n in no of nodes in tree
SC: O(h) --->h is height of tree

"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def get_size(root):
    if not root:
        return 0
    return 1 + get_size(root.left) + get_size(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    print(f"{get_size(root)}")
