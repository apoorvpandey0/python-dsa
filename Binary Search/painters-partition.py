https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557?leftPanelTabValue=PROBLEM


same funda as in capacity of ships, book allocation, split array
def findLargestMinDistance(nums:list, k:int):
    lo = max(nums)
    hi = sum(nums)
    ans = float('inf')

    while lo<=hi:
        mid = (lo+hi)//2

        paintersRequired = 1
        tmpSum = 0

        for i in range(len(nums)):
            tmpSum+=nums[i]
            if tmpSum > mid:
                paintersRequired+=1
                tmpSum = nums[i]
        
        if paintersRequired > k:
            lo = mid + 1
        else:
            hi = mid - 1
            ans = min(mid,ans)
    return ans
