input_list = [5, 4, 2, 1, 4, 0]
input_list.remove(4)
print(input_list)

if __name__ == '__main__':
    n = input()
    l = []
    for _ in range(int(n)):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
        else:
            print(l)


"""
def insert_at_index(arr,index, key):
    arr.insert(index, key)

def print_list(arr):
    print(arr)

def remove_first_occurance(arr, key):
    arr.remove(key)

def append_key(arr, key):
    arr.append(key)

def sort_array(arr):
    arr.sort()

def pop_last(arr):
    arr.pop()

def reverse_array(arr):
    arr.sort(reverse=True)


if __name__ == '__main__':
    N = int(input())
    output_list = list()
    for _ in range(N):
        cmd = input()
        cmd_list = cmd.split()
        if 'insert' in cmd:
            insert_at_index(output_list,int(cmd_list[1]), int(cmd_list[2])) 
        elif 'print' in cmd:
            print_list(output_list)
        elif 'remove' in cmd:
            remove_first_occurance(output_list,int(cmd_list[1]))
        elif 'append' in cmd:
            append_key(output_list,int(cmd_list[1]))
        elif 'sort' in cmd:
            sort_array(output_list)
        elif 'pop' in cmd:
            pop_last(output_list)
        elif 'reverse' in cmd:
            reverse_array(output_list)

"""