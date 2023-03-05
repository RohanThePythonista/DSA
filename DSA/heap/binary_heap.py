"""
Binary heap used in heap sort,
There two types:
    1. MIN heap->highest priority item assigned lowest value
    2. MAX heap->highest priority item assigned highest value
It is complete binary tree
It is typically stored as an array
"""
import sys


class BinaryHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [0 for _ in range(capacity)]

    def insert(self, key):
        # TC:O(log(size))
        if self.is_full() is True:
            print('heap array is full')
            return
        self.size += 1
        self.array[self.size - 1] = key  # insert key as last ele
        i = self.size - 1
        self.maintain_min_heap_property(i)

    def maintain_min_heap_property(self, index):
        while index != 0 and self.array[self.parent(index)] > self.array[index]:
            # swap if parent node > curr node
            self.array[index], self.array[self.parent(index)] = self.array[self.parent(index)], self.array[index]
            index = self.parent(index)

    def min_heapify(self, index: int) -> None:
        # TC, SC: O(h)-->height proportional to log(n)-->n:no, of nodes
        smallest = index
        left = self.left(index)
        right = self.right(index)
        # below two conditions to find smallest from curr node and its children
        if left < self.size and self.array[left] < self.array[index]:
            # first condition is IMP to check if child is exists
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            # first condition is IMP to check if child is exists
            smallest = right
        # check if heapify requires
        if smallest != index:
            # if curr node is not smallest so, swap it with its smallest child node
            self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
            # heapify on smallest to ensure min heap property followed
            self.min_heapify(smallest)

    def max_heapify(self, index: int) -> None:
        # TC, SC: O(h)-->height proportional to log(n)-->n:no, of nodes
        largest = index
        left = self.left(index)
        right = self.right(index)
        # below two conditions to find largest from curr node and its children
        if left < self.size and self.array[left] > self.array[index]:
            # first condition is IMP to check if child is exists
            largest = left
        if right < self.size and self.array[right] > self.array[largest]:
            # first condition is IMP to check if child is exists
            largest = right
        # check if heapify requires
        if largest != index:
            # if curr node is not largest so, swap it with its largest child node
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            # heapify on largest to ensure MAX heap property followed
            self.max_heapify(largest)

    def extract_min(self) -> int:
        # TC, SC: O(h)-->height proportional to log(n)-->n:no, of nodes
        if self.is_empty() is True:
            # if heap is empty return INF
            return sys.maxsize
        if self.size == 1:
            self.size -= 1  # decrease size
            return self.array[0]
        # swap root and last array nodes
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        # decrease size of array
        self.size -= 1
        # perform min heapify on root index 0
        self.min_heapify(0)
        return self.array[self.size]  # swapped root minimum

    def extract_max(self) -> int:
        # TC, SC: O(h)-->height proportional to log(n)-->n:no, of nodes
        if self.is_empty() is True:
            # if heap is empty return INF
            return -sys.maxsize
        if self.size == 1:
            self.size -= 1  # decrease size
            return self.array[0]
        # swap root and last array nodes
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        # decrease size of array
        self.size -= 1
        # perform max heapify on root index 0
        self.max_heapify(0)
        return self.array[self.size]  # swapped root maximum

    def delete(self, index: int) -> None:
        if self.is_empty() is True:
            print('heap is empty')
            return
            # swap index value to be deleted with last ele in array
        self.array[index], self.array[self.size - 1] = self.array[self.size - 1], self.array[index]
        self.size -= 1  # reduce array size
        self.min_heapify(index)

    def decrease_val_at_index_with_given_key(self, index: int, key: int) -> None:
        """
        Decrease a key value at given index
        :param index: int , index of array where key to replaced
        :param key: int, key to be replaced
        :return: None
        """
        self.array[index] = key
        self.maintain_min_heap_property(index)

    def build_min_heap(self) -> None:
        print('build_min_heap')
        i = self.size - 2 // 2  # this is bottom most right most node
        # assumed input array is available
        while i >= 0:
            self.min_heapify(i)
            i -= 1
        print('min heap:{}'.format(self.array[0:self.size]))

    def build_max_heap(self):
        print('build_max_heap')
        # get index of bottom most right most node
        i = (self.size - 2) // 2
        while i >= 0:
            self.max_heapify(i)
            i -= 1
        print('max heap:{}'.format(self.array[0:self.size]))

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def parent(self, index: int) -> int:
        return int(index - 1 / 2)

    def left(self, index: int) -> int:
        return 2 * index + 1

    def right(self, index: int) -> int:
        return 2 * index + 2

    def heap_sort(self):
        pass


if __name__ == '__main__':
    heap = BinaryHeap(20)
    from DSA.template.template import *

    input_array = get_random_array(10, 0, 100)
    for val in input_array:
        heap.insert(val)
    heap.build_min_heap()
    heap.build_max_heap()
