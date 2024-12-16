https://www.naukri.com/code360/problems/aggressive-cows_1082559



from itertools import combinations

# Solution 1 - Brute forced
Find all combinations and then find the max of all minimum distances in each combination
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
