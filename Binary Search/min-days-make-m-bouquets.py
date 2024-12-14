https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

Core logic:
Count all adjacent subarrays where bloom is True
If bloom is false for a current index, reset the adjacent array bloom counter
class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        lo = min(nums)
        hi = max(nums)
        ans = float('inf')
        while lo<=hi:
            day = (lo+hi)//2

            # Validation logic
            tmpK = k
            count = 0
            for ele in nums:
  
                # if adjacent bloomed tmpK--
                if ele<=day:
                    tmpK-=1
                
                # If not adjacent then reset tmpK
                else:
                    tmpK = k

                # Check if bouquet is possible at every element, count++ and reset tmpK for next bouquet
                if tmpK == 0:
                    count+=1
                    tmpK = k
            
            # Update binary search conditions
            if count>=m:
                ans = min(ans,day)
                hi = day - 1
            else: lo = day + 1
              
        return -1 if ans == float('inf') else ans
