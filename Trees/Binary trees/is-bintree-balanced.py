"""
    Find if a binary tree is balanced or not
    Desc: Balanced means the difference in height between left and right subtrees should not be more than 1
    Link: https://leetcode.com/problems/balanced-binary-tree/
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Runtime: 52 ms, faster than 90.23% of Python3 online submissions for Balanced Binary Tree.
    # Memory Usage: 18.9 MB, less than 22.76% of Python3 online submissions for Balanced Binary Tree.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
            
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]