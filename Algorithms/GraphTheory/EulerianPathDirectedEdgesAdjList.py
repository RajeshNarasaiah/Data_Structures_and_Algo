from collections import defaultdict

"""
Finding Eulerian Path in a directed graph.

Time: O(E) ==> computing in and out deg and dfs are linear.
"""
class EulerianPathDirectedEdgesAdjList:
    in_deg = []
    out_def = []
    edgecount = 0
    euler_path = []
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.initialize()
        
    def initialize(self):
        self.visited = [False] * self.num_nodes
        self.in_deg  = [0] * self.num_nodes
        self.out_deg = [0] * self.num_nodes
        self.graph   = defaultdict(list)
        
    def addDirectedEdge(self, frm, to):
        self.graph[frm].append(to)

    def setup(self):
        for frm in range(self.num_nodes):
            for to in self.graph[frm]:
                self.in_deg[to] += 1
                self.out_deg[frm] += 1
                self.edgecount += 1
            
    def print_graph(self):
        print(self.graph)
        print(self.visited)
        
    def graphHasEulerPath(self):
        if self.edgecount == 0:
            return False
        startnodes = 0
        endnodes   = 0
        
        for node in range(self.num_nodes):
            if self.out_deg[node] - self.in_deg[node] > 1 or self.in_deg[node] - self.out_deg[node] > 1:
                return False
            elif self.out_deg[node] - self.in_deg[node] == 1:
                startnodes += 1
            elif self.in_deg[node] - self.out_deg[node] == 1:
                endnodes   += 1
                
        return ( startnodes == 0 and endnodes == 0 ) or ( startnodes == 1 and endnodes == 1 )
        
    def findStartNode(self):
        start = 0
        for node in range(self.num_nodes):
            if self.out_deg[node] - self.in_deg[node] == 1:
                return node
            elif self.out_deg[node] > 1: # start at a node with an outgoing edge.
                start = node
                
        return start
        
    def dfs(self, node):
        while self.out_deg[node] != 0:
            nxt = self.graph[node][self.out_deg[node] - 1]
            self.out_deg[node] -= 1
            self.dfs(nxt)
        
        self.euler_path.append(node)

    # Returns a list of edgeCount + 1 node ids that give the Eulerian path or
    # null if no path exists or the graph is disconnected.  
    def euler(self):
        self.setup()
        
        #Step 1: check existence of euler path in a graph.
        if self.graphHasEulerPath() == False:
            return []
            
        #step 2: find appropriate start node.
        st = self.findStartNode()
        
        #Step 3: modified dfs
        self.dfs(st)
        
        #step 4: validate if the path returned is indeed an euler path.
        #        making sure all the edges are traversed.
        if len(self.euler_path) != self.edgecount + 1 :
            return []
            
        return self.euler_path[::- 1]
        
graph = EulerianPathDirectedEdgesAdjList(7)

graph.addDirectedEdge( 1, 2);
graph.addDirectedEdge( 1, 3);
graph.addDirectedEdge( 2, 2);
graph.addDirectedEdge( 2, 4);
graph.addDirectedEdge( 2, 4);
graph.addDirectedEdge( 3, 1);
graph.addDirectedEdge( 3, 2);
graph.addDirectedEdge( 3, 5);
graph.addDirectedEdge( 4, 3);
graph.addDirectedEdge( 4, 6);
graph.addDirectedEdge( 5, 6);
graph.addDirectedEdge( 6, 3);

print(graph.euler())
