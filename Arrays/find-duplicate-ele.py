"""
    Find the duplicate number
    Link: https://leetcode.com/problems/find-the-duplicate-number/
"""


# Solution 1:
# If the array is Mutable
# Logic:
# Each nums[abs(ele)] will be positive except if its a duplicate
# And will be the same element
# Time: 0(n) | Space O(1)
# Runtime: 819 ms, faster than 55.50% of Python3 online submissions for Find the Duplicate Number.
def find(nums):
    """
        Example:
        Input: [1,3,4,3,2]
        Output: 3

        Dry run:                        
        for ele = 1 : 
            [1,-3,4,3,2]
        for ele = -3 : 
            [1,-3,4,-3,2]
        for ele = 4 : 
            [1,-3,4,-3,-2]
        for ele = -3 : 
            [1,-3,4,-3,-2]
            Since element at abs(-3) is -ve => duplicate
            return abs(ele)
    """
    for ele in nums:
        if nums[abs(ele)] > 0:
            nums[abs(ele)] *= -1
        else:
            return abs(ele)
    return None


# Solution 2:
# Flyods cycle detection algorithm
# Check YT for proof of correctness: https://www.youtube.com/watch?v=dfIqLxAf-8s
# Time: O(n) | Space O(1)
# Runtime: 985 ms, faster than 37.89% of Python3 online submissions for Find the Duplicate Number.
def find2(nums):
    slow = fast = ans = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while ans != slow:
        ans = nums[ans]
        slow = nums[slow]
    return ans
