"""
    Sum of all left leaves in a binary tree.
    Link: https://leetcode.com/problems/sum-of-left-leaves/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Both soln 1 and 2 are essentially same and logically 2nd should be faster and more space efficient.

# Solution 1:
# Runtime: 33 ms, faster than 85.05% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.6 MB, less than 73.24% of Python3 online submissions for Sum of Left Leaves.\
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def pot(node,inLeft):
            if node == None: return
            if inLeft and not node.left and not node.right: ans.append(node.val)
            pot(node.left,True)
            pot(node.right,False)
        pot(root,False)
        return sum(ans)


# Solution 2:
# Runtime: 51 ms, faster than 41.60% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.7 MB, less than 50.88% of Python3 online submissions for Sum of Left Leaves.
class Solution2:
    total = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def pot(node,inLeft):
            if node == None: return
            if inLeft and not node.left and not node.right: self.total += node.val
            pot(node.left,True)
            pot(node.right,False)
        pot(root,False)
        return self.total