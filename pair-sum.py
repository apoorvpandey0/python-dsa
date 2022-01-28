class Solution:
    """
        Pair sum problem:
        Given an array find first pair with given sum S.
        https://leetcode.com/problems/two-sum/submissions/
    """
    
    # Unordered set approach O(n) time
    # Runtime: 60 ms 
    def twoSum(self, nums, target):
        temp = set()
        for i,num in enumerate(nums):
            j = target - num
            if j in temp:
                return [i,nums.index(j)]
            temp.add(num)
    
    # Two pointer technique Time O(nlog(n))
    # Runtime: 68 ms
    def twoSum2(self, numl, target):
        # Time O(nlog(n))
        # This is done to keep track of old indexes after sorting numl
        # Format of tuples in nums is [(oldIndex,value),...]
        nums = sorted(enumerate(numl),key= lambda i:i[1])
        
        i = 0
        j = len(nums)-1
        
        # Time O(n)
        while(i<j):
            
            temp = nums[i][1]+nums[j][1]
            
            if temp==target:
                return [nums[i][0],nums[j][0]]
            elif target>temp:
                i+=1
            else:
                j-=1
    
    # All pair sums in a given list Mtehod 1 modification
    def twoSum(self, nums, target):
        temp = set()
        pairs = []
        for i,num in enumerate(nums):
            j = target - num
            if j in temp:
                pairs.append([i,nums.index(j)])
            temp.add(num)
        return pairs
                
print(Solution().twoSum([2,7,5,4],9))
# print(Solution().twoSum2([3,2,4],6))
# print(Solution().twoSum2([7,7,11,15],14))
# print(Solution().twoSum([2,9,11,15],9))