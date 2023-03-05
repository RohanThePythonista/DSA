from DSA.linked_list.practise.base import Single_LL

"""
Naive approach: Using counter and two traversal
    - count all node in list in first traversal
    - then to print middle traverse list till counter/2 nodes
        so it will be middle node
    -in case odd no. of nodes middle will be exact position
    -in case even no. of nodes consider second middle as middle node

Better approach: Using only traversal
    - use two pointer approach while traversing
    - use slow and fast pointer concept
    - update slow ptr by one node every time
    - and update fast ptr by two node every time
    - handle base cases no, 1, 2 nodes in list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)   -->result middle node data
    
"""


def print_middle_node(head):
    if head is None:
        return
    elif head.next is None:
        print(head.data)
        return
    elif head.next.next is None:
        print(head.next.data)
        return
    curr = head
    prev = head
    while curr and curr.next:
        prev = prev.next
        curr = curr.next.next
    print(prev.data)


if __name__ == '__main__':
    sll = Single_LL()
    for i in range(1, 5, 1):
        sll.insert_at_beg(i)
    sll.print_list()
    print_middle_node(sll.head)
