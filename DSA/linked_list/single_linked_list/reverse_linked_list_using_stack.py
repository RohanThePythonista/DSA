class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def reverse(self, stack):
        temp = self.head
        while temp:
            stack.push(temp)
            temp = temp.next
        node = stack.pop()
        self.head = node
        temp2 = self.head
        while not stack.is_empty():
            temp2.next = stack.pop()
            temp2 = temp2.next
        temp2.next = None

    def reverse_iterative(self):
        prev = None
        curr = self.head
        _next = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = _next
            if _next:
                _next = _next.next
        self.head = prev

    def insert_at_end(self, node):
        if not self.head:
            self.head = node
            self.head.next = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node


class Stack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.arr = [0 for _ in range(self.capacity)]

    def push(self, key):
        if not self.is_overflow():
            self.top += 1
            self.arr[self.top] = key

    def pop(self):
        if not self.is_empty():
            popped = self.arr[self.top]
            self.top -= 1
            return popped

    def is_empty(self):
        return self.top == -1

    def is_overflow(self):
        return self.top == self.capacity - 1

    def top_(self):
        if not self.is_empty():
            return self.arr[self.top]

    def print_stack(self):
        temp = self.top
        while temp > -1:
            print(self.arr[self.top], end=" ")
            temp -= 1
        print("\n")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(1)
    ll.insert_at_beg(2)
    ll.insert_at_beg(3)
    ll.insert_at_beg(4)
    ll.insert_at_beg(5)
    ll.print_ll()
    stack_ = Stack(20)
    ll.reverse(stack_)
    ll.print_ll()
