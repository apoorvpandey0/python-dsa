"""
    Bubble sort 
    is a sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
"""
from typing import List


# Algorithm:
# Time: O(n^2) | Space O(1)
# Best case: O(n) | Average case: O(n^2) | Worst case: O(n^2)
# Stability: Stable
def bubbleSort(nums) -> List[int]:
    n = len(nums)

    for _ in range(n):
        # We use flag to break if array is already sorted
        flag = False

        for i in range(n - 1):
            # Check the next element if smaller => swap
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                flag = True

        # If array is already sorted, break
        if not flag:
            break
    return nums


if __name__ == '__main__':
    assert bubbleSort([]) == []
    assert bubbleSort([1]) == [1]
    assert bubbleSort([1, 3, 4, 3, 2]) == [1, 2, 3, 3, 4]
    assert bubbleSort([1, 3, 4, 3, 2, -1, -2]) == [-2, -1, 1, 2, 3, 3, 4]
