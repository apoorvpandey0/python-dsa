from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        print(s, t)
        a = set(s)
        b = Counter(t)
        window = set()
        start = 0
        end = 0
        # print(a)
        # print(b)
        # print(b.issubset(a))
        while end < len(s):
            if s[end] in window:
                end+=1
            else:
                window.add(s[end])
        print(s[start:end+1])
        
        # Starting index cleaner
        for i in range(len(s[start:end+1])):
            if s[i] not in b:
                start+=1
            else:
                break

        # print(window,s[start:end+1])
        return s[start:end+1]


# print(Solution().minWindow("hello","elo"))


# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# print(Solution().minWindow("ADOBECODEBANC","ABC"))
print(Solution().minWindow("ABAACBAB","ABC"))

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# print(Solution().minWindow("a","a"))

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# print(Solution().minWindow("a","aa"))