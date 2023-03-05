def get_equilibrium_point(arr):
    if len(array) == 1:
        return 1
    left_sum = 0
    total_sum = sum(arr)
    for index, value in enumerate(arr, start=1):
        total_sum -= value
        if total_sum == left_sum:
            return index
        left_sum += value
    return -1


if __name__ == '__main__':
    # array = [1, 3, 5, 2, 2]
    # print(get_equilibrium_point(array))
    test_cases = int(input())
    for t_case in range(test_cases):
        n = map(int, input().split())
        array = list(map(int, input().split()))
        print(get_equilibrium_point(array))
