"""
    Find the first missing positive
    Desc: Return the smallest missing positive integer.
    Link: https://leetcode.com/problems/first-missing-positive/
"""
from typing import List

"""
    The ideal array must be like this [1,2,3,4,5] so that the missing element becomes lastelement+1
"""
# Solution 1:
# Time: O(n) | Space: O(n)
# Runtime: 804 ms, faster than 97.75% of Python3 online submissions for First Missing Positive.
# Memory Usage: 69 MB, less than 17.71% of Python3 online submissions for First Missing Positive.
def firstMissingPositive(self, nums: List[int]) -> int:
    ms = set(nums)
    if max(nums) <1: return 1

    # Checking every number from 1 to max(nums)
    for i in range(1,max(nums)+2):
        if i not in ms: 
            return i


# Solution 2:
# We are following a three step algorithm

# Time: O(n) | Space: O(1)
# Runtime: 1099 ms, faster than 63.13% of Python3 online submissions for First Missing Positive.
# Memory Usage: 59.7 MB, less than 79.49% of Python3 online submissions for First Missing Positive.
def firstMissingPositive(self, nums: List[int]) -> int:
    N = len(nums)
    onePresent = False

    # Neutralizing all the unnessesary elements
    # Unnecessary elements include all the elements which are less than 1 and greater than N
    # Set them to 1 , If  1 is found in the array mark onePresent as True
    for i in range(N):
        if nums[i]== 1:
            onePresent = True
        elif N<nums[i] or nums[i]<1:
            nums[i] = 1
    # print(nums)

    # If onePresent is True, then the first missing positive is 1
    if not onePresent: return 1
    
    # Now the array contains only elements between 1 and N
    # Mark the elements at index nums[i]-1 as negative implying they are reachable
    for i in range(N):
        index = abs(nums[i])
        nums[index-1] = abs(nums[index-1])*-1
    # print(nums)

    # Now the array contains only positive elements
    # Find the first positive element
    for i in range(N):
        if nums[i]>0:
            return i+1
    # print(nums)

    # If all the elements are negative, then the first missing positive is N+1
    return N+1
    