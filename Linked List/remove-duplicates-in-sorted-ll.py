"""
    Remove duplicates from a sorted linked list.
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


# Move next to next.next if duplicate
# Time: O(n) | Space: O(1)
# Runtime: 59 ms, faster than 45.37% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 81.46% of Python3 online submissions for Remove Duplicates from Sorted List.
def clean(head):
    tmp = head
    while tmp and tmp.next:
        if tmp.val == tmp.next.val:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    return head