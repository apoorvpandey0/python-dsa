"""
    Merge k sorted linked lists and return it as one sorted list.
    Link: https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = None

class Mergesort:
    def merge(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.merge(a.next, b)
        return a or b

    def sortList(self,head):

        # Base case when only one/zero elements are left in LL 
        if not head or not head.next: return head

        # Finding left and right parts 
        # pre pointer is used to cut off left and right Lists
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        
        # Recursive calls to each left and right part
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge left,right
        return self.merge(left,right)


# Solution 4:
# Using heap - Best solution
# Time: O(nlog(n)) | Space: O(n)
# Runtime: 125 ms, faster than 69.48% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18.4 MB, less than 19.34% of Python3 online submissions for Merge k Sorted Lists.
def mergeKLists4(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Create a heap from all the given LL
    heap = []
    for head in lists:
        tmp = head
        while tmp:
            heapq.heappush(heap,tmp.val)
            tmp = tmp.next
    
    # Create a new LL from the heap
    curr = ListNode(-1)
    sentinal = ListNode(-1,curr)
    while heap:
        node = ListNode(heapq.heappop(heap))
        curr.next = node
        curr = curr.next
    return sentinal.next.next


# Solution 3:
# Using Divide and Conquer
# Height of the tree = Log2(K) where k is number of linked lists
# Time: O(nlog2(n)) | Space: O(n)
# Runtime: 211 ms, faster than 24.43% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 26.5 MB, less than 5.52% of Python3 online submissions for Merge k Sorted Lists.
def mergeKLists3(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    # Base case
        
    if not lists: return None
    if len(lists)<2: return lists[0]

    # Finding mid point
    mid = len(lists)//2
    left = mergeKLists3(lists[:mid])
    right = mergeKLists3(lists[mid:])
    return Mergesort().merge(left,right)

# Solution 2:
# Join all lists and sort them.
# Time: O(nlog(n)) | Space: O(n)
# Runtime: 160 ms, faster than 48.87% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 26.4 MB, less than 5.52% of Python3 online submissions for Merge k Sorted Lists.
def mergeKLists2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists: return None
    
    # Create one list fom all the lists
    tail = ListNode(-1)
    sentinal = ListNode(-1,tail)
    for head in lists:
        if head:
            tail.next = head
            while tail.next:
                tail = tail.next
    newHead = sentinal.next.next

    # Sorting the new list
    return Mergesort().sortList(newHead)


# Solution 1:
# Find out minimum in each list and append to new list.
# Time: O(nk) | Space: O(n)
# TLE  - Is not accepted on Leetcode
def mergeKLists1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
    sentinal = ListNode(-1)
    head = sentinal
    while any(lists):

        # Finding min element in lists
        tmp = []
        minele = float('inf')
        minIndex = -1
        for i in range(len(lists)):
            if lists[i]:
                tmp.append(lists[i].val)
                if lists[i].val<minele:
                    minele = lists[i].val
                    minIndex = i
            else:
                tmp.append(float('inf'))
        
        # Adding min element to new list
        head.next = ListNode(minele)
        lists[minIndex] = lists[minIndex].next
        head = head.next
    return sentinal.next











