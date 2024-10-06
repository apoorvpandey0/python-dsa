"""
    Sort colors or 102 sort
    aka Dutch national flag problem
    Link: https://leetcode.com/problems/sort-colors/
"""

from collections import Counter


# Solution 2:
# Using low, mid and high pointers
# swap and sort the 0's and 2's then 1's will automatically be sorted
# Time: O(n)
# Runtime: 32 ms, faster than 86.59% of Python3 online submissions for Sort Colors.
def cs(nums):
    """
        Soln: https://www.youtube.com/watch?v=sEQk8xgjx64

        Quicksort Partition

        Algo:
            if arr[m]==0: swap it with left index and m++,l++
            if arr[m]==1: skip it as it will be in place automatically ie m++
            if arr[m]==2: swap it with high/right index h--

        Nots:
        while m<=h and not just m<h
        Processing All Elements: The index m represents the current element being examined. 
        The loop needs to continue as long as there are unprocessed elements between m and h. 
        If we only use m < h, we might miss processing the element at index h, especially when m and h are equal, which indicates there’s still an element left to check.

        Note 2:
        We do not increment m on 2 because on swapping with "h" we might bring another 2 in "m" position which will simply get skipped if m got ++
        Try this ex: [0, 1, 2, 2, 0, 1, 2]
        at m = first 2
        swapping with h = last 2
        and incrementing m will place m at 2nd 2
        completely skipping the new swapped 2 which is now the first 2
    """
    l = 0
    m = 0
    h = len(nums) - 1

    # m<h won't work try this: [2,0,1]
    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        elif nums[m] == 2:
            nums[h], nums[m] = nums[m], nums[h]
            h -= 1
    return nums


# Solution 2 : Not accepted on Leetcode
# Time: O(n)
def cs1(nums):
    c = Counter(nums)
    answer = []
    if c.get(0):
        answer.extend([0] * c[0])
    if c.get(1):
        answer.extend([1] * c[1])
    if c.get(2):
        answer.extend([2] * c[2])
    return answer


print(cs([2, 0, 1]))
print(cs([1, 2, 2, 2, 0, 0, 0, 1]))
