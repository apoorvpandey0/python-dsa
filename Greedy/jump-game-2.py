"""
    Jump game 2
    Find the minimum number of jumps to reach the last index
    Link: https://leetcode.com/problems/jump-game-ii/submissions/
"""
# Using greedy and BFS approach
# Runtime: 145 ms, faster than 80.29% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.1 MB, less than 52.43% of Python3 online submissions for Jump Game II.
def solve(nums):
    res = 0
    l = r = 0
    while r<len(nums)-1:
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest,i+nums[i])
        l = r+1
        r = farthest
        res+=1
    return res