"""

"""


from typing import List, Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Algorithm
    # Find a the root (mid) node 
    # Create a new node with the value of the mid node
    # Recursively call the left and right sub-trees
    # Time: O(n) | Space: O(log(n))
    # Runtime: 113 ms, faster than 62.16% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    # Memory Usage: 15.6 MB, less than 87.87% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(l,r):
            if l>r: return None
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = create(l,m-1)
            node.right = create(m+1,r)
            return node
        return create(0,len(nums)-1)
            