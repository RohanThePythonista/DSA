def print_snake_traversal_pattern(matrix):
    rows = len(matrix)
    i = 0
    while i < rows:
        j = 0
        if i and i % 2 == 1:
            j = -1
            while j != -4:
                print(matrix[i][j], end=" ")
                j = j - 1
        else:
            while j < 3:
                print(matrix[i][j], end=" ")
                j += 1
        i += 1
        # print("\n")


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print_snake_traversal_pattern(mat)
    # for i in range(5, -1, -1):
    #     print(i)
