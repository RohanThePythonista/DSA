def search(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and (mid == 0 or arr[mid - 1] != x):
            return mid
        elif arr[mid] >= x:
            high = mid - 1  # go to left half side
        else:
            low = mid + 1
    return -1


def find_right_most_index(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and (mid == n - 1 or arr[mid + 1] != x):
            return mid
        elif arr[mid] <= x:
            low = mid + 1  # go to right half side
        else:
            high = mid - 1
    return -1


def square_root(x):
    low = 1
    high = x
    if x == 0 or x == 1:
        return x
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans


def major_element(arr, n):
    """
    major element is nothing but which occurs in array >= n/2 times
    :param arr: list
    :param n: len of array
    :return: major ele

    we can use Moore Voting algorithm -->Explore
    """
    count_dict = dict()
    majority = n // 2
    for ele in arr:
        if ele in count_dict:
            count_dict[ele] += 1
            if count_dict[ele] >= majority:
                return ele
        else:
            count_dict[ele] = 1

    return -1


def peak_element(arr, n):
    """
    peak element means it is greater than it's neighbour elements
    corner elements can be also peak elements
    e.g.1 2 3 --->peak is 3

    :param arr:
    :param n:
    :return:

    one line solution

    return arr.index(max(arr))
    """
    left_ptr = 1
    right_ptr = n - 1
    if n >= 2:
        if arr[0] > arr[left_ptr]:
            return 0
        elif arr[right_ptr] > arr[right_ptr - 1]:
            return right_ptr
    else:
        return 0
    right_ptr = n - 2
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] > arr[mid]:
            right_ptr = right_ptr - 1
            pass
        else:
            left_ptr = left_ptr + 1
            pass
    return -1


if __name__ == '__main__':
    # print(search([2, 3, 3, 3], 4, 3))
    print(find_right_most_index([1, 1, 1, 1, 1, 5], 6, 5))
    # print(square_root(28))
    # print(major_element([3, 1, 3, 3, 2], 3))
    # print(peak_element([5, 10, 20, 15, 7], 5))
    # print(peak_element([5], 1))
