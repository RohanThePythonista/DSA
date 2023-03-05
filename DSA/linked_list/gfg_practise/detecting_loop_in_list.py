"""
Naive approaches:

Using two loops:

    for each node in list:
        from start to curr each node:
            check curr node is its next node


using modified Node structure using visited field in each node
    traverse list and mark each curr node as visited
        while traversing check if curr node is already visited
            then return True
    else return False

Using dummy node and changing links to point dummy node
dummy_node = Node()
traverse list
    for each node point its next node to new dummy node
        if curr.next is None:
            return False
        check if curr next is already pointing to this dummy node curr.next == dummy_node:
            return True
        next_ = curr.next  # hold curr next before pointing it to dummy node
        curr.next = dummy_node
        curr = next_  # update to next node in list

Using hashing: TC O(n)
        traverse list from start
            check if curr node's next is present in hash
                loop is detected
            else:
                add curr node to hash map
                move to next node

Better approach:
Using floyd's algorithm
    -use two ptrs to traverse
    -initialize slow = fast = head
    -idea is to move fast ptr by two positions and slow by one position
    -this algorithm proves that slow and fast ptrs meets at second last node of loop if exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

"""


def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_len_of_loop(head):
    if head == head.next:
        return True, 1
    slow = fast = head
    counter = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            while slow != fast:
                counter += 1
                slow = slow.next
            return True, counter
    return False, counter
