"""
    Find numbere of provinces
    Or find number of commected components in a graph given as Adjacency Matrix
    Link: https://leetcode.com/problems/number-of-provinces/submissions/
"""

from typing import List

class Solution:
    visited = set()

    # DFS Implementation
    # Ideal Time: O(V+E) | Space: O(V)
    # This code Time: O(V+E) | Space: O(V^2)
    # 1. Visit each node, if node is not visited then call dfs on that node
    # 2. This will mark the entire component connected with that node
    def findCircleNum(self, mat: List[List[int]]) -> int:
        """
            Runtime: 204 ms, faster than 86.82% of Python3 online submissions for Number of Provinces.
            Memory Usage: 15 MB, less than 13.14% of Python3 online submissions for Number of Provinces.
        """
        self.visited = set()

        def matrixToList(M):
            """For Adjacency Matrix -> Adjacency list conversion"""
            N = len(M)
            lst = { row:set() for row in range(N) }
            for row in range(N):
                for col in range(N):
                    if M[row][col]:
                        lst[row].add(col)
            return lst
        
        lst = matrixToList(mat)
        
        def dfs(node,lst):
            if node in self.visited: return
            self.visited.add(node)
            for nxt in lst[node]:
                dfs(nxt,lst)
        
        counter = 0
        for n in range(len(lst)):
            if n not in self.visited:
                counter+=1
                dfs(n,lst)
        return counter
        
  