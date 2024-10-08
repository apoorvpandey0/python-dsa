"""
    Rotate 1D array by k positions clockwise
    Link: https://leetcode.com/problems/rotate-array/
    https://leetcode.com/problems/rotate-array/solutions/5550096/video-using-remainder-with-3-solutions
"""


# While reversing any subarray, us array ke mid tak he reverse karna hai, else wo array wapas unreversed ho jayega
# start and end are indices of the array
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums

def reverseWithForLoop(l,r,nums):
    for i in range(l,(r-l)//2):
        tmp = nums[r-i]
        nums[r-i] = nums[i]
        nums[i] = tmp
    print(nums)
    
# print(reverse([1, 2, 3, 4, 5, 6, 7, 8], 3, 6))


# Solution 1:
# Runtime: 204 ms, faster than 97.60% of Python3 online submissions for Rotate Array.
def sol1(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


# Solution 2:
# Using reversing method
# Runtime: 228 ms, faster than 74.00% of Python3 online submissions for Rotate Array.
def sol2(nums, k):
    """
        Reverse nums[:n-k]
        Reverse nums[n-k:]
        Reverse nums
    """
    k = k % len(nums)
    n = len(nums)

    nums[:n - k] = reverse(nums[:n - k], 0, n - k - 1)
    nums[n - k:] = reverse(nums[n - k:], 0, k - 1)
    nums[:] = reverse(nums, 0, n - 1)
    return nums

def sol21(self, nums: List[int], k: int) -> None:
        """
        Same as sol 2, in place
        """
        def rev(l,r,nums):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
            return nums
        
        N = len(nums)-1
        k %= N+1
        # Nums is passed by reference in python
        r1 = rev(0,N-k,nums)
        r2 = rev(N-k+1,N,r1)
        r3 = rev(0,N,r2)
        return nums

def sol3(self, nums: List[int], k: int) -> None:
    """
    This is not an in place solution
    """
    N = len(nums)
    ans = [None for i in range(N)]
    for i in range(N):
        ans[ (i+k) % N ] = nums[i]
    return ans


print(r3(nums=[1, 2, 3, 4, 5, 6, 7], k=0))
# print(
#     r2([
#         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
#         39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53
#     ],
#        k=82))
