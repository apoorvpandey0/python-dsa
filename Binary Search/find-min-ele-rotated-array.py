"""
    Find Minimum in Rotated Sorted Array
    Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


# Runtime: 44 ms, faster than 59.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
def findMin(arr):
    if len(arr) == 0:
        return -1

    # case when array is not at all rotated
    if arr[0] < arr[-1] or len(arr) == 1:
        return arr[0]

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)

        # Minimum element condition
        if (arr[mid] < arr[mid - 1]):
            return arr[mid]

        # Case: [ 4, 5, 6 1,2,3]
        # (mid is 4) or (mid is 2)
        elif (arr[mid] > arr[0]) or (arr[mid] > arr[-1]):
            left = mid + 1
        else:
            right = mid
    return -1


# print(findMin(a))
# print(findMin([5, 1, 2, 3, 4]))
# print(findMin([3, 4, 5, 1]))
# print(findMin([3, 1]))
# print(findMin([5, 4]))
# print(findMin([1]))


# Best case O(n)
# Worst case O(log(n))
# Runtime: 90 ms, faster than 18.48% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
def findMin2(arr):
    # With duplicates
    if len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(left, mid, right)
        # Case: [ 4, 5, 6, 1, 2, 3] and mid = 5
        if (arr[mid] > arr[right]):
            left = mid + 1

        # Case: [ 4, 5, 6, 1, 2, 3] and mid = 2
        elif arr[mid] < arr[right]:
            right = mid

        # Case: [ 4, 5, 6,6,6,6,7, 1, 2, 3] and mid = 6
        else:
            right -= 1
    return arr[mid]


# print(findMin2([1, 2, 3, 4]))

# print(findMin2([2]))
# print(findMin2([2, 2]))
# print(findMin2([2, 2, 2, 2, 2, 2]))

# print(findMin2([3, 2, 2, 2, 0, 1]))
# print(findMin2([2, 2, 2, 2, 0, 1]))

# print(findMin2([0, 1, 4, 4, 4, 4]))

# print(findMin2([4, 4, 0, 1, 3, 4, 4]))
# print(findMin2([10, 1, 10, 10, 10, 10]))
# print(findMin2([3, 3, 0, 2, 3, 3, 3, 3]))

# print(findMin2([5, 4]))
