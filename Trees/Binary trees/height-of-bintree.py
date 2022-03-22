"""
    Find height of binary tree
    Height of a node is defined as: the length of the longest path from the node to a leaf.
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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