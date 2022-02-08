"""
    Reverse Linked List 2
    Reverse a List from given start and end indexes
    Link: https://leetcode.com/problems/reverse-linked-list-ii/
"""
from basic import *


# Accepted Solution
# Algorithm:
# Insert the next element to the start of L position
# Time: O(n) | Space: O(1)
# Runtime: 42 ms, faster than 47.58% of Python3 online submissions for Reverse Linked List II.
def rev2(head, left, right):
    """
        Solution with Photo examples
        Link: https://leetcode.com/problems/reverse-linked-list-ii/discuss/1167109/Python3-One-pass-iterative-solution-beats-95.50-(with-figure-explanation)
    """
    if not head or not head.next or left == right:
        return head

    # dummy_head = ListNode(val=-1, next=head)
    dummy_head = Node(-1, next=head)
    prev = dummy_head

    # Iterate prev to the (left-1)-th node
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next  # curr is at the left-th node

    # Within the reverse part, iteratively move the next node of curr to the beginning
    """
        Full list,curr for values:
            [1,2,3,4,5,6,7], LEFT = 2,RIGHT = 5
            1->2->3->4->5->6->7->None  | 2->3->4->5->6->7->None
            1->3->2->4->5->6->7->None  | 2->4->5->6->7->None
            1->4->3->2->5->6->7->None  | 2->5->6->7->None
            Answer = 1->5->4->3->2->6->7->None
        Lets say prev = 1,curr = 2
    """
    for _ in range(right - left):
        print(prev, curr)
        # Init next as curr.next i.e. 3
        nextp = curr.next

        # Since we want to remove next
        # Link curr.next to 4 i.e next.next element
        curr.next = nextp.next

        # Set Node 3 behind node 2
        nextp.next = prev.next

        # Link prev to out next node ie Link 1 to 3
        prev.next = nextp

        # Now value of prev and curr will remain same
        # Only next ele to cur will be 4 now and so on!
    return dummy_head.next


# My Solution:
# Algorithm:
# 1. Create a new LL of items in [L,R]
# 2. Reverse the new LL
# 3. Insert it in correct places in original LL
# This is more complex approach and is not easily portable to Leetcode
def reverse(head, left, right):
    if head == None:
        return
    counter = 1
    curr = head
    vals = []
    prevL = Node(head.value, head.next)
    prevR = None
    # Take out all elements b/w [L,R] with their L,R pointers
    while curr:
        if counter + 1 == left:
            prevL = curr
        if counter == right:
            prevR = curr
        if left <= counter <= right:
            vals.append(curr.value)
        curr = curr.next
        counter += 1
    # Create a new LL out of these
    if not vals:
        return []
    new = LinkedList(values=vals)

    # Reverse the new list
    prev = None
    curr = new.head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    new.head = prev
    # print(new)
    # print(prevL)
    # print(prevR)

    # Update the left and right pointers in original list to point to new list

    # Update left pointer
    if left == 1:
        head = new.head
    else:
        prevL.next = new.head

    # Update right pointer
    curr = new.head
    while curr.next:
        curr = curr.next
    if prevR:
        curr.next = prevR.next
    return head


if __name__ == '__main__':
    a = LinkedList(values=[1, 2, 3, 4, 5, 6, 7])
    # print(reverse(a.head, 9, 9))
    print(rev2(a.head, 2, 5))
