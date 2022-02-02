"""
    Buy sell stocks 
    Desc: Pick the one best transaction that'll give max returns
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


# Solution 1:
# Using right max array
# Time: O(n) | Space O(n)
# Runtime: 1789 ms, faster than 41% of Python3 online submissions for Best Time to Buy and Sell Stock.
def bss1(nums):
    # Build right max array
    right = [-1] * len(nums)
    right[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        right[i] = max(nums[i], right[i + 1])

    # Compare the right and nums values for each i
    answer = 0
    for i in range(len(nums)):
        answer = max(answer, right[i] - nums[i])
    return answer


# Solution 2:
# Using minPrice since start method
# Time: O(n) | Space: O(1)
# Runtime: 1132 ms, faster than 59.02% of Python3 online submissions for Best Time to Buy and Sell Stock.
def bss2(nums):
    minPrice = nums[0]
    answer = 0
    for i in range(len(nums)):
        minPrice = min(nums[i], minPrice)
        answer = max(answer, nums[i] - minPrice)
    return answer


print(bss1([7, 1, 5, 3, 6, 4]))
