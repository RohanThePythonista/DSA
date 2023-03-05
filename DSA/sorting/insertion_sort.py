"""
O(n^2)
It is like arranging cards in left hand based on picked ele in right hand
Every time we check picked card with cards in left hand one by one
if curr card picked in right hand < cards in right hand
then make room for it ...and finally place it at its sorted pos in available cards
"""


def insertion_sort(arr):
    for j in range(1, arr.__len__()):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


if __name__ == '__main__':
    input_array = [0, 1, 2, 3, 45, 10, 9, 8, 0, 5, 4, 3, 2, 1]
    insertion_sort(input_array)
    print(input_array)
