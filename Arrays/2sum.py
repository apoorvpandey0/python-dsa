Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
https://leetcode.com/problems/two-sum/description/

1. Brute O(n^2)
2. Sort -> BS O(nlogn)
3. Set -> O(n)

Modification
Find all pair values (not indices) whose sum is = target
1. Brute force
2. Sort array then use Two pointers
3. ...
def FindAllPairs(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    l = 0
    r = len(nums)-1
    ans = []
    while l<r:
        sm = nums[l] + nums[r]
        print(l,r,sm)
        if sm==target: 
            ans.append([nums[l],nums[r]])
            l+=1
        elif sm>target: r-=1
        elif sm<target: l+=1
    return ans[0]
