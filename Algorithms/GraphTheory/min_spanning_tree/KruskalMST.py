"""
Kruskal algo for finding Minimum Spanning tree.
1. Sort edges in increasing order.
2. pick the smallest edge. check if it forms a cycle. If not, 
   add it to the result. Else discard.
3. repeat step 2 until there are V - 1 edges. V = num of vertices

Time : 
  Sorting : O(ElogE)
  Find and union : atmost O(LogV)
  Overall : O(ElogE + ElogV) = O(ElogE)
  
"""
class KruskalMST:
    parent = {}
    rank = {}
    graph = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
            
        return self.parent[p]
        
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        
        if a == b:
            return 
        
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        elif self.rank[b] > self.rank[a]:
            self.parent[a] = b
        else:
            self.parent[a] = b
            self.rank[a]   += 1
    
    def addEdge(self, frm, to, wgt):
        self.graph.append([frm, to, wgt])
        
    def computeKruskal(self):
        ans = []
        e = 0
        
        for idx in range(self.num_nodes):
            self.parent[idx] = idx
            self.rank[idx]   = 0
                
        self.graph = sorted(self.graph, key = lambda item:item[2])
        print(self.graph)
        
        idx = 0
        while e < self.num_nodes - 1:
            frm, to, wgt = self.graph[idx]
            idx         += 1
            x            = self.find(frm)
            y            = self.find(to)
            
            if x != y:
                #not a cycle
                e += 1
                ans.append([frm, to, wgt])
                self.union(x, y)
        
        minCost = 0
        for edge in ans:
            u, v, w = edge
            minCost += w
            
        print(minCost)
        print(ans)
    

g = KruskalMST(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.computeKruskal()
