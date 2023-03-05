"""
Assume all are distinct ele in array
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

Method 1 (Simple Solution)
    A simple solution is to sort the given array using a O(N log N) sorting algorithm like Merge Sort, Heap Sort, etc
    and return the element at index k-1 in the sorted array.
    TC is O(N Log N)

Method 2 (Using Min Heap – HeapSelect)
    We can find k’th smallest element in time complexity better than O(N Log N).
    A simple optimization is to create a Min Heap of the given n elements
     and call extractMin() k times.

Method 3 (Using Max-Heap)
    We can also use Max Heap for finding the k’th smallest element. Following is algorithm.
    1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)
    2) For each element, after the k’th element (arr[k] to arr[n-1]), compare it with root of MH.
    ……a) If the element is less than the root then make it root and call heapify for MH
    ……b) Else ignore it.
    // The step 2 is O((n-k)*logk)
    3) Finally, root of the MH is the kth smallest element.
    Time complexity of this solution is O(k + (n-k)*Logk)

Method 4 (QuickSelect)
    This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step.
    In QuickSort, we pick a pivot element,
     then move the pivot element to its correct position
     and partition the array around it.
    The idea is, not to do complete quicksort,
     but stop at the point where pivot itself is k’th smallest element.
    Also, not to recur for both left and right sides of pivot,
     but recur for one of them according to the position of pivot.
    The worst case time complexity of this method is O(n2),
     but it works in O(n) on average.
"""


def find_k_th_smallest(arr, l, r, k):
    # method 4
    if 0 < k <= r - l + 1:  # chained comparison in python
        pos = partition_algorithm(arr, l, r)
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:  # if pos is more, recur in left sub-array
            return find_k_th_smallest(arr, l, pos - 1, k)
        # if pos is less, recur in right sub-array
        return find_k_th_smallest(arr, pos + 1, r, k - pos + l - 1)


def partition_algorithm(array, left, right):
    pivot = array[right]
    i = left
    j = left
    while j < right:
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[i], array[j] = array[j], array[i]
    return i


if __name__ == '__main__':
    print(find_k_th_smallest([5, 4, 3, 1], 0, 3, 2))
