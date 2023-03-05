# import time
#
#
# def get_sqrt(x):
#     low = 0
#     high = x - 1
#     res = 1
#     while low <= high:
#         mid = low + (high - low) // 2
#         square_of_mid = mid * mid
#         if square_of_mid == x:
#             print("2 1000")
#             return mid
#         elif square_of_mid < x:
#             low = mid + 1
#             res = mid
#         else:
#             high = mid - 1
#     return res
#
#
# val = pow(2, 1000) + 1
# t = time.time()
# print(get_sqrt(val))
# print(time.time() - t)
import binascii

key_2 = [0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe, 0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81,
         0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7, 0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4]

key_hex = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
key_str = binascii.a2b_hex(key_hex)
key = list(key_str)
# print(list(key_str))
print(key)
key = [str(item) for item in key]
key = "".join(key)
print(key)
