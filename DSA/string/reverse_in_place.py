"""
i/p: text = "rohan prachi mukund"
o/p result = "nahor ihcarp dnukum"
"""


def reverse_in_place(text):
    print("i/p text:{}".format(text))
    result = [char for char in text]
    i = 0
    while i < len(text):
        start_index_of_curr_word = i
        while i < len(text) and text[i] != ' ':
            i += 1
        swap(result, start_index_of_curr_word, i - 1)  # this line reverse current word
        i += 1
    print(result)
    print(''.join(result))


def swap(result, start, end):
    while start <= end:
        result[start], result[end] = result[end], result[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    input_string = "rohan prachi mukund"
    print(reverse_in_place(input_string))
