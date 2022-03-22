"""
    N ary tree traversals
    Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
    Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class PreOrder:

    # Time: O(n) | Space: O(n)
    # Runtime: 68 ms, faster than 79.62% of Python3 online submissions for Palindrome Number.
    # Memory Usage: 14 MB, less than 43.14% of Python3 online submissions for Palindrome Number.
    def iterative(self, root: Node) -> List[int]:
        stack = [root]
        res = []
        while stack:
            # print(stack)
            curr = stack.pop()
            # print(curr.val)
            if curr:
                res.append(curr.val)
                stack.extend(reversed(curr.children))
        return res
    # TODO: Implement the recursive solution 