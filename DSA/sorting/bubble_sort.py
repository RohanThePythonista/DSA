from template.template import *

"""
O(n^2):
it checks adj ele.s and swaps it if cuu ele is less than its next ele 
"""


def bubble_sort(arr):
    i, j = 0, 0
    while i < arr.__len__():
        while j < arr.__len__():
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
        print(arr)
        j = 0
    print("sorted:{}".format(arr))


if __name__ == '__main__':
    bubble_sort(get_random_array(n=5, from_=0, to_=100))
