
Variable length sliding window
If found a match add to ans and shrink the window else keep expanding
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counts = {"a":0,"b":0,"c":0}
        l = 0
        ans = 0

        for r in range(n):
            counts[s[r]]+=1

            while counts['a'] and counts['b'] and counts['c'] :
                ans += n-r
                counts[s[l]] -= 1
                l+=1
        return ans
