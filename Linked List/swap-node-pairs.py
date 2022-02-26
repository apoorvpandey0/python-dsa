"""
    Swap nodes pairs
    Link: https://leetcode.com/problems/swap-nodes-in-pairs/
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solution 1
# What i came up with
# Runtime: 21 ms, faster than 98.94% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 44.39% of Python3 online submissions for Swap Nodes in Pairs.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        sentinal = ListNode(-1,head)
        curr = head.next
        prev = head
        last = sentinal
        while curr and curr:
            nxt = curr.next
            curr.next = prev
            prev.next = nxt
            last.next = curr
            if nxt == None:
                break
            last = prev
            prev = nxt
            if nxt:
                curr = nxt.next
        return sentinal.next

# Solution 2:
# Same logic but cleaner code
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
        return dummy.next