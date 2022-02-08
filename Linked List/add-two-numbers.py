# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1:
# Time: O(n) - Single pass solution
# Runtime: 78 ms, faster than 58.04% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 82.52% of Python3 online submissions for Add Two Numbers.
def addTwoNumbers(self, i: Optional[ListNode], j: Optional[ListNode]):
    head = None
    prev = None
    curr = None
    carry = 0
    while i or j or carry:
        a, b, sumab = 0, 0, 0
        if i:
            a = i.val
            i = i.next
        if j:
            b = j.val
            j = j.next

        sumab = a + b + carry
        onesPlaceDigit = sumab % 10
        carry = sumab // 10
        if head == None:
            head = ListNode(onesPlaceDigit)
            prev = head
        else:
            curr = ListNode(onesPlaceDigit)
            prev.next = curr
            prev = curr

    return head


# Solution 2:
# Solution that could sum arbitrarily many addends, not just two:
def add2(l1, l2):
    """
    https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
    """
    addends = l1, l2
    dummy = end = ListNode(0)
    carry = 0
    while addends or carry:
        carry += sum(a.val for a in addends)
        addends = [a.next for a in addends if a.next]
        end.next = end = ListNode(carry % 10)
        carry /= 10
    return dummy.next