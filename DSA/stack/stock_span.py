def naive_stock_span(array):
    i = 0
    j = 0
    n = len(array)
    while i < n:
        j = i - 1
        span = 1
        while j >= 0:
            if array[j] <= array[i]:
                span += 1
            else:
                break
            j -= 1
        print(span, end=" ")
        i += 1


def stock_span(array):
    """
    :param array:
    :return:
    """
    n = len(array)
    stack = list()
    stack.append(0)
    i = 1
    while i < n:
        while len(stack) != 0 and array[stack[-1]] <= array[i]:
            stack.pop()
        span = i + 1 if len(stack) == 0 else i - stack[-1]
        stack.append(i)
        print(span, end=" ")
        i += 1


if __name__ == '__main__':
    from practise.arrays.template import *

    # arr = get_random_array(10, 1, 31)
    arr = [15, 13, 12, 17, 14, 16, 8, 6, 4, 10, 30]
    stock_span(arr)
    naive_stock_span(arr)
