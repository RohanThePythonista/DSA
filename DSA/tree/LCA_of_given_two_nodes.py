class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def find_lca(root, n1, n2):
    path1 = []
    path2 = []
    # Find paths from root to n1 and root to n2.
    # if either n1 or n2 not present return -1
    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return -1

    i = 0
    # compare paths to get first different value
    while i < len(path1):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


"""
Function to find the path from root node to
given root of the tree, Stores the path in a
list path[], returns true if path exists
otherwise false
"""


def find_path(root, path, k):
    # base case
    if not root:
        return False
    """
    Store this node in path list.
    The node will be removed if
    not in path from root to k
    """
    path.append(root.data)
    if root.data == k:
        return True
    # Check if k is found in left or right sub-tree
    if (root.left and find_path(root.left, path, k)) or (root.right and find_path(root.right, path, k)):
        return True
    # If not present in subtree rooted with root,
    # remove root from path[] and return false
    path.pop()
    return False


"""
If we assume that the keys are present in Binary Tree, 
we can find LCA using single traversal of Binary Tree 
and without extra storage for path arrays.

The idea is to traverse the tree starting from the root node. 
If any of the given keys (n1 and n2) matches with root, 
then root is LCA (assuming that both keys are present). 
If root doesn't match with any of the keys, we recur for left and right subtrees. 
The node which has one key present in its left subtree 
and the other key present in the right subtree is the LCA. 
If both keys lie in left subtree, then left subtree has LCA also, otherwise, 
LCA lies in the right subtree
"""


def find_lca_method2(root, n1, n2):
    if not root:
        return

    # if n1 or n2 matches root key then that would be LCA
    if root.data == n1 or root.data == n2:
        return root.data

    left_lca = find_lca_method2(root.left, n1, n2)
    right_lca = find_lca_method2(root.right, n1, n2)

    if left_lca and right_lca:
        return root.data

    return left_lca if left_lca else right_lca


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4, 5) = {}".format(find_lca(root, 4, 5)))
    print("LCA(4, 6) = {}".format(find_lca(root, 4, 6)))
    print("LCA(3, 4) = {}".format(find_lca(root, 3, 4)))
    print("LCA(2, 4) = {}".format(find_lca(root, 2, 4)))

    print("Using method2")
    print("LCA(4, 5) = {}".format(find_lca_method2(root, 4, 5)))
    print("LCA(4, 6) = {}".format(find_lca_method2(root, 4, 6)))
    print("LCA(3, 4) = {}".format(find_lca_method2(root, 3, 4)))
    print("LCA(2, 4) = {}".format(find_lca_method2(root, 2, 4)))

    """
    The time complexity of the above solution is O(N) 
    where N is the number of nodes in the given Tree 
    and the above solution also takes O(N) extra space
    So, basically it requires three tree traversals plus extra spaces for path arrays.
    """
