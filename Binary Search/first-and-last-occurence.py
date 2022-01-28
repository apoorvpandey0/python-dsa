#  First and last occurences of a number in an array
# Link: https://leetcode.com/problems/first-and-last-position-of-element-in-sorted-array/
# This solution is based on binary search with O(Log(n)) time complexity
# Runtime: 127 ms, faster than 27.16% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

arr = [-1, 0, 3, 5, 5, 5, 9, 12]
arr2 = [5, 7, 7, 8, 8, 10]


class Solution:

    def isFirst(self, i, arr):
        # When arr i is already == target
        if i == 0:
            return True
        if arr[i - 1] == arr[i]:
            return False
        if arr[i - 1] < arr[i]:
            return True

    def isLast(self, i, arr):
        # When arr i is already == target
        if i == len(arr) - 1:
            return True
        if arr[i + 1] == arr[i]:
            return False
        if arr[i + 1] > arr[i]:
            return True

    def fo(self, target, arr):
        left = 0
        right = len(arr) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if arr[mid] == target:
                # print(isFirst(mid, arr))
                if self.isFirst(mid, arr):
                    return mid
                else:
                    right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return -1

    def lo(self, target, arr):
        left = 0
        right = len(arr) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if arr[mid] == target:
                # print(isLast(mid, arr))
                if self.isLast(mid, arr):
                    return mid
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return -1

    def searchRange(self, nums, target):
        return [self.fo(target, nums), self.lo(target, nums)]


print(Solution().searchRange(arr, 5))
