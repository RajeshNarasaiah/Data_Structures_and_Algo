from collections import defaultdict
import heapq

"""
Single source shortest path with Dijkstra.

- Doesn't work with -ve weight edges.

Algo:
 - relax vertices starting from source until all vertices are reached.
 
Time: O(ElogV)
"""
class Dijkstra:
    graph = defaultdict(list)
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        
    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        
    def dijkstraUtil(self, src):
        pq = []
        done = [False] * self.num_nodes
        parent = [-1] * self.num_nodes
        dist = [float('inf')] * self.num_nodes
        
        heapq.heapify(pq)
        heapq.heappush(pq, [0, src])
        dist[src] = 0
        
        while pq:
            _, u = heapq.heappop(pq)
            for edge in self.graph[u]:
                v = edge[0]
                w = edge[1]
                if not done[v] and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, [dist[v], v])
            
            done[u] = True
            
        print(dist)
        print(parent) 
        
        
        
g = Dijkstra(5)
g.addEdge(0, 1, 10)
g.addEdge(0, 4, 3)
g.addEdge(1, 2, 2)
g.addEdge(1, 4, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 2, 7)
g.addEdge(4, 1, 1)
g.addEdge(4, 2, 8)
g.addEdge(4, 3, 2)

print(g.graph)
g.dijkstraUtil(0)
