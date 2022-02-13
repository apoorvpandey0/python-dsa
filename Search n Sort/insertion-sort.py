"""
    Insertion sort 
    is a sorting algorithm that works by repeatedly inserting an element into the sorted sequence.
"""
from typing import List


# Algorithm:
# Time: O(n^2) | Space O(1)
# Best case: O(n) | Average case: O(n^2) | Worst case: O(n^2)
# Stability: Unstable
def InsertionSort(nums) -> List[int]:
    n = len(nums)
    for left in range(1, n):
        # Find the correct position in sorted array
        hole = left
        value = nums[hole]
        while nums[hole - 1] > value and hole > 0:
            nums[hole], nums[hole - 1] = nums[hole - 1], nums[hole]
            # print(value, nums[hole])
            hole -= 1
        nums[hole] = value
    return nums


if __name__ == '__main__':
    # print(InsertionSort([1, 5, 4, 3, 2]))
    assert InsertionSort([]) == []
    assert InsertionSort([1]) == [1]
    assert InsertionSort([1, 3, 4, 3, 2]) == [1, 2, 3, 3, 4]
    assert InsertionSort([1, 3, 4, 3, 2, -1, -2]) == [-2, -1, 1, 2, 3, 3, 4]