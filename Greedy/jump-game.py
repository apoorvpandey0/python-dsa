"""
    Jump game
    Desc: Given an array of non-negative integers, you are initially positioned at the first index of the array.
            Each element in the array represents your maximum jump length at that position.
            Determine if you are able to reach the last index.
    Link: https://leetcode.com/problems/jump-game/
"""


# Solution 1:
# Max reachable approach
# Time: O(n) | Space: O(1) 
# Runtime: 577 ms, faster than 67.90% of Python3 online submissions for Jump Game.
# Memory Usage: 15.1 MB, less than 88.59% of Python3 online submissions for Jump Game.
def jumps(nums):
    """
        You can take at most nums[i] steps from position i to reach position i + nums[i]
    """
    N = len(nums)
    
    # Since we are starting from index 0 max_reachable_index = 0
    max_reachable = 0
    for i in range(N):
        
        # This means we are at an index which is not reachable from the previous indices
        if i>max_reachable: return False
        
        # Max index that can be reached from index i is i + nums[i]    
        max_reachable = max(max_reachable,i+nums[i])
    
    return True