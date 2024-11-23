https://leetcode.com/problems/single-element-in-a-sorted-array/description/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.


Soln1: O N solution using XOR
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y,nums)


Soln2: using BS log N
"""
    The pairs which are on the left of the single element, will have the first element in an even position and the second element at an odd position. 
    All the pairs which are on the right side of the single element will have the first position at an odd position and the second element at an even position.
    Use this fact to decide whether to go to the left side of the array or the right side.
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start<end:
            mid = (start+end)//2

            if nums[mid+1] == nums[mid]:
                if mid %2 == 0:
                    start = mid+2
                else:
                    end = mid - 1
            elif nums[mid+1] != nums[mid]:
                if mid % 2 == 0:
                    end = mid
                else:
                    start = mid + 1
        return nums[start]
