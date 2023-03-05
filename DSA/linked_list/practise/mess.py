from DSA.linked_list.practise.base import Single_LL


def reverse_ll(curr):
    prev = None
    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
    return prev


def reverse(head, prev=None):
    if head is None:
        return None
    if head.next is None:
        head.next = prev
        return head
    next_ = head.next
    head.next = prev
    return reverse(next_, head)


if __name__ == '__main__':
    sll = Single_LL()
    for i in range(5):
        sll.insert_at_beg(i)
    sll.print_list()
    sll.head = reverse(sll.head)
    sll.print_list()
