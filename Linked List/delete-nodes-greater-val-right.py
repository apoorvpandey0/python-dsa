"""
    Delete nodes having greater value on right side
    Desc: Delete a node if any larger value exists on its right side
    Link: https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right-side/1
"""


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Algorithm:
# Reverse the list
# Check from back if a nodes needs to be deleted
# Reverse the list again
# Time: O(n) | Space: O(1)
def compute(self, head):
    # Reversing the list
    prev = None
    tmp = head
    while tmp:
        nxt = tmp.next
        tmp.next = prev
        prev = tmp
        tmp = nxt

    # Checking the nodes to be deleted
    max_val = prev.data
    head = prev
    tmp = prev
    right = Node(-1)
    right.next = prev
    while tmp:
        if tmp.data < max_val:
            right.next = tmp.next
        else:
            right = tmp
        max_val = max(max_val, tmp.data)
        tmp = tmp.next

    # Reversing the list again
    tmp = head
    newPrev = None
    while tmp:
        nxt = tmp.next
        tmp.next = newPrev
        newPrev = tmp
        tmp = nxt

    return newPrev
