https://www.naukri.com/code360/problems/allocate-books_1090540
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937



===================== Brute force ====================





===================== Optimized BS soln ====================





===================== Extremely basic brute force ====================
Generate all combination of array splits into m parts, and find minM of all maxM sum of subarrays

from itertools import combinations
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, nums, m):

        if m>len(nums): return -1
    
        ans = float('inf')
    
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
            
            if nums[start:]: 
                tmp.append(nums[start:])
                maxM = max(maxM,sum(nums[start:]))
            
            ans = min(ans,maxM)
            if len(tmp) == m: 
                subs.append(tmp)
        return ans
    
