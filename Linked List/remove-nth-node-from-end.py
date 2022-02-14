"""
    Remove nth node from end LL
    Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1:
    # Two pass algorithm
    # Find length
    # Find and remove nth node from end
    # Runtime: 56 ms, faster than 26.29% of Python3 online submissions for Remove Nth Node From End of List.
    # Memory Usage: 14 MB, less than 67.01% of Python3 online submissions for Remove Nth Node From End of List.
    def removeNthFromEnd(self, head, k):
        N = 0

        # Finding length
        tmp = head
        while tmp:
            tmp = tmp.next
            N += 1

        # Finding the node just before the actual node to be removed
        sentinal = ListNode(-1, head)
        prev = sentinal
        tmp = head
        for _ in range(N - k):
            prev = tmp
            tmp = tmp.next

        # remove the nth node
        prev.next = tmp.next
        return sentinal.next

    # Few more solutions:
    # 1. Recursion and fast/slow
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164537/Short-and-Simple-One-Pass-Solution-w-Explanation-or-Beats-100-or-No-dummy-node-required!

    # Solution 2:
    # One pass(Kindof) - fast/slow
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head

        # Iterate fast over first k nodes
        for i in range(k):
            fast = fast.next

        # If fast is already null => we have to delete head node itself => return head.next
        if not fast: return head.next

        # Iterate fast and slow until fast reaches the end
        # ie. slow will reach the node just before kth node from end
        while fast.next:
            fast, slow = fast.next, slow.next

        # remove the kth node
        slow.next = slow.next.next
        return head