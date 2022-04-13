graph = [
    [1,4],
    [2,4],
    [1,3],
    [2,4],
    [1,3]
]

class Solution:
    counter=0
    visited = set()
    def isCycle(self, V, adj):
        self.counter = 0
        self.visited = set()
        print(adj)
        def cycledfs(curr,par):
            print('Running ',curr,par,self.visited)
            if curr in self.visited and curr!=par: 
                self.counter+=1
                print('Found',curr,par)
                return
            if curr in self.visited: return
            
            self.visited.add(curr)
            
            print(adj[curr])
            for nxt in adj[curr]:
                
                if nxt!=curr and nxt!=par:
                    cycledfs(nxt,curr)
        
            
        
        for i in range(V):
            # print(i,self.visited)
            if i not in self.visited:
                cycledfs(i,-1)
                
        print(self.counter)
        return False
print(Solution().isCycle(5,graph))