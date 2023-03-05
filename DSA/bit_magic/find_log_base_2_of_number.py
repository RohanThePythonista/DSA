def find_log_base_2_of_number(number):
    count = 0
    while number:
        number = number >> 1
        count += 1
    print(count-1)
    print(2**(count-1))


if __name__ == '__main__':
    find_log_base_2_of_number(100)
