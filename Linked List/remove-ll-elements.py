"""
    Remove linked list elements
    Desc: Given the head of a linked list and an integer val,
    remove all the nodes of the linked list that has Node.val == val, and return the new head.
    Link: https://leetcode.com/problems/remove-linked-list-elements/
"""
from basic import *


# Time: O(n) | Space: 0(1)
# Runtime: 76 ms, faster than 58.54% of Python3 online submissions for Remove Linked List Elements.
def removeAll(self, val: int):
    if self.head == None:
        return None
    while self.head and self.head.value == val:
        self.head = self.head.next
    tmp = self.head
    prev = Node()
    while tmp is not None:
        if tmp.value == val and tmp != None:
            prev.next = tmp.next
        else:
            prev = tmp
        tmp = tmp.next
    return self.head


if __name__ == "__main__":
    # c = LinkedList(values=[6, 6, 6, 1, 2, 6, 6, 6, 3, 4, 5, 6, 6, 6])
    # c.removeAll(6)
    # print(c)
    c = LinkedList(values=[6, 6, 6])
    c.removeAll(6)
    print(c)