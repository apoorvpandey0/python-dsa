"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
    # Runtime: 84 ms, faster than 38.16% of Python3 online submissions for Trapping Rain Water.
    def trap(self,heights):
        left = []
        right = []
        water = 0

        # building left array
        for i in range(len(heights)):
            if i==0:
                left.append(heights[i])
            else:
                left.append(max(left[-1],heights[i]))

        # building right array
        for i in range(len(heights)-1,-1,-1):
            if i==len(heights)-1:
                right.append(heights[i])
            else:
                right.append(max(right[-1],heights[i]))
        right = right[-1::-1]
        # print(heights)
        # print(left)
        # print(right)

        for i in range(len(heights)):
            water += min(left[i],right[i]) - heights[i]
        # print(water)

        return water

Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])