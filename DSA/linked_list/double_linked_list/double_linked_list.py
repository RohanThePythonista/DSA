class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.data = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def print_reverse(self):
        if not self.head:
            return
        elif not self.head.next:
            print(self.head.data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print("\n")


if __name__ == "__main__":
    d_ll = DoubleLinkedList()
    d_ll.insert_at_beg(1)
    d_ll.insert_at_beg(2)
    d_ll.insert_at_beg(3)
    d_ll.insert_at_beg(4)
    d_ll.insert_at_beg(5)
    d_ll.print_list()
    d_ll.print_reverse()
