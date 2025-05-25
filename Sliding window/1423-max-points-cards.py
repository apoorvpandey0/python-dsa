class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ps = [0 for i in range(n)]
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = nums[i] + ps[i-1]

        minM = float('inf')
        ws = n - k
        # re visit this logic
        for j in range(ws-1,len(nums)):
            i = j - ws + 1
            subSum = ps[j] - (ps[i - 1] if i > 0 else 0)
            minM = min(minM,subSum)

        return sum(nums) - minM
