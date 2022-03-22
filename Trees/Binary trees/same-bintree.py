"""
    Same tree
    Check if two given binary trees are same or not
    By sturucture and by value
    Link: https://leetcode.com/problems/same-tree/
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1
# Run any of three traversals two times and compare the results.
# Runtime: 49 ms, faster than 36.50% of Python3 online submissions for Same Tree.
# Memory Usage: 13.9 MB, less than 47.65% of Python3 online submissions for Same Tree.
class Solution1:
    def pot(self,root):
        res = []
        def rec(node):
            if not node: 
                res.append(None)
                return
            res.append(node.val)
            rec(node.left)
            rec(node.right)
        rec(root)
        return res

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.pot(p) == self.pot(q)
# Solution 2
# Check node by node if they are same
# Runtime: 40 ms, faster than 61.55% of Python3 online submissions for Same Tree.
# Memory Usage: 13.9 MB, less than 47.65% of Python3 online submissions for Same Tree.
class Solution2:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(node1, node2):
            
            # If both trees are empty return True coz empty trees are also equal
            if not node1 and not node2:                
                return True
            
            # If One of the trees is empty return False 
            if not node1 or not node2:                
                return False

            # If both trees are not empty and have same different value return False
            if node1.val != node2.val:                
                return False
            
            # If both trees have same value then check their left and right subtrees recursively
            return is_same(node1.left, node2.left) and is_same(node1.right, node2.right)
        
        return is_same(p, q)