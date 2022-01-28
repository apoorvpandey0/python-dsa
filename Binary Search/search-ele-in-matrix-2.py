"""
    Search a 2D Matrix II
    Desc: Given a matrix m x n with properties:
            Integers in each row are sorted in ascending from left to right.
            Integers in each column are sorted in ascending from top to bottom.
    Link: https://leetcode.com/problems/search-a-2d-matrix-ii
    Explaination: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/1079154/Python-O(m-%2B-n)-solution-explained
"""


# Time: O(m+n)
# Runtime: 168 ms, faster than 67.98% of Python3 online submissions for Search a 2D Matrix II.
def searchMatrix(nums, target):
    x, y = len(nums[0]) - 1, 0
    while x >= 0 and y <= len(nums) - 1:
        if nums[y][x] > target:
            x -= 1
        elif nums[y][x] < target:
            y += 1
        else:
            return True
    return False


def bs(nums, target):
    print("Running bs in: ", nums)
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def searchMatrix2(nums, target):
    top, bottom = 0, len(nums) - 1
    while top <= bottom:
        mid = (top + bottom) // 2
        print(top, mid, bottom)
        if nums[mid][0] <= target <= nums[mid][-1]:
            return bs(nums[mid], target) >= 0
        elif nums[mid][-1] < target:
            top = mid + 1
        else:
            bottom = mid - 1


print(
    searchMatrix2([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                   [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
