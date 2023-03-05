"""
Method 1: Using list : not thread safe
Method 2: Using collections.deque
            only append and pop are atomic for thread safety and others are not,
            doesn't give indexing capability so faster than list implementation
Method 2: Using queue.LifoQueue :
            all operations(put, get and others) are thread safe so slight overhead

Applications:
    1. Function calls : executed in LIFO order
    2. Checking for balanced parenthesis : string of parenthesis
    3. Reversing items in sequence
    4. Infix to prefix/postfix conversion
    5. Evaluation of prefix/postfix expressions
    6. Undo/redo or forward/backward ---> IMP in problems
    7. Stock span problem and its variations ---> MOST IMP in stack problems
"""

from collections import deque

stack = deque()


def push(key):
    stack.append(key)


def pop():
    return stack.pop()


if __name__ == '__main__':
    for i in range(10):
        push(i)
    for i in range(10):
        print(pop())
