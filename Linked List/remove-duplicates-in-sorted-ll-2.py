"""
    Remove duplicates from a sorted linked list.
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution:
# Time: O(n) | Space: O(1)
# Runtime: 68 ms, faster than 26.53% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14 MB, less than 80.11% of Python3 online submissions for Remove Duplicates from Sorted List II.
def deleteDuplicates(head):
    """
        Good explaination: https://youtu.be/R6-PnHODewY?t=93
        1. head is the node we'll use to iterate over the duplicates
        2. prev will contain the prev non duplicate node
        3. sentinal points to the new head of the LL
    """
    prev = ListNode(-1, head)
    sentinal = prev
    while head and head.next:
        # print(head.val, head.next.val, prev.val)

        # If duplicates start is found
        if head.val == head.next.val:

            # Loophead over all the duplicates
            while head and head.next and head.val == head.next.val:
                head = head.next

            # Assign prev.next to the next of the last duplicate ie head.next
            prev.next = head.next

            # Take head out of duplicates list
            head = head.next

        # If duplicate list is not found simply move both prev and head forward
        else:
            prev = head
            head = head.next

    # Since sentinal points to the absolute head of L return sentinal.next
    return sentinal.next