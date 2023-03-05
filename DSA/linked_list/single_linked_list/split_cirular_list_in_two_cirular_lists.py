from practise.linked_list.single_linked_list.improved_circular_ll import *


class SplitCircular(Circular):
    """
    Given a Cirular Linked List split it into two halves circular lists.
    If there are odd number of nodes in the given circular linked list
    then out of the resulting two halved lists,
    first list should have one node more than the second list.
    The resultant lists should also be circular lists and not linear lists.
    """

    def __init__(self):
        super(SplitCircular, self).__init__()

    def split_sequence_in_two_halves(self):
        first_circular_tail = None
        second_circular_tail = None
        if not self.tail:
            return first_circular_tail, second_circular_tail
        elif self.tail.next == self.tail:
            return first_circular_tail, second_circular_tail
        elif self.tail.next == self.tail.next.next.next:
            if first_circular_tail is None:
                first_circular_tail = Node(self.tail.next.data)
                first_circular_tail.next = first_circular_tail
            if second_circular_tail is None:
                second_circular_tail = Node(self.tail.next.next.data)
                second_circular_tail.next = second_circular_tail
            return first_circular_tail, second_circular_tail
        slow = fast = self.tail.next
        while fast and fast.next:
            if fast.next.next == self.tail.next:
                # even nodes
                fast = fast.next
                break
            elif fast.next.next == self.tail:
                # odd nodes
                fast = fast.next.next
                slow = slow.next
                break
            slow = slow.next
            fast = fast.next.next
        # print(slow.data, fast.data)
        first_last = slow
        head = self.tail.next
        while head != first_last:
            if first_circular_tail is None:
                first_circular_tail = Node(head.data)
                first_circular_tail.next = first_circular_tail
            else:
                new_node = Node(head.data)
                new_node.next = first_circular_tail.next
                first_circular_tail.next = new_node
                first_circular_tail = first_circular_tail.next
            head = head.next
        new_node = Node(head.data)
        new_node.next = first_circular_tail.next
        first_circular_tail.next = new_node
        first_circular_tail = first_circular_tail.next

        slow = slow.next
        while slow != self.tail.next:
            if second_circular_tail is None:
                second_circular_tail = Node(slow.data)
                second_circular_tail.next = second_circular_tail
            else:
                new_node = Node(slow.data)
                new_node.next = second_circular_tail.next
                second_circular_tail.next = new_node
                second_circular_tail = second_circular_tail.next
            slow = slow.next
        return first_circular_tail, second_circular_tail

    def split_alternate(self, tail, first_circular_tail_dummy, second_circular_tail_dummy):
        first_circular_tail = None
        second_circular_tail = None
        head = self.tail.next
        curr = head
        first = True
        second = False
        while curr.next != head:
            if first is True:
                print("FIRST:{}".format(curr.data))
                first = False
                second = True
                if first_circular_tail is None:
                    first_circular_tail = Node(curr.data)
                    first_circular_tail.next = first_circular_tail
                else:
                    new_node = Node(curr.data)
                    new_node.next = first_circular_tail.next
                    first_circular_tail.next = new_node
                    first_circular_tail = first_circular_tail.next
            elif second is True:
                print("SECOND:{}".format(curr.data))
                second = False
                first = True
                if second_circular_tail is None:
                    second_circular_tail = Node(curr.data)
                    second_circular_tail.next = second_circular_tail
                else:
                    new_node = Node(curr.data)
                    new_node.next = second_circular_tail.next
                    second_circular_tail.next = new_node
                    second_circular_tail = second_circular_tail.next
            curr = curr.next
        if first:
            print("FIRST:{}".format(curr.data))
            new_node = Node(curr.data)
            new_node.next = first_circular_tail.next
            first_circular_tail.next = new_node
            first_circular_tail = first_circular_tail.next
        else:
            new_node = Node(curr.data)
            new_node.next = second_circular_tail.next
            second_circular_tail.next = new_node
            second_circular_tail = second_circular_tail.next
        first_circular_tail_dummy.next = first_circular_tail
        second_circular_tail_dummy.next = second_circular_tail


if __name__ == '__main__':
    split = SplitCircular()
    for i in range(1, 3, 1):
        split.insert_at_last(i)
    split.print_list(split.tail)
    first_circular_tail, second_circular_tail = split.split_sequence_in_two_halves()
    split.print_list(first_circular_tail)
    split.print_list(second_circular_tail)
    # dummy1 = Node(-1)
    # dummy2 = Node(-1)
    # split.split_alternate(split.tail, dummy1, dummy2)
    # first_list = dummy1.next
    # second_list = dummy2.next
    # split.print_list(first_list)
    # split.print_list(second_list)
"""
void splitList(Node *head, Node **head1_ref, Node **head2_ref)

"""

"""
split alternate 
void splitList(Node *head, Node **first_circular_tail, Node **second_circular_tail)
{
    if(head == NULL){
        return;
    }
    Node *curr = head;
    int first = 1;
    int second = 0;
    while (curr->next != head){
        if(first == 1){
            first = 0;
            second = 1;
            if(*first_circular_tail == NULL){
                    *first_circular_tail = new Node(curr->data);
                    (*first_circular_tail)->next = *first_circular_tail;
            }
            else {
                struct Node *new_node = new Node(curr->data);
                new_node->next = (*first_circular_tail)->next;
                (*first_circular_tail)->next = new_node;
                *first_circular_tail = (*first_circular_tail)->next;
            }
        }
        else if(second == 1){
            first = 1;
            second = 0;
            if(*second_circular_tail == NULL){
                    *second_circular_tail = new Node(curr->data);
                    (*second_circular_tail)->next = *second_circular_tail;
            }
            else {
                struct Node *new_node = new Node(curr->data);
                new_node->next = (*second_circular_tail)->next;
                (*second_circular_tail)->next = new_node;
                *second_circular_tail = (*second_circular_tail)->next;
            }
        }
     curr = curr->next;   
    }
    if(first == 1){
        struct Node *new_node = new Node(curr->data);
        new_node->next = (*first_circular_tail)->next;
        (*first_circular_tail)->next = new_node;
        *first_circular_tail = (*first_circular_tail)->next;
    }
    else{
        struct Node *new_node = new Node(curr->data);
        new_node->next = (*second_circular_tail)->next;
        (*second_circular_tail)->next = new_node;
        *second_circular_tail = (*second_circular_tail)->next;
    }
    *second_circular_tail = (*second_circular_tail)->next;
    *first_circular_tail = (*first_circular_tail)->next;
}

"""
"""
spilt sequence
void splitList(Node *head, Node **first_circular_tail, Node **second_circular_tail)
{
    if(head == NULL){
        return;
    }
    else if( head == head->next->next){
        insertFirstTime(first_circular_tail, head->data);
        insertFirstTime(second_circular_tail, head->next->data);
        return;
    }
    Node *slow = head;
    Node *fast = head;
    Node *tail_original = head;
    while(tail_original->next != head){
        tail_original = tail_original->next;
    } 
    while( fast && fast->next){
        if( fast->next->next == head){
                // even nodes
                fast = fast->next;
                break;
        }
        else if( fast->next->next == tail_original){
                // odd nodes
                fast = fast->next->next;
                slow = slow->next;
                break;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    Node * first_last = slow;
    Node * start = head;    

    //start building  first list
    while(start != first_last){
        if(*first_circular_tail == NULL){
            insertFirstTime(first_circular_tail, start->data);
        }
        else{
            insertAtLast(first_circular_tail, start->data);
        }    
        start = start->next;
    }
    insertAtLast(first_circular_tail, start->data);
    
    //start building second list
    slow = slow->next;
    while(slow != head){
        if(*second_circular_tail == NULL){
            insertFirstTime(second_circular_tail, slow->data);
        }
        else{
            insertAtLast(second_circular_tail, slow->data);
        }
        slow = slow->next;            
    }
    *second_circular_tail = (*second_circular_tail)->next;
    *first_circular_tail = (*first_circular_tail)->next;
}

void insertAtLast(Node **tail, data){
        struct Node *new_node = new Node(data);
        new_node->next = (*tail)->next;
        (*tail)->next = new_node;
        *tail = (*tail)->next;    
}

void insertFirstTime(Node **tail, data){
    *tail = new Node(curr->data);
    (*tail)->next = *tail;
}
"""
