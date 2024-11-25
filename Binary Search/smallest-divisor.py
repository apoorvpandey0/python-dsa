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
O N * LOG N Solution

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        ans = float('inf')
        while start<=end:
            mid = (start+end)//2
            tmpSum = 0
            for ele in nums:
                tmpSum+= math.ceil(ele/mid)
            if tmpSum<=threshold:
                ans = min(mid,ans)
            
            if tmpSum>threshold: start = mid + 1
            else: end = mid - 1
        return ans

"""
1.  If we did not used start<=end and used start<end
    We would not reach cases where answer is atstart or end of the answer space
    Ex: Input: nums = [44,22,33,11,1], threshold = 5
    Output: 44
2. We have to use start = mid + 1 and end = mid - 1 and not just start = mid or end = mid, to make the exit for the while loop
"""
