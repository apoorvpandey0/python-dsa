"""
    Maximum path sum of a Binary Tree
    Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
    Best explaination: https://youtu.be/TO5zsKtc1Ic
"""

from typing import Optional

"""
    1. Path may start and end at any point but it should be continuous
    2. Path may or may not go through root
    3. Path should have at least one node
"""

"""
There are three cases to take care of:
    CASE 1: Current node is in path of max sum
    CASE 2: Current node is root of max sum path
    CASE 3: Current node is not in path of max sum
    CASE 4: Current node is itself the max path sum
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # This should be -inf else if this is set to default 0, negative sums will get skipped in max()
    max_sum = float('-inf')

    # Runtime: 100 ms, faster than 74.53% of Python3 online submissions for Binary Tree Maximum Path Sum.
    # Memory Usage: 21.4 MB, less than 40.66% of Python3 online submissions for Binary Tree Maximum Path Sum.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        We'll reach the leftmost leaf first then we'll reach the rightmost leaf.
        Then we'll check the cases and move along the path. Bottom up!
        """
        def count(node):
            if not node: return 0
            left = count(node.left)
            right = count(node.right)

            # Whether to take Left or Right subtree with root node OR current node alone
            case1 = max(  max(left, right) + node.val,   node.val  )

            # Whether current node is the root of the max sum path tree
            case2 = max(  case1, left + right + node.val  )

            # Choose max_sum from case1, case2 and current node
            self.max_sum = max(  case2, self.max_sum  )
            
            # print(left,right,case1,case2,node.val)
            return case1
        count(root)
        return self.max_sum
