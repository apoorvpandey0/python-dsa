class Solution:
    """
        Given a string s, find the length of the longest substring without repeating characters.
        Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    
    # Sliding window solution
    # Time O(n)
    # Runtime: 84 ms, faster than 34.23% of Python3 online submissions for Longest Substring Without Repeating Characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start = 0
        end = 0
        count = 0
        max_count = 0
        while end<len(s):

            # We are not clearing dictionary so checking if the index of the element is at least after start index
            if s[end] in dict and dict[s[end]]>=start:
                start+=1
                count -=1
            else:
                dict[s[end]] = end
                end+=1
                count+=1
            max_count = max(max_count,count)
        return max_count

print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
