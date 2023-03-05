"""
Given sub_array_sum and an array.
Check if sub-array with given sum is exists or not.
e.g. input_array = [1,2,3,4,5,8], sub_array_sum = 15
        output = True --> from index 0 to 4, there is sub array with sum 15
    input_array = [1,2,3], sub_array_sum = 10
    output = False, --->there is sub array with sum 10

Method 1:
    Naive approach
        Use two loops
        For each ele(i) in array in outer loop
            traverse inner loop from j=(i) to n-1
                and keep track of sum to check with given sum
    TC:O(n^2)
    SC:O(1)

Method 2:
    TC:O(n)
    SC:O(n)
    Efficient solution using mapping of curr sum to index for curr_sum till current index
    Idea is to create mapping of curr_sum till each curr index element
        if curr_sum is equal to sub_array_sum
            then sub_array is present from index 0 to curr_index
        if curr_sum - sub_array_sum is present in mapping
            then sub_array is present from mapping[curr_sum - sub_array_sum] + 1 index to curr index

"""


def find_sub_array(arr, sub_array_sum):
    n = len(arr)
    curr_sum = 0
    curr_sum_dict = dict()
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == sub_array_sum:
            print("Sum found between indexes 0 to", i)
            return
        if curr_sum - sub_array_sum in curr_sum_dict:
            print("Sum found between indexes", curr_sum_dict[curr_sum - sub_array_sum] + 1, "to", i)
            return
        curr_sum_dict[curr_sum] = i


if __name__ == '__main__':
    sum_of_sub_array = 23
    # input_list = get_sequence_list(10)
    input_list = [15, 2, 4, 8, 9, 5, 10, 23]
    print("is present:{}".format(find_sub_array_with_given_sum(input_list, sum_of_sub_array)))
    # find_max_sum_of_k_elements(input_list, 3)
