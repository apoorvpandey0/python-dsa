"""
    Sort array by parity
    Desc: Put all even elements at left
    Link: https://leetcode.com/problems/sort-array-by-parity/
"""


# 012 sort inspired algorithm
# Time: O(n)
# Runtime: 68 ms, faster than 99.46% of Python3 online submissions for Sort Array By Parity.
def s(nums):
    l = 0
    r = 0

    while r < len(nums):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        else:
            r += 1
    return nums


print(s([3, 1, 2, 4]))
