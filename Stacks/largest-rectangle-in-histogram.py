"""
    Largeest Rectangle in Histogram
    Link: https://www.leetcode.com/problems/largest-rectangle-in-histogram/
    Sol: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1729427/Python-%2B-Easy-Approach-%2B-Complexity
"""

from collections import deque
# TODO: Work on lack of clarity
# Time: O(n) | Space: O(n)
# Runtime: 1290 ms, faster than 38.36% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 28.5 MB, less than 29.23% of Python3 online submissions for Largest Rectangle in Histogram.
def solve(nums):
    N = len(nums)
    
    stack = deque()
    left = [0] * N
    for i in range(N):
        while stack and nums[stack[-1]]>=nums[i]:
            # Remove all nodes having values greater than current value from the stack
            stack.pop()
        if not stack:
            # This means there is no limit on the left end 
            # So the max it can tek it is uptill 0th index
            # Hence left[i] = 0
            left[i] = 0
        else:
            # Ex: The left limit for index  in array [2,1,5,6,2,3] will be index 2. (And not index 1)
            # So, the limit for the element will be the next element ie +1
            left[i] = stack[-1]+1
        stack.append(i)
        # print(i,stack,left)
    
    stack.clear()
    right = [0] * N
    for i in range(N)[::-1]:
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()
        if not stack:
            right[i] = N-1
        else:
            right[i] = stack[-1]-1
        stack.append(i)  
    
    maxH = 0
    for i in range(N):
        maxH = max(maxH,(right[i]-left[i]+1)*nums[i])
    return maxH
print(solve([2,1,5,6,2,3]))