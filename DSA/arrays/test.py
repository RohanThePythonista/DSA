# def rotate_left_by_one(arr):
#     temp = arr[0]
#     i = 1
#     while i < len(arr):
#         arr[i - 1] = arr[i]
#         i += 1
#     arr[-1] = temp


def rotate_left_by_one(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rotate_left_by_k_pos(arr, k):
    for i in range(k):
        rotate_left_by_one(arr)
    print(arr)


def rotate_right_by_k_pos(arr, k):
    for i in range(k):
        temp = arr[-1]
        j = len(arr) - 2
        while j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[0] = temp
    print(arr)


def rotate_left_by_k_pos_using_aux_space(arr, k):
    temp = [arr[i] for i in range(k)]  # store first k elements
    i = 0
    while i < len(arr) - k:
        arr[i] = arr[i + k]
        i += 1
    print(arr)
    i = -k
    while i < 0:
        arr[i] = temp[i]
        i += 1
    print(arr)


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def rotate_left_by_k_using_juggling_algorithm(arr, k):
    gcd = get_gcd(len(arr), k)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            s = j + k
            # instead of following if block we can use s = (j+k)%len(arr)
            if s >= len(arr):
                s = s - len(arr)
            if s == i:
                break
            arr[j] = arr[s]  # shift to left
            j = s
        arr[j] = temp


def find_max_sum_in_array():
    from DSA.template import template
    array = template.get_random_array(10, -20, 20)
    prefix_array = get_prefix_sum_array(array)
    max_sum = 0
    for val in prefix_array:
        if val > max_sum:
            max_sum = val
    return max_sum


def get_prefix_sum_array(arr):
    prefix_sum_array = []
    res = 0
    for val in arr:
        res += val
        prefix_sum_array.append(res)
    print("prefix array:{}".format(prefix_sum_array))
    return prefix_sum_array


if __name__ == '__main__':
    #     rotate_left_by_k_pos([1, 2, 3, 4, 5, 6], 2)
    """
    Step 1 i=0, j=i, temp = arr[0]:
        j = 0    s= j+2(0+2) arr[j(0)] = arr[s(2)] j = s(2)
        j = 2    s= j+2(2+2) arr[j(2)] = arr[s(4)] j = s(4)
        j = 4    s= j+2(4+2) if s(6)>=len(arr)(6): s= s-len(arr)(0) s(0)==i(0): break
        arr[j(4)] = temp(arr[0])

    Step 2 i=1, j=i, temp = arr[1]:
        j = 1    s= j+2(1+2) arr[j(1)] = arr[s(3)] j = s(3)
        j = 3    s= j+2(3+2) arr[j(3)] = arr[s(5)] j = s(5)
        j = 5    s= j+2(5+2) if s(7)>=len(arr)(6): s= s-len(arr)(1) s(1)==i(1): break
        arr[j(5)] = temp(arr[1])

    """
    # rotate_right_by_k_pos([1, 2, 3, 4, 5, 6], 1)
    # rotate_left_by_k_pos_using_aux_space([1, 2, 3, 4, 5, 6], 2)
    print(find_max_sum_in_array())
