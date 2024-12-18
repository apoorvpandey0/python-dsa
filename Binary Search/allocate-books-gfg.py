https://www.naukri.com/code360/problems/allocate-books_1090540
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937

# Re learn!


===================== Brute force ====================
TLE
# Validate the entire answers range
class Solution:
    
    def findPages(self, nums, m):

        if m>len(nums): return -1
    
        ans = float('inf')
    
        lo = max(nums)
        hi = sum(nums)
    
        for maxPages in range(lo,hi+1):
            tmpMax = float('-inf')
            tmpSum = 0
            
            tmpK = 1
            for ele in nums:
                if tmpSum + ele > maxPages:
                    tmpMax = max(tmpMax,tmpSum)
                    tmpSum = 0
                    tmpK+=1
                tmpSum+=ele
            
            # print(maxPages,tmpK,tmpSum)

            # idk why not tmpK ==m and the one below
            if tmpK <= m:
                ans = min(ans,maxPages)

        return ans



===================== Optimized BS soln ====================
def findPages(nums: [int], n: int, m: int) -> int:
    if m>n: return -1

    ans = float('inf')

    lo = max(nums)
    hi = sum(nums)

    while lo<=hi:
        maxPages = (lo+hi)//2
        tmpMax = float('-inf')
        tmpSum = 0
        
        tmpK = 1
        for ele in nums:
            if tmpSum + ele > maxPages:
                tmpMax = max(tmpMax,tmpSum)
                tmpSum = 0
                tmpK+=1
            tmpSum+=ele
        
        # print(maxPages,tmpK,tmpSum)
        
        if tmpK<=m: 
            hi = maxPages - 1
            ans = min(ans,maxPages)
        else: 
            lo = maxPages+1
            

    return ans




===================== Extremely basic brute force ====================
Generate all combination of array splits into m parts, and find minM of all maxM sum of subarrays

from itertools import combinations

# TLE on all platforms hopefully correct logic
# Time | Space - 
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, nums, m):

        if m>len(nums): return -1
    
        ans = float('inf')

        # Generate till m-1 combinations because it will give us end index of each subarray
        # If we take m then we will get start of each subarray - complicated subs formation islie do m-1
        combs = combinations([i for i in range(len(nums))],m-1)
    
        subs = []
        for c in combs:
            # print(c)
            tmp = []
            start = 0
            maxM = float('-inf')
            for end in c:
                tmp2 = []
                tmp2Sum = 0
                for i in range(start,end+1):
                    tmp2Sum+=nums[i]
                    tmp2.append(nums[i])
                    start = end + 1
                maxM = max(maxM,tmp2Sum)
                tmp.append(tmp2)

            # To account for IF last subarray getting missed
            if nums[start:]: 
                tmp.append(nums[start:])
                maxM = max(maxM,sum(nums[start:]))
            
            ans = min(ans,maxM)
            if len(tmp) == m: 
                subs.append(tmp)
        return ans
    
