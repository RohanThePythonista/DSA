def rotate_array_left_by_one(input_array):
    """
    Idea is to save first ele and then shift all elements from an array to
    one position ahead, at last put saved first ele to last pos in array
    :param input_array: list --an input array
    :return:
    """
    temp = input_array[0]
    for index in range(0, len(input_array) - 1, 1):  # range(start, stop:n-1(to avoid index error), step)
        input_array[index] = input_array[index + 1]
    input_array[-1] = temp


def rotate_array_left_by_k_positions(arr, k):
    """
    TC-O(n^2)
    SC-O(1)
    left rotate by k pos
    e.g input_array = [1,2,3,4,5,6,7], k = 2
    output = [3,4,5,6,7,1,2]
    :param arr: list ---an array to rotated
    :param k: int, rotate array by k pos
    :return:
    """
    if k <= 0:
        return
    print("rotate_array_left_by_{}_positions".format(k))
    for _ in range(k):
        rotate_array_left_by_one(arr)
    print(arr)


def rotate_array_clockwise_by_k_positions(arr, k):
    """
    e.g input_array = [1,2,3,4,5,6,7], k = 2
    output = [7,6,1,2,3,4,5]
    TC-O(n^2)
    SC-O(1)
    Idea is to use two loops
    for i = 0 to k:
        save last ele
        for j = -1 to -len(array)(iterate reverse on inner loop)
            push jth index ele to next index
            (shift each ele to its next index)
    :param arr: list, input array
    :param k: int, rotate right by k pos
    :return:
    """
    if k <= 0:
        return
    print("rotate_array_clockwise_by_{}_positions".format(k))
    for _ in range(k):
        temp = arr[-1]
        for index in range(-1, -len(arr), -1):
            arr[index] = arr[index - 1]
        arr[0] = temp
    print(arr)


def reversal_array_algorithm(arr, k):
    """
    Idea to use reversal algorithm to left rotation
    TC-O(n)
    SC-O(1)
    1.It reverses first k elements
    2.then it reverses next n-k elements
    3.and after than it reverses all n elements
        so array will be rotated left by k elements
    :param arr: list, input array
    :param k: int,
    :return:
    """
    rotate_array(arr, 0, k - 1)
    rotate_array(arr, k, len(arr) - 1)
    rotate_array(arr, 0, len(arr) - 1)
    print(arr)


def rotate_array(arr, start, end):
    # simple two pointer swapping technique used in school
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_left_by_k_pos_using_aux_space(arr, k):
    #  TC: O(n)
    # SC: O(n)
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


def rotate_left_by_k_using_juggling_algorithm(arr, k):
    gcd = get_gcd(len(arr), k)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            # update step to rotate
            s = j + k
            # instead of following if block we can use s = (j+k)%len(arr)
            if s >= len(arr):
                s = s - len(arr)
            if s == i:
                break
            # shift to left
            arr[j] = arr[s]
            # update j for next step rotation
            j = s
        # final position of ith element
        arr[j] = temp


def get_gcd(a, b):
    # import math could be used like return math.gcd(x, y)
    if b == 0:
        return a
    return get_gcd(b, a % b)


"""
# Python code to demonstrate naive
# method to compute gcd ( Loops )
  
  
def get_gcd(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return gcd
    
# Python code to demonstrate naive
# method to compute gcd ( Euclidean algorithm )
  
  
def get_gcd(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
"""

if __name__ == '__main__':
    array = [i for i in range(1, 8)]
    print("Input array:{}".format(array))
    import copy

    # test_arr = copy.deepcopy(array)
    # rotate_array_left_by_k_positions(test_arr, 2)
    # test_arr = copy.deepcopy(array)
    # rotate_array_clockwise_by_k_positions(test_arr, 2)
    # test_arr = copy.deepcopy(array)
    # reversal_array_algorithm(test_arr, 3)
    # test_arr = copy.deepcopy(array)
    # rotate_left_by_k_pos_using_aux_space(test_arr, 3)
    test_arr = copy.deepcopy(array)
    rotate_left_by_k_using_juggling_algorithm(test_arr, 3)
    """
    rotate_left_by_k_using_juggling_algorithm
    [1, 2, 3, 4, 5, 6], 2
    Step 1 i=0, j=i, temp = arr[0]:
        j = 0    s= j+2(0+2) arr[j(0)] = arr[s(2)] j = s(2) -->[3, 2, 3, 4, 5, 6]
        j = 2    s= j+2(2+2) arr[j(2)] = arr[s(4)] j = s(4) -->[3, 2, 5, 4, 5, 6]
        j = 4    s= j+2(4+2) if s(6)>=len(arr)(6): s= s-len(arr)(0) s(0)==i(0): break
        arr[j(4)] = temp(arr[0]) -->[3, 2, 5, 4, 1, 6]

    Step 2 i=1, j=i, temp = arr[1]:
        j = 1    s= j+2(1+2) arr[j(1)] = arr[s(3)] j = s(3)  -->[3, 4, 5, 4, 1, 6]
        j = 3    s= j+2(3+2) arr[j(3)] = arr[s(5)] j = s(5) -->[3, 4, 5, 6, 1, 6]
        j = 5    s= j+2(5+2) if s(7)>=len(arr)(6): s= s-len(arr)(1) s(1)==i(1): break
        arr[j(5)] = temp(arr[1]) -->[3, 4, 5, 6, 1, 2]

    """
