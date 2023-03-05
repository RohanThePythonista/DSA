"""
# https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
Given K sorted linked lists of size N each, merge them and print the sorted output.

Method 1 (Simple)
A Simple Solution is to initialize result as first list.
Now traverse all lists starting from second list.
Insert every node of currently traversed list into result in a sorted way.
TC: O(N^2) where N is total number of nodes, i.e., N = kn.
SC: O(1)

Method 2 (Using Min Heap)
A Better solution is to use Min Heap based solution
Step1: Create min heap of size k with all heads of k lists (Use priority queue(pq))
        create head pointer for result list
        and last pointer, to add new node at last of result list
Step2: Now iterate until queue not become empty:
            take top out of pq:
                if it has next node:
                    push it to pq
            check if head is None
                save head = top
            else
                # insert 'top' at the end of the merged list so far
                last -> next = top
            save last = top
        return head # result list head
TC: O(nk Log k)
SC: O(k)

Method 3 (Using Divide and Conquer))
Best solution
Merging of two linked lists can be done in O(n) time and O(1) space.
 (For arrays O(n) space is required).
The idea is to pair up K lists and merge each pair in linear time using O(1) space.
After first cycle, K/2 lists are left each of size 2*N.
After second cycle, K/4 lists are left each of size 4*N and so on.
We repeat the procedure until we have only one list left.
TC:  O(nk Log k)
SC: O(1)
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


# method 3
def merge_k_lists(arr_ptr, last):
    while last != 0:
        i = 0
        j = last
        # (i, j) forms a pair
        while i < j:
            # merge List i with List j and store merged list in List i
            arr_ptr[i] = sorted_merger(arr_ptr[i], arr_ptr[j])
            # consider next pair
            i += 1
            j -= 1
            # If all pairs are merged, update last
            if i >= j:
                last = j
    return arr_ptr[0]


def sorted_merger(head1: Optional[None], head2: Optional[None]) -> Node:
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
        temp.next = sorted_merger(head1.next, head2)
    else:
        temp = head2
        temp.next = sorted_merger(head1, head2.next)
    return temp


if __name__ == '__main__':
    list_1 = LinkedList()
    for val in range(0, 10, 2):
        list_1.append(val)
    list_1.print_lists()
    list_2 = LinkedList()
    for val in range(1, 13, 2):
        list_2.append(val)
    list_3 = LinkedList()
    for val in [10, 13, 15, 17]:
        list_3.append(val)
    list_3.print_lists()
    array_pointer = [list_3.head, list_2.head, list_1.head]
    result = LinkedList()
    result.head = merge_k_lists(array_pointer, len(array_pointer) - 1)
    result.print_lists()
