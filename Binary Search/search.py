class Solution:

    def binarySearch(self, nums, target):
        """
            Time O(log(n))
            Given array must be sorted
        """
        # print("Running for target:",target, "in nums:",nums)

        if len(nums) == 0:
            return -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            # print(low,mid,high)
            # print(nums[low],nums[mid],nums[high])
        else:
            return -1


print(Solution().binarySearch([1, 3], 0))
