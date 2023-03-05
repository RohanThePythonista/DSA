"""
Given two sorted singly linked lists.
Create a new sorted linked list by merging given two lists.

"""
from typing import Optional


class Node:
    def __init__(self, key: int):
        self.data = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_lists(self) -> None:
        print('print lists')
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print('')

    def append(self, key: int) -> None:
        """
        method to add key at end of linked list
        :param key:key to be inserted at en of list
        :return:None
        """
        new_node = LinkedList.get_new_node(key)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last and last.next:
                last = last.next
            last.next = new_node

    @staticmethod
    def get_new_node(key: int) -> Node:
        """
        Create new node with given key
        :param key:
        :return:
        """
        return Node(key)


def merge_two_sorted_linked_lists(head1: Optional[None], head2: Optional[None]) -> Node:
    """
    Iterative method to merge two sorted list and return head of new_list
    Uses dummy node to store reference of head of new list
    :param head1:
    :param head2:
    :return:
    """
    # a dummy first node to hang the result on
    dummy_node = LinkedList.get_new_node(-1)
    # tail->next is the place to add new nodes to the result
    tail = dummy_node
    while True:
        if head1 is None:
            tail.next = head2
            break
        elif head2 is None:
            tail.next = head1
            break
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    # dummy_node.next point to first node in resulted list
    return dummy_node.next


def merger(head1: Optional[None], head2: Optional[None]) -> Node:
    """
    Recursive method to merge two sorted list and return head of new_list
    :param head1:
    :param head2:
    :return:
    """
    # temp to store result list head
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = merger(head1.next, head2)
    else:
        temp = head2
        temp.next = merger(head1, head2.next)
    return temp


if __name__ == '__main__':
    list_1 = LinkedList()
    for val in range(0, 10, 2):
        list_1.append(val)
    list_1.print_lists()
    list_2 = LinkedList()
    for val in range(1, 13, 2):
        list_2.append(val)
    list_2.print_lists()
    list_3 = LinkedList()
    list_3.head = merger(list_1.head, list_2.head)
    list_3.print_lists()
