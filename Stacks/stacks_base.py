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
