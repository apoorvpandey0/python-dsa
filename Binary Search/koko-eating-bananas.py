https://leetcode.com/problems/koko-eating-bananas/description/

# Search the answer space as in finding the sqrt using binary search

# Brute - max(piles) * len(nums) or O N^2


# Best - O(N∗Log(max(Piles))
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = end
        while start<=end:
            mid = (start+end)//2

            tmpHours = 0
            for i,ele in enumerate(piles):
                tmpHours += math.ceil(ele / mid)
            if tmpHours<= h:
                ans = min(ans,mid)
                end = mid - 1
            else: 
                start = mid+1
        # print(start,mid,end)
        return ans
