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



# print(merge([4],[2]))
print("Answer: ",mergesort([5,4,3,2,1]))