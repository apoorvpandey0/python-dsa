"""
    Merge Intervals
    Desc: Given overlapping intervals, merge them into one.
    Link: https://leetcode.com/problems/merge-intervals/
"""


# Time: O(n(log(n)))
# Beats 100%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        ans = []
        l,r = intervals[0]
        
        for tl,tr in intervals:
            if tl<=r:
                if tr>r: r = tr
            else:
                ans.append([l,r])
                l,r = tl,tr
        ans.append([l, r])
        return ans


print(
    mi([[1, 3], [2, 4], [15, 18], [8, 9], [8, 10], [9, 11], [2, 6], [16, 17]]))
