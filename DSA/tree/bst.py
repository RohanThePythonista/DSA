import sys


class Node:
    """
    Binary tree node with three instance attributes
    data: holds key/value inserted in node
    left: reference to left child node
    right: reference to right child node
    """

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BSTTree:
    """
    search, insert, delete operations in BST are O(log(h)), h-height of tree -->in avg case
    if BST is either left or right skewed then these operations takes O(n) time
    height of single node is zero
    height of empty tree is -1
    """

    def __init__(self):
        self.root = None

    def insert(self, root, key):
        """
        Idea is to insert key in BST is to follow BST property while inserting
        In recursive approach:
        insert(root, key):
            check if root is None
                then insert new node and assign its ref to this root
                and return this root to caller
                root = get_new_node(key)
                return root
            check if key is less than or equal to current root data:
                then recursively call on left subtree
                root.left = insert(root.left, key)
            else:
                call then recursively call on right subtree
                root.right = insert(root.right, key)
        finally return root
        return root

        :param root: root of BST
        :param key: key/value to be inserted in BST
        :return: root
        """
        if root is None:
            root = BSTTree.get_new_node(key)
            return root
        if key <= root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def insert_iterative(self, key):
        """
        TODO: check how to implement it
        :param key:
        :return:
        """
        if self.root is None:
            self.root = BSTTree.get_new_node(key)
            return
        curr = self.root
        if key <= self.root.data:
            if self.root.left is None:
                self.root.left = BSTTree.get_new_node(key)
                return
        else:
            if self.root.right is None:
                self.root.right = BSTTree.get_new_node(key)
                return
        if key > curr.data:
            while curr.right:
                curr = curr.right
            curr.right = BSTTree.get_new_node(key)
        else:
            while curr.left:
                curr = curr.left
            curr.left = BSTTree.get_new_node(key)

    @staticmethod
    def get_new_node(key):
        return Node(key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def iterative_pre(self):
        """
        Idea is to use stack while traversing in pre-order
        curr = self.root
        keep traversing left subtree
        while curr:
            print(curr.data)
            if it has right node
                push it to stack
            curr = curr.left
            if curr is None and stack:
                curr = stack.pop()
        :return:
        """
        if self.root is None:
            return
        curr = self.root
        stack = []
        while curr:
            print(curr.data, end=' ')
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
            if curr is None and stack:
                curr = stack.pop()

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' ')

    def post_order_iterative(self):
        from collections import defaultdict
        if self.root is None:
            return
        node_to_its_occurrence_map = dict()
        stack = list()
        stack.append(self.root)
        while stack:
            temp = stack[-1]
            if node_to_its_occurrence_map.get(temp, 0) == 0:
                if temp.left:
                    node_to_its_occurrence_map[temp] = 0
                    stack.append(temp.left)
            elif node_to_its_occurrence_map.get(temp) == 1:
                if temp.right:
                    stack.append(temp.right)
            elif node_to_its_occurrence_map.get(temp) == 2:
                print(temp.data, end=' ')
            else:
                stack.pop()
            node_to_its_occurrence_map[temp] = node_to_its_occurrence_map.get(temp, 0) + 1

    def delete(self, root, key):
        if root is None:
            return
        if root.data > key:
            root.left = self.delete(root.left, key)
        elif root.data < key:
            root.right = self.delete(root.right, key)
        else:
            # found case
            if root.left is None and root.right is None:
                # case 1: node is leaf node
                del root
                root = None
            elif root.left is None:
                # case 2: node have a child
                temp = root
                root = root.right
                del temp
            elif root.right is None:
                # case 2: node have a child
                temp = root
                root = root.left
                del temp
            else:
                # case 3: node have two children
                new_root_data = self.find_min(root.right)
                root.data = new_root_data
                root.right = self.delete(root.right, new_root_data)
        return root

    def find_min(self, root):
        if root and root.left is None:
            return root.data
        if root is None:
            return -1
        data = self.find_min(root.left)
        return data

    def find_max(self, root):
        if root and root.right is None:
            return root.data
        if root is None:
            return -1
        data = self.find_max(root.right)
        return data

    def search(self, root, key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif root.data < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def search_iterative(self, key):
        if self.root is None:
            return False
        curr = self.root
        while curr:
            if curr.data == key:
                return True
            if curr.data < key:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def find_height_of_tree(self, root):
        """
        Idea is to use recursion and get max of height of left-subtree and right-subtree
        and add 1 to it
        If root is None it return -1 ....assuming height of empty tree as -1
        :param root:
        :return:
        """
        if root is None:
            return -1
        return max(self.find_height_of_tree(root.left), self.find_height_of_tree(root.right)) + 1

    def level_order_traversal(self):
        print('level order traversal using queue')
        if self.is_empty():
            print('BST is empty')
            return
        queue = list()
        queue.append(self.root)
        while queue:
            curr = queue.pop(0)
            print(curr.data, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print('')

    def level_order_traversal_line_by_line(self, left_view_only=False):
        """
        Idea is to use for level order traversal using queue
        To print level line by line
            size = use queue size  # this line is IMP, it would be wrong to iterate over direct queue and not its size
                iterate over queue size
                    curr = dequeue
                    print  curr.data
                    insert curr.left and curr.right node to queue if exists
        :param left_view_only:
        :return:
        """
        print('level_order_traversal_line_by_line using queue')
        if self.is_empty():
            print('BST is empty')
            return
        queue = list()
        queue.append(self.root)
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if left_view_only is True:
                    # print only first(left) node in each level
                    if i == 0:
                        print(curr.data, end=' ')
                else:
                    # print all nodes in level in a line
                    print(curr.data, end=' ')
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print('')
        print('')

    def spiral_level_order_traversal(self):
        """
        Idea is to use line by line level order traversal using queue and also use stack
        while queue is not empty
            iterate over curr size of queue
                If level is even then push left and then right nodes to stack
                and if level is odd then push right and and then left nodes to stack
            while stack is not empty
                pop and enqueue to queue

        :return:
        """
        print('spiral_level_order_traversal')
        # TODO: please study and come back to me
        if self.is_empty():
            return
        queue = list()
        stack = list()
        queue.append(self.root)
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                print(curr.data, end=' ')
                if level % 2 == 1:
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                else:
                    if curr.left:
                        stack.append(curr.left)
                    if curr.right:
                        stack.append(curr.right)
            while stack:
                queue.append(stack.pop())
            level += 1
            print('')

    def right_view(self):
        """
        Idea is to use same concept for level order traversal using queue
        To print right view of tree
            size = use queue size  # this line is IMP, it would be wrong to iterate over direct queue and not its size
                iterate over queue size
                    curr = dequeue
                    if i== size -1      # this is IMP, to consider last node of each level
                        print  curr.data
                    insert curr.left and curr.right node to queue if exists
        :return:

        :return:
        """
        print('right_view using queue')
        if self.is_empty():
            print('BST is empty')
            return
        queue = list()
        queue.append(self.root)
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if i == size - 1:
                    # print only right node at each level
                    print(curr.data, end=' ')
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print('')
        print('')

    def bottom_view(self, root):
        """
        If we look at tree from bottom,
        it is obvious that you would be able to see only leaf nodes of that tree
        Basically idea is to use recursive approach to find all leaf nodes and print them
        :param root:
        :return:
        """
        if root is None:
            # if root is None return to immediate it latest caller
            return
        if not root.left and not root.right:
            # leaf node found, so print it
            print(root.data, end=' ')
        self.bottom_view(root.left)
        self.bottom_view(root.right)

    def is_empty(self):
        return self.root is None

    def get_size(self, root):
        """
        TC- O(n) --simply traversal of all nodes in tree
        SC- O(h)--proportional to height-->no. active fun calls in stack <= height of tree at any moment
        :param root:
        :return: int size of tree(total no. of nodes in tree)
        """
        if root is None:
            return 0
        else:
            return 1 + self.get_size(root.left) + self.get_size(root.right)

    def get_size_using_queue(self):
        """
        Idea is to use level order traversal using queue
        Keep counter to count no. of nodes until queue is not empty
        :return:
        """
        if self.root is None:
            return 0
        queue = list()
        queue.append(self.root)
        counter = 0
        while queue:
            counter += 1
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return counter

    def get_max_in_binary_tree(self, root):
        """
        Idea is to using recursion find max from root, left-subtree and right-subtree
        This solution is for binary tree.....(for BST there is better solution)
        TC- O(n)
        SC- O(h)---at most h+1 fun calls in stack-----using level order traversal --O(w)--width of tree
        :param root:
        :return: max value from tree
        """
        if root is None:
            return -sys.maxsize
        else:
            return max(root.key, max(self.get_max_in_binary_tree(root.lef), self.get_max_in_binary_tree(root.right)))

    def print_k_dist_nodes(self, root, k):
        """
        Idea is to use recursion and find kth level nodes in left and right subtrees
        Pass k as argument to fun call
        if root is empty simply return
        if k == 0 then that is kth level node root
            print root.data
        else:
            recursively call left and right subtree with k-1
        :param root:
        :param k:
        :return:
        """
        if root is None:
            return
        if k == 0:  # this should be after only above base case check else none.data would be tried
            print(root.data, end=' ')
        else:
            self.print_k_dist_nodes(root.left, k - 1)
            self.print_k_dist_nodes(root.right, k - 1)

    def is_balanced_tree(self, root):
        """
        TC--->O(n)/theta(n)
        SC-->O(h)--->height of tree
        Idea is to find height of each node recursively in left and right subtree
        And check if there height diff is not more than 1
        When height is obtained of left and right subtree of each node
            it will decide is balanced or not by comparing height diff
        :param root:
        :return:
        """
        if root is None:
            return 0
        left_height = self.is_balanced_tree(root.left)
        if left_height == -1:
            return -1
        right_height = self.is_balanced_tree(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1

    def get_max_width_of_tree(self):
        """
        TC-->theta(n)-->just traversing all nodes and doing const. operation using queue
        SC-->O(n)-->theta(w)---max. width would be in a queue at any time
        Idea is to use level order traversal line by line using queue
        max width would be the max. no. of nodes in any level in the tree
        :return: int --> max_width in tree
        """
        if self.root is None:
            return 0
        queue = list()
        queue.append(self.root)
        max_width = 0
        while queue:
            size = len(queue)
            max_width = max(max_width, size)
            for _ in range(size):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return max_width

    def bin_tree_to_double_linked_list(self, root):
        pass

    def spiral_level_order_traversal_using_queue_and_stack(self):
        """
        Use line by line level order traversal using queue
        reverse = False
        while queue:
            size = len(queue)
            for _ in range(size):
                if level has to printed reverse
                    then push that curr node data to stack
                else
                    print(curr.data, end=' ')
                push left and right
            while stack:
                print(stack.pop(), end=' ')
            reverse = not reverse
            print('')  # new line  for line by line spiral traversal
        :return:
        """
        print('spiral_level_order_traversal_using_queue_and_stack')
        if self.is_empty():
            return
        queue = list()
        stack = list()
        queue.append(self.root)
        reverse = False
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                if reverse:
                    stack.append(curr.data)
                else:
                    print(curr.data, end=' ')
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if reverse:
                while stack:
                    print(stack.pop(), end=' ')
            reverse = not reverse
            print('')

    def spiral_improved(self):
        """
        Idea is to use two stacks
        First stack to print a level in left to right order
        second stack to print a level in right to left order
        :return:
        """
        if self.root is None:
            return
        stack1 = list()
        stack2 = list()
        stack1.append(self.root)
        while stack1 or stack2:
            while stack1:
                """
                push in stack2 left and right order
                """
                curr = stack1.pop()
                print(curr.data, end=' ')
                if curr.left:
                    stack2.append(curr.left)
                if curr.right:
                    stack2.append(curr.right)
            print('')
            while stack2:
                """
                reverse order push
                push in stack1 right and left order
                """
                curr = stack2.pop()
                print(curr.data, end=' ')
                if curr.right:
                    stack1.append(curr.right)
                if curr.left:
                    stack1.append(curr.left)
            print('')


if __name__ == '__main__':
    bst = BSTTree()
    # input_array = [15, 10, 20, 8, 12, 17, 25]
    # input_array = [1, 2, 3, 4, 5, 6]
    # input_array = [10, 5, 20, 3, 7]
    # input_array = [100, 80, 300, 10, 90, 200, 700, 8, 9, 150]
    input_array = [150, 50, 200, 30, 90, 180, 300, 20, 40, 70, 100, 250, 500, 10]
    for val in input_array:
        bst.root = bst.insert(bst.root, val)
    print('inorder')
    bst.inorder(bst.root)
    print('')
    # print('preorder')
    # bst.preorder(bst.root)
    # print('')
    print('postorder')
    bst.postorder(bst.root)
    print('')
    bst.post_order_iterative()
    # print("MIN:{}".format(bst.find_min(bst.root)))
    # print("max:{}".format(bst.find_max(bst.root)))
    # print("search:{}".format(bst.search(bst.root, -1)))
    # print("search_itrative:{}".format(bst.search_iterative(-1)))
    # print(bst.find_height_of_tree(bst.root))
    # print('iterative pre')
    # bst.iterative_pre()
    # print('')
    # bst.root = bst.delete(bst.root, 12)
    # print('Inorder')
    # bst.inorder(bst.root)
    # print('')
    # bst.level_order_traversal()
    # bst.level_order_traversal_line_by_line()
    # bst.level_order_traversal_line_by_line(left_view_only=True)
    # bst.right_view()
    # print('bottom view using recursion')
    # bst.bottom_view(bst.root)
    # print('')
    # # bst.spiral_level_order_traversal(bst.root)
    # print(bst.get_size(bst.root))
    # print(bst.get_size_using_queue())
    # print('k dist nodes')
    # bst.print_k_dist_nodes(bst.root, 2)
    # print('')
    # bst.spiral_level_order_traversal()
    # bst.spiral_level_order_traversal_using_queue_and_stack()
