"""
given an arr of stock prices on sequential days
calculate max. profit that can be made using stock buy and sell on particular days

Idea is to use local min and local max arrays
iterate i.p arr left to right:
    if curr ele is less than it's prev and next
        then it is local min
    elif curr ele is greater that it's prev and next
        then it is local max

At end just aggregate result using local min and max arr by iterating over common len
    result += local_max[i] - local_min[i]
"""


def get_max_profit(arr):
    n = len(arr)
    local_min = []
    local_max = []
    for i in range(n - 1):
        if i == 0:
            if arr[i + 1] > arr[i]:
                local_min.append(arr[i])

        elif arr[i - 1] < arr[i] > arr[i + 1]:
            local_max.append(arr[i])

        elif arr[i - 1] > arr[i] < arr[i + 1]:
            local_min.append(arr[i])

        elif i == n - 2:
            if arr[i + 1] > arr[i]:
                local_max.append(arr[i + 1])

    result = 0
    for i in range(len(local_max)):
        result += local_max[i] - local_min[i]
    return result


if __name__ == '__main__':
    array = [1, 5, 3, 8, 12]
    print(get_max_profit(array))
