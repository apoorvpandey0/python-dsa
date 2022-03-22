"""
    Flatten a binary tree in to a linked list or a skewed tree
    Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

"""
Input: 
          1
        /   \
       2     5
      / \     \               
     3   4     6
              / 
             7

Outut:
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
               \
                7
"""

from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Solution 1 using recursion
    # Time: O(n) | Space: O(n)
    prev = None
    def soln1(self, root: Optional[TreeNode]) -> None:
        """
        Runtime: 57 ms, faster than 45.06% submissions.
        Memory Usage: 15.2 MB, less than 87.33% submissions.
    
        Do not return anything, modify root in-place instead.
        """
        
        def rpost(node):
            if not node: return
            rpost(node.right)
            rpost(node.left)
            node.right = self.prev
            node.left  = None
            self.prev = node
        rpost(root)
    
    # Solution 2 using Stack 
    # Time: O(n) | Space: O(n)

    # Solution 3 without using extra space
    # Time: O(n) | Space: O(1)
    def soln3(self, root: Optional[TreeNode]) -> None:
        """
        Runtime: 30 ms, faster than 98.87% submissions.
        Memory Usage: 15.4 MB, less than 11.50% submissions.
        
        Do not return anything, modify root in-place instead.
        """
        if root:
            currentRight = root.right
            root.right = root.left
            
            dummy = root
            while dummy.right:
                dummy = dummy.right    
            dummy.right = currentRight
            
            root.left = None
            self.flatten(root.right)