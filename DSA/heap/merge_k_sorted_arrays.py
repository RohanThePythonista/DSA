"""
Given k sorted arrays.
Create a new sorted array by merging given arrays

Method 1: Naive approach
    Use sorting algorithm

Method 2: Better solution
    Use binary heap(min heap)
    1. Create an output array of size n*k
    2. Create a min heap of size k and insert 1st element in all the arrays into the heap
    3. Repeat following steps n*k times
     a) Get minimum element from heap (minimum is always at root) and store it in output array.
     b) Replace heap root with next element from the array from which the element is extracted.
        If the array doesn’t have any more elements, then replace root with infinite.
        After replacing the root, heapify the tree.
     TC: O(nk Log k)
"""
from queue import PriorityQueue
from typing import List, Optional

Matrix = List[List[int]]


class MinHeapNode:
    def __init__(self, ele, i, j):
        self.element = ele  # the element to be sorted
        self.i = i  # index of array from which element is taken
        self.j = j  # index of next element to be picked from array


class MinHeap:
    def __init__(self, arr: List[MinHeapNode], size: int):
        self.pq = PriorityQueue()
        self.size = size
        self.array = arr
        self.build_mean_heap(self.size)

    def build_mean_heap(self, heap_size):
        i = heap_size - 2 // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def min_heapify(self, index: int):
        smallest = index
        left_child_index = self.left_child_of_parent_index(index)
        right_child_index = self.right_child_of_parent_index(index)
        if left_child_index < self.size and self.array[left_child_index].element < self.array[index].element:
            smallest = left_child_index
        if right_child_index < self.size and self.array[right_child_index].element < self.array[smallest].element:
            smallest = right_child_index
        if smallest != index:
            self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
            self.min_heapify(smallest)

    def parent_index_of_child_index(self, index: int) -> int:
        return int(index - 1 / 2)

    def left_child_of_parent_index(self, index: int) -> int:
        return 2 * index + 1

    def right_child_of_parent_index(self, index: int) -> int:
        return 2 * index + 2

    def get_min(self) -> Optional:
        if self.size > 0:
            return self.array[0]

    # Replace root with new root
    def replace_min(self, root):
        self.array[0] = root
        self.min_heapify(0)


def merge_k_sorted_arrays(input_arr: Matrix, k: int):
    heap_array = []
    result_size = 0
    for i in range(len(input_arr)):
        node = MinHeapNode(input_arr[i][0], i, 1)
        heap_array.append(node)
        result_size += len(input_arr[i])

    min_heap = MinHeap(heap_array, k)
    output_array = [0] * result_size
    # TODO


if __name__ == '__main__':
    pass
