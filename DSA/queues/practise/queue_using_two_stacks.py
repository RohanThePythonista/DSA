"""
implement queue using two stacks by making enqueue operation costly
implement queue using two stacks by making dequeue operation costly
implement queue using only stack (we can use one recursion call stack here)
"""

from collections import deque

stack = deque()
stack2 = deque()


def enqueue(key):
    print(f'enqueue={key}')
    stack.append(key)


def dequeue():
    """ implement queue using two stacks by making dequeue operation costly """
    while not len(stack2):
        while len(stack):
            stack2.append(stack.pop())
    return stack2.pop()  # blocking call


def enqueue2(key):
    """ implement queue using two stacks by making enqueue operation costly """
    print(f'enqueue={key}')
    while len(stack2):
        stack.append(stack2.pop())
    stack.append(key)
    while len(stack):
        stack2.append(stack.pop())


def dequeue2():
    return stack2.pop()


if __name__ == '__main__':
    for i in range(5):
        enqueue2(i)
    for i in range(5):
        print(f'dequeue={dequeue2()}')
