"""
    53. Maximum Subarray
    Desc: Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    Link: https://leetcode.com/problems/maximum-subarray/
"""


# Solution:
# Using Kdanes algorithm
# Dry run the program for this to make sense
# Time: O(n)
# Runtime: 744 ms, faster than 78.32% of Python3 online submissions for Maximum Subarray.
def ms(nums):
    curr = 0
    answer = float('-inf')
    for i in range(len(nums)):
        curr += nums[i]
        if curr < nums[i]:
            curr = nums[i]
        answer = max(answer, curr)
        print(curr, answer, nums[i])
    return answer


# print(ms([-2, -3, 4, -1, 8, -8, 5, -3]))  #11
# print(ms([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  #6
# print(ms([1]))  #1
print(ms([-1, -2]))
