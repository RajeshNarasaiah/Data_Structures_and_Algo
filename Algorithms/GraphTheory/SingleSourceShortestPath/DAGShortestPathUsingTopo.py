from collections import defaultdict

class DAGShortestPath:
    graph = defaultdict(list)
    topo_order = []
    visited = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.visited = [False] * self.num_nodes
        self.dist = [float('inf')] * self.num_nodes
        
    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        
    def dfs(self, vtx):
        if self.visited[vtx] == False:
            self.visited[vtx] = True
            
            for neighbor in self.graph[vtx]:
                if self.visited[neighbor[0]] == False:
                    self.dfs(neighbor[0])
                
            self.topo_order.append(vtx)
            
            
    def topo(self,src):
        self.dfs(src)
        self.topo_order = self.topo_order[::-1]
        
    def ShortestPath(self, src):
        dist = [float('inf')] * self.num_nodes
        dist[src] = 0
        
        for vtx in self.topo_order:
            for node, wgt in self.graph[vtx]:
                if dist[node] > dist[vtx] + wgt:
                    dist[node] = dist[vtx] + wgt
                    
        print(dist)
        
g = DAGShortestPath(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
        
print(g.graph)
print(g.visited)
g.topo(1)
print(g.topo_order)
g.ShortestPath(1)
