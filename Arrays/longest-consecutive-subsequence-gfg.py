https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

#Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,nums):
        ans = 0
        tmp = 1
        s = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            if nums[i] - nums[i-1] == 1: # Check consecutive
                tmp+=1
            else:
                # capturing starting index
                s = i
                # reset to 1 because elemenet in itself is a subsequence with length = 1
                tmp = 1
            ans = max(tmp,ans)
        return ans
