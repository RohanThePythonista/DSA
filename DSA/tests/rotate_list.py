test_list = [1, 2, 3, 4, 5, 6, 7]


def rotate_by_one_left(array):
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[-1] = temp


def rotate_list(array, count):
    print("Rotate list {} by {}".format(array, count))
    for i in range(count):
        # rotate_by_one_left(array)
        rotate_by_one_right(array)
    print("Rotated list {} by {}".format(array, count))


def rotate_by_one_right(array):
    temp = array[-1]
    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    array[0] = temp


# [1,2,3,4,5,6,7] = [7,1,2,3,4,5,6]


if __name__ == "__main__":
    rotate_list(test_list, 1)

