"""
    How to reverse a Linked List
    Link: https://leetcode.com/problems/reverse-linked-list/
    Solution: https://leetcode.com/problems/reverse-linked-list/discuss/1449712/Easy-C%2B%2BJavaPythonJavaScript-Explained%2BAnimated
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n) | Space: O(1)
# Runtime: 40 ms, faster than 64.26% of Python3 online submissions for Reverse Linked List.
def reverse(head):
    """
    Visual aid:
          next
           ↓
None  1 -> 2 -> 3 -> None
      ↑    ↑   
     prev curr

     """
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverse2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
        https://leetcode.com/submissions/detail/718730097/
    """
    if not head: return
    prev = None
    nxt = head.next
    
    while nxt!=None:
        head.next = prev
        prev = head
        head = nxt
        nxt = nxt.next
    head.next = prev
    # print(prev)
    return head
