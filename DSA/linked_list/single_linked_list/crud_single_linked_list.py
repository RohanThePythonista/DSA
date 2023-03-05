class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # NULL value


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print("printing list")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def insert_at_beginning(self, value):
        print("inserting at beg:{}".format(value))
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        print("inserting at end:{}".format(value))
        if not self.head:
            self.head = Node(value)
            return
        cur = self.head

        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def insert_after_given_node_value(self, given_value, new_value):
        pass

    def find_mid_value_in_list(self):
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Mid pt of list:{}".format(slow.data))


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(5):
        linked_list.insert_at_beginning(i)
    linked_list.print_list()
    # for i in range(6):
    #     linked_list.insert_at_end(i)
    # linked_list.print_list()
    linked_list.find_mid_value_in_list()
