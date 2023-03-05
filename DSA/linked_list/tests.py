class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, value):
        new_node = SingleLinkedList.get_new_node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + "-->", end=" ")
            temp = temp.next
        print("\n")

    def insert_at_end(self, value):
        temp = self.head
        new_node = SingleLinkedList.get_new_node(value)
        if not temp:
            print("Inserting first time node")
            self.head = new_node
            return
        while temp.next:
            # travers and go to last node
            temp = temp.next
        temp.next = new_node

    @staticmethod
    def get_new_node(value):
        return Node(value)

    def delete_from_beg(self):
        if self.head:
            temp = self.head.next
            self.head = temp
            del temp

    def delete_from_end(self):
        temp = self.head
        prev = None
        while temp and temp.next:
            prev = temp
            temp = temp.next
        if prev:
            prev.next = None
        del temp

    def delete_from_n_position(self, n):
        if n <= 0 or not self.head:
            return
        if n == 1:
            self.delete_from_beg()
            return
        temp = self.head
        prev = None
        for i in range(n - 1):
            if temp:
                prev = temp
                temp = temp.next
            if not temp:
                print("List has less no. of nodes than given value")
                return
        prev.next = temp.next
        del temp

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

    def print_recursive_forward(self, head):
        if not head:
            return
        print(head.data, end=" ")
        self.print_recursive_forward(head=head.next)

    def print_recursive_reverse(self, head):
        if not head:
            return
        self.print_recursive_reverse(head=head.next)
        print(head.data, end=" ")


"""
1->2->3->4->5->None
1.
    actual
        prev = None 
        curr = 1    
        next = 2   
                
    expectation
        prev = 1 prev = 2 prev = 3 prev = 4     prev = None 
        curr = 2 curr = 3 curr = 4 curr = 5     curr = None 
        next = 3 next = 4 next = 5 next = None  next = None 
    
"""

if __name__ == "__main__":
    # linked_list = SingleLinkedList()
    # linked_list.insert_at_end(1)
    # linked_list.insert_at_end(2)
    # linked_list.insert_at_end(3)
    # linked_list.insert_at_end(4)
    # linked_list.insert_at_end(5)
    # linked_list.print_list()
    # linked_list.reverse_iterative()
    # linked_list.print_list()
    # linked_list.print_recursive_forward(linked_list.head)
    # print("\n")
    # linked_list.print_recursive_reverse(linked_list.head)

    def print_forward(i):
        if i == 5:
            return
        print(i, end=" ")
        print_forward(i + 1)


    def print_reverse(i):
        if i == 5:
            return i
        i = i + 1
        print_forward(i)
        print(i, end=" ")


    print_reverse(1)
