"""
    Find all nodes at distance k from a given node.
    Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque

class Solution:
    # Runtime: 47 ms, faster than 65.42% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    # Memory Usage: 14.2 MB, less than 82.69% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
            Levels here are like Onion peels around target node and not like in traversal.
            Ex: 
                              20
                            /    \
                           8      22 
                          /   \
                         4    12 
                             /   \
                            10    14
                Target = 8, k = 2
                Level 0: 8
                Level 1: 4, 12, 20
                Level 2: 10, 14, 22
        
            Trees here are Directed,Acyclic and connected graphs.
            So we need to make them Sort of undirected that is done in PART 1, where we keep track of parents of each node.
            And then treat the tree as a graph and do BFS in PART 2.
        """
        
        # PART 1:
        # Create a hash table to store each node's parent using DFS.
        # Doing this will convert the problem to more of a graph problem.
        # This way we can track parent of each node
        hashtable = {}  
        res = []
        def dfs(node, parent):
            if not node:
                return
            hashtable[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)   
            
        dfs(root, None) 
        

        # PART 2:
        # Once we have an adacency list (hash table), run a simple bfs search like any other graph problem
        q = deque([(target, 0)])
        visit = set()
        visit.add(target)
        while q:
            # Check if the leftmost value in queue has level == k. If so, return all values in q.
            # We will only have one level of nodes in the queue at a time.
            if q[0][1] == k:
                for node, level in q:
                    res.append(node.val)
                return res
            
            # BFS
            node, level = q.popleft()
            for nei in [node.left, node.right, hashtable[node]]:
                if nei and nei not in visit:
                    q.append((nei, level + 1))
                    visit.add(nei)
                    
        return res