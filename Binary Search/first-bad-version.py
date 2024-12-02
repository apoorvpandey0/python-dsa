# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n

        while lo < hi:
            mid = (lo+hi)//2

            if isBadVersion(mid):
                hi = mid
            
            else: lo = mid+1

        return lo


or

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n

        while lo < hi:
            mid = (lo+hi)//2

            if not isBadVersion(mid):
                lo = mid+1
            
            else: hi = mid

        return lo
