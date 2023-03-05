class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """ADT - abstract data type- just
        LIFO - operations performed from top only
        O(1)  operations - push, pop
        push- insert at beg in list
        pop- delete at beg in list
        applications : fun calls/ recursion
                        undo in editors, balanced parentheses
    """

    def __init__(self):
        self.top = None

    def push(self, data):
        print("pushed:{}".format(data))
        new_top = Node(data)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        if self.is_empty():
            print("stack is empty, pop operation aborted")
            return
        popped_item = self.top.data
        temp = self.top.next  # to update top
        del self.top
        self.top = temp
        print("popped:{}".format(popped_item))
        return popped_item

    def _top(self):
        if self.is_empty():
            print("stack is empty, get top operation aborted")
            return
        return self.top.data

    def is_empty(self):
        return not self.top

    def print_stack(self):
        temp = self.top
        if self.is_empty():
            print("stack is empty, print stack operation aborted")
            return
        print("printing stack")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def get_top(self):
        return self._top()


if __name__ == '__main__':
    stack = Stack()
    # print(stack.is_empty())
    # print(stack.get_top())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_stack()
    # print(stack.get_top())
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()
