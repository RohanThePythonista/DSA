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

    def reverse(self, head, k):
        current = head
        next_node = None
        prev = None
        count = 0
        while current is not None and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        if next_node is not None:
            head.next = self.reverse(next_node, k)
        return prev

    def reverse_using_stack(self, head, k):
        curr = head
        ptr = head
        stack = list()
        while curr is not None:
            i = 0
            while i < k and curr is not None:
                stack.append(curr.data)
                curr = curr.next
                i += 1
            while ptr is not None and stack:
                ptr.data = stack.pop()
                ptr = ptr.next
        return head


if __name__ == '__main__':
    ll = HeadTailLinkedList()
    for i in range(10):
        ll.insert_at_end(i)
    ll.print_linked_list()
    ll.head = ll.reverse_using_stack(ll.head, 3)
    ll.print_linked_list()
