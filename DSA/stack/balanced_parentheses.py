def check_balanced_parentheses(string):
    stack = list()
    matches = [("(", ")"), ("{", "}"), ("[", "]")]
    if len(string) % 2:
        """
        base condition to early check assuming string has only parentheses
        """
        return False
    for char in string:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if len(stack) == 0:
                return False
            last_opening = stack.pop()
            if (last_opening, char) not in matches:
                return False
            # prev = stack.pop()
            # if char == ')':
            #     if prev != "(":
            #         return False
            # elif char == "}":
            #     if prev != "{":
            #         return False
            # elif char == "]":
            #     if prev != "[":
            #         return False
            """
            other approach for checking matches like
            matches = [("(",")"),("{","}"),("[","]")]
            last_opening = stack.pop()
            if (last_opening, curr_char )not in matches:
                return False
            """
    return len(stack) == 0


if __name__ == '__main__':
    exp = "([{}])"
    print(check_balanced_parentheses(exp))
