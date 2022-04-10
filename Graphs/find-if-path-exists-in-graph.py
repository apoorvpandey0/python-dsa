"""
    Find path if exists in graph 
    Return True/False
    Link: https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/
    Soln: https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/1473226/Python-DFS-and-UnionFind-and-BFS-with-explanation
"""

from typing import List

class Solution:
    def edgeToList(self,edges):
        """For edge list -> adjacency list conversion"""
        graph = dict()
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = set()
            if edge[1] not in graph:
                graph[edge[1]] = set()

            graph[edge[0]].add(edge[1])   
            graph[edge[1]].add(edge[0])   

        return graph

    # DFS Solution - Slow
    answer = False
    def soln1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
            Runtime: 3402 ms, faster than 16.77% of Python3 online submissions for Find if Path Exists in Graph.
            Memory Usage: 337.1 MB, less than 5.02% of Python3 online submissions for Find if Path Exists in Graph.
        """
        if source == destination:return True
        edges = self.edgeToList(edges)
        
        visited = set()
        self.answer = False
        def dfs(at):
            if at in visited:return
            
            # Using the class variable update the answer variable
            if at == destination: 
                self.answer = True
                return
            
            visited.add(at)
            
            for nxt in edges[at]:
                dfs(nxt)
        dfs(source)
        return self.answer

    # BFS Solution - better
    def soln2(self, n: int, edges: List[List[int]], start: int, destination: int) -> bool:
        """
            Runtime: 2700 ms, faster than 47.80% of Python3 online submissions for Find if Path Exists in Graph.
            Memory Usage: 120.8 MB, less than 28.64% of Python3 online submissions for Find if Path Exists in Graph.
        """
        q = [start]
        
        # Making adjacency list out of given edge list
        graph = {}
        for vertex in range(n):
            graph[vertex] = set()
        
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        visited = set()
        
        # BFS logic
        while q:
            node = q.pop()
            if node in visited:continue

            # Add all children of current layer to the queue
            q.extend(graph[node])
            visited.add(node)
            
            # If found return True
            if node == destination:
                return True
        
        return False
    
    # Union method
    def soln3(self, n: int, edges: List[List[int]], start: int, destination: int) -> bool:
        pass









