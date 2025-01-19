https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
#User function Template for python3
from collections import deque

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

class Solution:
    def InfixtoPostfix(self,expression):
        # Priority of operators
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = Stack()
        postfix = ""
    
        for char in expression:
            if char.isalnum():
                postfix += char
            elif char == '(':
                stack.push(char)
            elif char == ')':
                # Pop until '(' is found
                while not stack.is_empty() and stack.peek() != '(':
                    postfix += stack.pop()
                stack.pop()  # Remove '(' from the stack
            elif char in precedence:
                # Pop operators with higher or equal precedence
                while (not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[char]):
                    postfix += stack.pop()
                stack.push(char)  # Push the current operator onto the stack
    
        # Pop remaining operators in the stack
        while not stack.is_empty():
            postfix += stack.pop()
    
        return postfix
