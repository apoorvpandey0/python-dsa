https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque
class Q:
    def __init__(self):
        self.q = deque()
    def enqueue(self,val):
        self.q.appendleft(val)
    def dequeue(self):
        return self.q.pop()
    def size(self):
        return len(self.q)
    def peek(self):
        return self.q[-1]
    def empty(self):
        return self.size() == 0

class MyStack:

    def __init__(self):
        self.swapQ = Q()
        self.currQ = Q()

    def push(self, x: int) -> None:
        for _ in range(self.currQ.size()):
            tmp = self.currQ.dequeue()
            self.swapQ.enqueue(tmp)
        
        self.currQ.enqueue(x)
        
        for _ in range(self.swapQ.size()):
            tmp = self.swapQ.dequeue()
            self.currQ.enqueue(tmp)      

    def pop(self) -> int:
        return self.currQ.dequeue()

    def top(self) -> int:
        return self.currQ.peek()

    def empty(self) -> bool:
        return self.currQ.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
