class SegmentTree:
    def __init__(self, n):
        if n % 2 == 0:
            self.seg_siz = 4 * n 
        else:
            self.seg_siz = (4 * n)
        
        self.segTree = [0] * self.seg_siz
        
    
    def buildTree(self, arr, idx, lo, hi):
        if lo == hi:
            self.segTree[idx] = arr[lo]
            return
        
        mid = lo + (hi - lo)//2
        self.buildTree(arr, 2 * idx + 1, lo, mid)
        self.buildTree(arr, 2 * idx + 2, mid + 1, hi)
        
        #merge operation - problem specific. here we are building
        #                  a range sum tree
        self.segTree[idx] = self.segTree[2 * idx + 1] + self.segTree[2 * idx + 2]
    
    def querySum(self, tree_idx, lo, hi, idx, jdx):
        """
        3 scenarios:
            1. Total overlap: return with val.
            2. Partial overlap: split down.
            3. No overlap: return 0
        """
        if lo > jdx or hi < idx:
            # no overlap
            return 0
        
        if lo >= idx and hi <= jdx:
            # complete overlap
            return self.segTree[tree_idx]
            
        mid = lo + (hi - lo)//2
        if idx > mid:
            return self.querySum(2 * tree_idx + 2, mid + 1, hi, idx, jdx)
        elif jdx <= mid:
            return self.querySum(2 * tree_idx + 1, lo, mid, idx, jdx)
            
        lft = self.querySum(2 * tree_idx + 1, lo, mid, idx, mid)
        rgt = self.querySum(2 * tree_idx + 2, mid + 1, hi, mid + 1, jdx)

        return lft + rgt
        
    def updateNode(self, treeIdx, lo, hi, arrIdx, val):
        if lo == hi:
            self.segTree[treeIdx] = val
            return
        
        mid = lo + (hi - lo)//2
        
        if arrIdx > mid:
            self.updateNode(2 * treeIdx + 2, mid + 1, hi, arrIdx, val)
        elif arrIdx <= mid:
            self.updateNode(2 * treeIdx + 1, lo, mid, arrIdx, val)
            
        self.segTree[treeIdx] = self.segTree[2 * treeIdx + 2] + self.segTree[2 * treeIdx + 1]

arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]    
sTree = SegmentTree(len(arr))
print(sTree.segTree)

sTree.buildTree(arr, 0, 0, len(arr) - 1)
print(sTree.segTree)

print(sTree.querySum(0, 0, len(arr) - 1, 2,5))

sTree.updateNode(0, 0, len(arr) - 1, 5, 13)

print(sTree.segTree)
