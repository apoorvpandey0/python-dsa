# Solution 1:
# TLE on leetcode for input 38
# T(n) = T(n-1) + T(n-2)
def count(n):
    if n <= 1: return 1
    return count(n - 1) + count(n - 2)


# Solution 2
# Optimized overlapping subproblems using DP table
# Time: O(n)
# Runtime: 24 ms, faster than 96.59% of Python3 online submissions for Climbing Stairs.
def climb(n):
    #edge cases
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2
    dp = [0] * (n + 1)  # considering zero steps we need n+1 places
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # print(dp)
    return dp[n]


print(count(3))
# print(climb(38))