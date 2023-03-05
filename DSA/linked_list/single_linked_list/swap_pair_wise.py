from practise.linked_list.single_linked_list.template import *


class Swapping(HeadTailLinkedList):
    def __init__(self):
        super(Swapping, self).__init__()

    def swap_pair_wise(self):
        print("I am called")
        if not self.head or not self.head.next:
            return
        curr = self.head.next.next
        prev = self.head
        self.head = self.head.next
        self.head.next = prev
        while curr and curr.next:
            next_node = curr.next.next
            prev.next = curr.next
            prev = curr
            curr.next.next = curr
            curr = next_node
        prev.next = curr

    def swap_data_pair_wise(self, head):
        if head and head.next:
            head.data, head.next.data = head.next.data, head.data
            self.swap_data_pair_wise(head.next.next)


if __name__ == '__main__':
    ll = Swapping()
    for i in range(10):
        ll.insert_at_end(i)
    ll.print_linked_list()
    ll.swap_pair_wise()
    ll.swap_data_pair_wise(ll.head)
    ll.print_linked_list()
