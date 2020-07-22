# Write a function in python that can reverse a string using stack data structure.

from collections import deque


class Stacky:
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

    def ReverseString(self, str):
        stack = Stacky()

        for char in str:
            stack.push(char)

        resr = ''
        while stack.size() != 0:
            resr += stack.pop()
        return resr


objStack = Stacky()
print(objStack.ReverseString("I will conqur Covid - 19"))
