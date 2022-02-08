"""
    Reverse nodes in k groups
    Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
    My post: https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/1755722/python3-clean-code-commented-and-explained
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rev(head, left, right):
    # Ths is the solution from reverse a linked list 2
    if not head or not head.next or left == right:
        return head

    dummy_head = ListNode(-1, head)
    prev = dummy_head
    curr = head
    for _ in range(1, left):
        prev = curr
        curr = curr.next

    for _ in range(right - left):
        next = curr.next
        curr.next = next.next
        next.next = prev.next
        prev.next = next
    return dummy_head.next


# Runtime: 62 ms, faster than 52.29% of Python3 online submissions for Reverse Nodes in k-Group.
def reverseKGroup(self, head: Optional[ListNode],
                  k: int) -> Optional[ListNode]:

    # Find length of linked list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Generate left,right values for reversing the List using k and bounded by length
    left = 1
    right = k
    while right <= length:
        head = rev(head, left, right)
        left += k
        right += k
    return head
