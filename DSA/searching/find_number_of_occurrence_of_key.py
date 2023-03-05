"""
1
135 342
4 4 9 12 16 20 24 26 30 36 39 41 45 49 50 57 61 64 73 74 75 76 79 79 79 83 87 99 100 101 108 109 112 115 121 134 148 149 150 160 160 162 164 184 190 194 194 197 198 201 209 209 211 217 219 223 236 244 245 251 253 253 257 258 262 265 267 277 278 279 281 286 291 292 295 306 308 311 313 327 329 331 334 335 338 341 341 341 342 352 353 355 361 366 366 368 370 371 381 382 387 391 392 393 393 400 419 420 425 429 432 433 433 434 436 439 450 453 459 468 472 475 478 480 483 484 488 490 490 491 493 493 498 498 498
"""


def find_no_of_occurrence_of_key(arr, low, high, key):
    left_most_index = find_left_most_index(arr, low, high, key)
    if left_most_index == -1:
        print(-1)
        return
    right_most_index = find_right_most_index(arr, low, high, key)
    print(right_most_index - left_most_index + 1)


def find_left_most_index(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and (mid == 0 or arr[mid - 1] != key):
            return mid
        elif arr[mid] >= key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_right_most_index(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and (mid == 5 or arr[mid + 1] != key):
            return mid
        elif arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    # print(find_right_most_index([1, 1, 1, 1, 1, 5], 0, 5, 5))
    #
    t = int(input())
    for _ in range(t):
        no_of_elements_and_key = list(map(int, input().split()))
        no_of_elements = no_of_elements_and_key[0]
        key_ = no_of_elements_and_key[1]
        n_list = list(map(int, input().split()))
        find_no_of_occurrence_of_key(n_list, 0, len(n_list) - 1, key_)
