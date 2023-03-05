def get_max_increasing_sub_sequence(arr):
    i = 1
    n = len(arr)
    j = 0
    dp = arr[:]
    while i < n:
        while j < i:
            if dp[j] < dp[i] < dp[i] + dp[j]:
                dp[i] = dp[j] + dp[i]
            j += 1
        i += 1
    return max(dp)


if __name__ == '__main__':
    # arr = [1, 101, 2, 3, 100, 4, 5]
    # print(get_max_increasing_sub_sequence(arr))
    test_cases = int(input())
    for t_case in range(test_cases):
        n = map(int, input().split())
        array = list(map(int, input().split()))
        print(get_max_increasing_sub_sequence(array))
