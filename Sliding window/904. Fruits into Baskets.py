# https://leetcode.com/problems/fruit-into-baskets/description/

# subarray with at most k distinct elements
class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        lastO = {}
        i = 0
        ans = 0
        for j in range(len(nums)):
            lastO[nums[j]] = j

            if len(lastO)>2:
                del_idx = min(lastO.values())
                del lastO[nums[del_idx]]
                i = del_idx + 1
            ans = max(ans,j-i+1)
        return ans
