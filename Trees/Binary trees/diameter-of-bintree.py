"""
    Diameter of a binary tree
    Desc: The length of a path between two nodes is represented by the number of edges between them.
          Diameter can also be called as longest path b/w two nodes in a binary tree
    Link: https://leetcode.com/problems/diameter-of-binary-tree/
    Partial soln: https://www.youtube.com/watch?v=ey7DYc9OANo
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Runtime: 49 ms, faster than 77.66% of Python3 online submissions for Diameter of Binary Tree.
    # Memory Usage: 16.3 MB, less than 83.83% of Python3 online submissions for Diameter of Binary Tree.
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
            
        def dfs(root):
            if not root: return 0
            leftLongestPath = dfs(root.left)
            rightLongestPath = dfs(root.right)
            
            # keep track of the longest path that goes through the current
            # node i.e. the longest path from it's left child to leaf
            # through to its right child to a leaf and return that
            # We do not add 1 here because question asks us to find the no. of edges
            # Diameter at any node would be height of left subtree + height of right subtree
            # If that's greater than previous diameter then update the diameter
            self.diameter = max(self.diameter, (leftLongestPath + rightLongestPath))
            
            # this is the standard recursive procedure
            # for calculating maximum height for a tree
            # i.e. longest path recursively from either 
            # left or right subtree + 1 for the current
            # level. For instance, if there's just one node
            # we'll check its left and right subtree, both of
            # which will return 0 from our base condition
            # and then max(0, 0) + 1 => 1 the correct height
            return max(leftLongestPath, rightLongestPath) + 1
        
        dfs(root)
        return self.diameter