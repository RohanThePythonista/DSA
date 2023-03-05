class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def is_tree_follows_children_sum_property(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    sum_ = 0
    if root.left:
        sum_ += root.left.data
    if root.right:
        sum_ += root.right.data
    return (sum_ == root.data and is_tree_follows_children_sum_property(
        root.left) and is_tree_follows_children_sum_property(root.right))


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)
    root.left.right = Node(5)
    print(is_tree_follows_children_sum_property(root))
