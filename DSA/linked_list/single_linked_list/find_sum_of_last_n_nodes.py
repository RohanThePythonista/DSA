from practise.linked_list.single_linked_list.template import *


class FindSumOfLastNNodes(HeadTailLinkedList):
    """
    This can be done in four ways
    method1: using recursion
        use dummy nodes for passing and strong last n nodes and sum
        recursively traverse to end
        then check on n till it become zero --> and add head.data with sum.data after traversal
    method2: using external stack
        push until last node to stack
        then iterate from n to 0
            -> pop data and keep adding
    method3: reversing ll
        first reverse
        then iterate from n to 0
            --> keep adding data of reversed list
        revers list again to make it original
    method4: using traversing/iterating
        1. find total no. of nodes
        2. traverse to last nth node --->total -n
        3. traverse from nth node to last --->keep adding data
    """
    def __init__(self):
        super(FindSumOfLastNNodes, self).__init__()

    def find_sum_of_last_n_nodes(self, last_n_nodes):
        sum_of_last_n_nodes = 0
        curr = self.head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        last_nth_node = 1
        curr = self.head
        print("N:{}".format(n))
        while last_nth_node != n - last_n_nodes + 1:
            curr = curr.next
            last_nth_node += 1
        print("last_nth_node:{}".format(last_nth_node))
        while curr:
            sum_of_last_n_nodes += curr.data
            curr = curr.next
        return sum_of_last_n_nodes

    def find_sum_recursive(self, head, n, sum_n):
        if not head:
            return
        self.find_sum_recursive(head.next, n, sum_n)
        if n.data > 0:
            sum_n.data += head.data
            n.data -= 1

    def print_rev(self, head):
        if head is None:
            return
        self.print_rev(head.next)
        print(head.data, end=" ")


def arr_sum(arr, n):
    prefix_sum_array = []
    sum_ = 0
    for val in arr:
        sum_ += val
        prefix_sum_array.append(sum_)
    print(prefix_sum_array)
    print(sum(prefix_sum_array[-n:]))


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     n = input()
    #     n_list = list(map(int, input().split()))
    #     k = int(input())
    #     ll = FindSumOfLastNNodes()
    #     for i in n_list:
    #         ll.insert_at_end(i)
    #     print(ll.find_sum_of_last_n_nodes(k))
    # arr = [i for i in range(1, 11, 1)]
    # arr_sum(arr, 3)
    ll = FindSumOfLastNNodes()
    for i in range(1, 11, 1):
        ll.insert_at_end(i)
    ll.print_linked_list()
    dummy_sum = Node(0)
    dummy_n = Node(5)
    ll.find_sum_recursive(ll.head, dummy_n, dummy_sum)
    print(dummy_sum.data)
