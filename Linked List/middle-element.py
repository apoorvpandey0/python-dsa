"""
    Find middle element of a linked list
    Or return length//2 +1 st element
    Link: https://leetcode.com/problems/middle-of-the-linked-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1:
# Trivial solution
# Find the length and loop over to middlemost ele
# Runtime: 54 ms, faster than 14.58% of Python3 online submissions for Middle of the Linked List.
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    mid = length // 2 + 1

    curr = head
    for _ in range(mid - 1):
        curr = curr.next
    return curr


# Solution 2:
# Runtime: 49 ms, faster than 20.46% of Python3 online submissions for Middle of the Linked List.
# Tortoise and hare approach/ Fast - Slow approach
# While slow moves one step forward, fast moves two steps forward.
# Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
def mid(head):
    """
        For example, head = [1, 2, 3, 4, 5], I bolded the slow and fast in the list.
        step 0: slow: ['1', 2, 3, 4, 5], fast: [1, 2, '3', 4, 5]
        step 1: slow: [1, '2', 3, 4, 5], fast: [1, 2, 3, '4', 5]
        step 2: slow: [1, 2, '3', 4, 5], fast: [1, 2, 3, 4, '5']
        end because fast cannot move forward anymore and return [3, 4, 5]

        For example, head = [1, 2, 3, 4, 5, 6], I bolded the slow and fast in the list.
        step 0: slow: ['1', 2, 3, 4, 5, 6], fast: [1, 2, '3', 4, 5, 6]
        step 1: slow: [1, '2', 3, 4, 5, 6], fast: [1, 2, 3, '4', 5, 6]
        step 2: slow: [1, 2, '3', 4, 5, 6], fast: [1, 2, 3, 4, '5', 6]
        step 2: slow: [1, 2, 3, '4', 5, 6], fast: [1, 2, 3, 4, 5, '6']
        end because fast cannot move forward anymore and return [4, 5, 6]

    """
    # IMP: Start both from head, if you start fast from 2nd element(head.next) it will cause issues in even case
    slow = fast = head

    # Both fast and fast.next are required here
    # fast breaks the loop in odd cases
    # fast.next breaks the loop in even cases
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
