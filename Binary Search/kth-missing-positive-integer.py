https://leetcode.com/problems/kth-missing-positive-number/


# Time and space O(N)
class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        st = set(nums)
        ans = None
        for i in range(1,max(nums)+k+1):
            if i not in st: 
                ans = i
                k-=1
            if k == 0: break
        return ans



# O(LOG N ) solution ...
The missing number can be 1. Inside the array or 2. Outside the array
This solution makes current array as answer space
Find lowest and highest bounds between which the kth missing number should be
We will always use lower bound, calculate missing numbers before it and add the difference to lower bound 
This solves for both cases 1 and 2
In Binary search impl, hi stores lower bound and lo stores higher bound of k
class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        lo = 0
        hi = len(nums)-1
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2

            # Check how many missing numbers are before mid and adjust lo and hi
            if nums[mid] - (mid + 1)<k:
                lo = mid + 1
            else: hi = mid - 1

        # add the remaining missing numbers to lower bound
        return nums[hi] + k -(nums[hi] - (hi + 1))
        
