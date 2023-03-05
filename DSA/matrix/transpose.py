def get_transpose(matrix):
    """
    I made mistake here of not creating same size array
    :param matrix:
    :return:
    """
    temp = [[0 for i in range(3)] for j in range(3)]

    for j in range(3):
        for i in range(3):
            temp[i][j] = matrix[j][i]
    print(temp)


"""
00 -> 00 10 -> 01 20 -> 02
01 -> 10 11 -> 11 21 -> 12
02 -> 20 12 -> 21 22 -> 22
"""

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    get_transpose(mat)


# # transpose of a matrix
#
# N = 4
#
#
# # This function stores
# # transpose of A[][] in B[][]
#
# def transpose(A, B):
#     for i in range(N):
#         for j in range(N):
#             B[i][j] = A[j][i]
#
#         # driver code
#
#
# # A = [[1, 1, 1, 1],
# #      [2, 2, 2, 2],
# #      [3, 3, 3, 3],
# #      [4, 4, 4, 4]]
# A = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
# # B = A[:][:]  # To store result
# B = [[0 for x in range(4)] for y in range(4)]
#
# transpose(A, B)
#
# print("Result matrix is")
# for i in range(N):
#     for j in range(N):
#         print(B[i][j], " ", end='')
#     print()
