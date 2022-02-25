"""
    Even Odd Seperate
    Seperate even and odd nodes in a linked list.
    Link: https://leetcode.com/problems/odd-even-linked-list/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # Solution 1:
    # Time: O(n) | Space: O(n)
    # Runtime: 62 ms, faster than 47.55% of Python3 online submissions for Odd Even Linked List.
    # Memory Usage: 17.1 MB, less than 5.02% of Python3 online submissions for Odd Even Linked List.
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oc = ListNode(-1)
        oh = ListNode(-1,oc)
        
        ec = ListNode(-1)
        eh = ListNode(-1,ec)
        
        i = 1
        while head:
            if i%2==0:
                new = ListNode(head.val)
                ec.next = new
                ec =ec.next
            else:
                new = ListNode(head.val)
                oc.next = new
                oc =oc.next
            head = head.next
            i+=1
        
        # Add two lists
        oc.next = eh.next.next
        return oh.next.next
    
    # Solution 2:
    # This approach just manipulates pointers 
    # Runtime: 49 ms, faster than 67.16% of Python3 online submissions for Odd Even Linked List.
    # Memory Usage: 16.6 MB, less than 39.02% of Python3 online submissions for Odd Even Linked List.
    # Time: O(n) | Space O(1)
    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oc = head
        oh = ListNode(-1,oc)
        
        ec = head.next
        eh = ListNode(-1,ec)
        
        while ec and oc and ec.next:
            oc.next = oc.next.next
            ec.next = ec.next.next
            oc = oc.next
            ec = ec.next
            
        oc.next = eh.next
        return oh.next
            
    