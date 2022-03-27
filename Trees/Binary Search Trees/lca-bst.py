"""
    Find lowest common ancestor in a binary search tree
    Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    Video: https://youtu.be/gs2LMfuOR9k
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Runtime: 114 ms, faster than 47.31% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    # Memory Usage: 18.9 MB, less than 22.92% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
            More explaination can be added!
            Given that p is not necessarily smaller than q:
            1. If a node is in between p and q OR q and p then the node is the LCA

        """
        
        def lca(node):
            if not node: return
            
            if p.val<=node.val<=q.val or q.val<=node.val<=p.val: return node
            
            elif node.val<q.val or node.val<p.val: return lca(node.right)
            
            else: return lca(node.left)
        
        return lca(root)