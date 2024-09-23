"""
    Buy sell stocks 
    Desc: Pick the one best transaction that'll give max returns
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


# Solution 1:
# Using right max array
# Time: O(n) | Space O(n)
# Very slow
def maxProfit(self, prices: List[int]) -> int:
    lMin = [float('-inf') for i in prices]
    
    tmp = prices[0]
    for i in range(len(prices)):
        tmp = min(prices[i],tmp)
        lMin[i] = tmp
        
    ans = 0
    for i in range(len(prices)):
        ans = max(ans,prices[i]-lMin[i])
    return ans

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
