from practise.linked_list.single_linked_list.template import *


class SegregateEvenOdd(HeadTailLinkedList):
    def __init__(self):
        super(SegregateEvenOdd, self).__init__()

    def segregate_even_odd_nodes(self):
        curr = self.head
        even_start = None
        odd_start = None
        even_end = None
        odd_end = None
        while curr:
            if curr.data % 2 == 0:
                if even_start is None:
                    even_start = Node(curr.data)
                    even_end = even_start
                else:
                    even_end.next = Node(curr.data)
                    even_end = even_end.next
            else:
                if odd_start is None:
                    odd_start = Node(curr.data)
                    odd_end = odd_start
                else:
                    odd_end.next = Node(curr.data)
                    odd_end = odd_end.next
            curr = curr.next
        if even_start is None or odd_start is None:
            return
        self.head = even_start
        even_end.next = odd_start
        odd_end.next = None


if __name__ == '__main__':
    if __name__ == '__main__':
        t = int(input())
        for _ in range(t):
            n = input()
            n_list = list(map(int, input().split()))

            ll = SegregateEvenOdd()
            for i in n_list:
                ll.insert_at_end(i)
            ll.print_linked_list()
            ll.segregate_even_odd_nodes()
            ll.print_linked_list()
