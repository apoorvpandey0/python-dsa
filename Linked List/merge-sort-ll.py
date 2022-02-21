"""
    Merge sort Linked list
    Link: https://leetcode.com/problems/sort-list/
    Good exp: https://leetcode.com/problems/sort-list/discuss/892759/Python-O(n-log-n-log-n)-merge-sort-explained
"""


# Merge sort Top down approach
# Time: O(nlog(n)) | Space: Some space used for recursion stack
# Runtime: 512 ms, faster than 48.07% of Python3 online submissions for Sort List.
# Memory Usage: 54.3 MB, less than 5.04% of Python3 online submissions for Sort List.
class Solution:
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