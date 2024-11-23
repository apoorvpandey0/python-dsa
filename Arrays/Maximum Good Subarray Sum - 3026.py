# https://leetcode.com/problems/maximum-good-subarray-sum/description/
# https://www.youtube.com/watch?v=zFxDDglHb4o

# clean soln: https://leetcode.com/problems/maximum-good-subarray-sum/solutions/4672257/python-easy-solution-prefix-sum/

"""
Concepts used two sum, prefix sum, hash map
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        values = {nums[0]:0}
        ps = [0 for i in nums]
        ans = float('-inf')

        tmp = 0
        for i,ele in enumerate(nums):
            tmp+=ele
            ps[i] = tmp

        for j in range(1,len(nums)):
            
            if nums[j] in values: values[nums[j]] = min(ps[j-1],values[nums[j]] )
            else: values[nums[j]] = ps[j-1]
            # print(values)
            a = nums[j] + k
            b = nums[j] - k 
            # print(nums[j],a,b)
            if a in values:
                ans = max(ans,ps[j]-values[a])
            if b in values:
                ans = max(ans,ps[j]-values[b])
            # print(ans)
        return ans if ans != float('-inf') else 0
            
