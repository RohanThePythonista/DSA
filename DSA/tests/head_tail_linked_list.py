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

    def get_first_node(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("list is empty ")

    def get_last_node(self):
        if not self.is_empty():
            return self.tail.data
        else:
            print("list is empty ")

    def is_empty(self):
        return self.head is None

    def get_middle_node(self):
        if self.is_empty():
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("middle node:{}".format(slow.data)) if self.head.next and self.head.next.next else print(
            'insufficient list')


if __name__ == "__main__":
    linked_list = HeadTailLinkedList()
    for i in range(5):
        linked_list.insert_at_beginning(i + 6)
    linked_list.print_linked_list()
    for i in range(5):
        linked_list.insert_at_end(i)
    linked_list.print_linked_list()
    for _ in range(2):
        linked_list.delete_from_end()
    linked_list.print_linked_list()
    for _ in range(2):
        linked_list.delete_from_beginning()
    linked_list.print_linked_list()
    for i in range(2):
        linked_list.insert_at_beginning(i + 6)
    linked_list.print_linked_list()
    for i in range(2):
        linked_list.insert_at_end(i)
    linked_list.print_linked_list()
