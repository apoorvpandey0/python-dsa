"""
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    Example:    Input: nums = [100,4,200,1,3,2] | Output: 4
                Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution:
    # Time O(n)
    # Runtime: 188 ms, faster than 86.40% of Python3 online submissions for Longest Consecutive Sequence.
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # check if num can be a starting element for a chain
            # If yes then start the chain
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Check until the chain ends
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    # Brute Force approach
    # This isin't brute forced solution
    # Time O(n2)
    # Runtime: 2724 ms, faster than 7.73% of Python3 online submissions for Longest Consecutive Sequence.

    def longestConsecutive1(self, nums):
        myset = set(nums)
        answer = 0
        for i in range(len(nums)):
            counter = 0
            # print(i,answer)
            if nums[i] - 1 not in myset:
                counter = 1
                temp = nums[i]
                while temp + 1 in myset:
                    counter += 1
                    temp += 1
            if counter > answer:
                answer = counter
        return answer


print(Solution().longestConsecutive([100, 4, 200, 0, 1, 3, 2]))  # 5
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 0, 8, 4, 6, 1]))  # 9
print(Solution().longestConsecutive([1, 2, 0, 1]))  # 3
