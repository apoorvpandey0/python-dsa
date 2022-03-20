"""
    Max width of a binary tree
    Desc: The width of a tree is the maximum width among all levels. 
            The binary tree has the same structure as a full binary tree, but some nodes are null.
    Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        These solutions are based on indexing of tree nodes.
        We can index the tree with 0 or 1.
        Ex 0 based indexing: 
                root
               /    \
              left   right

        Here if root has index 0, then left and right will have index 1 and 2 respectively.
        Or if root has index i, then left and right will have index 2i+1 and 2i+2 respectively.
        
        Ex 1 based indexing: 
                root
               /    \
              left   right

        Here if root has index 1, then left and right will have index 2 and 3 respectively.
        Or if root has index i, then left and right will have index 2i and 2i+1 respectively.

        Once we have properly indexed the tree nodes then the width of the tree is:
            The difference between the rightmost and leftmost node index + 1
        
        And we can find the max using this formula for each level run:
            max = max(leftmost-rightmost+1,ans)
        
    """
    
    # Soln1 and soln2 are similar but with different approaches
    # Runtime: 84 ms, faster than 18% of Python3 online submissions for Maximum Width of Binary Tree.
    # Memory Usage: 14.7 MB, less than 79% of Python3 online submissions for Maximum Width of Binary Tree.    
    def soln1(self, root: Optional[TreeNode]) -> int:
        """

        """
        # Queue will have each level in it for each while iteration
        # This will contain (Treenode,Index) values
        q = deque()
        q.append((root,0))
        ans = float('-inf')

        while q:
            # Width of current lvl is the difference between the rightmost and leftmost node index +1
            leftmost,rightmost = q[-1][1],q[0][1]
            ans = max(leftmost-rightmost+1,ans)

            # Remove current lvl elements and add next level elements in the queue
            for _ in range(len(q)):
                curr,idx = q.popleft()
                if curr.left:
                    q.append((curr.left,2*idx+1))
                if curr.right:
                    q.append((curr.right,2*idx+2))
        return ans
    
    # Runtime: 48 ms, faster than 85.57% of Python3 online submissions for Maximum Width of Binary Tree.
    # Memory Usage: 15.7 MB, less than 25.74% of Python3 online submissions for Maximum Width of Binary Tree.             
    def soln2(self, root: Optional[TreeNode]) -> int:
        """
            This is more time efficient soln, But, I have to take a look at it again.
        """
        map = {}
        q = deque([(root,1,1)])
        maxc = 0

        while len(q) :
            out, c, lvl = q.popleft()
            if lvl not in map : map[lvl] = [c,0]
            mmc = map[lvl]

            if mmc[0] > c : mmc[0] = c 
            if mmc[1] < c : mmc[1] = c
            maxc = max(maxc, abs(mmc[1]-mmc[0])+1 )

            if out.left : q.append((out.left, 2*c, lvl+1))
            if out.right : q.append((out.right, 2*c +1, lvl+1))
        return maxc