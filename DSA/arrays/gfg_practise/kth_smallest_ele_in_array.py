def get_kth_smallest_ele_in_array(arr, k, n):
    pass


if __name__ == '__main__':
    test_cases = int(input())
    for t_case in range(test_cases):
        n = map(int, input().split())
        array = list(map(int, input().split()))
        k = map(int, input().split())
        print(get_kth_smallest_ele_in_array(array, k, n))
