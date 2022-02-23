"""
    Find the equilibrium index
    Desc: An equilibrium index P such that 0 ≤ P ≤ N and the sum of elements of lower indices is equal to the sum of elements of higher indices.
    Link: https://leetcode.com/problems/find-pivot-index/
"""
# Solution 1: 
# Using left and right sum arrays
# Time: O(n) | Space: O(n)
# Runtime: 227 ms, faster than 46.27% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.2 MB, less than 70.98% of Python3 online submissions for Find Pivot Index.
def eqI(nums):
    n = len(nums)
    if n <2: return 0
    
    # Build left sum array
    ps = [nums[0]]
    for i in range(1,n):
        ps.append(nums[i]+ps[i-1])
    ps.insert(0,0)
    # print(ps)
    
    # Build right sum array
    rs = [-1 for i in range(n)]
    rs[n-1] = nums[n-1]
    for i in range(n-2,-1,-1):
        rs[i] = (nums[i]+rs[i+1])
    rs.append(0)
    # print(rs)
    
    # Check if leftsum[i] == rightsum[i+1]
    for i in range(0,n):
        if ps[i] == rs[i+1]:
            return i
    else:
        return -1

# Solution 2:
# Only using Left sum counters
# Time: O(n) | Space: O(1)
# Runtime: 194 ms, faster than 61.07% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.3 MB, less than 70.98% of Python3 online submissions for Find Pivot Index.
def eqI2(nums):
    if len(nums) == 1: return 0
    # Sum fo left subarray(index<0), sum of right subarray(1<index<n)
    left, right = 0, sum(nums)

    for i in range(0, len(nums)):
        # At index i right  = sum of all elements to the right of i ie i+1 to n-1
        right -= nums[i]
        # At index i left = sum of all elements to the left of i ie 0 to i-1
        if left == right:
            return i
        
        # Add nums[i] since we will move to i+1 now in next iteration
        left += nums[i]
    return -1