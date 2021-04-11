"""
Hamiltonian cycle is a path that vists each vertx exactly once. A hamiltonian cycle 
(or Hamiltonian circuit) is a Hamiltonian path such that there is an edge from the last vertex
to the first vertex of the hamiltonian path. i.e., path begins and ends on the same vertex.
"""
class HamiltonianCycle:
    def __init__(self, vertices):
        self.graph = [ [0 for _ in range(vertices)] for _ in range(vertices) ]
        self.V = vertices
        
    # 1. if an edge exists between prev vtx in the path and the curr vtx.
    # 2. curr vtx not already in the path.
    def isSafe(self, vtx, path, pos):
        if self.graph[path[pos - 1]][pos] != 1:
            return False
            
        for vertex in path:
            if vertex == vtx:
                return False
                
        return True
        
    def HamiltonUtil(self, path, pos):
        #base case : If all vertices are included in the path
        if pos == self.V:
            # check if the last vtx in the path has an edge to the first 
            # vtx in the path.
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False
                
        for v in range(self.V):
            if self.isSafe(v, path, pos) == True:
                path[pos] = v
            
                if self.HamiltonUtil(path, pos + 1) == True:
                    return True
                    
                path[pos] = -1
                
    def HamCycle(self):
        path = [-1] * self.V
        
        path[0] = 0
        
        if self.HamiltonUtil(path, 1) == False:
            print('No hamiltonian cycle present')
            return
            
        print('hamilton cycle found : ', path)
        
g1 = HamiltonianCycle(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1], 
            [0, 1, 1, 1, 0], ]
            
g1.HamCycle()
         
