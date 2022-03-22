"""
    Construct binary trees from:
    1. Preorder traversal and inorder traversal
    2. Postorder traversal and inorder traversal

    NOTE: Inorder to construct a binary tree, we always need at leas one of the given traversals to be INORDER.
"""
from typing import List,Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PreorderInorder:
    
    # Runtime: 227 ms, faster than 42.17% of Python3 online submissions.
    # Memory Usage: 88.5 MB, less than 36.46% of Python3 online submissions.
    def soln1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder,inorder):
            if not preorder or not inorder: return
            # Build a root node, preorder[0] will always contain some root node as preorder = Root L R
            root = TreeNode(preorder[0])

            # Find the index of the root node in the inorder
            mid = inorder.index(preorder[0])

            # Build the left subtree
            # In inorder everything upto mid (not including) is the left subtree
            # In preorder everything upto mid (including) is the left subtree
            root.left = build(preorder[1:mid+1],inorder[:mid])

            # Build the right subtree
            # In inorder everything from mid+1 (including) to end is the right subtree
            # In preorder everything from mid+1 (including) to end is the right subtree
            root.right = build(preorder[mid+1:],inorder[mid+1:])

            # Now left and right subtrees will get recursively built out
            # And root will have links to all of the nodes in the left and right subtrees
            return root
        
        return build(preorder,inorder)
    
    # This is more efficient than the above solution.
    # Runtime: 73 ms, faster than 86.43% of Python3 online submissions.
    # Memory Usage: 18.9 MB, less than 73.17% of Python3 online submissions.
    def soln2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        inorder_map = {v:k for k,v in enumerate(inorder)}
        def construct(left, right):
            # Base case
            if left > right: return None

            # Find the root value first based on the preorder's property
            # Create the root with the value
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # Find the index of the root value and to split the inorder
            index = inorder_map[root_val]


            root.left = construct(left, index - 1)
            root.right = construct(index + 1, right)
            return root
        return construct(0, len(inorder)-1)
            
class PostorderInorder:
    # Runtime: 205 ms, faster than 40.09% submissions,
    # Memory Usage: 88.8 MB, less than 19.55% submissions,
    def soln1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(postorder,inorder):
            if not postorder or not inorder: return
            ele = postorder.pop()
            root = TreeNode(ele)
            mid = inorder.index(ele)
            root.left = build(postorder[:mid],inorder[:mid])
            root.right = build(postorder[mid:],inorder[mid+1:])
            return root
        
        return build(postorder,inorder)