https://www.interviewbit.com/problems/nearest-smaller-element/
from collections import deque

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        
        stack = Stack()
        ans = []
        for ele in A:
            while not stack.empty() and stack.peek() >= ele:
                stack.pop()
            ans.append( -1 if stack.empty() else stack.peek())
            stack.push(ele)
        return ans


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
