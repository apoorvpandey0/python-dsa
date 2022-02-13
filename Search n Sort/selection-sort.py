"""
    Selection sort 
    is a sorting algorithm that works by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
"""
from typing import List


# Algorithm (In place):
# Find minimum in right subarray
# Swap it with current left pointer
# Time: O(n^2) | Space O(1)
# Stability: Unstable
def selectionSort(nums) -> List[int]:
    n = len(nums)
    # This will run n times
    for left in range(n):
        min_index = left
        # This will run n-left times
        for j in range(left, n):
            # Finding the index of the next minimum element
            if nums[min_index] > nums[j]:
                min_index = j
        # swap min ele with left pointer
        nums[left], nums[min_index] = nums[min_index], nums[left]
    # Total time: n*(n-1)/2 = O(n^2)
    return nums


if __name__ == '__main__':
    assert selectionSort([]) == []
    assert selectionSort([1]) == [1]
    assert selectionSort([1, 3, 4, 3, 2]) == [1, 2, 3, 3, 4]
    assert selectionSort([1, 3, 4, 3, 2, -1, -2]) == [-2, -1, 1, 2, 3, 3, 4]
