class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single_LL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, key):
        new_node = Single_LL.get_node(key)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def get_node(key):
        return Node(key)

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.is_empty():
            print('LL is empty')
            return
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print('')


if __name__ == '__main__':
    ll = Single_LL()
    for i in range(5):
        ll.insert_at_beg(i)
    ll.print_list()
