"""
    Insertion Sort List
    Link: https://leetcode.com/problems/insertion-sort-list/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1:
# Swapping method
# Time: O(n^2) | Space: O(1)
# TLE on leetcode
def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """ 
        Example iterations for print(head) after nested loop completes:
        [4, 3, 1, 2]
        [3, 4, 1, 2]
        [1, 3, 4, 2]
        [1, 2, 3, 4]
    """
    curr = head
    while curr:
        tmp = head
        while tmp != curr:
            # This loop will swap and place all values in order
            # Try dry running this for above ex. for better understanding
            if tmp.val > curr.val:
                tmp.val, curr.val = curr.val, tmp.val
            tmp = tmp.next

        # Print List after each new insertion
        # print(head)
        curr = curr.next
    return head


# Solution 2:
# Actual node insertion method
# Time: O(n^2) | Space: O(1)
# Runtime: 175 ms, faster than 87.37% of Python3 online submissions for Insertion Sort List.
# Link: https://leetcode.com/problems/insertion-sort-list/discuss/1176552/Python3-188ms-Solution-(explanation-with-visualization)
def insertionSort(head):
    # Use dummy_head will help us to handle insertion before head easily
    dummy_head = ListNode(val=-5000, next=head)
    last_sorted = head  # last node of the sorted part
    cur = head.next  # cur is always the next node of last_sorted
    while cur:
        if cur.val >= last_sorted.val:
            last_sorted = last_sorted.next
        else:
            # Search for the position to insert
            prev = dummy_head
            while prev.next.val <= cur.val:
                prev = prev.next

            # Insert
            last_sorted.next = cur.next
            cur.next = prev.next
            prev.next = cur

        cur = last_sorted.next

    return dummy_head.next