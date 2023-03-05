queue_1 = []
queue_2 = []
"""
Assume two queue's q1 & q2.
makes sure that newly entered element is always at the front of ‘q1’.
pop operation just dequeues from ‘q1’.
‘q2’ is used to put every new element at front of ‘q1’.



//x is the element to be pushed and s is stack
push(s, x): 
1) Enqueue x to q2
2) One by one dequeue everything from q1 and enqueue to q2.
3) Swap the names of q1 and q2
// Swapping of names is done to avoid one more movement of all elements from q2 to q1.

pop(s):
1) Dequeue an item from q1 and return it.
"""


def push_in_stack(x):
    # global declaration
    global queue_1
    global queue_2
    queue_2.insert(0, x)
    while queue_1:
        queue_2.insert(0, queue_1.pop())
    queue_1, queue_2 = queue_2, queue_1
    # code here


def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''

    # global declaration
    global queue_1
    global queue_2
    if queue_1:
        return queue_1.pop()
    return -1
    # code here


def push(key):
    global queue_1
    global queue_2
    queue_2.append(key)
    while queue_1:
        queue_2.insert(0, queue_1.pop())
    queue_1, queue_2 = queue_2, queue_1


def pop():
    global queue_1
    global queue_2
    return queue_1.pop()


if __name__ == '__main__':
    # push_in_stack(2)
    push(2)
    # push_in_stack(3)
    push(3)
    # print(pop_from_stack())
    print(pop())
    # push_in_stack(4)
    push(4)
    # print(pop_from_stack())
    print(pop())
