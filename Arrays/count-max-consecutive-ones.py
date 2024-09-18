class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        tmp = 0
        for n in nums:
            if n == 1:
                tmp+=1
            elif n == 0:
                tmp = 0
            ans = max(tmp,ans)
        return ans
