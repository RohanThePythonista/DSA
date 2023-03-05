"""
Check if given input array is min heap array.
Min heap:
    root is minimum of all nodes.
    each node value is smallest than its children
"""


def is_min_heap(input_heap_array: list):
    n = len(input_heap_array)
    if n == 1:
        return True
    elif n == 0:
        return False
    for i in range(n):
        l = left(i)
        r = right(i)
        if l < n and input_heap_array[l] < input_heap_array[i]:
            return False
        if r < n and input_heap_array[r] < input_heap_array[i]:
            return False
    return True


def parent(index: int) -> int:
    return index - 1 // 2


def left(index: int) -> int:
    return 2 * index + 1


def right(index: int) -> int:
    return 2 * index + 2


if __name__ == '__main__':
    arr = [10, 15, 14, 25, 30]
    print(is_min_heap(arr))
