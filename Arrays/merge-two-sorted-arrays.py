"""
    Merge two sorted arrays
    Link: https://leetcode.com/problems/merge-sorted-array/
"""


# Solution 1:
# Time: O(n) | Space O(1)
# Runtime: 46 ms, faster than 49.40% of Python3 online submissions for Merge Sorted Array.
def merge(nums1, nums2):
    """
        Given nums1 has extra n zeroes at the end to make it's length m+n.
    """
    n = len(nums2)
    m = len(nums1) - n
    while m > 0 and n > 0:
        # Index to append to: len(nums1)-1 = m+n-1
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1  # Check the next element in nums1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1  # Check the next element in nums2
        # print(m, n, nums1)
    # The remaining k elements in nums2 can just be inserted into the front
    # If k == 0, nums2 has already been merged, so this for loop is also skipped
    for i in range(n):
        nums1[i] = nums2[i]
    return nums1


# print(merge(nums1=[1, 2, 3, 0, 0, 0], nums2=[2, 5, 6]))
# print(merge(nums1=[5, 8, 10, 12, 15, 0, 0, 0], nums2=[2, 5, 12]))
# print(merge(nums1=[2, 5, 12], nums2=[5, 8, 10, 12, 15]))
# print(merge([1, 3, 5, 7], [0, 2, 6, 8, 9]))


# Solution 2:
# Not accepted on leetcode
# Time: 0(n)  | Space: O(m+n)
def merge2(nums1, nums2):
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


# print(merge2(nums1=[5, 8, 10, 12, 15], nums2=[2, 5, 12]))
# print(merge2(nums1=[2, 5, 12], nums2=[5, 8, 10, 12, 15]))
# print(merge2([1, 3, 5, 7], [0, 2, 6, 8, 9]))
