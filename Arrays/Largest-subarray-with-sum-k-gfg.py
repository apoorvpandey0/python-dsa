https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

class Solution:
    def lenOfLongestSubarr(self, nums, k):  
        ps = [0 for i in nums]
        
        
        ps[0] = nums[0]
        for i in range(1,len(nums)):
            ps[i]  = ps[i-1] + nums[i]
        
        # print(ps)
        ans = 0

        # values store the prefix sums value with their least index at which that sum occured
        values = {0:-1}
        for i,ele in enumerate(nums):
            
            if ps[i] in values: min(values[ps[i]],i)
            else: values[ps[i]] = i
            
            
            if ps[i] - k in values: 
                ans = max(ans,i - values[ps[i] - k])
                
            # print(values)
            # print(ele,ans)
        return ans
            
