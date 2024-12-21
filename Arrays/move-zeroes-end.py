whenever we find 0, shift entire array by 1 place and set 0 at end of array
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        i = 0
        while i<j:
            # print(i,j,nums)
            if nums[i] == 0:
                for p in range(i,j):
                    nums[p] = nums[p+1]
                nums[j] = 0
                j-=1
            else:
                i+=1
            # print(nums)
        return nums
        
