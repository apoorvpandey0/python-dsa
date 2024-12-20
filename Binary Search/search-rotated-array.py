"""
    Search an element in Rotated Ascending Sorted Array with distinct values
    Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

    SOL 1:
    One pass soln: https://www.youtube.com/watch?v=U8XENwh8Oy8
    
    SOL 2:
    Time: O(log(n)) or 2log(n)
    
"""

=========================== LOG N Solution using if conditions without finding pivot element ================
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2

            if nums[mid] == target: return mid

            # First array
            if nums[mid]>= nums[0]:
                if target > nums[mid]: 
                    start = mid+1
                elif target < nums[0]: 
                    start = mid + 1
                else:
                    end = mid - 1

            # Second array
            elif nums[mid] < nums[0]:
                if target<nums[mid]: 
                    end = mid - 1
                elif target>=nums[0]: 
                    end = mid - 1
                else:
                    start = mid+1
            
            # print(start,mid,end)
        return -1 if start>end else mid

=================== Log N solution using find the pivot then solve method ========================

class Solution2:
    # Function Time: O(log(n))
    def findPivot(self, nums):
        # Finding the pivot/max value's index
        left, right = 0, len(nums) - 1

        # Case: [4]
        if len(nums) == 1:
            return 0

        # Case: [2,3,4,5,6]
        if nums[0] < nums[-1]:
            return len(nums) - 1

        # Cases: [6, 7, 0, 1, 2]
        while left < right:
            mid = left + (right - left) // 2

            # case: nums[mid] == 7
            if nums[mid] > nums[mid + 1]:
                return mid

            # if mid is smaller than left, max is on the left hand side
            if nums[mid] < nums[left]:
                right = mid
            else:  # mid is greater than left, then max is on the right hand side
                left = mid + 1
        return -1
    # Function Time: O(log(n))
    def bs(self, arr, target):
        # print("running bs in ", arr, "for ", target)
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
        return -1

    def search(self, nums, target):
        print("Input: ", nums, "target ", target)
        if not nums:
            return -1
        pivotIndex = -1
        answer = -1
        # Finding the pivot element O(log(n))
        pivotIndex = self.findPivot(nums)
        print("Pivot:", nums[pivotIndex])

        # Finding the element in correct increasing array O(log(n))
        left_arr = nums[0:pivotIndex + 1]
        right_arr = nums[pivotIndex + 1:]
        # print(left_arr, right_arr)
        if left_arr[0] <= target <= left_arr[-1]:
            answer = self.bs(left_arr, target)
        else:
            answer = self.bs(right_arr, target)
            if answer != -1:
                answer += (pivotIndex + 1)
        return answer


# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
# print(Solution().search([1, 3], 1))
# print(Solution().search([], 0))
# print(Solution().search([0], 0))
print(Solution().search([1, 3], 3))
# print(Solution().search([3, 1], 1))

# Rotated array 2
# print(Solution().search([2, 5, 6, 0, 0, 1, 1, 1, 2], 2))
# print(Solution().bs([1, 0, 1, 1, 1], 0) != -1)
