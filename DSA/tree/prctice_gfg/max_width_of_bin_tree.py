import queue

aux_queue = queue.Queue()


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def get_max_width(root):
    if not root:
        return 0
    aux_queue.put_nowait(root)
    res = 0
    while not aux_queue.empty():
        count = aux_queue.qsize()
        res = max(res, count)
        for _ in range(count):
            curr = aux_queue.get_nowait()
            if curr.left:
                aux_queue.put_nowait(curr.left)
            if curr.right:
                aux_queue.put_nowait(curr.right)
    return res


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.right = Node(60)
    print(get_max_width(root))
