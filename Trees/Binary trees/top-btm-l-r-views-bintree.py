"""
    
"""

# My top view approach could not work because of this tree
# [2, 1 ,10 ,null, null, 3, null, null ,6 ,4 ,9 ,null ,5]

from typing import Optional, List
# Tree Node GFG
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

from collections import defaultdict
class TopViewofBinaryTree:
    """
        Link: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#
    """
    def vot(self, root):
        ds = defaultdict(lambda: defaultdict(list))
        res = []
        # print(ds['hi'])
        # print(ds['hi']['hi'])
        def pot(node,row,col):
            if not node: return
            ds[col][row].append(node.data)
            # print(node.val,col,row,ds[col][row])
            pot(node.left,row+1,col-1)
            pot(node.right,row+1,col+1)
        pot(root,0,0)
        
        for key1,value1 in sorted(ds.items()):
            tmp = []
            for key2,value2 in sorted(value1.items()):
                tmp.extend(sorted(value2))
            res.append(tmp)
        return res
    
    def topView(self,root):
        """
            Top view consists of the nodes that would be visible if the bintree is viewed from the top.
            Ex: 
                      1
                    /     \
                    2      3
                  /  \    /  \
                 N    5   N   N
                     /  \
                    6    N     
                   /  \
                 7     N
            Top view will be: [7,2,1,3]
        
        """

        # We can simply find the Vrtical order traversal of the tree and 
        # The first node in each column L->R will be in the top view
        res = []
        for col in self.vot(root):
            res.append(col[0])
        return res

from collections import defaultdict
class BottomViewofBinaryTree:
    """
        Link: https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
    """
    def vot(self, root):
        ds = defaultdict(lambda: defaultdict(list))
        res = []
        def pot(node,row,col):
            if not node: return
            ds[col][row].append(node.data)
            pot(node.left,row+1,col-1)
            pot(node.right,row+1,col+1)
        pot(root,0,0)
        
        for key1,value1 in sorted(ds.items()):
            tmp = []
            for key2,value2 in sorted(value1.items()):
                # We have removed sorting from here because we need the right most node in case of same row,col nodes
                tmp.extend(value2)
            res.append(tmp)
        return res
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def bottomView(self,root):
        """
            IMP CASE:
            In case of conflicting nodes (Nodes at same row,col values):
                We need totake the right most node
                In contrast to normal Vertical order traversal where we sort the conflicting nodes
            Ex: 
                       1
                     /   \
                    2    3
                  /  \  /  \
                 4   [5,6]   7
                     /  \
                    8    9                      
            Bottom view will be: [4,8,6,9,7]
        """
        res = []
        for col in self.vot(root):
            # Also we need to take the last element of each column for bottom view
            res.append(col[-1])
        return res

# Tree node Leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class RightViewofBinaryTree:
    """
        Link: https://leetcode.com/problems/binary-tree-right-side-view/
    """
    def lot(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if not curr: continue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)         
            if level: result.append(level)
        return result

    # Runtime: 48 ms, faster than 48.88% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 13.8 MB, less than 98.53% of Python3 online submissions for Binary Tree Right Side View.   
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            Given a binary tree, imagine yourself standing on the right side of it,
            Right view is simply last elements from each row of level order traversal
        """
        res = []
        for row in self.lot(root):
            res.append(row[-1])
        return res

from collections import deque
class LeftViewofBinaryTree:      
    """
        Link: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
    """     
    def lot(self,root):
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if not curr: continue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.data)         
            if level: result.append(level)
        return result


    def LeftView(self,root):
        """
            Given a binary tree, imagine yourself standing on the left side of it,
            Left view is simply first elements from each row of level order traversal
        """
        res = []
        for row in self.lot(root):

            # Take the first element of each row
            res.append(row[0])
        return res
        
