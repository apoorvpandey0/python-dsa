"""
    53. Maximum Subarray
    Desc: Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    Link: https://leetcode.com/problems/maximum-subarray/
"""


# Solution:
# Using Kdanes algorithm
# Dry run the program for this to make sense
# Time: O(n)
# Minimum sum subarray ke lie just signs change
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

# Also counting the subarray indices which has the maxium sum
def maxSubArray(self, nums: List[int]) -> int:
    # SubArray track
    l = 0
    r = 0

    # usual
    curr = 0
    answer = float('-inf')

    for i,ele in enumerate(nums):
        curr+=ele
        if curr<ele:
            curr = ele

            # Update the starting pointer of subarray as i
            l = i

        if curr> answer:
            answer = curr

            # At this point we have stepped out of the max subarray
            # Hence update end pointer with i
            r = i
        answer = max(curr,answer)


# print(ms([-2, -3, 4, -1, 8, -8, 5, -3]))  #11
# print(ms([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  #6
# print(ms([1]))  #1
print(ms([-1, -2]))
