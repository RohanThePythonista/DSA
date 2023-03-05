"""
TC: O(n) --->n in no of nodes in tree
SC: O(h) --->h is height of tree

"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(f"{root.data}", end=' ')
    inorder_traversal(root.right)


def preorder_traversal(root):
    if not root:
        return
    print(f"{root.data}", end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(f"{root.data}", end=' ')


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    inorder_traversal(root)
    print('')
    preorder_traversal(root)
    print('')
    postorder_traversal(root)
    print('')
