"""
Suppose there is a circle. There are n petrol pumps on that circle.
You are given two sets of data.
1.The amount of petrol that every petrol pump has.
2.Distance from that petrol pump to the next petrol pump.
Calculate the first point from where a truck will be able to complete the circle
(The truck will stop at each petrol pump and it has infinite capacity).
Expected time complexity is O(n).
Assume for 1-litre petrol, the truck can go 1 unit of distance.


Solution:
Method1:
    TC:O(n)
    SC:O(n)
    Use a aux space array to store diff between petrol and distance
    iterate over input array
        Create diff array
        Keep a track of sum of ele of diff array
    if sum < 0 then clearly there is no circular point
        as amount of petrol < dist. to be travel
        return -1
    sum_= 0
    start_point = 0 # initially assume first index is start point in circular travel
    for i = 0 to n: # iterate to find start point in circular travel
        # keep track of sum_ for diff array
        sum_ += diff_array[i]
        if sum< <0:
            update start point to next index and make sum_ = 0
            start_point += 1
            sum_ = 0
    return start_point
    # this would be start point in circular travel to complete travel successfully

Method 2:
    TC:O(n)
    SC:O(1)

    # https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/
    Idea is to use given array like queue

    use a Queue to store the current tour.
    We first enqueue first petrol pump to the queue,
    we keep enqueueing petrol pumps till we either complete the tour,
    or the current amount of petrol becomes negative.
    If the amount becomes negative,
    then we keep dequeuing petrol pumps until the queue becomes empty.

    Instead of creating a separate queue,
    we use the given array itself as a queue.
    We maintain two index variables start and end
    that represent the rear and front of the queue.
"""


def get_index_of_circular_tour(array, n):
    # method1
    petrol_and_distance_difference = []
    sum_ = 0
    for i in range(n):
        """
        array[i][0] -->petrol
        array[i][1] -->distance
        """
        petrol_and_distance_difference.append(array[i][0] - array[i][1])
        sum_ += petrol_and_distance_difference[-1]
    if sum_ < 0:
        return -1
    start_point = 0
    sum_ = 0
    for i in range(n):
        sum_ += petrol_and_distance_difference[i]
        if sum_ < 0:
            start_point = i + 1
            sum_ = 0
    return start_point


def print_tour(arr, n):
    # Consider first petrol pump as starting point
    start = 0
    end = 1
    curr_petrol = arr[start][0] - arr[start][1]
    # array[i][0] -->petrol
    # array[i][1] -->distance

    # Run a loop while all petrol pumps are not visited
    # And we have reached first petrol pump again with 0
    # or more petrol
    while end != start or curr_petrol < 0:
        # If current amount of petrol pumps are not visited
        # And we have reached first petrol pump again with
        # 0 or more petrol
        while curr_petrol < 0 and start != end:

            # Remove starting petrol pump. Change start
            curr_petrol -= arr[start][0] - arr[start][1]
            start = (start + 1) % n

            # If 0 is being considered as start again, then
            # there is no possible solution
            if start == 0:
                return -1

        # Add a petrol pump to current tour
        curr_petrol += arr[end][0] - arr[end][1]

        end = (end + 1) % n

    return start


if __name__ == '__main__':
    a = [[4, 6], [6, 5], [7, 3], [4, 5]]
    # a = [[96, 25], [46, 83], [68, 15], [65, 35], [51, 44], [9, 88], [79, 77], [85, 89]]
    print(get_index_of_circular_tour(a, len(a)))
    print(print_tour(a, len(a)))
