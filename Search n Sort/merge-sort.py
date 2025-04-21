"""
    Merge sort is a divide and conquer algorithm.
"""

def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    i, j = 0, 0
    answer = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            answer.append(nums1[i])
            i += 1
        else:
            answer.append(nums2[j])
            j += 1
        if i == m:
            answer.extend(nums2[j:])
        if j == n:
            answer.extend(nums1[i:])
    return answer


# Time: O(nlog(n)) | Space On(n) for merge function which can be optimized
def mergesort(arr):
    if len(arr)<2:return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)


===================================== 2=====================================
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums1, nums2):
            ans = []
            m, n = 0, 0
            while m < len(nums1) and n < len(nums2):
                if nums1[m] < nums2[n]:
                    ans.append(nums1[m])
                    m += 1
                else:
                    ans.append(nums2[n])
                    n += 1
            ans.extend(nums1[m:])
            ans.extend(nums2[n:])
            return ans

        def sort(i, j):
            if i == j:
                return [nums[i]]
            mid = (i + j) // 2

            # It's important to go from i-> mid and mid+1 -> end
            # Else errors
            left = sort(i, mid)
            right = sort(mid + 1, j)
            return merge(left, right)

        return sort(0, len(nums) - 1)
