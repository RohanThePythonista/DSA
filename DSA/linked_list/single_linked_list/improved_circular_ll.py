class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular:
    def __init__(self):
        self.tail = None

    def insert_at_beg(self, data):
        if self.is_empty():
            self.tail = Node(data)
            self.tail.next = self.tail
        else:
            new_node = Node(data)
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_at_last(self, data):
        if self.is_empty():
            self.tail = Node(data)
            self.tail.next = self.tail
        else:
            new_node = Node(data)
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = self.tail.next

    def print_list(self, tail):
        if not tail:
            return
        if self.is_empty() is not None:
            head = tail.next
            curr = head
            while curr.next != tail.next:
                print(curr.data, end=" ")
                curr = curr.next
            print(curr.data, end=" ")
        print('')

    def is_empty(self):
        return self.tail is None


if __name__ == '__main__':
    cl = Circular()
    for i in range(1, 6, 1):
        cl.insert_at_last(i)
    for i in range(6, 11, 1):
        cl.insert_at_beg(i)
    cl.print_list(cl.tail)
