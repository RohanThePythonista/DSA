def print_mat(row, col, matrix):
    i = 0
    unique_list = []
    temp = 0
    while i < row and temp < row * col:
        curr_row = matrix[temp:col + temp]
        if curr_row not in unique_list:
            for j in curr_row:
                print(j, end=" ")
            print("$", end="")
            unique_list.append(curr_row)
        i += 1
        temp += col


if __name__ == '__main__':
    # print_mat(5, 3, [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 2, 3])
    i_p = [1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1]
    print_mat(4, 7, i_p)
