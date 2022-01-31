"""
    229. Majority Element
    Desc: List all elements having count> n/3
    Link: https://leetcode.com/problems/majority-element-ii/
"""

from collections import Counter


# Solution 1:
# Using python Collections
# Runtime: 181 ms, faster than 25.82% of Python3 online submissions for Majority Element II.
def me(nums):
    c = Counter(nums)
    return list(filter(lambda x: c[x] > len(nums) / 3, c))


# Solution 2:
# Using Boyre Moores algorithm

print(me([3, 2, 3]))
