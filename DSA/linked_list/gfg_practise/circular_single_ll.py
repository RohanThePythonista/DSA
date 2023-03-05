class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class CircularSingleLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_beg(self, key):
        """
        Using tail ptr/ref
            -It is O(1) operation to insert at beginning in linked list
        :param key:int, data of new node to be inserted
        :return: None
        """
        new_node = CircularSingleLinkedList.get_new_node(key)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
            return
        new_node.next = self.tail.next  # hold old head in new node's next
        self.tail.next = new_node  # update new head in tails' next

    def insert_at_end(self, key):
        """
        Using tail ptr/ref
            -It is O(1) operation to insert at end in circular linked list
            -tail ptr/ref works efficiently to insert at end in const time operation
        :param key:int, data of new node to be inserted
        :return: None
        """
        new_node = CircularSingleLinkedList.get_new_node(key)
        if self.tail is None:
            # if empty then create first node with circular link to itself
            self.tail = new_node
            new_node.next = self.tail
            return
        new_node.next = self.tail.next  # hold head in new node's next
        self.tail.next = new_node  # insert new node at end of list
        self.tail = self.tail.next  # update tail to new inserted node

    def delete_from_beg(self):
        if self.tail is None:
            print(f"no nodes to delete")
            return
        if self.tail is self.tail.next:
            print(f"deleting last node from list")
            del self.tail
            self.tail = None
            return
        head = self.tail.next  # hold head to be deleted
        self.tail.next = head.next  # link head's next to tail's next for new head update
        del head

    @staticmethod
    def get_new_node(key):
        return Node(key)

    @staticmethod
    def print_list(tail):
        if tail is None:
            print(f"Oho!, your list is empty")
            return
        head = tail.next
        while head != tail:
            print(head.data, end=' ')
            head = head.next
        print(head.data, end=' ')
        print('')


if __name__ == '__main__':
    cll = CircularSingleLinkedList()
    for i in range(5):
        cll.insert_at_beg(i)
    cll.print_list(cll.tail)
    for i in range(5):
        cll.insert_at_end(i)
    cll.print_list(cll.tail)
    for i in range(5):
        cll.delete_from_beg()
    cll.print_list(cll.tail)
    for i in range(5):
        cll.delete_from_beg()
    cll.print_list(cll.tail)
