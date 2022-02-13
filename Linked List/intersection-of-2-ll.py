"""
    Find the intersection point of two Linked lists
    Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Solution 1:
    # Brute forced
    # Time: O(n^2) | Space: O(1)
    # Algorithm:
    #     For each pointer in list 1

    #         Check if the pointer exists in the list two
    #         For the first value which satisfies this will be intersection point

    #         else no intersection

    # Solution 2:
    # Algorithm:
    # 1. Add one of the list to set
    # 2. iterate over second list
    # 3. The point when the element of 2nd ll is in set
    # 4. This is the point of intersection
    # Time: O(n) | Space: O(n)
    # Runtime: 201 ms, faster than 52.19% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 30.1 MB, less than 7.77% of Python3 online submissions for Intersection of Two Linked Lists.
    def getIntersectionNode(self, h1: ListNode,
                            h2: ListNode) -> Optional[ListNode]:

        # Add one of the List to set
        s = set()
        tmp = h1
        while tmp:
            s.add(tmp)
            tmp = tmp.next

        # Loop over second one to find the intersexction point
        tmp = h2
        while tmp:
            if tmp in s:
                return tmp
            tmp = tmp.next
        else:
            return None

    # Solution 3:
    # Step by step making d = 0
    # Time: O(n) | Space: O(1)
    # Runtime: 299 ms, faster than 8.58% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 29.3 MB, less than 95.76% of Python3 online submissions for Intersection of Two Linked Lists.
    def getIn3(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:

        # Finding Lengths of Linked lists
        m, n = 0, 0
        tmp = h1
        while tmp:
            m += 1
            tmp = tmp.next
        tmp = h2
        while tmp:
            n += 1
            tmp = tmp.next

        # Identifying bigger an smaller lists
        d = m - n
        if d > 0:
            bigger = h1
            smaller = h2
        else:
            bigger = h2
            smaller = h1
        tmp = bigger
        d = abs(d)

        # Iterating over bigger list to make difference = 0
        while d:
            tmp = tmp.next
            d -= 1
        bigger = tmp
        # print(bigger)
        # print(smaller)

        # Now as the difference in lengths is 0 we can iterate over both lists together and find the answer
        while bigger != None and smaller != None:
            if bigger == smaller:
                return bigger
            bigger = bigger.next
            smaller = smaller.next
        else:
            return None

    # Solution 4:
    # Make d = 0 but cleaner
    # Time: O(n) | Space: O(1)
    # Runtime: 165 ms, faster than 75.68% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 29.6 MB, less than 34.22% of Python3 online submissions for Intersection of Two Linked Lists.
    def getIn4(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
        curr1, curr2 = h1, h2

        # This loop will make h1 and h2 lists of same length
        # If the smaller list reaches the end just move head of bigger list by one step
        while curr1 or curr2:
            if curr1 == None: h2 = h2.next
            else: curr1 = curr1.next
            if curr2 == None: h1 = h1.next
            else: curr2 = curr2.next

        # Now we have two lists of same length and we can find the intersection point
        while h1 is not h2:
            h1 = h1.next
            h2 = h2.next

        return h1

    # Solution 5:
    # Make diff = 0 but with even cleaer code
    # Runtime: 213 ms, faster than 47.57% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 29.7 MB, less than 29.39% of Python3 online submissions for Intersection of Two Linked Lists.
    def getIn5(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB

        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next

        return currA