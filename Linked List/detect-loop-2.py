"""
    Return node which is at cycle start
    Link: https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Solution 1:
    # Simply put elements in set approach
    # O(n) time and O(n) space.
    # Runtime: 69 ms, faster than 51.04% of Python3 online submissions for Linked List Cycle II.
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            else:
                visited.add(curr)
            curr = curr.next
        else:
            return None

    # Solution 2:
    # Tortoise and hare algorithm
    # O(n) time and O(1) space.
    # Runtime: 49 ms, faster than 83.84% of Python3 online submissions for Linked List Cycle II.
    def detect(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # print(slow.val,fast.val)
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None