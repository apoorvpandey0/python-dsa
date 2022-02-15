"""
    Single number
    Desc: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Link: https://leetcode.com/problems/single-number/
"""

from typing import List
"""
    XOR Table:
    0 ^ 0 = 0
    0 ^ 5 = 5
    7 ^ 0 = 7
    8 ^ 8 = 0
"""


# XOR approach
# Any element that occurs even times XOR's to 0
# Any element that occurs odd times XOR's to itself
# Runtime: 154 ms, faster than 65.04% of Python3 online submissions for Single Number.
def singleNumber(nums: List[int]) -> int:
    result = 0
    for ele in nums:
        print(result)
        result ^= ele
    return result
