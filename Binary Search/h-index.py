https://leetcode.com/problems/h-index-ii/solutions/6492651/binary-search-on-sorted-citations-100-beat/?envType=study-plan-v2&envId=binary-search


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations) - 1
        
        while start <= end:
            mid = (start+end)//2
            if len(citations) - mid == citations[mid]:
                return citations[mid]
            elif len(citations) - mid > citations[mid]:
                start = mid+1
            else:
                end = mid-1
        
        return len(citations) - start
