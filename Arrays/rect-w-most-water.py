"""
    Container with most water
    Desc: Find the container which could hold most water
    Link: https://leetcode.com/problems/container-with-most-water
"""


# Algortihm:
# We follow two pointers, with greedy approach
# Time: O(n) | Space: O(1)
# Runtime: 855 ms, faster than 64.09% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.3 MB, less than 90.11% of Python3 online submissions for Container With Most Water.
def maxArea(nums):
    l,r = 0,len(nums)-1
    max_area = 0
    while l<r:
        # Calculating and assigning max_area
        curr_area = min(nums[l],nums[r])*(r-l)
        max_area = max(max_area,curr_area)

        # Main juice
        # If left height is smaller than right, move left pointer by +1
        # If right height is smaller than left, move right pointer by -1
        # If left height == right height, move any(here right) pointers by 1
        if nums[l]<nums[r]: l+=1
        else: r-=1
    return max_area