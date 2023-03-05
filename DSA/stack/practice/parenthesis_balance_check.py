from collections import deque

stack = deque()
opens = {'[', '{', '('}
closed = {']', '}', ')'}
pairs = {('[', ']'), ('{', '}'), ('(', ')')}


def are_parenthesis_balanced(string):
    for char in string:
        if char in opens:
            stack.append(char)
        elif char in closed:
            match = stack.pop()
            if (match, char) in pairs:
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    input_str = "{{{}}]}"
    print(are_parenthesis_balanced(input_str))
