def remove_duplicates(arr):
    my_dict = {}
    for i, val in enumerate(arr):
        if val not in my_dict:
            my_dict[val] = val
        else:
            arr.pop(i)
    print(arr)
    # for val in arr:
    #     if arr[abs(val)] > 0:
    #         arr[abs(val)] = - arr[abs(val)]
    # aux = []
    # for val in array:
    #     if val < 0:
    #         aux.append(val)
    # print(aux)


if __name__ == '__main__':
    array = [1, 2, 3, 1, 4, 2]
    remove_duplicates(array)
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     array = list(map(int, input().split()))
    #     remove_duplicates(array)
    #     for i in array:
    #         print(i, end=" ")
    #     print('')
    from collections import OrderedDict as Od

    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        order = Od()
        for ele in arr:
            order[ele] = order.get(ele, 0) + 1
        print(*order.keys())
        t -= 1