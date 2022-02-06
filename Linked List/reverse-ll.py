"""
    How to reverse a Linked List
    Link: https://leetcode.com/problems/reverse-linked-list/
    Solution: https://leetcode.com/problems/reverse-linked-list/discuss/1449712/Easy-C%2B%2BJavaPythonJavaScript-Explained%2BAnimated
"""


# Time: O(n) | Space: O(1)
# Runtime: 40 ms, faster than 64.26% of Python3 online submissions for Reverse Linked List.
def reverse(head):
    # 1 -> 2 -> 3 -> None
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
