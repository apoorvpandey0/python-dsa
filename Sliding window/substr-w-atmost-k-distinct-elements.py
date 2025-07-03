# https://www.naukri.com/code360/problems/distinct-characters_2221410?leftPanelTabValue=PROBLEM

from collections import defaultdict
def kDistinctChars(k, nums):
    freq = defaultdict(int)
    i = 0
    ans = 0
    
    for j in range(len(nums)):
        freq[nums[j]] += 1
        
        while len(freq) > k:
            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
            i += 1
        
        ans = max(ans, j - i + 1)
    
    return ans
