"""
    Find the number of connected components in a Graph
    Link: https://practice.geeksforgeeks.org/problems/number-of-provinces/1/
"""

class Solution:

    # DFS approach
    # Time: O(n^2) | Space: O(V+E)
    def soln1(self, M, N):
        
        # Phase 01: Preparing graph
        
        # For Adjacency Matrix -> Adjacency list conversion
        N = len(M)
        lst = { row:set() for row in range(N) }
        for row in range(N):
            for col in range(N):
                if M[row][col]:
                    if row!=col:
                        lst[row].add(col)
        visited = set()
        
        # Phase 2: Actual work
        
        # Regular DFS logic
        def dfs(at):
            if at in visited:return
            visited.add(at)
            for nxt in lst[at]:
                dfs(nxt)
        
        # Visit each node and mark all its neighbours as visited
        # If you visit a node which is not yet marked that means its must be a new component hence count+=1
        count = 0
        for i in lst:
            if i not in visited:
                count+=1
                dfs(i)
        return count