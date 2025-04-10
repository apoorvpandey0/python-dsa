https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

Mudde ke points: 
Start tmpDays with 1
update currSum after if
condition ------>   currrSum + currWeight > capacity

class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        lo = max(nums)  # Minimum capacity is at least the largest single package
        hi = sum(nums)  # Maximum capacity is the sum of all packages
        ans = float('inf')
        
        while lo <= hi:
            capacity = (lo + hi) // 2
            
            # Think of this like at least one day will be required when counting with max capacity ships
            tmpDays = 1  
            currSum = 0

          # Validate the capacity
            for weight in nums:
                if currSum + weight > capacity:
                    tmpDays += 1 
                    currSum = 0  
                currSum += weight
          
            # Make changes as per the number of days taken by assumed capacity
            if tmpDays <= days:  
                ans = min(ans, capacity)
                hi = capacity - 1
            else:
                lo = capacity + 1
        
        return ans
