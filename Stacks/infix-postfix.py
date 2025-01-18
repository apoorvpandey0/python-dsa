https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
#User function Template for python3

from collections import deque
class Stack:
    """Stack implementation using deque."""
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.stack) == 0

class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        pri = {'+':1,'-':1,'*':2,'/':2,''}
        stack == Stack()
        postfix = ""
        for char in s:
            if char == '(':
                stack.push(char)
            elif char in pri:
                if pri[char] > pri[stack[-1]]:
                    stack.push()
                else:
                    # Pop until stack[-1] < pri[char]
            elif char == ')'
            # Pop until '('
        return ans
                    
