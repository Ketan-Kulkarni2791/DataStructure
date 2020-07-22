from _collections import deque

stack = deque()
# print(dir(stack))

stack.append('500')
stack.append('600')
# print("Stack : ", stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


objStack = Stack()
objStack.push(200)
objStack.push('Bc')
print(objStack.size())
print(objStack.is_empty())
objStack.pop()
print(objStack.peek())
