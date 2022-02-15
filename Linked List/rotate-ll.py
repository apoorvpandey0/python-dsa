"""
    Rotate a LL k times
    https://leetcode.com/problems/rotate-list/
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 37 ms, faster than 77.45% of Python3 online submissions for Rotate List.
    # Memory Usage: 14 MB, less than 67.25% of Python3 online submissions for Rotate List
    def rotateRight(head, k):

        # Handling base cases when len == 0 or 1

        N = 0

        # Finding length of the list
        tmp = head
        while tmp:
            N += 1
            tmp = tmp.next

        # Normalizing k
        k = k % N

        # i.e. no ratation required
        if k == 0:
            return head

        # Finding the new head
        left = right = head

        # Move right k positions
        for _ in range(k):
            right = right.next

        # Move both N-k-1 positions
        for _ in range(N - k - 1):
            left = left.next
            right = right.next
        # print(left.val,right.val)

        # Now left points to the new head and right to the last element
        # Make adjustments accordingly
        newHead = left.next
        right.next = head
        left.next = None
        return newHead
