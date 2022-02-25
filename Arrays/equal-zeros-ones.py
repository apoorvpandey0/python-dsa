"""
    Contiguous Array
    Desc: Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
    Link: https://leetcode.com/problems/contiguous-array/
"""

# Solution 1:
# Brute forced - TLE

# Solution 2:
# Using dictionary
# Time: O(n) | Space: O(n) 
# Runtime: 896 ms, faster than 83.37% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.5 MB, less than 40.93% of Python3 online submissions for Contiguous Array.
def findMaxLength( nums):
    """
        Observation: If we replace all zeroes with -1, the problem is reduced to finding largest subarray with sum = 0
    """
    tmp = {}
    longest = 0
    curr_sum = 0
    for i,ele in enumerate(nums):
        # Adding -1 instead of 0 to make it easier to find the subarray with sum = 0
        curr_sum+= -1 if ele==0 else 1

        # Sum ==0 means subarray starts from left 0 till right i
        # => Length of subarray is i+1        
        if curr_sum ==0:
            longest = i+1
        
        # If the sum is already in the dictionary, then we have found a subarray with equal number of 0 and 1    
        if curr_sum in tmp:
            longest = max(longest,i-tmp[curr_sum])
        
        # Adding the sum to the dictionary
        else:
            tmp[curr_sum] = i
        # print(tmp)
    return longest
            