https://www.naukri.com/code360/problems/aggressive-cows_1082559

# TODO: add time complexities



======================================== Solution 1 - Brute force =================================

# Find all combinations and then find the max of all minimum distances in each combination

from itertools import combinations
def aggressiveCows1(stalls, c):

    stalls.sort()

    all_combinations = combinations(stalls, c)

    max_min_distance = 0

    # Check each combination
    for combination in all_combinations:
        
        # Calculate the minimum distance between consecutive stalls
        min_distance = float('inf')
        for i in range(1, len(combination)):
            min_distance = min(min_distance, combination[i] - combination[i - 1])

        # Update the maximum of the minimum distances
        max_min_distance = max(max_min_distance, min_distance)

    return max_min_distance



======================================== Solution 2 - Better Brute force =================================

""" 
    Its not that difficult to maximize the minimum distance between any two cows
    Minimum distance between any two cows can be in the range of 1 -> farthest barn position - closest barn position
    Iterate over the above range and Validate that can we place all C cows maintaining the minimum
    If so then take the maximum of all those minimum distances, and here's your answer
"""
def aggressiveCows(nums, c):
    nums.sort()
    ans = -1
    
    for minM in range(1,max(nums)-min(nums)+1):

        # Since first cow is already set in barn with index 0 
        k = c - 1
        prevCow = 0
        # placed = [nums[0]]

        # Validating if all cows can be accomodated in the choosen minM
        # Since first index barn is fixed hence starting from 1 -> last barn's index
        for i in range(1,len(nums)):
            if nums[i] - nums[prevCow] >= minM:
                prevCow = i
                k-=1
                # placed = nums[i]
        
        # print(k,minM,placed)
        
        if k<=0:    
            ans = max(ans,minM)

    return ans


======================================== Solution 3 - Optimized solution =================================

Just added binary search to above logic
def aggressiveCows(nums, c):
    nums.sort()
    ans = -1
    lo = 1
    hi = max(nums)-min(nums)
    while lo<=hi:
        minM = (lo+hi)//2

        k = c - 1
        prevCow = 0
        for i in range(1,len(nums)):
            if nums[i] - nums[prevCow] >= minM:
                prevCow = i
                k-=1
                
        if k<=0:    
            ans = max(ans,minM)
            lo = minM + 1
        else:
            hi = minM - 1

    return ans



























