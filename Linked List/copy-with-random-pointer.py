"""
    Copy Linked list with Random Pointer
    Desc: Given a linked list, a random pointer which is pointing to a random node in the linked list,
    Link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Solution 1:
# Using stack
# Time: O(n) | Space: O(n)
# TODO: Complete this


# Solution 2:
# Algorithm
# 1. Create a new copy of Linked list with null random pointers and valid next pointers
# 2. Make the next of original list point to corresponding new elements
# 3. Point the random pointers of new list to corresponding original elements
# 4. Now new.random = new.random.random.next
# Time: O(n) | Space: O(1)
# Runtime: 63 ms, faster than 24.75% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15 MB, less than 58.85% of Python3 online submissions for Copy List with Random Pointer
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        ctmp = Node(-1)
        copy = Node(-1,ctmp)
        tmp = head
        while tmp:
            new = Node(tmp.val,tmp.next,tmp)
            
            # Add to second LL
            ctmp.next = new
            
            # Update original next to copied LL
            nxt = tmp.next
            tmp.next = new
            
            # Next iteration
            ctmp = ctmp.next
            tmp = nxt
        tmp = copy.next.next
        while tmp:
            if tmp.random.random:
                tmp.random = tmp.random.random.next
            else: 
                tmp.random = None
            tmp = tmp.next
        return copy.next.next    
            
        
        