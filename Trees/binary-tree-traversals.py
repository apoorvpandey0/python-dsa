"""
    Preorder traversal of a binary tree
    Inorder traversal of a binary tree
    Postorder traversal of a binary tree
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class PreOrderTraversal:
    """
        Preorder traversal of a binary tree
        Link: https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
    """
    # Runtime: 41 ms, faster than 56.15% of Python3 online submissions for Binary Tree Preorder Traversal.
    # Memory Usage: 13.9 MB, less than 83.27% of Python3 online submissions for Binary Tree Preorder Traversal.
    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def pot(root):
            if root == None:
                return
            ans.append(root.val)
            pot(root.left)
            pot(root.right)
        pot(root)
        return ans

    # Runtime: 48 ms, faster than 39.11% of Python3 online submissions for Binary Tree Preorder Traversal.
    # Memory Usage: 13.8 MB, less than 98.24% of Python3 online submissions for Binary Tree Preorder Traversal.    
    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = [] 
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return res

class InOrderTraversal:
    # Runtime: 46 ms, faster than 43.74% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 13.8 MB, less than 83.92% of Python3 online submissions for Binary Tree Inorder Traversal.
    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def iot(root):
            if root == None:
                return
            iot(root.left)
            ans.append(root.val)        
            iot(root.right)
        iot(root)
        return ans
    
    # Runtime: 37 ms, faster than 67.18% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 13.9 MB, less than 81.18% of Python3 online submissions for Binary Tree Inorder Traversal.
    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = [] 
        curr = root
        while stack or curr!=None:
            # Go to the leftest leaf
            while curr!=None:
                stack.append(curr)
                curr = curr.left
            # When reached the leftest leaf pop the stack and add the value to the result
            curr = stack.pop()
            res.append(curr.val)

            # Go to the rightest leaf of the leftest leaf and so on
            curr = curr.right
            
        return res 

class PostOrderTraversal:
    """
        Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
    """
    # Runtime: 38 ms, faster than 62.13% of Python3 online submissions for Binary Tree Postorder Traversal.
    # Memory Usage: 13.8 MB, less than 83.42% of Python3 online submissions for Binary Tree Postorder Traversal.
    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def pot(root):
            if root == None:
                return
            pot(root.left)      
            pot(root.right)
            ans.append(root.val)  
        pot(root)
        return ans
    
    # Runtime: 29 ms, faster than 87.89% of Python3 online submissions for Binary Tree Postorder Traversal.
    # Memory Usage: 13.9 MB, less than 80.66% of Python3 online submissions for Binary Tree Postorder Traversal.
    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        s1 = [root]
        s2 = []
        res = []
        while s1:
            # print(s1,s2)
            node = s1.pop()
            if node: 
                s2.append(node.val)
                if node.left:s1.append(node.left)
                if node.right:s1.append(node.right)
        
        while s2:
            res.append(s2.pop())
        return res