https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum
Using similar concepts to LC 3026, https://leetcode.com/problems/maximum-good-subarray-sum/solutions/4672257/python-easy-solution-prefix-sum/
class Solution:
    def maxLen(self, nums):
        # Generating prefix sum
        ps = [0 for i in nums]
        ps[0] = nums[0]
        for i in range(1,len(nums)):
            ps[i] = ps[i-1] + nums[i]
        # print(ps)

        """
          Since we want to find the largest subarray, we need to track the minimum index where sum_0-a meets the required conditions
          Store key - prefix sum : value - minimum index where we got the prefix sum
        """

        # prefix sum 0 has to be set to key -1 because of answer subs starting at 0 index, their length would be j - i + 1 or in this case j + 1 
        values = {0:-1}
        ans = 0
        
        for i,ele in enumerate(nums):
            
            if ps[i] in values: values[ps[i]] = min(values[ps[i]],i)
            else: values[ps[i]] = i
            
            # print(i,values)

            # Update answer if conditions meet
            if ps[i] in values:
                ans = max(ans,i - values[ps[i]])
        return ans
