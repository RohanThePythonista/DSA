# def find_first_non_repeating_char_in_stream(stream):
#     non_repeating_queue = list()
#     char_dict = dict()
#     for char in stream:
#         flag = 0
#         char_dict[char] = char_dict.get(char, 0) + 1
#         if char_dict[char] == 1:
#             non_repeating_queue.append(char)
#         while non_repeating_queue:
#             front_char = non_repeating_queue[0]
#             if char_dict[front_char] == 1:
#                 print(char, end=" ")
#                 flag = 1
#                 break
#             else:
#                 non_repeating_queue.pop(0)
#         if flag == 0:
#             print(-1, end=" ")


def find_first_non_repeated(stream):
    """
    Idea is to use queue and an array for maintain repeated marking
    queue all non repeated chars
        -> if curr char is not in queue add it
        ->else remove it from queue and mark it as repeated in array using its ordinal value as index
        if queue is empty means no no repeated found
        else print always first ele from queue
    :param stream:
    :return:
    """
    repeated = [False] * 256
    queue = list()
    for char in stream:
        if repeated[ord(char)] is False:
            if char not in queue:
                queue.append(char)
            else:
                queue.remove(char)
                repeated[ord(char)] = True
        if len(queue) == 0:
            print(-1, end=" ")
        else:
            print(queue[0], end=" ")


if __name__ == '__main__':
    test_cases = int(input())
    stream_input = []
    for _ in range(test_cases):
        n = int(input())
        stream_input = list(input().split())
        find_first_non_repeated(stream_input)
        print('')
