import math


class Solution:
    """
        Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
        Question: https://leetcode.com/problems/subarray-sum-equals-k/
        Solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/503178/Python5-Approaches-easy-to-understand-with-detailed-explanations
                  https://leetcode.com/problems/subarray-sum-equals-k/discuss/867435/DETAILED-EXPLANATION-OF-MATH-BEHIND-O(N)-SOLUTION-PYTHON3
        Video: https://www.youtube.com/watch?v=HbbYPQc-Oo4
        https://www.youtube.com/watch?v=fFVZt-6sgyo
    """

    # Solution 1
    # Brute force | TLE
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
    
        # Check all subarrays
        for start in range(n):
            current_sum = 0  # Reset sum for new starting point
            for end in range(start, n):
                current_sum += nums[end]  # Add the current element to the sum
                if current_sum == k:  # Check if the sum equals k
                    count += 1  # Increment the count
        return count

    
    # Solution 2:
    # Prefix sum method
    # Time: O(n^2) | TLE
    def subarraySum1(self, nums, k):
        solutions = []
        counter = 0

        # Creating prefix sum array
        ps = [0] * len(nums)
        ps[0] = nums[0]
        for i in range(1, len(nums)):
            ps[i] = nums[i] + ps[i - 1]
        # print("Original arrat:",nums)
        # print("Prefix sum array:",ps)

        for left in range(len(nums)):

            # start from left+1 if arr[i] == k case is not allowed
            for right in range(left, len(nums)):

                # PS[right] - PS[left] with edge case handling
                if ps[right] - (0 if left == 0 else ps[left - 1]) == k:

                    counter += 1
        return counter


    # Try this
    # Input
    # nums =
    # [3,4,7,-2,2,1,4,2]
    # k =
    # 7
    # Stdout
    # i,counter,preFixSum,,dict
    # 3 0 3 {0: 1, 3: 1}
    # 4 1 7 {0: 1, 3: 1, 7: 1}
    # 7 2 14 {0: 1, 3: 1, 7: 1, 14: 1}
    # -2 2 12 {0: 1, 3: 1, 7: 1, 14: 1, 12: 1}
    # 2 3 14 {0: 1, 3: 1, 7: 1, 14: 2, 12: 1}
    # 1 3 15 {0: 1, 3: 1, 7: 1, 14: 2, 12: 1, 15: 1}
    # 4 4 19 {0: 1, 3: 1, 7: 1, 14: 2, 12: 1, 15: 1, 19: 1}
    # 2 6 21 {0: 1, 3: 1, 7: 1, 14: 2, 12: 1, 15: 1, 19: 1, 21: 1}
    # Solution 2:
    # Prefix sum with Dictionary and Single pass method
    # Algorithm: 
    # 1. Create a dictionary with key as sum and value as count of subarrays with that sum
    # 2. Iterate over the array and keep adding the current sum to the dictionary
    # 3. If the sum is in the dictionary, then increment the count
    # 3. If the sum -k is in dict, ie. the sum has been seen before => then increment the count
    # 4. Return the count
    # Time O(n) | 244ms fastrer than 93% of Python submissions
    def subarraySum(self, nums, k):
        dict = {}
        # I dont clearly understand this part
        dict[0] = 1
        sum = 0
        counter = 0
        # lets take nums as [1,1,1,1] and k = 2 => ans = 3
        # Prefix sum array: [1, 2, 3, 4]
        for ele in nums:
            # tack prefix sum till this element
            sum += ele

            # 0 -> j (sum) subtract 0 -> i (another subarray) = k i.e subarray with sum k is i -> j
            # => If  0 -> j (sum) - k is in dict then we have already found a subarray which will satisfy the eq above
            # counter += how many time we have encountered the subarray before, in line above
            if sum - k in dict:
                counter += dict[sum - k]

            # store sum 0 ->j values in dict for later use
            if sum in dict:
                dict[sum] += 1
            else:
                dict[sum] = 1
            # print(dict)
        return counter

    # Sliding window will work only for positive sorted numbers

    # Solution 3
    # Solution 2's cleaner implementation
    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return (count)

"""
Solution 2 with another explanation:
The question asks how many subarray sum equals to k. For a subarray to sum to k, you need a subarray, as in a part of the array from index 'a' to index 'b' to have a sum equal to k. 
But when we reach any index 'b', we obviously do not know, if there was a subarray from index 'a' to index 'b' equal to k. 
However we do have the sums from 0 to index 'a' in our hash map, because we have been storing all sums starting from index '0' to every single index till now, and the count of them as the value of the key. 
Now obviously sum_0_to_a + sum_a_to_b  = total sum so far (curSum). If we go to the original ask, which is we need a prefix that is sum_a_to_b to be equal to k. For that to hold true, replace sum_a_to_b with 'k'. Hence, sum_0_to_a + k  = curSum. Hence curSum - k = sum_0_to_a. 
And then since we have been storing all possible values of sum_0_to_a so far in the hashmap, curSum - k must exist in the hashmap as a key, and we can simply add the value from the hashmap to add number of prefixes from 0 to any index which equalled to curSum - k .

OR

Think of 

let subarray with sum = k be subarray from index a->b

cumulative_sum = sum_0_a + sum_a_b                    ------ 1

replacing sum_a_b with k as asked in question: cumulative_sum = sum_0_a + k

=> sum0_a = cumulative_sum - k                               --------2 
new question is find all sum_0_a for each index from 0->n where sum0_a is eq 2


** Order of if conditions is important
** cumulative sum can be written as sum_0_b
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # The first IF has to be above the second if case fail [1], 0
        
        ans = 0
        freq = {0:1}
        currSum = 0
        for i,ele in enumerate(nums):
            currSum+=ele
        
            if currSum - k in freq: ans+=freq[currSum-k]

            if currSum in freq: freq[currSum]+=1
            else: freq[currSum] = 1
        return ans

"""
    Above solution Without 0:1
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        freq = {}
        currSum = 0
        for i,ele in enumerate(nums):
            currSum+=ele

            if currSum == k: ans+=1
            if currSum - k in freq: ans+=freq[currSum-k]

            if currSum in freq: freq[currSum]+=1
            else: freq[currSum] = 1
        
        return ans

# print(Solution().subarraySum([1,1,1],2))
print(Solution().subarraySum([-1, 1, 2, 3, 4], -1))
# print(Solution().subarraySum([1, -1, 0, 0, 0], 0))
