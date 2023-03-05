def postfix_evaluation(exp):
    operands = ["*", "/", "+", "-"]
    operand_list = list()
    for char in exp:
        if char not in operands:
            operand_list.append(char)
        else:
            op2 = operand_list.pop()
            op1 = operand_list.pop()
            if char == "*":
                operand_list.append(mul_(op1, op2))
            elif char == "/":
                operand_list.append(div_(op1, op2))
            elif char == "+":
                operand_list.append(sum_(op1, op2))
            elif char == "-":
                operand_list.append(sub_(op1, op2))
    print("result:{}".format(operand_list.pop()))


def mul_(op1, op2):
    return int(op1) * int(op2)


def div_(op1, op2):
    return int(op1) // int(op2)


def sum_(op1, op2):
    return int(op1) + int(op2)


def sub_(op1, op2):
    return int(op1) - int(op2)


if __name__ == '__main__':
    exp_ = "23*54*+9-"
    postfix_evaluation(exp_)
