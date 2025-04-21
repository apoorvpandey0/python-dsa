https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self,height):
        stack = []
        total_water = 0
        for i, h in enumerate(height):
            # Process stack when current height is higher than top
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[bottom]
                total_water += distance * bounded_height
            stack.append(i)
        return total_water
