https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824

An efficient solution is based on the observation that this problem reduces to finding a maximum sum of two consecutive elements in array. If (x,y) is the pair such that (x+y) is the answer, then x and y must be consecutive elements in the array.

class Solution:
    def pairWithMaxSum(self, arr):
        ans = float('-inf')
        for i in range(1,len(arr)):
            ans = max(ans,arr[i]+arr[i-1])
        return ans
