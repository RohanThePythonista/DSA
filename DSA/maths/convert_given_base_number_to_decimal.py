def val(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 10


def char_from_int(value):
    if 0 <= value <= 9:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))


def convert_to_decimal_from_given_base(num, base):
    num = reversed(num)
    decimal = 0
    for i, digit in enumerate(num):
        if val(digit) >= base:
            print('Invalid Number')
            return -1
        decimal = decimal + (base ** i) * val(digit)
    return decimal


def convert_from_given_decimal_to_given_base(num, base):
    result = ''
    while num > 0:
        result += char_from_int(num % base)
        num = int(num / base)
    result = result[::-1]
    return result


if __name__ == '__main__':
    input_num = input('Enter a num having 0 to 9 and optional A to Z added:')
    input_base = int(input('Enter a base:'))
    res = convert_to_decimal_from_given_base(input_num, input_base)
    print(res)
    print(convert_from_given_decimal_to_given_base(res, 16))
