import queue

my_queue = queue.Queue()


def print_n_nos(n):
    my_queue.put('5')
    my_queue.put('6')
    for _ in range(n):
        key = my_queue.get_nowait()
        print(key, end=' ')
        my_queue.put(key + '5')
        my_queue.put(key + '6')


if __name__ == '__main__':
    print_n_nos(10)
