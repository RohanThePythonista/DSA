from practise.linked_list.single_linked_list.template import *


class DeleteRepeating(HeadTailLinkedList):
    def __init__(self):
        super(DeleteRepeating, self).__init__()

    def delete_repeat(self, curr, deleted=None):
        while curr and curr.next:
            if deleted == curr.data:
                self.delete_single_node(curr.data, self.head)
            prev = curr
            curr = curr.next
            if prev.data == curr.data:
                self.delete_single_node(curr.data, self.head)
                self.delete_repeat(self.head, prev.data)

    def delete_single_node(self, data, head):
        curr = head
        prev = head
        if head and head.data == data:
            self.head = self.head.next
            return
        else:
            while curr and curr.next and curr.data != data:
                prev = curr
                curr = curr.next
            if curr and curr.data == data:
                prev.next = curr.next
                del curr
                return

    def delete_recursive(self, head, curr, deleted=None):
        if not head:
            return
        if not curr:
            return
        if deleted == curr.data:
            deleted = curr.data
            temp = curr.next
            head_is_current = False
            if curr == head:
                head_is_current = True
            del curr
            if head_is_current:
                head = temp
            curr = temp
            self.delete_recursive(head, curr, deleted)
        elif head.next and head.data == head.next.data:
            deleted = head.data
            temp = head.next
            head_is_current = False
            if head == curr:
                head_is_current = True
            del head
            if head_is_current:
                curr = temp
            head = temp
            self.delete_recursive(head, curr, deleted)
        elif curr and curr.next:
            if curr.data == curr.next.data:
                deleted = curr.data
                temp = curr.next
                del curr
                curr = temp
            else:
                deleted = None
                curr = curr.next
            self.delete_recursive(head, curr, deleted)


if __name__ == '__main__':
    ll = DeleteRepeating()
    nodes = [1, 2, 2, 4, 3, 5, 5, 5, 7, 6]
    # nodes = [1, 2, 3, 4, 5, 6]
    for i in nodes:
        ll.insert_at_end(i)
    ll.print_linked_list()
    # ll.delete_nodes()
    # ll.delete_repeat(ll.head)
    ll.delete_recursive(ll.head, ll.head)
    ll.print_linked_list()
