https://leetcode.com/problems/daily-temperatures/description/

from collections import deque
class Solution:
    # Need to find next greater element
    # greater means we need to remove smaller elements -> decreasing stack
    # for next we go from reverse
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = deque()
        ans = [0] * n
        for i in range(n-1,-1,-1):
            # if current element if >= stack.peek() pop the stack
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            # Index diff of stack.peek() and current element
            # Since we are iterating in reverse index of stack[-1] >= i
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans
