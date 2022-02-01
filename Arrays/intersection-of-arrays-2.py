"""
    Intersection of Two Arrays II
    Desc: Given two arrays, write a function to compute their intersection.
    Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from collections import Counter


# Time: O(n)
# Runtime: 44 ms, faster than 91.17% of Python3 online submissions for Intersection of Two Arrays II.
def i(a, b):
    c = Counter(a)
    d = Counter(b)
    answer = []
    arr = c if len(c) >= len(d) else d
    for i in arr:
        # print(i, min((c[i], d[i])))
        if i in c and i in d:
            answer.extend([i] * min((c[i], d[i])))
    return answer


print(i([1, 2, 2, 1], [2, 2]))
print(i([4, 9, 5], [9, 4, 9, 8, 4]))
