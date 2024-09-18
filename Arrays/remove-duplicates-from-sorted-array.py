# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 1. Use set to store unique values and count
# 2. Use two pointer method
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:return 1
        l = 1
        r = 1

        while r<len(nums):
            if nums[r-1]!=nums[r]: 
                nums[l] = nums[r]
                l+=1
            r+=1
        return l
