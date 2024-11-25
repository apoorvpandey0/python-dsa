https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/



================ Brute Forced ==================

O N^2 | TLE 52/71 test cases
I believe this is correct otherwise
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = float('inf')
        for i in range(start,end+1):
            tmpSum = 0
            for ele in nums:
                tmpSum+= math.ceil(ele/i)
            if tmpSum<=threshold:
                ans = min(i,ans)
        return ans


================ Optimized ======================
