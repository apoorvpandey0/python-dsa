"""
    Search a 2D Matrix
    Desc: Given is a m x n matrix with properties:
            Integers in each row are sorted from left to right.
            The first integer of each row is greater than the last integer of the previous row.
    Solution 2 is preffered solution
    Link: https://leetcode.com/problems/search-a-2d-matrix/
"""


# Solution 1
# Run a BS on rows to determine the row number
# Run a BS in the row found in prev step
# Time: 2Log(n)
# Runtime: 85 ms, faster than 7.91% of Python3 online submissions for Search a 2D Matrix
def bs(nums, target):
    left, right = 0, len(nums) - 1
    print("Running bs: ", nums)
    while left <= right:
        mid = (left + right) // 2
        # print(left, mid, right)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def searchMatrix(nums, target):
    if target < nums[0][0]:
        return False

    if nums[-1][0] <= target:
        return bs(nums[-1], target) >= 0

    left, right = 0, len(nums) - 2
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid][0] <= target < nums[mid + 1][0]:
            return bs(nums[mid], target) >= 0
        elif nums[mid][0] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# Solution 2
# Treat the 2D matrix as an 1D array and do a BS
# Time: O(log(n))
# Runtime: 44 ms, faster than 76.67% of Python3 online submissions for Search a 2D Matrix.
"""
    Explaination:
    let a matrix be:
         0   1  2  3
        [1,  2, 3, 4]
        
         4   5  6  7
        [5,  6, 7, 8]

         8   9 10 11
        [9, 10,11,12]

        For an element at index 9
            rowIndex = 9 // numerOfColumns
            colIndex = 9 % numberOfColumns
        Since the numbering has been donw columnwise
"""


def searchMatrix2(nums, target):
    rows = len(nums)
    cols = len(nums[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        normal_midpoint = (left + right) // 2
        midpoint_ele = nums[normal_midpoint // cols][normal_midpoint % cols]
        # print(nums[left], midpoint_ele, right)
        if midpoint_ele == target:
            return True
        elif midpoint_ele <= target:
            left = normal_midpoint + 1
        else:
            right = normal_midpoint - 1
    return False


# print(searchMatrix2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23))
# print(searchMatrix2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1))
# print(searchMatrix2([[5]], 10))
# print(
#     searchMatrix2(
#         [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], [70, 80, 90, 100]],
#         100))
