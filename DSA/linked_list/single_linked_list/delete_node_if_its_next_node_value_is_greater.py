class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HeadTailLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        """
        inserting at beginning in any linked list happens in O(1) time
        :param data:
        :return:
        """
        print("inserting at beginning:{}".format(data))
        new_node = Node(data)
        if self.is_empty():
            self.insert_first_node(data)
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        using tail pointer insertions happens in O(1) time in singly linked lists
        :param data:
        :return:
        """
        print("inserting at end:{}".format(data))
        if self.is_empty():
            self.insert_first_node(data)
            return
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def insert_first_node(self, data):
        print("inserting very first node:{}".format(data))
        self.head = Node(data)
        self.tail = self.head

    def delete_from_beginning(self):
        """
        deleting from beginning in any linked list happens in O(1) time
        :return:
        """
        if self.is_empty():
            print("list is empty, deleting from beginning aborted")
            return
        head_next = self.head.next
        print("deleting from beginning:{}".format(self.head.data))
        del self.head
        self.head = head_next

    def delete_from_end(self):
        print("deleting from end")
        if self.is_empty():
            print("list is empty, deleting aborted")
            return
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        if prev is None:
            del self.head
            self.head = None
            self.tail = None
            return
        prev.next = None
        self.tail = prev
        del curr

    def print_linked_list(self):
        """
        traversing always takes linear time O(n)
        :return:
        """
        print("printing list")
        curr = self.head
        while curr:
            print(curr.data, sep=' ', end=' ')
            curr = curr.next
        print('')

    def is_empty(self):
        return not self.head

    def delete_lesser_nodes_brute_force(self):
        """
        Use two loops. In the outer loop, pick nodes of the linked list one by one.
        In the inner loop, check if there exist a node whose value is greater than the picked node.
        If there exists a node whose value is greater, then delete the picked node.
        Time Complexity: O(n^2)
        :return:
        """
        curr = self.head
        while curr and curr.next:
            pass

    def delete_lesser_nodes(self):
        """
        1. Reverse the list.
        2. Traverse the reversed list. Keep max till now.
           If next node is less than max, then delete the next node, otherwise max = next node.
        3. Reverse the list again to retain the original order.
        Time Complexity: O(n)
        :return:
        """
        self.head = self.reverse_list(self.head)
        self._delete(self.head)
        self.head = self.reverse_list(self.head)

    def _delete(self, head):
        curr = head
        max_node = head
        temp = None
        while curr and curr.next:
            if curr.next.data < max_node.data:
                temp = curr.next
                curr.next = temp.next
                del temp
            else:
                curr = curr.next
                max_node = curr

    def reverse_list(self, head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == '__main__':
    ll = HeadTailLinkedList()
    for val in [10, 20, 30, 40, 50, 60]:
        ll.insert_at_end(val)
    ll.print_linked_list()
    ll.delete_lesser_nodes()
    ll.print_linked_list()
