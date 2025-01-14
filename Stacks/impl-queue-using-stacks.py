https://leetcode.com/problems/implement-queue-using-stacks/
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

class MyQueue:

    def __init__(self):
        self.currS = Stack()
        self.swapS = Stack()

    def push(self, x: int) -> None:
        for _ in range(self.currS.size()):
            tmp = self.currS.pop()
            self.swapS.push(tmp)
        self.currS.push(x)

        for _ in range(self.swapS.size()):
            tmp = self.swapS.pop()
            self.currS.push(tmp)

    def pop(self) -> int:
        return self.currS.pop()

    def peek(self) -> int:
        return self.currS.peek()

    def empty(self) -> bool:
        return self.currS.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
