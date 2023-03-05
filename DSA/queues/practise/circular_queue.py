class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [-1]*capacity
        self.front = 0
        self.size = 0

    def dequeue(self):
        if self.is_empty():
            print(f'queue is empty')
            return
        res = self.queue[self.front]
        self.front = (self.front+1) % self.capacity
        self.size -= 1
        return res

    def enqueue(self, key):
        if self.is_full():
            print(f'queue is full')
            return
        rear = self.get_rear()
        rear = (rear + 1) % self.capacity
        self.queue[rear] = key
        self.size += 1

    def is_full(self):
        return self.capacity == self.size

    def is_empty(self):
        return self.size == 0

    def get_rear(self):
        if self.is_empty():
            return -1
        return (self.front + self.size - 1) % self.capacity


if __name__ == '__main__':
    que = CircularQueue(5)
    for i in range(7):
        que.enqueue(i)
    for i in range(7):
        print(que.dequeue())
