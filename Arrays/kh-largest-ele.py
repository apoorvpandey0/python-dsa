import heapq


# Create heap: O(n) time
# Push/Pop in the heap: O(log(n)) time
# Overall timefor this solution : n + n + k*log(n)
# Runtime: 70 ms, faster than 63.50% of Python3 online submissions for Kth Largest Element in an Array.
def kle(nums, k):
    nums = [-1 * i for i in nums]
    h = heapq.heapify(nums)
    answer = False
    while k:
        answer = heapq.heappop(nums) * -1
        k -= 1
    return answer


print(kle([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(kle([3, 2, 1, 5, 6, 4], 2))
