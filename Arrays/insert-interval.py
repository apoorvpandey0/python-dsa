"""
    Insert Interval
    Desc:   Insert a new interval in a list of sorted non overlapping intervals
            Output should be non overlapping as well
    Link: https://leetcode.com/problems/insert-interval/
"""


# This is a helper function to the main ii function
def mi(nums):
    # Time: O(nlogn)
    nums.sort(key=lambda x: x[0])
    # print(nums)
    answer = []

    # Time: O(n)
    tmp = nums[0]
    for i, pair in enumerate(nums):
        if pair[0] <= tmp[1]:
            tmp[1] = max(tmp[1], pair[1])
        else:
            answer.append(tmp)
            tmp = pair
    answer.append(tmp)

    return answer


# Solution 1:
# Trivial approach
# Time: O(nlog(n))
# Runtime: 153 ms, faster than 11.78% of Python3 online submissions for Insert Interval.
def ii(nums, ele):
    n = len(nums)

    # Time: O(Log(n))
    # Finding insert Index
    l, r = 0, n - 1
    insert = -1
    while l <= r:
        m = (l + r) // 2
        # print(l, m, r)
        if nums[m][0] <= ele[0] <= nums[m][1]:
            insert = m + 1
            break
        elif ele[0] > nums[m][1]:
            l = m + 1
        else:
            r = m - 1
    print(insert)

    # Time: O(n)
    nums.insert(insert, ele)
    print(nums)

    # O(nLog(n))
    return mi(nums)


# [[1,2],[3,10],[12,16]]
print(ii([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [6, 8]))

# Solution 2:
# Time: O(n) space 0(1)
# https://leetcode.com/problems/insert-interval/discuss/790477/Python-Binary-Search%3A-O(n)-time-%2B-O(1)-space
