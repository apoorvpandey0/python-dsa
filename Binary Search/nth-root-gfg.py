Same concept as in sqrt,
based on BS on answer space concept
https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		
		start = 1
		end = m
		
		while start<=end:
		    mid = (start+end)//2
		    
		    if mid ** n == m: return mid
          
		    elif mid ** n > m: end = mid -1
		    
        else: start = mid + 1
		return -1

