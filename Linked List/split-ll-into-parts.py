"""
    Split a linked list into parts
    Desc: Given a (singly) linked list with head node,
            write a function to split the linked list into k consecutive linked list parts.
            The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.
    Link: https://leetcode.com/problems/split-linked-list-in-parts/
"""


# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Runtime: 52 ms, faster than 56.27% of Python3 online submissions for Split Linked List in Parts.
    # Memory Usage: 14.3 MB, less than 89.10% of Python3 online submissions for Split Linked List in Parts.
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0

        # Finding length of Linked list
        tmp = head
        while tmp:
            n+=1
            tmp = tmp.next
        
        # Size of each chunk, remaining elements
        # If n>k: then size will be positive else: 0
        # If n<k: then left will be k and add 1 element to each chunk as size will be 0
        size,left = n//k,n%k
        chunkHead = head
        res = []
        
        # Create k chunks
        for _ in range(k):

            # Create a new chunk or size + 1 if left elements
            # This is so that max difference bw two chunks is 1
            # Also left will always be < n
            nodeSize = size + (1 if left>0 else 0)
            tmp = chunkHead
            prev = None
            for _ in range(nodeSize):
                prev = tmp
                tmp = tmp.next
            
            # Cutting off the last node
            if prev:
                prev.next = None
            
            # Appending the chunk to result
            res.append(chunkHead)

            # Updating chunkHead to point to next chunk
            chunkHead = tmp

            # Updating left as 1 will always be added to curr chunk
            left-=1
        return res
                