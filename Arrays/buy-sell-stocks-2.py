"""
    Buy sell stocks 2
    Desc: sum all the profitable transactions 
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


# Time: O(n) | Space: O(1)
# Runtime: 84 ms, faster than 42.19% of Python3 online submissions for Best Time to Buy and Sell Stock II.
def bss(nums) -> int:
    if len(nums) < 2:
        return 0
    profit = 0
    for i in range(1, len(nums)):
        # print(nums[i - 1], nums[i])
        if nums[i - 1] < nums[i]:
            diff = nums[i] - nums[i - 1]
            profit += diff
            # print("Profit: ", profit)
    return profit
