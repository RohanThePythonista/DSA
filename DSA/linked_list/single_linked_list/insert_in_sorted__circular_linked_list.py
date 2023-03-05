from practise.linked_list.single_linked_list.improved_circular_ll import *


class InsertInCircularSortedList(Circular):
    def __init__(self):
        super(InsertInCircularSortedList, self).__init__()

    def sorted_insert(self, data):
        if self.is_empty():
            self.insert_at_beg(data)
        elif data <= self.tail.next.data:
            self.insert_at_beg(data)
        elif data >= self.tail.data:
            self.insert_at_last(data)
        else:
            head = self.tail.next
            curr = head
            prev = head
            while curr.data <= data:
                prev = curr
                curr = curr.next
            new_node = Node(data)
            prev.next = new_node
            new_node.next = curr


if __name__ == '__main__':
    cl = InsertInCircularSortedList()
    from practise.arrays.template import *

    array = get_random_array(10, 0, 101)
    for i in array:
        cl.sorted_insert(i)
    cl.print_list(cl.tail)
    cl.sorted_insert(-1)
    cl.print_list(cl.tail)
    cl.sorted_insert(103)
    cl.print_list(cl.tail)


"""
void insertAtFirst(Node** tail, int data);
void insertAtLast(Node** tail, int data);
void sortedInsert(Node** head, int data)
{
    Node* tail = NULL;
    Node* curr = NULL;
    if(head == NULL){
        insertAtFirst(&tail, data);
        return;
    }
    curr = *head;
    while(curr->next != *head){
        curr = curr->next;
    }
    tail = curr;
    if(data <= (*head)->data){
        insertAtFirst(&tail, data);
        *head = tail->next;
    }
    else if(data >= (tail)->data){
        insertAtLast(&tail, data);
    }
    else{
        Node* curr = *head;
        Node* prev = *head;
        while(curr->data <= data){
            prev = curr;
            curr = curr->next;
            
        }
            Node* new_node = new Node(data);
            prev->next = new_node;
            new_node->next = curr;
        }
    }

void insertAtFirst(Node** tail, int data){
    if(*tail == NULL){
        *tail = new Node(data);
        (*tail)->next = *tail;
    }
    else{
        Node* new_node = new Node(data);
        new_node->next = (*tail)->next;
        (*tail)->next = new_node;
    }
        
    }
void insertAtLast(Node **tail, int data){
    if(*tail == NULL){
        *tail = new Node(data);
        (*tail)->next = *tail;
    }
    else{
        Node * new_node = new Node(data);
        new_node->next = (*tail)->next;
        (*tail)->next = new_node;
    }
}


//https://ide.geeksforgeeks.org/dCxUYLJAa9
"""