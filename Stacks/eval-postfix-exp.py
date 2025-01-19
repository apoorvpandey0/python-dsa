Postfix expressions also known as Reverse Polish notation

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

def is_alnum_with_neg(string):
    if string.startswith('-'):
        string = string[1:]
    return string.isalnum()

# Easiest way in python3 to achieve "division between two integers always truncates toward zero" is to do the normal float division, and then convert it to integer, like -> int(a/b).

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        for ele in tokens:
            if is_alnum_with_neg(ele):
                stack.push(int(ele))
            else:
                b = stack.pop()
                a = stack.pop()
                if ele == '+':
                    stack.push(a+b)
                elif ele == '-':
                    stack.push(a-b)
                elif ele == '*':
                    stack.push(a*b)
                elif ele == '/':
                    stack.push(int(a/b))
        return stack.peek()
