"""
input
2
5 16
9 7 2 16 4
7 98
1 22 57 47 34 18 66

output
4  --->first index of 16
-1 --->98 is not present
"""


def find_index_of_value_in_array(arr, value):
    index = -1
    for i, key in enumerate(arr, 1):
        if key == value:
            index = i
            break
    if index == -1:
        print(-1)
    else:
        print(index)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        no_of_elements_and_key = list(map(int, input().split()))
        no_of_elements = no_of_elements_and_key[0]
        key_ = no_of_elements_and_key[1]
        n_list = list(map(int, input().split()))
        find_index_of_value_in_array(n_list, key_)
