from practise.linked_list.single_linked_list.template import *


class FindNode(HeadTailLinkedList):
    def __init__(self):
        super().__init__()

    def find_nth_node_from_end(self, n):
        if self.is_empty():
            return -1
        self.reverse()
        nth_node = self.get_kth_node(n)
        self.reverse()
        return nth_node

    def get_kth_node(self, k):
        if self.is_empty():
            return -1
        curr = self.head
        k -= 1
        while curr and k:
            curr = curr.next
            k -= 1
        if curr and k == 0:
            return curr.data
        else:
            return -1

    def reverse(self):
        if self.is_empty():
            return
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev


if __name__ == "__main__":
    ll = FindNode()
    for i in range(1, 11, 1):
        ll.insert_at_end(i)
    ll.print_linked_list()
    print("nth node:{}".format(ll.find_nth_node_from_end(10)))



"""
def count(head, search_for):
    if head is None:
        return 0
    # count_ = 0
    # curr = head
    # while curr:
    #     if curr.data == search_for:
    #         count_ += 1
    #     curr = curr.next
    # return count_
    return (head.data == search_for) + count(head.next, search_for)  # recursive solution
"""