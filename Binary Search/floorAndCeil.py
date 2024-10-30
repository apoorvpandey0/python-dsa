https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=PROBLEM
Find Floor and Ceil of a number in a given sorted array,
Alternative qs: upper and lower bound qs on GFG

def getFloorAndCeil(a, n, x):
    # Write your code here.
    n = len(a)
    floor, ceiling = -1, -1
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] == x:
            return a[mid], a[mid]  # x is both its own floor and ceiling
        
        elif a[mid] < x:
            floor = a[mid]  # potential floor found, move right
            left = mid + 1
        
        else:
            ceiling = a[mid]  # potential ceiling found, move left
            right = mid - 1

    return floor, ceiling
