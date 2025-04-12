from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0
    def __repr__(self):
        return f"Stack({list(self.stack)})"


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return -1 if self.is_empty() else self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0 

    def peek(self):
        return -1 if self.is_empty() else self.stack[-1]
