"""
    Preorder traversal of a binary tree
    Inorder traversal of a binary tree
    Postorder traversal of a binary tree
"""

from typing import List, Optional
from collections import deque,defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Traversals of a binary tree
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
                # The order of appending child is R,L because stack follows LIFO
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
    
    # Using 2 Stack
    # Runtime: 29 ms, faster than 87.89% of Python3 online submissions for Binary Tree Postorder Traversal.
    # Memory Usage: 13.9 MB, less than 80.66% of Python3 online submissions for Binary Tree Postorder Traversal.
    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
            1. Push the root node to the stack
            2. While the stack is not empty
                1. Pop the top node from the stack
                2. Push the node to the stack
                3. Push the left child of the popped node to the stack
                4. Push the right child of the popped node to the stack
            Stack 2 will contain the post order traversal
        """
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
    
    # Using 1 Stacks
    def iterative2(self, root: TreeNode) -> List[int]:
        ans, s = [], []
        
        curr = root
        while curr or s:
            while curr:
                s.append((curr, curr.right))
                curr = curr.left
            
            p = s.pop()
            
            # right child is none for popped node - it means we have either
            # explored right subtree or it never existed. In both cases,
            # we can simply visit popped node i.e. add its val to ans list
            if not p[1]:
                ans.append(p[0].val)
            else:
                # Add popped node back in stack with its right child as None.
                # None right child denotes that when we pop this node in future,
                # we already explored its right subtree as we are going to do
                # that by setting curr to right child in the next step.
                s.append((p[0], None))
                
                # Explore right subtree
                curr = p[1]
        return ans

    # Pythonic solution
    def iterative3(self, root: TreeNode) -> List[int]:
        stack, result = [None, root], []

        while cur := stack.pop():
            result.append(cur.val)
            stack.extend(x for x in (cur.left, cur.right) if x)

        return result[::-1]

class AllThreeTraversals:
    # It works!
    # Based on number of counts each node is visited concept
    def allinOneTraversals(self, root: TreeNode) -> List[List[int]]:
        ans = []
        count = defaultdict(int)
        pre = []
        ino = []
        pos = []
        def pot(root):
            if root == None:
                return
            count[root]+=1
            if count[root]==1: pre.append(root.val)
            ans.append(root.val)
            
            pot(root.left)
            count[root]+=1
            if count[root]==2: ino.append(root.val)
                
            pot(root.right)
            count[root]+=1
            if count[root]==3: pos.append(root.val)
        pot(root)
        # print(count.values())
        return ino

class LevelOrderTraversal:
    # Time: O(n) | Space: O(n)
    # Runtime: 59 ms, faster than 29.68% of Python3 online submissions for Binary Tree Level Order Traversal.
    # Memory Usage: 14.3 MB, less than 44.12% of Python3 online submissions for Binary Tree Level Order Traversal.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
        """
        queue = deque()
        queue.append(root)
        result = []

        # This loop iterates over each level of the tree
        # The queue on each iteration of while loop contains all elements of one level
        while queue:
            level = []
            
            # Algorithm:
            # Iterate the entire level L -> R
            # Add the next level elements in the queue 
            # And add the current level elements to level list            
            for _ in range(len(queue)):
                # Explaination len(queue): 
                """
                    Length of the queue denotes number of elements in the current level
                    n = 3
                    for i in range(n):
                        print(i)
                        n+=1
                    The output of this code is 0,1,2 and not an infinite loop
                """
                
                curr = queue.popleft()
                
                if not curr: continue
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
                level.append(curr.val)         
            
            # To avoid the single case when the tree is empty we use if
            # else always at least one element would be there in a level
            if level: result.append(level)
        return result