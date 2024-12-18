https://leetcode.com/problems/split-array-largest-sum/description/
Redo this Q


================================== Brute forced ===============================
TLE
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ans = float('inf')

        for curr in range(max(nums),sum(nums)+1):
            subs = []
            maxSubSum = float('-inf')

            countSubs = 0
            tmpSubArray = []
            tmpSubArraySum = 0
            for ele in nums:
                if tmpSubArraySum + ele > curr:
                    maxSubSum = max(maxSubSum,tmpSubArraySum)
                    subs.append(tmpSubArray)
                    tmpSubArraySum = 0
                    countSubs += 1
                    tmpSubArray = []
                tmpSubArraySum += ele
                tmpSubArray.append(ele)
                
            if tmpSubArray:
                maxSubSum = max(maxSubSum, tmpSubArraySum)
                subs.append(tmpSubArray)
                countSubs += 1
            
            # print(curr,maxSubSum,countSubs,tmpSubArraySum,subs)

            if countSubs <= k:
                ans = min(ans,maxSubSum)
            
        return ans

================================== Optimized BS ===============================

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        lo = max(nums)
        hi = sum(nums)+1
        while lo<=hi: 
            curr = (lo+hi)//2
            
            subs = []
            maxSubSum = float('-inf')

            countSubs = 0
            tmpSubArray = []
            tmpSubArraySum = 0
            for ele in nums:
                if tmpSubArraySum + ele > curr:
                    maxSubSum = max(maxSubSum,tmpSubArraySum)
                    subs.append(tmpSubArray)
                    tmpSubArraySum = 0
                    countSubs += 1
                    tmpSubArray = []
                tmpSubArraySum += ele
                tmpSubArray.append(ele)
                
            if tmpSubArray:
                maxSubSum = max(maxSubSum, tmpSubArraySum)
                subs.append(tmpSubArray)
                countSubs += 1
            
            # print(curr,maxSubSum,countSubs,tmpSubArraySum,subs)

            if countSubs <= k:
                hi = curr - 1
                ans = min(ans,maxSubSum)
            else: lo = curr+1
            

        return ans
