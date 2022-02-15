# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1:
    # Create a new list approach
    # Time Complexity: O(n) | Space: O(n)
    # Runtime: 59 ms, faster than 33.42% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 14 MB, less than 81.73% of Python3 online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, h1, h2):
        # To keepp track of current node in new list
        curr = ListNode(-1)

        # Head of new list
        new = ListNode(-1, curr)

        # Until any one list reaches its end
        while h1 and h2:
            # Create new nodes and add them to curr.next
            if h1.val < h2.val:
                curr.next = ListNode(h1.val, h1.next)
                curr = curr.next
                h1 = h1.next
            else:
                curr.next = ListNode(h2.val, h2.next)
                curr = curr.next
                h2 = h2.next

        # Handling the uneven length cases
        if h1 == None:
            curr.next = h2
        if h2 == None:
            curr.next = h1

        # New list will always contain two dummy elements
        return new.next.next

    # Solution 2:
    # Recursive approach - Algorithm:
    # Make sure a is always the smaller list
    # If not swap the pointers
    # Time Complexity: O(n) | Space: O(1)
    def soln2(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.soln2(a.next, b)
        return a or b

    # Explaination for return statement
    # The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
    # The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
