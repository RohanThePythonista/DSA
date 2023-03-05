def print_leaders_in_array(arr):
    leaders = list()
    leaders.append(arr[-1])
    for i in range(-2, -len(arr) - 1, -1):
        if arr[i] >= leaders[-1]:
            leaders.append(arr[i])
    return leaders


if __name__ == '__main__':
    test_cases = int(input())
    for t_case in range(test_cases):
        n = map(int, input().split())
        array = list(map(int, input().split()))
        led = print_leaders_in_array(array)
        for i in range(-1, -len(led) - 1, -1):
            print(led[i], end=" ")
        print('')
