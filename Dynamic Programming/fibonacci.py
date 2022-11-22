class Solution:
    def golden_ratio(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)

    def iterative(self, n: int) -> int:
        if n ==0: return 0
        if n==1 or n==2: return 1
        a = 1
        b = 1
        c = a+b
        for i in range(2,n):
            # print(c)
            c = a+b
            a = b
            b = c
        return c
    
    def recursive(self,n):
        if n ==0: return 0
        if n==1 or n==2: return 1
        return self.recursive(n-1) + self.recursive(n-2)
    
    def memoization(self,n,dp):
        # Top down strategy
        # Answer to base cases
        if n<1:return n
        if n in dp: return dp[n]
        else: dp[n] = self.memoization(n-1,dp)+self.memoization(n-2,dp)
        
    def tabulation(self,n):
        # Bottom up strategy
        # Base cases to answer
        dp = {0:0,1:1}
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        
        