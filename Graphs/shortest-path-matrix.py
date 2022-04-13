"""
    Unsolved
"""
from typing import List
from collections import deque

class Solution:
    # Runtime: 654 ms, faster than 87.13% of Python3 online submissions for Shortest Path in Binary Matrix.
    # Memory Usage: 14.2 MB, less than 96.35% of Python3 online submissions for Shortest Path in Binary Matrix.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def valid(r,c):
            """Returns if a given position is within the matrix of not."""
            if r<0 or c<0 or r>rows-1 or c>cols-1: return False
            else: return True
        
        rows = len(grid)
        cols = len(grid[0])
        
        # Edge case if first element itself is not accessible
        if grid[0][0] !=0 or grid[rows-1][cols-1]: return -1
        

        
        q = deque([(0,0,1)])
        grid[0][0] = 2
        
        # (row, col) or (dy, dx)
        dirs = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))

        # While there are still nodes left in the matrix to be explored
        while q:

            # Take first node
            r,c,lvl= q.popleft()

            # if this is the end node return lvl
            if r ==rows-1 and c == cols-1: return lvl

            # else add all its eligible neighbours to the queue
            for dy,dx in dirs:
                nr = r + dy
                nc = c + dx

                if not valid(nr,nc):continue

                if grid[nr][nc] >0: continue

                grid[nr][nc] = 2
                q.append((nr,nc,lvl+1))
        return -1

class Solution2:
    # Concise python code
    # Runtime: 569 ms, faster than 97.81% of Python3 online submissions for Shortest Path in Binary Matrix.
    # Memory Usage: 14.8 MB, less than 54.35% of Python3 online submissions for Shortest Path in Binary Matrix.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Edge case for when it is the first or last element of matrix
        if grid[0][0] or grid[n-1][n-1]: return -1

        # Initialize queue and start from first element
        q = [(0, 0, 1)]
        grid[0][0] = 1

        """
            Since queue size will increase the loop will adjust to run through all the elements
            The following is an infinite loop
            a = [1]
            for i in a:
                a.append(i)
        """
        for i, j, d in q:

            # if this is the end node return lvl
            if i == n-1 and j == n-1: return d

            # else add all its eligible neighbours to the queue
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1