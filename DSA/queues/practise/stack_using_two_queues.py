"""
implement stack using two queues by making push operation costly
implement stack using two queues by making pop operation costly
implement stack using only queue (we can use recursion call stack here)
"""
import queue

my_queue = queue.Queue()
my_queue2 = queue.Queue()


def push(key):
    """ implement stack using two queues by making push operation costly """
    while my_queue.qsize():
        my_queue2.put_nowait(my_queue.get_nowait())
    my_queue.put_nowait(key)
    while my_queue2.qsize():
        my_queue.put_nowait(my_queue2.get_nowait())


def pop():
    res = -1
    try:
        res = my_queue.get_nowait()
    except queue.Empty:
        pass
    return res


def push2(key):
    """ implement stack using two queues by making pop operation costly """
    my_queue.put_nowait(key)


def pop2():
    res = -1
    try:
        if not my_queue2.qsize():
            while my_queue.qsize() and my_queue.qsize() != 1:
                my_queue2.put_nowait(my_queue.get_nowait())
        res = my_queue.get_nowait()
        while my_queue2.qsize():
            my_queue.put_nowait(my_queue2.get_nowait())
    except queue.Empty:
        pass
    return res


if __name__ == '__main__':
    for i in range(5):
        push(i)
    for i in range(7):
        print(f"pop:{pop()}")
