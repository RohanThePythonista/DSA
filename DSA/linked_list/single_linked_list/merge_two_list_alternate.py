class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print("printing list")
        temp = self.head
        while temp:
            print(str(temp.data) + "-->", end=" ")
            temp = temp.next

    def insert_at_beginning(self, value):
        # print("inserting at beg:{}".format(value))
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        # print("inserting at end:{}".format(value))
        new_node = Node(value)
        temp = self.head
        if not self.head:
            self.head = new_node
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def merger(self, ll_two):
        # TODO: check for diff len of lists and add test cases
        temp = self.head
        while temp.next:
            t2 = temp.next
            temp.next = ll_two.head
            ll_2.head = ll_2.head.next
            temp.next.next = t2
            temp = temp.next.next


if __name__ == '__main__':
    ll_1 = LinkedList()
    i = 10
    ll_2 = LinkedList()
    while i > 5:
        # ll_1.insert_at_beginning(i)
        ll_1.insert_at_end(i)
        i -= 1
    # i = 5
    # while i > 0:
    #     ll_2.insert_at_beginning(i)
    #     i -= 1
    print(ll_1.print_list())
    # print(ll_2.print_list())
    # ll_1.merger(ll_2)
    # print(ll_1.print_list())
