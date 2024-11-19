https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620
class Solution:
    def leaders(self, nums):
        ans = []
        rSum = [0 for i in nums]
        
        mx = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            mx = max(mx,nums[i])
            rSum[i] = mx
                
        # print(rSum)
        
        for i,ele in enumerate(nums):
            if ele>=rSum[i]:
                ans.append(ele)
        return ans
