from practise.linked_list.single_linked_list.template import *


class InsertAtMiddle(HeadTailLinkedList):
    def __init__(self):
        super(InsertAtMiddle, self).__init__()

    # def insert_at_middle(self, data, len_of_list):
    #     slow = self.head
    #     fast = self.head
    #     prev_slow = None
    #     while fast and fast.next:
    #         prev_slow = slow
    #         slow = slow.next
    #         fast = fast.next.next
    #     if len_of_list % 2 == 0:
    #         temp = prev_slow.next
    #         prev_slow.next = Node(data)
    #         prev_slow.next.next = temp
    #     else:
    #         temp = slow.next
    #         slow.next = Node(data)
    #         slow.next.next = temp

    def insert_at_middle(self, data):
        if self.head.next is None:
            """
            if only head exists
            """
            self.head.next = Node(data)
            return
        slow = self.head
        fast = self.head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if fast is None:
            """
            even no of nodes in list
            insert after first middle
            """
            temp = prev_slow.next
            prev_slow.next = Node(data)
            prev_slow.next.next = temp
        else:
            """
            odd no of nodes
            insert after middle 
            """
            temp = slow.next
            slow.next = Node(data)
            slow.next.next = temp


if __name__ == '__main__':
    if __name__ == '__main__':
        t = int(input())
        for _ in range(t):
            n = input()
            n_list = list(map(int, input().split()))
            data = int(input())
            ll = InsertAtMiddle()
            for i in n_list:
                ll.insert_at_end(i)
            ll.print_linked_list()
            ll.insert_at_middle(data)
            ll.print_linked_list()
