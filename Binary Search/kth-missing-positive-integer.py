https://leetcode.com/problems/kth-missing-positive-number/


# Time and space O(N)
class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        st = set(nums)
        ans = None
        for i in range(1,max(nums)+k+1):
            if i not in st: 
                ans = i
                k-=1
            if k == 0: break
        return ans



# O(LOG N ) solution ...
