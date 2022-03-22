"""
    Time taken to burn a binary tree
    Link: https://practice.geeksforgeeks.org/problems/burning-tree/1#
"""

#User function Template for python3
from collections import deque
class Solution:
    target = 0
    def minTime(self, root,target):
        
        # Finding the node with target value
        def pot(node):
            if not node: return
            if target == node.data: self.target = node 
            pot(node.left)
            pot(node.right)
        pot(root)
        
        # Create a hash table to store each node's parent using DFS.
        # Doing this will convert the problem to more of a graph problem.
        hashtable = {}  
        res = []
        def dfs(node, parent):
            if not node:
                return
            hashtable[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)   
            
        dfs(root, None) 
        
        # Once we have an adacency list (hash table), run a simple bfs search like any other graph problem
        q = deque([(self.target, 0)])
        visit = set()
        visit.add(self.target)
        time = 0
        while q:
            time = max(q[0][1],time)    
            # BFS
            node, level = q.popleft()
            for nei in [node.left, node.right, hashtable[node]]:
                if nei and nei not in visit:
                    q.append((nei, level + 1))
                    visit.add(nei)
                    
        return time