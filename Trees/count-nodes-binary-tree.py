"""
    Count number of nodes in binary tree
    Link: https://leetcode.com/problems/count-complete-tree-nodes/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CountNodesInBinaryTree:

    # Runtime: 134 ms, faster than 29.47% of Python3 online submissions for Count Complete Tree Nodes.
    # Memory Usage: 21.3 MB, less than 98.89% of Python3 online submissions for Count Complete Tree Nodes.
    def recursive(self, root: Optional[TreeNode]) -> int:
        """
            Total nodes T(node) = 1 + Total nodes in left sub tree T(left) + Total nodes in right sub tree T(right)
        """
        def count(root):
            if not root: return 0
            return 1+count(root.left)+count(root.right)
        return count(root)

    # TODO: Implement the iterative solution 
    def iterative(self, root: Optional[TreeNode]) -> int:
        pass