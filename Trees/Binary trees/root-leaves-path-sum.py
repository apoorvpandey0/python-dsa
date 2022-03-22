"""
    Path Sum 1
    Desc: Given a binary tree and a sum, find if path with sum exists in the tree.
    Link: https://leetcode.com/problems/path-sum/

    Path sum 2
    Desc: Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    Link: https://leetcode.com/problems/path-sum-ii/
"""
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PathSum1:
    # Runtime: 52 ms, faster than 69.25% of Python3 online submissions for Path Sum.
    # Memory Usage: 15.1 MB, less than 65.25% of Python3 online submissions for Path Sum.
    ps = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        def pot(node):
            if not node: return

            # Add the current node to the path
            path.append(node.val)
            self.ps+=node.val

            # Traverse normally
            l = pot(node.left)
            r = pot(node.right)

            # If curr node is a leaf and the path sum equals targetSum, add the path to result
            if not node.left and not node.right and self.ps == targetSum:
                return True
            
            # Since we'll go back one level in recursion stack, we need to pop the last element from path
            path.pop()
            self.ps-=node.val
            return l or r
        
        return pot(root)
class PathSum2:

    # Runtime: 48 ms, faster than 85.68% of Python3 online submissions for Path Sum II.
    # Memory Usage: 15.6 MB, less than 57.11% of Python3 online submissions for Path Sum II.
    
    # ps represents the path sum at each step
    ps = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        def pot(node):
            if not node: return

            # Add the current node to the path
            path.append(node.val)
            self.ps+=node.val

            # Traverse normally
            pot(node.left)
            pot(node.right)

            # If curr node is a leaf and the path sum equals targetSum, add the path to result
            if not node.left and not node.right and self.ps == targetSum:
                res.append(path.copy())
            
            # Since we'll go back one level in recursion stack, we need to pop the last element from path
            path.pop()
            self.ps-=node.val
        
        pot(root)
        return res