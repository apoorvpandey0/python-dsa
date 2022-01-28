"""
    Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,
    then the whole array will be sorted in ascending order.
    Return the shortest such subarray and output its length.
    https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""

import math
# Runtime: 264 ms, faster than 21.92% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
class Solution:
    def isOutofOrder(self, nums, i):
        # i==0 for left edge case of the array
        if i == 0 :
            if nums[i]<nums[i+1]:
                return False
            else:
                # Out of order
                return True
        if i == len(nums)-1:
            return nums[i]<nums[i-1]
        
        # For all the other elements
        if nums[i]<nums[i+1] and nums[i]>nums[i-1]:
            return False
        else:
            # Out of order
            return True
            
        return False
    
    def findUnsortedSubarray(self, nums):
        if len(nums)<2:
            return 0
        
        # These are the start and end elements of the unsorted subarray
        smallest = math.inf
        largest = - math.inf
        
        # Finding the smallest and largest elements out of order
        for i in range(len(nums)):
            # len(nums) - 1 for right edge case of the array
            
            if(self.isOutofOrder(nums,i)):
                smallest = min(smallest,nums[i])
                largest = max(largest,nums[i])
        
        print(smallest,largest)
        
        # Finding places to insert these elements
        if smallest == math.inf:
            return 0
        
        left = 0
        while smallest>=nums[left] and left<len(nums)-1:
            left+=1
        
        right = len(nums)-1
        while largest<=nums[right] and right>0:
            right-=1
        
        # case when subarray consists of same elements
        if len(set(nums[left:right+1])) ==1 or right - left +1 < 0:
            return 0
        
        return right-left+1
        
            


print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15])) # 5
print(Solution().findUnsortedSubarray([1,2,3,3,3])) # 0
print(Solution().findUnsortedSubarray([1,3,2,3,3])) # 2
print(Solution().findUnsortedSubarray([2,1,3])) # 2

