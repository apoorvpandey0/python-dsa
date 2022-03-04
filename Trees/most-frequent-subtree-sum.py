"""
    Find the most frequent subtree sum
    Desc: If there are multiple subtree sums that occur the same number of times,
    return all the subtree sums
    Link: https://leetcode.com/problems/most-frequent-subtree-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:

    # Runtime: 44 ms, faster than 97.86% of Python3 online submissions for Most Frequent Subtree Sum.
    # Memory Usage: 17.3 MB, less than 77.31% of Python3 online submissions for Most Frequent Subtree Sum.
    def findFrequentTreeSum(self, root):        
        fq = defaultdict(int)
        def count(node):
            if not node: return 0
            sm =  count(node.left) + count(node.right) + node.val
            fq[sm]+=1
            return sm
        count(root)
        
        mx = max(fq.values())
        return [k for k, v in fq.items() if v == mx]