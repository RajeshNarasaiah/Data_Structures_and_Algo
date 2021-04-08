"""
Single source shortest path using Bellman-Ford algo.

-ve edges okay but will not work on -ve wgt cycles.

Algo:
1. Create array of size V (num_nodes) and initialize all values to inf except src = 0.
2. Perform edge relaxation V - 1 times.
3. for every edge in the grapph, try performing edge relaxation one more time.
   if edge relaxation possible, then graph has -ve cycles.
   
"""

class Bellman_Ford:
    graph = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        
    def addEdge(self, u , v, w):
        self.graph.append([u, v, w])
        
    def BFUtil(self, src):
        dist = [float('inf')] * self.num_nodes
        dist[src] = 0
        
        for _ in range(self.num_nodes - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print('graph has -ve cycles')
                return
            
        print(dist)
        
        
g = Bellman_Ford(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
# Print the solution 
g.BFUtil(0)
                
        
