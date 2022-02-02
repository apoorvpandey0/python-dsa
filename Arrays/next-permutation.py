"""
    31. Next Permutation
    Desc: Find the next permutation such that:
            It is lexicographically greater than the current permutation.
    Link: https://leetcode.com/problems/next-permutation/
"""


# Time: n + n/2 + (n-peak)log(n-peak)
# i.e: O(Log(n))
# Runtime: 50 ms, faster than 48.73% of Python3 online submissions for Next Permutation.
def np(nums):
    n = len(nums)
    # Find the last peak
    peak = -1
    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            peak = i

    # If array is in Descending order
    if peak == -1:
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
        return nums

    # Find the smallest element after peak which is:
    # Greater than nums[peak-1] and <nums[peak]
    # If found: swap peak-1 with it
    # Else swap peak with peak -1
    # Sort the right array in ascending order
    index = peak
    for i in range(peak, n):
        if nums[i] > nums[peak - 1] and nums[i] < nums[peak]:
            index = i
    nums[peak - 1], nums[index] = nums[index], nums[peak - 1]
    nums[peak:] = sorted(nums[peak:])
    print(nums)
    # return nums


# [1, 2, 3, 2, 2, 1, 1, 3, 4]
# print(np([1, 2, 3, 2, 1, 4, 3, 2, 1]))

# [1, 2, 3]
print(np([3, 2, 1]))

# [1, 2, 3, 5, 4]
# print(np([1, 2, 3, 4, 5]))

# [1, 2, 4, 2, 3, 5]
# print(np([1, 2, 3, 5, 4, 2]))
