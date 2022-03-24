"""
    Validate a BST
    A tree is  BST IFF:
        1. All the nodes in the left subtree of a node are smaller than the node itself
        2. All the nodes in the right subtree of a node are greater than the itself
    Link: https://leetcode.com/problems/validate-binary-search-tree/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    # Runtime: 67 ms, faster than 44.50% of Python3 online submissions for Validate Binary Search Tree.
    # Memory Usage: 16.5 MB, less than 77.50% of Python3 online submissions for Validate Binary Search Tree.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node,mine,maxe):
            if not node: return True
            
            # print(node.val,mine,maxe)
            if not mine<node.val<maxe: return False
            
            l = validate(node.left,mine,node.val)
            r = validate(node.right,node.val,maxe)
            
            # print(node.val,mine,maxe,l,r)
            
            return l and r
    
        return validate(root,float('-inf'),float('inf'))
            