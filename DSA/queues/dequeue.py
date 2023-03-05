# class Deque:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.items = [0] * capacity
#         self.size = 0
#         self.left_front = -1
#         self.left_rear = -1
#         self.right_front = capacity
#         self.right_rear = capacity
#
#     def add_front(self, item):
#         if self.is_full():
#             print('queue is full')
#             return
#         elif self.left_rear == -1:
#             self.left_front = 0
#         self.left_rear += 1
#         self.items[self.left_rear] = item
#
#     def add_rear(self, item):
#         if self.is_full():
#             print('queue is full')
#             return
#         elif self.right_rear == self.capacity:
#             self.right_front = self.capacity - 1
#         self.right_rear -= 1
#         self.items[self.right_rear] = item
#
#     def remove_front(self):
#         if self.is_empty():
#             print('queue is empty')
#             return
#         if self.left_front == self.left_rear:
#         res = self.items[self.left_front]
#         self.left_front = self.left_front % 1
#         return res
#
#     def remove_rear(self):
#         if self.is_empty():
#             print('queue is empty')
#             return
#
#     def is_empty(self):
#         return self.items == []
#
#     def is_full(self):
#         return self.size == self.capacity
#
#     def get_size(self):
#         return self.size
#
#
# if __name__ == '__main__':
#     d = Deque()
#     d.add_front("rohan")
#     d.add_rear("prachi")
#     print(d.remove_front() + ' ' + d.remove_rear())
