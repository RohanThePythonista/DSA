class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, root):
        """
        Assuming only distinct keys
        :param key:
        :param root:
        :return:
        """
        if root is None:
            root = BinarySearchTree.get_new_node(key)
            return root
        if key > root.data:
            root.right = self.insert(key, root.right)
        elif key < root.data:
            root.left = self.insert(key, root.left)
        return root

    def iterative_insert(self, key):
        """
        Idea to search the parent of key to be inserted
        Assuming keys are distinct
        new_node = get_new_node(key)
        If tree is empty
            make new node as root and return
        curr = root
        while curr is not None:
            parent = curr # it is to maintain parent to insert new_node
            if key > curr.data:
                go to right
                curr = curr.right
            elif key < curr.data:
                go to left
                curr = curr.left
            else:
                # key is already present in tree
                return
            # now check for left or right place where new_node would be inserted
            if parent.data < key:
                # insert as right child
                parent.right = new_node
            else:
                # insert as left child
                parent.left = new_node
        :param key:
        :return:
        """
        new_node = BinarySearchTree.get_new_node(key)
        if self.root is None:
            # this is for empty tree
            self.root = new_node
            return
        curr = self.root
        parent = curr
        while curr:
            # this loop search correct place for new_node and also maintain parent for it
            parent = curr  # maintain parent for new node to be inserted
            if key > curr.data:
                curr = curr.right
            elif key < curr.data:
                curr = curr.left
            else:
                print('key:{} is already present'.format(key))
                return
        if parent.data > key:
            # if parent is greater than key insert key to left
            parent.left = new_node
        else:
            # if parent is less than key insert key to right
            parent.right = new_node

    @staticmethod
    def get_new_node(key):
        return Node(key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)

    def search(self, key, root):
        if root is None:
            return False
        if key == root.data:
            return True
        elif key > root.data:
            return self.search(key, root.right)
        else:
            return self.search(key, root.left)

    def iterative_search(self, key):
        print('search iterative:{}'.format(key))
        if self.root is None:
            return False
        curr = self.root
        while curr:
            if key == curr.data:
                print('key found')
                return True
            elif key > curr.data:
                curr = curr.right
            else:
                curr = curr.left
        else:
            print('key not found')
            return False

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            # go to left subtree
            root.left = self.delete(root.left, key)
        elif key > root.data:
            # go to right subtree
            root.right = self.delete(root.right, key)
        else:
            # key found
            if root.left is None and root.right is None:
                # case 1: node is leaf node
                del root
                root = None
            elif root.right is None:
                # case 2: node has a child
                temp = root
                root = root.left
                del temp
            elif root.left is None:
                # case 2: node has a child
                temp = root
                root = root.right
                del temp
            else:
                inorder_successor = self.find_min(root.right)
                root.data = inorder_successor
                root.right = self.delete(root.right, inorder_successor)
        return root

    def find_min(self, root):
        if root and root.left is None:
            return root.data
        elif root is None:
            return -1
        return self.find_min(root.left)

    def find_max(self, root):
        if root and root.right is None:
            return root.data
        elif root is None:
            return -1
        return self.find_max(root.right)

    def find_floor(self, x):
        """
        Idea is to use BST search mechanism
        res = None
        while curr node is not empty:
            if root value is equal to given key then:
                return root
            else if root value is greater than key:
                then go to left side
            else:
                update res = current root(which is potential floor) and go to right side
        return res
        :param x: int key whose floor to be find in BST
        :return: int floor of input key
        """
        if self.root is None:
            return
        if self.root.data == x:
            return x
        curr = self.root
        floor = None
        while curr:
            if curr.data == x:
                return x
            elif curr.data > x:
                curr = curr.left
            else:
                floor = curr.data
                curr = curr.right
        return floor

    def find_ceil(self, key):
        """
        Idea is to use BST search mechanism
        res = None
        while curr node is not empty:
            if root value is equal to given key then:
                return root
            else if root value is less than key:
                then go to right side
            else:
                update res = current root(which is potential ceil) and go to left side
        return res
        :param key: int key whose ceil to be find in BST
        :return: int ceil of input key
        """
        if self.root is None:
            return
        curr = self.root
        res = None
        while curr:
            if curr.data == key:
                return curr.data
            elif curr.data < key:
                curr = curr.right
            else:
                res = curr.data
                curr = curr.left
        return res


if __name__ == "__main__":
    bst = BinarySearchTree()
    # for i in range(10, 0, -1):
    #     bst.root = bst.insert(i, bst.root)
    input_array = [50, 30, 70, 20, 40, 60, 80, 55, 65]
    for i in input_array:
        bst.iterative_insert(i)
    print('inorder traversal')
    bst.inorder(bst.root)
    print('')
    # print(bst.find_max(bst.root))
    # print(bst.find_min(bst.root))
    # bst.root = bst.delete(bst.root, 50)
    # bst.inorder(bst.root)
    print(bst.find_ceil(69))
