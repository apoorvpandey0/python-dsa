"""
    Sort 0,1,2 in a Linked List
    Link: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1#
"""


class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Time: O(n) | Space: O(1)
# Creating three lists and then merging them together approach
def segregate(head):
    # Initializing three empty lists with head pointers
    zero = Node(-1)
    zh = Node(-1)
    zh.next = zero
    one = Node(-1)
    oh = Node(-1)
    oh.next = one
    two = Node(-1)
    th = Node(-1)
    th.next = two

    # Traversing the list and segregating the nodes
    sentinal = Node(-1)
    sentinal.next = head
    prev = sentinal
    tmp = head
    while prev:
        if prev.data == 0:
            zero.next = prev
            zero = zero.next
            zero.next = None
        if prev.data == 1:
            one.next = prev
            one = one.next
            one.next = None
        if prev.data == 2:
            two.next = prev
            two = two.next
            two.next = None
        prev = tmp
        if tmp:
            tmp = tmp.next
    # merging the lists
    one.next = th.next.next
    zero.next = oh.next.next
    return zh.next.next
