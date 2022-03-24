"""
    Find the kth smallest element in a BST.
    Note:
        You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
        Also k is 1 indexed.
    Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Video: https://www.youtube.com/watch?v=KqMm81Y7j9M
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ino = []

    # Algorithm:
    # 1. Find the inorder traversal of a BST
    # 2. kth element would be k-1th element in inorder traversal
    def soln1(self, root: Optional[TreeNode], k: int) -> int:
        """
            Time: O(n) | Space: O(n+Height)
            For some wierd reason this is not accepted in Leetcode
        """
        def iot(node):
            if not node: return
            iot(node.left)
            self.ino.append(node.val)
            iot(node.right)
        iot(root)
        print(self.ino)
        return self.ino[k-1]

    # Basically inroder traversal without storing the entire traversal
    # Code is not clean ik
    k = None
    def soln2(self, root: Optional[TreeNode], k: int) -> int:
        """
            Time: O(n) | Space: O(Height)
            Runtime: 70 ms, faster than 56.92% of Python3 online submissions for Kth Smallest Element in a BST.
            Memory Usage: 18 MB, less than 90.39% of Python3 online submissions for Kth Smallest Element in a BST.
        """
        self.k = k
        def find(node,k):
            if not node: return 0
            
            l = find(node.left,self.k)
            if l:return l
            
            self.k-=1
            if self.k == 0: return node.val
            
            r = find(node.right,self.k)
            
            return r
        return find(root,k)

        
    def soln3(self, root: Optional[TreeNode], k: int) -> int:
        """
            Involves changing the original TreeNode structure
        """
        pass
        
        

            