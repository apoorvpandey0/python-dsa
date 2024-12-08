https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        lo = max(nums)  # Minimum capacity is at least the largest single package
        hi = sum(nums)  # Maximum capacity is the sum of all packages
        ans = float('inf')
        
        while lo <= hi:
            capacity = (lo + hi) // 2
            
            tmpDays = 1  # Start with at least one day
            currSum = 0

          # Validate the capacity
            for weight in nums:
                if currSum + weight > capacity:
                    tmpDays += 1  # Need an additional day
                    currSum = 0  # Reset current sum
                currSum += weight
          
            # Make changes as per the number of days taken by assumed capacity
            if tmpDays <= days:  # If the capacity works within the days limit
                ans = min(ans, capacity)
                hi = capacity - 1
            else:  # Increase the minimum capacity
                lo = capacity + 1
        
        return ans
