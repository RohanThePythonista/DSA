class BinaryHeapBase:
    def __init__(self):
        self.size = 0
        self.array = []

    @staticmethod
    def parent(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def left_child(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def right_child(index: int) -> int:
        return 2 * index + 2

    def build_min_heap(self, input_array):
        n = len(input_array)
        self.array = input_array[:]
        self.size = n
        i = n - 2 // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def build_max_heap(self, input_array):
        n = len(input_array)
        self.array = input_array[:]
        self.size = n
        i = n - 2 // 2
        while i >= 0:
            self.max_heapify(i)
            i -= 1

    def min_heapify(self, index):
        smallest = index
        left = BinaryHeapBase.left_child(index)
        right = BinaryHeapBase.left_child(index)
        if left < self.size and self.array[index] > self.array[left]:
            smallest = left
        if right < self.size and self.array[smallest] > self.array[right]:
            smallest = right
        if smallest != index:
            self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
            self.min_heapify(smallest)

    def max_heapify(self, index):
        largest = index
        left = BinaryHeapBase.left_child(index)
        right = BinaryHeapBase.left_child(index)
        if left < self.size and self.array[index] < self.array[left]:
            largest = left
        if right < self.size and self.array[largest] < self.array[right]:
            largest = right
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.max_heapify(largest)

    def is_empty(self) -> bool:
        return self.size == 0
