from DSA.linked_list.practise.base import Single_LL


class Reverse(Single_LL):
    def __init__(self):
        super(Reverse, self).__init__()

    def reverse_recur(self, curr, prev=None):
        if curr is None:
            return None
        elif curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next_node = curr.next
        curr.next = prev
        self.reverse_recur(next_node, curr)

    def reverse_iter(self):
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


if __name__ == '__main__':
    rev = Reverse()
    for i in range(5):
        rev.insert_at_beg(i)
    rev.print_list()
    rev.reverse_iter()
    rev.print_list()
