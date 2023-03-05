from practise.linked_list.single_linked_list.template import *


class FindModularNode(HeadTailLinkedList):
    """
    basically we have to find data at index ....where index is largest multiple of given k
    method1: iterative
        index = 1
        traverse till last node
            >save data if curr index multiple of k ...i.e. index%k ==0
            index += 1
    method2: same as above using recursion
    """

    def __init__(self):
        super(FindModularNode, self).__init__()

    def find_modular(self, k):
        fast = self.head
        ctr = 1
        data = -1
        while fast:
            print("ctr:{}".format(ctr))
            if ctr % k == 0:
                data = fast.data
                print("ctr:{} data:{}".format(ctr, data))
            fast = fast.next
            ctr += 1
        return data

    def find_modular_recursive(self, head, k, index=1, result=-1):
        if head is None:
            return result
        if index % k == 0:
            result = head.data
        return self.find_modular_recursive(head.next, k, index + 1, result)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n_list = list(map(int, input().split()))
        k = int(input())
        ll = FindModularNode()
        for i in n_list:
            ll.insert_at_end(i)
        print(ll.find_modular(k))
        # print(ll.find_modular_recursive(ll.head, k))
