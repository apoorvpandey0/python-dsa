"""
    Island finder
    Desc: Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.
            An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
            You may assume all four edges of the grid are all surrounded by water.     
    Link: https://leetcode.com/problems/number-of-islands/submissions/
"""

from typing import List

# Runtime: 349 ms, faster than 75.07% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.5 MB, less than 63.55% of Python3 online submissions for Number of Islands.
class Solution:
    # When you land on a 1, mark the entire island as visited using DFS and increment the island count by 1
    def soln1(self, grid: List[List[str]]) -> int:

        def dfs(r,c,rows,cols):
            # print("Called",r,c)
        
            # Boundary conditions
            if r<0 or c<0 or r>rows-1 or c>cols-1:return
            
            # Mark the element as visited
            grid[r][c] = '2'

            
            # Top element
            if r-1>=0 and grid[r-1][c] == '1': dfs(r-1,c,rows,cols)

            # Down element
            if r+1<rows and grid[r+1][c] == '1': dfs(r+1,c,rows,cols)

            # Left element
            if c-1>=0 and grid[r][c-1] == '1': dfs(r,c-1,rows,cols)

            # Right element    
            if c+1<cols and grid[r][c+1] == '1': dfs(r,c+1,rows,cols)

        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # Go to each unvisited element and call dfs
        # dfs will mark the entire island connected with that element as visited
        # hence we can safely increase the island count by 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =='1':
                    islands+=1 
                    dfs(r,c,rows,cols)
                    # print(grid)
                
        return islands
                    