"""
    Find all the paths leading to leaves in a binary tree.
    Link: https://leetcode.com/problems/binary-tree-paths/submissions/
"""
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def converter(self,lst):
            """
                Converts [1,2,3] to "1->2->3"
            """
            if len(lst)==0: return ''
            if len(lst)==1: return str(lst[0])
            tmp = str(lst[0])
            for ele in lst[1:]:
                tmp+='->'+str(ele)
            return tmp
        
    # Runtime: 24 ms, faster than 99.48% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 14 MB, less than 43.83% of Python3 online submissions for Binary Tree Paths.
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        def pot(node):
            if not node: return

            # Add the current node to the path
            path.append(node.val)

            # Traverse normally
            pot(node.left)
            pot(node.right)

            # If curr node is a leaf, add the path to result
            if not node.left and not node.right:
                res.append(path.copy())
            
            # Since we'll go back one level in recursion stack, we need to pop the last element from path
            path.pop()
        
        pot(root)
        for index,ele in enumerate(res):
            res[index] = self.converter(ele)
            
        return res