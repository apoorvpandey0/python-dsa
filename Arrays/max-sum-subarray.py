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
def ms(self, nums: List[int]) -> int:

    # temporary subarray sum, this will keep iterating throughout array
    curr = 0

    # final ans
    answer = float('-inf')

    for i,ele in enumerate(nums):
        curr+=ele

        # reset current subarray to current element if subarray sun is <current element
        curr = ele if curr<ele else curr

        # answer should be maximum of current subarray sum and itself
        answer = max(curr,answer)
    return answer

# print(ms([-2, -3, 4, -1, 8, -8, 5, -3]))  #11
# print(ms([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  #6
# print(ms([1]))  #1
print(ms([-1, -2]))
