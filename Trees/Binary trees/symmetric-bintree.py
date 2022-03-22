"""
    Find if the given binary tree is symmetric or not.
    A binary tree is symmetric if the left and right subtrees of the root are mirror images of each other.
    Ex:
          1
         / \
        2   2
       / \ / \
      3  4 4  3
    is symmetric.
    Link: https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution1:
    """
        Using level order traversal:
            1. Store the Null values as well
            2. Check if each level is a pallindrome
    """
    def lot(self,node):
        q = deque()
        q.append(node)
        
        res = []
        curr = node
        
        while q:
            lvl = []
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    lvl.append(None)
                    continue
                else:
                    if curr.left: q.append(curr.left)
                    else: q.append(None)
                    if curr.right: q.append(curr.right)
                    else: q.append(None)
                    lvl.append(curr.val)
            # print(lvl)
            res.append(lvl)
        return res
              
    # Runtime: 40 ms, faster than 74.07% of Python3 online submissions for Symmetric Tree.
    # Memory Usage: 14 MB, less than 38.29% of Python3 online submissions for Symmetric Tree.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isPallindrome(s):
             return s == s[::-1]
        res = self.lot(root)
        # print(res)
        for row in res:
            if not isPallindrome(row):return False
        return True

class Solution2:
    # Using recursion
    pass