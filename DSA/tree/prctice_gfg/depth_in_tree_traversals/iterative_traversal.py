class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    pass


def preorder(root):
    if not root:
        return
    pass


def postorder(root):
    if not root:
        return
    pass


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    inorder(root)
    print('')
    preorder(root)
    print('')
    postorder(root)
    print('')
