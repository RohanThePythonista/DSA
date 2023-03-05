class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def print_list(head):
        if head is None:
            print(f"Oho!, your list is empty")
            return
        while head.next:
            print(head.data, end=' ')
            head = head.next
        print('')
        while head.prev:
            print(head.data, end=' ')
            head = head.prev
        print('')

    def insert_at_begin(self, key):
        new_node = DoubleLinkedList.get_new_node(key)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def get_new_node(key):
        return Node(key)


if __name__ == "__main__":
    dll = DoubleLinkedList()
    for val in range(5):
        dll.insert_at_begin(val)
    dll.print_list(dll.head)
    dll.print_list(dll.head)
