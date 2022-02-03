"""
    Merge Intervals
    Desc: Given overlapping intervals, merge them into one.
    Link: https://leetcode.com/problems/merge-intervals/
"""


# Time: O(n(log(n)))
def mi(nums):

    # Time: O(nlogn)
    nums.sort(key=lambda x: x[0])
    print(nums)
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


print(
    mi([[1, 3], [2, 4], [15, 18], [8, 9], [8, 10], [9, 11], [2, 6], [16, 17]]))
