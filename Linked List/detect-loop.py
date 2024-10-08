"""
    Detect loop in a linked list
    Link: https://leetcode.com/problems/linked-list-cycle/
"""

from typing import *


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Solution 1
    # Simply put elements in set approach
    # O(n) time and O(n) space.
    # Runtime: 78 ms, faster than 41.53% of Python3 online submissions for Linked List Cycle.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
            curr = curr.next
        else:
            return False

    # Solution 2:
    # Tortoise and hare algorithm
    # Fast will eventually catch up with slow if in a loop
    # Else fast would be none at some point throwing an error
    # O(n) time and O(1) space.
    # Runtime: 80 ms, faster than 39% of Python3 online submissions for Linked List Cycle.
    # The reason why fast will catch up in N steps: https://youtu.be/gBTe7lFR3vc?t=357
    def hasCycle2(self, head):
        """
            The "trick" is to not check all the time whether we have reached the end but to handle it via an exception.
            "Easier to ask for forgiveness than permission."
            Try it for 1->2->3->4->2
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False