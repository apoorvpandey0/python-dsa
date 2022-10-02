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
    # Solution 1
    # A bit complex
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
    
    # Solution 2
    # Clean code
    # Runtime: 47 ms, faster than 98.35% of Python3 online submissions for Balanced Binary Tree.
    # Memory Usage: 18.7 MB, less than 60.84% of Python3 online submissions for Balanced Binary Tree.
    def isBalanced2(self, root):
        def check(root):
            
            # Return heght of leaf node as 0
            if not root: return 0
            
            # Find height of left and right subtrees
            lh = check(root.left)
            rh = check(root.right)

            # If any of subtrees is not balanced i.e. -1 return -1            
            if lh == -1 or rh ==-1: return -1

            # if current node is not balanced return -1
            if abs(lh-rh)>1: return -1

            # Return height +1
            return max(lh,rh)+1

        # To return a boolean value
        return check(root)!=-1
