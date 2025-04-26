from collections import defaultdict
same as subarray sum = k and binary sum
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # subarray sum = k 
        n = len(nums)
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        ps = 0
        for ele in nums:
            ps+= 0 if ele%2==0 else 1
            ans += counts[ps- k]   
            counts[ps]+=1
        return ans
