import random


def get_random_array(length, from_, to_):
    arr = []
    for i in range(length):
        arr.append(random.randint(from_, to_))
    return arr


def get_sequence_arr(length, from_, to_, step=1):
    arr = []
    for i in range(from_, to_, step):
        arr.append(i)
