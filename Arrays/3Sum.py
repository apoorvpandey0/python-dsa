1. Brute force n^3
2. Sort + Two pointer 2Sum -> NlogN + N * N -> N^2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):

            # Since array is sorted we can skip duplicate i just by checking previous element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initializing two pointers of the two pointer 2Sum approach
            j = i + 1
            k = len(nums) - 1

            while j < k:

                # You cannot write if condition here for incrementing j as we did in above for loop
                
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # Move j to its next non duplicate value
                    # This has to be a while loop here, since we dont want the above logic to run unless we reach the next non duplicate value of j
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
