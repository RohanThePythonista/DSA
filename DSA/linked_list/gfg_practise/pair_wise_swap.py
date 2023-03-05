from DSA.linked_list.practise.base import Single_LL


def pair_wise_swap(head):
    if head is None or head.next is None:
        return
    curr = head.next.next
    prev = head
    head = head.next  # update head node first
    prev.next = head.next
    head.next = prev
    while curr and curr.next:  # imp check
        prev.next = curr.next
        prev = curr
        next_ = curr.next.next
        curr.next.next = curr
        curr = next_
    # curr will be null in case even no. of nodes else it is last node
    prev.next = curr  # imp update to update last node with curr node
    return head


if __name__ == '__main__':
    ll = Single_LL()
    for i in range(10, 0, -1):
        ll.insert_at_beg(i)
    ll.print_list()
    ll.head = pair_wise_swap(ll.head)
    ll.print_list()
