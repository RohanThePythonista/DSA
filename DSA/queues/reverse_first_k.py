def reverseK(queue, k, n):
    # print(queue, type(queue))
    # return queue
    queue = list(reversed(queue))
    stack = list()
    for _ in range(n - k):
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue

s = ''
# for i in ['1','3','5']:
s = ''.join()
