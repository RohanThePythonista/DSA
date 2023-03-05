"""
recursive result
TC: O(n) --->n in no of nodes in tree
SC: O(h) --->h is height of tree

"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_nodes_at_k_dist(root, k):
    if not root:
        return
    if k == 0:
        print(f"{root.data}", end=" ")
    else:
        print_nodes_at_k_dist(root.left, k - 1)
        print_nodes_at_k_dist(root.right, k - 1)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    print_nodes_at_k_dist(root, 2)
