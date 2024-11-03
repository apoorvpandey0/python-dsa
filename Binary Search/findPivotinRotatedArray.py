https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
  """
  Start will eventually come to the pivot and the loop will go INFINITE
  The stopping condition here is in while loop start<end
  because of the logic end will never be > start
  hence we need to stop only at start<end and not start<=end
  """
    def findMin(self, nums: List[int]) -> int:
        # Check if the array is not rotated
        if nums[-1] >= nums[0]:
            return nums[0]

        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
