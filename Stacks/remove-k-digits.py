# https://leetcode.com/problems/remove-k-digits/
from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = Stack()

        for ele in num:
          # <= will not work for case "112", 1
            while k>0 and not stack.empty() and ele<stack.peek():
                stack.pop()
                k-=1
            stack.push(ele)
            
        # Remove remaining digits if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Build the final result
        result = ''.join(stack.stack).lstrip('0')
        
        # If the result is empty, return "0"
        return result if result else "0"


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
