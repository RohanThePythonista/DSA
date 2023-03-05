class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # NULL value


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        temp = self.head
        if not self.head:
            # when inserting first time when head in null
            self.head = new_node
            new_node.next = self.head
            return
        else:
            # to update last node with new node ref
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        temp = self.head
        if not temp:
            self.head = new_node
            temp = new_node
        else:
            while temp.next != self.head:
                temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def print_list(self):
        print("printing list")
        if self.is_empty():
            print("List is empty")
            return
        temp = self.head
        while temp.next != self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data, end=" ")  # to print last node value
        print("\n")

    def is_circular(self):
        temp = self.head
        if self.is_empty():
            print("List is empty")
            return
        while temp.next != self.head:
            temp = temp.next
        print("is circular")
        """
            For cyclic chain checking
            we can use slow and fast ptr to traverse through linked list 
            if slow and fats ptr pts same node then it is cyclic list
        """

    def mid_point(self):
        slow = self.head
        fast = self.head
        if self.is_empty() or self.head == self.head.next or self.head == self.head.next.next:
            print("either LL is empty or has 2 or less nodes")
            return
        else:
            while fast.next != self.head:
                slow = slow.next
                fast = fast.next.next
                if fast.next.next == self.head:
                    # for even condition
                    break
        print("MID:{}".format(slow.data))

    def is_empty(self):
        return not self.head

    def delete_from_beg(self):

        if self.is_empty():
            print("List is empty")
            return
        elif self.head == self.head.next:
            # LL has only node
            del self.head
            self.head = None
        else:
            save_second_node = self.head.next
            temp = self.head
            while temp.next != self.head:
                # to update last node with head
                temp = temp.next
            del self.head
            self.head = save_second_node
            temp.next = self.head


if __name__ == "__main__":
    c_ll = LinkedList()
    # c_ll.insert_at_beginning(1)
    # c_ll.insert_at_beginning(2)
    # c_ll.insert_at_beginning(3)
    # c_ll.insert_at_beginning(4)
    # c_ll.insert_at_beginning(5)
    # c_ll.print_list()
    #
    # c_ll.insert_at_end(6)
    # c_ll.insert_at_end(7)
    # c_ll.insert_at_end(8)
    c_ll.insert_at_end(9)
    c_ll.insert_at_end(10)
    c_ll.print_list()

    c_ll.delete_from_beg()
    c_ll.delete_from_beg()
    c_ll.delete_from_beg()
    # c_ll.delete_from_beg()
    # c_ll.delete_from_beg()
    c_ll.print_list()
