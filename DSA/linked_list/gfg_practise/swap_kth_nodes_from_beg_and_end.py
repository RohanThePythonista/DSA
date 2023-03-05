from DSA.linked_list.practise.base import Single_LL


def swap_kth_nodes(head, k, n):
    curr = head
    # if k > n or odd nodes and k is middle of list
    if k > n or k == n // 2 + 1:
        return head
    elif k == n:  # swap first and last node links
        tail_prev = None
        while curr.next:
            tail_prev = curr
            curr = curr.next
        end_next = head.next
        tail_prev.next = head
        tail_prev.next.next = None
        head = curr
        head.next = end_next
        return head
    else:
        kth_start_prev, kth_start = get_kth_node_from_beg(head, k)
        kth_end_prev, kth_end = get_kth_node_from_end(head, k)
        if kth_start_prev is None:
            temp = head
            next_ = head.next
            head = kth_end
            kth_end.next = next_
            kth_end_prev.next = temp
            temp.next = None
            return head
        print(kth_start_prev.data, kth_start.data)
        print(kth_end_prev.data, kth_end.data)

        start_next = kth_start.next
        end_next = kth_end.next

        if kth_start == kth_end_prev:
            kth_start_prev.next = kth_end
            kth_end.next = kth_start
            kth_start.next = end_next
            return head

        kth_start_prev.next.next = start_next
        kth_end_prev.next.next = end_next

        kth_end_prev.next = kth_start
        kth_start.next = end_next

        kth_start_prev.next = kth_end
        kth_end.next = start_next
        return head


def get_kth_node_from_beg(head, k):
    prev = None
    for _ in range(k - 1):
        prev = head
        head = head.next
    if prev is None:
        return None, head
    return prev, head


def get_kth_node_from_end(head, k):
    curr = head
    for _ in range(k - 1):
        curr = curr.next
    last = head
    prev = None
    while curr.next:
        prev = last
        last = last.next
        curr = curr.next
    return prev, last


if __name__ == '__main__':
    ll = Single_LL()
    n = 10
    for i in range(n, 0, -1):
        ll.insert_at_beg(i)
    ll.print_list()
    k = 1
    ll.head = swap_kth_nodes(ll.head, k, n)
    ll.print_list()
