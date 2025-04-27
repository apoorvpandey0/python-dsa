# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastO = {}
        ans = 0
        i = 0
        
        for j in range(len(s)):
            # if current element is seen move i to next element    
            if s[j] in lastO:

                # in case "abba" when j reaches last "a"
                # last a will already be seen, in this case we should not move i backwards
                # hence we will use max of i, lastOccurrence of jth element
                i = max(i,lastO[s[j]] + 1)
            
            # in every case update lastO of each element with j
            lastO[s[j]] = j
            
            ans = max(ans,j-i+1)
            
        return ans


        
