class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        ans = 0
        counter = {}
        for j in range(len(s)):
            if s[j] in counter:
                counter[s[j]]+=1
            else:
                counter[s[j]] = 1
            
            while (j - i + 1) - max(counter.values()) > k:
                counter[s[i]] -= 1
                i += 1
            ans = max(ans,j-i+1) 
        return ans
