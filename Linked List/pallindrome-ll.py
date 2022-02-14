"""
    pallindrome LL
    Link: https://leetcode.com/problems/palindrome-linked-list/
"""
from collections import deque


# Runtime: 1287 ms, faster than 21.81% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 47.3 MB, less than 29.41% of Python3 online submissions for Palindrome Linked List.
def isPalindrome(head):
    N = 0

    # Finding length of LL
    tmp = head
    while tmp:
        N += 1
        tmp = tmp.next

    # Adding half items to stack
    stack = deque()
    for _ in range(N // 2):
        stack.append(head.val)
        head = head.next

    # If odd length LL -> Add middle element to stack, but dont move head to next!
    if N % 2:
        stack.append(head.val)

    # Compare stack and remaining LL
    while head:
        if stack.pop() != head.val:
            return False
        head = head.next
    return True