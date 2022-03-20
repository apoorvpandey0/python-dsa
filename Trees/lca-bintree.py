"""
    Lowest common ancestor of a binary tree
    Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    Video: https://www.youtube.com/watch?v=KobQcxdaZKY
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Runtime: 143 ms, faster than 14.70% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    # Memory Usage: 26 MB, less than 79.49% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Ex:               5    
                         / \
                        2   6
                       / \   \
                      3   4   7
        Here: LCA(2,3) = 2
              LCA(3,7) = 5

        In case of 2,3 we dont even need to check the subtrees below 2 if 3 is in them as LCS will already be 2
        """
        def pot(root):
            if  root == None or root.val == p.val or root.val == q.val:
                # We return node when we find p or q is because if q is below p LCA wll be p
                # print('Return',root.val if root else '')
                return root

            # print(root.val)
            l = pot(root.left)
            r = pot(root.right)

            # If both l and r are not None, then current node is LCA
            if l and r:
                return root
            
            # Else if any one of them is none then return the other one that may be LCA
            else:
                return l or r
        return pot(root)