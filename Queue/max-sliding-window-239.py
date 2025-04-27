import heapq
from collections import deque
# using Monotonically decreasing Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        
        for i, curr_val in enumerate(nums):
            # remove all those elements in the queue
            # which are smaller than the current element
            # this should maintain that the largest element
            # in a window would be at the beginning of the
            # queue
            while queue and nums[queue[-1]] <= curr_val:
                queue.pop()
            
            # add the index of the
            # current element always
            queue.append(i)
            
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
            
            # simple check to ensure that we
            # take into account the max element
            # only when the window is of size >= k
            # and since we're starting with an empty
            # queue, we'll initially have a window
            # of size 1,2,3....k-1 which are not valid
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
