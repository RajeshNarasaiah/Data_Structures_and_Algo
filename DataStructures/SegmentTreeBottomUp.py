class NumArray:
    """
    Segment tree implementation.
    """
    def __init__(self, nums: List[int]):
        self.lgt = len(nums)
        self.tree = [0] * 2 * self.lgt
        self.build(nums)
        
    def build(self, nums):
        idx = self.lgt
        jdx = 0
        
        while idx < 2 * self.lgt and jdx < self.lgt:
            self.tree[idx] = nums[jdx]
            idx += 1
            jdx += 1
            
        for idx in range(self.lgt - 1, 0, -1):
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
            
    def update(self, index: int, val: int) -> None:
        index += self.lgt
        self.tree[index] = val
        
        while index > 0:
            left = index
            right = index
            if left % 2 == 0:
                right = index + 1
            else:
                left = index - 1
                
            self.tree[index // 2] = self.tree[right] + self.tree[left]
            index = index // 2
    
    def sumRange(self, left: int, right: int) -> int:
        left += self.lgt
        right += self.lgt
        sm = 0
        
        while left <= right:
            if left % 2 == 1:
                sm += self.tree[left]
                left += 1
            if right % 2 == 0:
                sm += self.tree[right]
                right -= 1
                
            left = left // 2
            right = right // 2
            
        return sm
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
