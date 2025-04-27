# https://www.youtube.com/watch?v=slYh0ZNEqSw

from collections import deque
class StockSpanner:

    def __init__(self):
        self.nums = []

        # Stack will store tuple (span,num)
        self.stack = deque()
        

    def next(self, price: int) -> int:
        # starting span with 1 to count self element as well
        span = 1

        # maintain a decreasing monotonic stack with updating span
        while self.stack and self.stack[-1][1] <= price:
            _span,num = self.stack.pop()
            span += _span

        self.stack.append((span,price))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
