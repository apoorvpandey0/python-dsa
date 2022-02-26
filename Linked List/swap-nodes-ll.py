"""
    Swap nodes in LL
    Swap the values of the kth nodes from beginning and end
    Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 1393 ms, faster than 51.02% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.4 MB, less than 91.31% of Python3 online submissions for Swapping Nodes in a Linked List.
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = 0
        
        # Finding length
        tmp = head
        while tmp:
            N+=1
            tmp = tmp.next
        A,B = ListNode(),ListNode()
        
        # Finding nodes whose values are to be swapped
        index = 0
        tmp = head
        while tmp:
            if index == k-1:
                A = tmp
            if index == N-k:
                B = tmp
            tmp = tmp.next
            index+=1
        
        # Actual swapping
        A.val,B.val = B.val,A.val
        return head
            