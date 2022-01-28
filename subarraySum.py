import math
class Solution:
    """
        Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
        Question: https://leetcode.com/problems/subarray-sum-equals-k/
        Solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/503178/Python5-Approaches-easy-to-understand-with-detailed-explanations
        Video: https://www.youtube.com/watch?v=HbbYPQc-Oo4
    """
 
    # Prefix sum method
    # Time: O(n^2) | TLE
    def subarraySum1(self, nums,k):
        solutions = []
        counter = 0

        # Creating prefix sum array
        ps = [0] * len(nums)
        ps[0] = nums[0]
        for i in range(1,len(nums)):
            ps[i] = nums[i]+ps[i-1]
        # print("Original arrat:",nums)
        # print("Prefix sum array:",ps)

        for left in range(len(nums)):

            # start from left+1 if arr[i] == k case is not allowed
            for right in range(left,len(nums)):
                
                # print(left,right, ps[right] - (ps[left-1] if left!=0 else 0))
                if ps[right] - (0 if left==0 else ps[left-1]) == k:
                    
                    counter+=1                    
        return counter
    
    # Using Dictionary
    # Time O(n) | 244ms fastrer than 93% of Python submissions
    def subarraySum(self,nums,k):
        dict = {}
        dict[0] = 1
        sum =0
        counter = 0
        for ele in nums:
            sum+=ele
            if sum-k in dict:
                counter+=dict[sum-k]
            if sum in dict:
                dict[sum] += 1
            else:
                dict[sum] = 1
            # print(dict) 
        return counter
    
    # Sliding window will work only for positive sorted numbers 

# print(Solution().subarraySum([1,1,1],2))
# print(Solution().subarraySum([1,2,3,4],3))
# print(Solution().subarraySum([1,-1,0],0))
        