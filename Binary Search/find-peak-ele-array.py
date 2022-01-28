"""
    Find peak element in an array
    Desc: A peak element is an element that is strictly greater than its neighbors.
          If the array contains multiple peaks, return the index to any of the peaks.
    Link: https://leetcode.com/problems/find-peak-element/
"""


# Runtime: 40 ms, faster than 94.93% of Python3 online submissions for Find Peak Element.
# Time: O(log(n))
def peak(nums):

    # Edge cases
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums) - 1

    left, right = 1, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)

        # mid should be strictly greater than both its neighbours
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        # if righ element is greater move right
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1

        # if left element is greater move left
        else:
            right = mid
    return -1


# print(peak([1, 2, 1, 3, 5, 6, 4]))

print(peak([5, 4, 3, 2, 100]))
print(peak([5, 6, 3, 2, 100]))
print(peak([5, 6, 3, 102, 100]))
