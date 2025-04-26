from collections import defaultdict

#  Same as subarray sum = k
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        ps = 0
        for ele in nums:
            ps+=ele

            # if is not even required since dd will give 0 for non existent values
            if ps - goal in counts:
                ans += counts[ps- goal]   
            counts[ps]+=1
        return ans
