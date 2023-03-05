def split_me(input_string):
    input_string = input_string.strip(" ")
    i = 0
    split_me_list = []
    while i < len(input_string):
        if input_string[i] != " ":
            word_start = i
            while i < len(input_string) and input_string[i] != " ":
                i += 1
            split_me_list.append(input_string[word_start:i])
        i += 1
    print(split_me_list)


if __name__ == '__main__':
    split_me("rohan prachi")
