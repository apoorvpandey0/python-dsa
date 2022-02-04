"""
    Count max consecutive ones in a binary array
    Link: https://leetcode.com/problems/max-consecutive-ones/
"""

from itertools import groupby
from typing import List


class Solution:
    # Solution 1:
    # Time: O(n) | Space O(1)
    # Runtime: 388 ms, faster than 53.16% of Python3 online submissions for Max Consecutive Ones.
    def find(self, nums: List[int]) -> int:
        answer = 0
        counting = False
        tmp = 0
        for i in nums:
            if i == 1:
                counting = True
                tmp += 1
            if i == 0:
                counting = False
                tmp = 0
            answer = max(answer, tmp)
        return answer

    # Solution 2:
    # Time: O(n) | Space O(1)
    # Runtime: 348 ms, faster than 85.50% of Python3 online submissions for Max Consecutive Ones.
    def find2(self, nums: List[int]) -> int:
        return max(sum(g) for _, g in groupby(nums))
