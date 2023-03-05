from DSA.linked_list.practise.base import Single_LL

"""
To print nth node from last node

Naive approach:
    -traverse first for counting no. of nodes in list
    - then again traverse from head till (len - nth + 1) node
        ->print this node 


Better approach
    - use two pointer approach and counter
    - go to nth node from start using fast ptr
        -then start slow ptr from head and keep updating by one node
        -keep traversing until fast traverse till last node
    - when fast ptr reaches tail null node
        slow should be at nth node from last node
    fast = head
    slow = head
    counter = n
    - traverse fast ptr till nth node from head 
    while fast and counter > 0:
        - then once fast ptr reaches nth node,
        fast = fast.next
        counter -= 1
    
    while fast is not none or counter == 0:
            - slow = slow.next 
            - fast = fast.next
    print(slow.data) --->nth node from last
"""


def print_nth_node_from_end_of_ll(head, n):
    if head is None:
        return
    fast = head
    slow = head
    counter = n
    while fast and counter > 0:
        counter -= 1
        fast = fast.next
    if fast or counter == 0:  # IMP to check counter == 0 in case n is __eq__ to no. of nodes
        while fast:
            slow = slow.next
            fast = fast.next
        print(slow.data)
    else:
        print(f"n:{n} is greater than no. of nodes")
        return


if __name__ == '__main__':
    sll = Single_LL()
    for i in range(1, 11, 1):
        sll.insert_at_beg(i)
    sll.print_list()
    print_nth_node_from_end_of_ll(sll.head, 10)
