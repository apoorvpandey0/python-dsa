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

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for n in nums:
            if n in count: count[n] += 1
            else: count[n] = 1

            if len(count) > 2:
                new_count = {}
                for n, c in count.items():
                    if c > 1:
                        new_count[n] = c - 1
                count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
                
        return res


# Solution 2:
# Using Boyre Moores algorithm

print(me([3, 2, 3]))
