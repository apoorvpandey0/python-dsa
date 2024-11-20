1. Brute force n^3
2. Sort + Two pointer 2Sum -> NlogN + N * N -> N^2

"""
    Easiest solution
    Time: O N^2
    Space: O N
    Duplicate cases are automatically handled by using set
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = set()
        result = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tempsum = nums[i] + nums[j] + nums[k]
                if tempsum == 0:
                    temp.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tempsum < 0:
                    j += 1
                else:
                    k -= 1
        result = list(temp)
        return result

"""
    Without using the set above, now we need to programatically ignore the duplicates at each step
    a + b + c = total
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):

            """
                Since array is sorted we can skip duplicate i just by checking previous element
                Removing duplicates for position "a"    
            """
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initializing two pointers of the two pointer 2Sum approach
            j = i + 1
            k = len(nums) - 1

            while j < k:

                # You cannot write if condition here for incrementing j as we did in above for loop
                # if nums[j] == nums[j-1]: 
                #     j+=1
                #     continue
                # [-4, -1, -1, 0, 1, 2] in this case -1,-1,2 soln will get skipped as if will not let j to be 2nd index

                
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
                    # Removing duplicates for J
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
