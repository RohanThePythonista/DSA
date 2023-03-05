class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beg(self, value):
        new_node = Node(value)
        if not self.head:
            self.tail = new_node
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, value):
        new_node = Node(value)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_last(1)
    ll.insert_at_last(2)
    ll.insert_at_last(3)
    ll.insert_at_last(4)
    ll.insert_at_last(5)
    ll.insert_at_beg(11)
    ll.insert_at_beg(12)
    ll.insert_at_beg(13)
    ll.insert_at_beg(14)
    ll.insert_at_beg(15)
    ll.print_list()
