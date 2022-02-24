"""
    Find the maximum elements amongst sliding windows of size k.
    Gfg link: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
    LC Link: https://leetcode.com/problems/sliding-window-maximum/
    Soln: https://www.youtube.com/watch?v=LiSdD3ljCIE , https://algo.monster/problems/sliding_window_maximum
"""
import heapq
from collections import deque
from typing import List

# Solution 1:
# Brute forced
# Time: O(nk) | Space: O(1) - TLE not accepted on LC
def msw(nums,k):       
    n = len(nums)
    ans = []
    for i in range(n-k+1):
        ans.append(max(nums[i:i+k]))
    return ans

# Solution 2
# Using BST or Heap
# Time: O(nlogk) | Space: O(k)

# Solution 3:
# Using DLL or Deque
# Time: O(n)| Space: O(k)
# Algorithm:
# 1. Pop the front of Queue if its index is outside the window
# 2. Maintain the Queue in Descending order
# 3. Append urrent node to the Queue
# 4. Include max of current window (i>k-1)
# Runtime: 2480 ms, faster than 51.29% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 30.6 MB, less than 21.68% of Python3 online submissions for Sliding Window Maximum.
class Solution:
    """
       Soln:  https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # this deque will hold the 
        # index of the max element
        # in a sliding window
        queue = deque()
        res = []
        
        for i, curr_val in enumerate(nums):

            # Step 2:
            # remove all those elements in the queue
            # which are smaller than the current element
            # this should maintain that the largest element
            # in a window would be at the beginning of the
            # queue
            while queue and nums[queue[-1]] <= curr_val:
                queue.pop()
            
            # Step 3:
            # add the index of the
            # current element always
            queue.append(i)
            
            # Step 1
            # check if the first element in the queue
            # is still within the bounds of the window
            # i.e. the current index - k, if not
            # remove it (popleft)
            # 
            # here, storing the index instead of the
            # element itself becomes apparent, since
            # we're going linearly, we can check the
            # index of the first element in the queue
            # to see if it's within the current window
            # or not
            if queue[0] == i-k:
                queue.popleft()
            
            # Step 4:
            # simple check to ensure that we
            # take into account the max element
            # only when the window is of size >= k
            # and since we're starting with an empty
            # queue, we'll initially have a window
            # of size 1,2,3....k-1 which are not valid
            if i >= k-1:
                res.append(nums[queue[0]])
            
        return res
# print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
print(Solution().maxSlidingWindow([1,-1],1))
# Solution 3:
# Sliding window
# Time: O(n) | Space: O(k)                   