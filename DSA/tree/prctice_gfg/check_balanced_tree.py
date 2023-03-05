class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


"""
Balanced bin tree is having diff between left and right subtree's heights is <=1 
"""

"""
Naive approach: 
TC: O(n^2)
Idea is to use heights of left and right subtrees
so, tree will be balanced if left and and right subtree's heights diff is less than or equal to 1
and similarly left and right subtrees recursively has height less than 1
"""


def is_balanced(root):
    if not root:
        return True
    rh = height(root.right)
    lh = height(root.left)
    return abs(lh - rh) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


"""
Better Approach using height to check balance condition
TC:O(n)
"""


def is_balanced_2(root):
    if not root:
        return 0
    lh = is_balanced_2(root.left)
    if lh == -1:
        return -1
    rh = is_balanced_2(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    print(is_balanced(root))
    if is_balanced_2(root) == -1:
        print(False)
    else:
        print(True)
