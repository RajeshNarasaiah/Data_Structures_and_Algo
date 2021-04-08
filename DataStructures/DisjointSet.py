class DisjointSet:
    
    parent = {}
    
    rank = {}
        
    def make_set(self, universe):
        for idx in universe:
            self.parent[idx] = idx
            self.rank[idx]   = 0
            
    """
    Path compression : way of flattening the tree structure.
    Find recursively traverses up the tree and changes each node's parent
    reference to point to the root that is found.
    """
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
            
        return self.parent[p]
        
    """
    Union by rank : attach smaller tree to the root of larger tree.
    tree with smaller depth gets added under root of deeper tree.
    single element trees have rank 0
    whenever two trees of rank r are united, result has rank r + 1
    """
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

def printSet(universe, ds):
    print([ds.find(i) for i in universe])

universe = [1,2,3,4,5]

ds = DisjointSet()
ds.make_set(universe)
printSet(universe, ds)

ds.union(4,3)
printSet(universe, ds)

ds.union(2,1)
printSet(universe, ds)

ds.union(1,3)
printSet(universe, ds)
