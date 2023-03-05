from collections import deque
import queue

my_stack = deque()
my_queue = queue.Queue()


def reverse_iterative():
    while my_queue.qsize():
        my_stack.append(my_queue.get_nowait())
    while len(my_stack):
        my_queue.put_nowait(my_stack.pop())


def reverse_recursive(given_queue):
    if given_queue.empty():
        return
    x = given_queue.get_nowait()
    reverse_recursive(given_queue)
    given_queue.put_nowait(x)


if __name__ == '__main__':
    for i in range(5):
        my_queue.put_nowait(i)
    for val in my_queue.queue:  # my_queue.queue is deque iterable
        print(val, end=' ')
    print('')
    reverse_recursive(my_queue)
    for val in my_queue.queue:  # my_queue.queue is deque iterable
        print(val, end=' ')
    reverse_iterative()
    print('')
    for val in my_queue.queue:
        print(val, end=' ')
