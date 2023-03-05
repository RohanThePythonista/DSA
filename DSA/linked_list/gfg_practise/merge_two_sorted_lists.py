from DSA.linked_list.practise.base import Single_LL


def merge_two_sorted_lists(head1, head2):
    new_head = None
    tail = None
    while head1 and head2:
        if new_head is None:
            if head1.data <= head2.data:
                new_head = head1
                tail = head1
                head1 = head1.next
            else:
                new_head = head2
                tail = head2
                head2 = head2.next
        else:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return new_head


def print_sorted_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print('')


if __name__ == '__main__':
    ll = Single_LL()
    for i in [10, 8, 6, 4, 2]:
        ll.insert_at_beg(i)
    ll.print_list()
    ll2 = Single_LL()
    for i in [9, 7, 5, 3, 1]:
        ll2.insert_at_beg(i)
    ll2.print_list()

    sorted_head = merge_two_sorted_lists(ll.head, ll2.head)
    print_sorted_list(sorted_head)
