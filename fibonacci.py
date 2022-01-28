from functools import lru_cache

class Solution:
    """
       Problem: https://leetcode.com/problems/fibonacci-number/submissions/ 
       Solutions: https://leetcode.com/problems/fibonacci-number/discuss/308688/6-Python-solutions
    """
    # Runtime: 28 ms, faster than 83.90% of Python3 online submissions for Fibonacci Number.
    # Bottomo up approach of DP
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==1:
            return 1
        a = 0
        b = 1
        c = -1
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return c
    
    # Runtime: 24 ms, faster than 95.31% of Python3 online submissions for Fibonacci Number.
    # Formula approach
    def fibGoldenRatio(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)

    
    # LRU cache method
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)
        