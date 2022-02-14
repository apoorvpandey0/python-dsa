"""
    Remove the middle node from a linked list
    Link: https://leetcode.com/problems/middle-of-the-linked-list/
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Solution 1:
    # Fast/slow pointer approach
    # Runtime: 2205 ms, faster than 49.69% of Python3 online submissions for Delete the Middle Node of a Linked List.
    # Memory Usage: 60.6 MB, less than 88.26% of Python3 online submissions for Delete the Middle Node of a Linked List.
    def deleteMiddle(self, head):
        # Case for [1]
        if head.next == None:
            return None

        # Make the prev pointer point to the node just before the middle node
        slow = fast = head
        prev = ListNode(-1, head)
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # remove the middle node
        prev.next = slow.next
        return head

    # Solution 2:
    # Without using prev pointer
    # Its essentially the asme as solution 1
    def soln2(head):
        # fast runner slow runner
        if not head.next:
            return head.next

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            if not fast or not fast.next:
                slow.next = slow.next.next
            else:
                slow = slow.next

        return head