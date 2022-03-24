"""
     Search in s Binary Search Tree 
     Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

     Insert into BST
     Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
     V good blog: https://iq.opengenus.org/time-and-space-complexity-of-binary-search-tree/ 
"""
from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Space time table:

OPERATION	    WORST CASE	AVERAGE CASE	BEST CASE	SPACE
Search	        O(N)        O(logN)	        O(1)        O(N)
Insert	        O(N)        O(logN)	        O(1)        O(N)
Delete	        O(N)        O(logN)	        O(N)        O(N)
"""

class SearchBST:
    # Time: O(log(n)) | Space: O(n)
    def recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        """
            Runtime: 80 ms, faster than 85.07% submissions.
            Memory Usage: 16.3 MB, less than 84.34% submissions.
        """
        def search(node,target):
            if not node: return
            if node.val == target: return node
            if target>node.val: 
                t = search(node.right,target)
            if target<node.val: 
                t = search(node.left,target)            
            return t
        return search(root,val)

class InsertBST:
    # Runtime: 181 ms, faster than 53.12% submissions.
    # Memory Usage: 17 MB, less than 10.70% submissions.
    def recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
            There can be multiple correct ways to insert the node, all are accepted as long as output is a BST.
            We always insert at leaf nodes in this approach.
            Ex: 
                      2
                    /   \
                   1     3
                          \
                           6
            We insert 4 using this approach, we get:
                      2
                    /   \
                   1     3
                          \
                           6
                          /                            
                         4
        """
        if not root: return TreeNode(val)
        def insert(node,val):
            if not node: return
            
            if node.val<val: 
                if not node.right:
                    node.right = TreeNode(val)
                    return
                insert(node.right,val)

            if node.val>val: 
                if not node.left:
                    node.left = TreeNode(val)
                    return
                insert(node.left,val)
        insert(root,val)
        return root
    
class DeleteBST:
    """
        Best explaination: https://youtu.be/a-53QSxovUA
        Runtime: 110 ms, faster than 45.52% of Python3 online submissions for Delete Node in a BST.
        Memory Usage: 18.4 MB, less than 34.97% of Python3 online submissions for Delete Node in a BST
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Three possible situations for the key node
        # 1. no children
        # 2. only has one child
        # 3. has both left and right child
            
        if not root:
            return None
        
        if root.val == key:
            # Two if conditions cover both case 1 and 2
            if not root.left:
                # If left child is None assign right child to previous node
                return root.right

            if not root.right:
                # If right child is None assign left child to previous node
                return root.left
            
            # Case 3: get the minimum node in right child tree
            minNode = self.getMin(root.right)
            
            # delete the minimum node in the right child tree 
            # and update the root right child to
            # Min node is sure to be a leaf node
            root.right = self.deleteNode(root.right, minNode.val)
            
            # Replace the root node by the minNode
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # For "change": the func. need to return TreeNode.
        return root
    
    def getMin(self, root):
        # The minimum node in a BST is the most left leaf
        while root.left:
            root = root.left
        return root