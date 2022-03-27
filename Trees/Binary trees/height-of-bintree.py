"""
    Find height of binary tree
    Height of a node is defined as: the length of the longest path from the node to a leaf.
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Find minimum height of a binary tree
    Desc: Given a binary tree, find its minimum depth.
    Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
    Consider a tree with only root node.
    We know heigh of left and riht subtree would be zero and the height of tree is 1.
    So the recursive equations turns out to be 1 + max(height(left), height(right)) 
"""

class FindHeightOfBinTree:
    # To solve this que we can use two approaches
    # 1. Use level order traversal
    # 2. Use recursion

    # The recursive equation is 1 + max(left subtree,right subtree)
    # Runtime: 52 ms, faster than 64.61% of Python3 online submissions for Maximum Depth of Binary Tree.
    # Memory Usage: 16.4 MB, less than 22.84% of Python3 online submissions for Maximum Depth of Binary Tree.
    def recursive(self, root) -> int:
        def count(node):
            if not node: return 0
            
            # The code works with and without the line below
            if not node.left and not node.right: return 1

            # Return the max of the left and right subtrees plus 1
            else: return 1 + max(count(node.left),count(node.right))
        return count(root)
    
    # Runtime: 55 ms, faster than 58.62% of Python3 online submissions for Maximum Depth of Binary Tree.
    # Memory Usage: 15.2 MB, less than 99.11% of Python3 online submissions for Maximum Depth of Binary Tree.
    def iterative(self, root) -> int:
        if not root: return 0
        queue = [root]
        height = 0
        while queue:
            height += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return height

from collections import deque
class MinimumDepthOfBinTree:
    
    # Solution 1:
    # Using DFS approach with recursion 
    # Traverse the binary tree normally with Pre order traversal
    # When reached the leaf, update the min value with minimum of current min and current height.
    minm = float('inf')
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
            Runtime: 788 ms, faster than 41.84% of Python3 online submissions for Minimum Depth of Binary Tree.
            Memory Usage: 54.9 MB, less than 29.65% of Python3 online submissions for Minimum Depth of Binary Tree.
        """
        if not root: return 0
        self.minm =  float('inf')
        def pot(node,h):
            if not node: return
            
            # Reached a leaf node? Update the min value with minimum of current min and current height.
            if not node.left and not node.right:
                self.minm = min(self.minm,h)
            
            # Else continue traversal
            pot(node.left,h+1)
            pot(node.right,h+1)
        pot(root,1)
        return self.minm

    
    # Solution 2:
    # DFS with recursion but pythonic
    def minDepth(self, root):
        if not root: return 0
        d = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(d) or max(d))
    
    
    # Solution 3:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        """
            Runtime: 552 ms, faster than 90.32% of Python3 online submissions for Minimum Depth of Binary Tree.
            Memory Usage: 49.5 MB, less than 67.31% of Python3 online submissions for Minimum Depth of Binary Tree.
        """

        visit_queue = deque([(root, 1)])

        while len(visit_queue) != 0:
            # BFS Traversal

            next_visit, cur_depth =visit_queue.popleft()

            if next_visit is None:
                # empty node or empty tree
                continue
            
            # Since we are traversing each element in one level,
            # As soon as a leaf is found, it has to be the minDepth
            if next_visit.left is None and next_visit.right is None:
                # reach a leaf node
                # get the minimal depth of binary tree, early return
                return cur_depth

            #append left and right child into visit_queue, increase current depth by 1
            visit_queue.append( (next_visit.left, cur_depth+1) )
            visit_queue.append( (next_visit.right, cur_depth + 1) )

        # depth 0 for empty-tree
        return 0
