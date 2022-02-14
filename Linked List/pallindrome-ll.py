"""
    pallindrome LL
    Link: https://leetcode.com/problems/palindrome-linked-list/
"""
from collections import deque


# Solution 1
# Time: O(n) | Space: O(n)
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


# Some other good solutions 0(1) space
# 1. Find the middle element and reverse the LL then compare the two parts of LL for pallindrome
# https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
# 2. Similar but cleaner code
# https://leetcode.com/problems/palindrome-linked-list/discuss/1695170/Python-Very-Easy-Approach