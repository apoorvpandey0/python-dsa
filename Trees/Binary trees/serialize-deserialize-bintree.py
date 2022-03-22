"""
    Serialize or deserialize a binary tree.
    Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
        Runtime: 128 ms, faster than 88.12% of Python3 online submissions for Serialize and Deserialize Binary Tree.
        Memory Usage: 20.5 MB, less than 21.32% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    """
     
    res = ''

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def trav(node):
            if not node: 
                self.res+='*,'
                return 
            # print(node.val,self.res)
            self.res+=str(node.val)+','
            trav(node.left)
            trav(node.right)
        trav(root)
        # print(self.res)
        return self.res[:-1]
            
        

    def deserialize(self, data) ->TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = deque(data.split(','))
        # print(q)
        def build():
            elem = q.popleft()
            if not q or elem=='*':return None
            root = TreeNode(elem)
            root.left = build()
            root.right = build()
            return root
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))