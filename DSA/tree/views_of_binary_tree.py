class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            if i == 0:
                print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print('')


def right_view(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            if i == size - 1:
                print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print('')


def bottom_view(root):
    if root is None:
        return
    bottom_view(root.left)
    bottom_view(root.right)
    if root.left is None and root.right is None:
        print(root.data, end=" ")


def top_view(root):
    # TODO: this is wrong implementation please study it first
    if root is None:
        return
    queue = list()
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            if i == size - 1 or i == 0:
                print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print('')


def create_mirror_image_of_tree(root):
    if root is None:
        return
    else:
        create_mirror_image_of_tree(root.left)
        create_mirror_image_of_tree(root.left)
        temp = root.left
        root.left = root.right
        root.right = temp


def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data, end=" ")
    in_order_traversal(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # bottom_view(root)
    # print('')
    # left_view(root)
    # right_view(root)
    # top_view(root)
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.right = Node(4)
    # root.left.right.right = Node(5)
    # root.left.right.right.right = Node(6)
    # top_view(root)
    in_order_traversal(root)
    print('')
    create_mirror_image_of_tree(root)
    in_order_traversal(root)
    print('')
