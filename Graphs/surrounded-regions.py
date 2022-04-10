"""
    Capture all surrounded regions
    Desc: Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. 
            A region is captured by flipping all 'O's into 'X's in that surrounded region.
    Link: https://leetcode.com/problems/surrounded-regions/

"""

from typing import List
class Solution1:
    """
        This is two step DFS method
        1. Find all the regions that are surrounded
        2. Run another DFS to mark the region
    """
    visited = []
    surrounded = True
    
    # Time: O(MN) | Space: O(MN) 
    def solve(self, mat: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
            Runtime: 296 ms, faster than 17.92% of Python3 online submissions for Surrounded Regions.
            Memory Usage: 57.9 MB, less than 8.98% of Python3 online submissions for Surrounded Regions.
        """
        
        # surrounded  = True will mean the region is surrounded and should be marked as 'X'
        self.surrounded = True
        rows = len(mat)
        cols  = len(mat[0])
        self.visited = [[False]*cols for i in range(rows)]
        
        
        # Top, Bottom left right
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
        

        # Checks if given (r,c) lie inside the given 2D matrix
        def valid(r,c):
            if r>=0 and c>=0 and r<rows and c<cols:return True
            else: return False
        
        # Checks if the given (r,c) lie on the boundary of the matrix
        def isboundary(r,c):
            return r<=0 or c<=0 or r>=rows-1 or c>=cols-1 
        
        def dfs(r,c):
            
            # If point is outside matrix -> return
            if not valid(r,c):return
            
            # If point is X or is already visited -> return
            if mat[r][c] =='X' or self.visited[r][c]: return

            # If the point is O and is on boundary that means this region is not surrounded
            # hence we should skip marking it
            if mat[r][c] == 'O' and isboundary(r,c):
                self.surrounded = False
            
            # Mark the point as visited       
            self.visited[r][c] = True
            
            # Visit all the neighbours
            for dy,dx in dirs:
                nr = r + dy
                nc = c + dx
                dfs(nr,nc)
            
        # This function will visit all O neighbours and mark them as X
        # This fn will always be called on a sourrounded region
        def mark(r,c):
            
            # If point is outside matrix -> return
            if not valid(r,c):return
            
            # If point is X -> return
            if mat[r][c] =='X': return
            
            # Mark the point as X
            mat[r][c] = 'X'

            # Visit all the neighbours
            for dy,dx in dirs:
                nr = r + dy
                nc = c + dx
                mark(nr,nc)
        
        # For each point in the matrix excluding the boundary points
        for r in range(1,rows-1):
            for c in range(1,cols-1):

                # For each potential region mark surrounded as False 
                # Meaning this region is not surrounded
                self.surrounded = True

                # If point is O and is not visited run DFS
                if not self.visited[r][c] and mat[r][c]=='O':
                    dfs(r,c)
                    if self.surrounded:
                        mark(r,c)

class Solution2: 
    """
        One Step DFS Solution
        1. Start from the boundary 'O' and mark their regions as 'B'
        2. Run a for loop over matrix and 
            if we see 'B' convert back to 'O'
            if we see 'O' convert it to 'X'
    """
    visited = []
    surrounded = True

    # Time: O(MN) | Space: O(MN)    
    def solve(self, mat: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
            Runtime: 233 ms, faster than 37.19% of Python3 online submissions for Surrounded Regions.
            Memory Usage: 16.4 MB, less than 26.56% of Python3 online submissions for Surrounded Regions.
        """
        
        # surrounded  = True will mean the region is surrounded and should be marked as 'X'
        self.surrounded = True
        rows = len(mat)
        cols  = len(mat[0])
        self.visited = [[False]*cols for i in range(rows)]
        
        
        # Top, Bottom left right
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
        
        # Checks if given (r,c) lie inside the given 2D matrix
        def valid(r,c):
            if r>=0 and c>=0 and r<rows and c<cols:return True
            else: return False
        
        def dfs(r,c):
            
            # BASIC CHECKS
            # If point is outside matrix -> return
            if not valid(r,c):return
            
            # If point is X or is already visited -> return
            if mat[r][c] =='X' or self.visited[r][c]: return

            # CORE IDEA
            if mat[r][c] == 'O': mat[r][c] = 'B'
            
            # Mark the point as visited       
            self.visited[r][c] = True
            
            # Visit all the neighbours
            for dy,dx in dirs:
                nr = r + dy
                nc = c + dx
                dfs(nr,nc)
        
        
        # Run on both vertical boundaries where c = 0 and c = cols-1
        for r in range(rows):
            if not self.visited[r][0] and mat[r][0]=='O':
                dfs(r,0)
            if not self.visited[r][cols-1] and mat[r][cols-1]=='O':
                dfs(r,cols-1)

        # Run on both horizontal boundaries where r = 0 and r = rows-1
        for c in range(cols):
            if not self.visited[0][c] and mat[0][c]=='O':
                dfs(0,c)
            if not self.visited[rows-1][c] and mat[rows-1][c]=='O':
                dfs(rows-1,c)

        # Visit each node in matrix and change it accordingly    
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 'O': mat[r][c] = 'X'
                elif mat[r][c] == 'B': mat[r][c] = 'O'


    