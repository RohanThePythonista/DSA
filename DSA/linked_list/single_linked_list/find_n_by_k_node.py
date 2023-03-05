from practise.linked_list.single_linked_list.template import *
import math


class FindNode(HeadTailLinkedList):
    def __init__(self):
        super(FindNode, self).__init__()

    # def find_n_k_node(self, n, k):
    #     if self.head is None or k > n:
    #         return
    #     count = int(math.ceil(n / k))
    #     curr = self.head
    #     prev = None
    #     while count:
    #         count -= 1
    #         prev = curr
    #         curr = curr.next
    #     return prev.data

    def find_n_k_node(self, k):
        ctr = 1
        slow = fast = self.head
        while fast.next:
            fast = fast.next
            if ctr % k == 0:
                slow = slow.next
            ctr += 1
        return slow.data

    def find_n_k(self, k):
        curr = self.head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        curr = self.head
        if n % k == 0:
            f = n // k
        else:
            f = n // k
            f += 1
        for _ in range(f-1):
            curr = curr.next
        return curr.data


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n_list = list(map(int, input().split()))
        k = int(input())
        ll = FindNode()
        for i in n_list:
            ll.insert_at_end(i)
        print(ll.find_n_k_node(k))
