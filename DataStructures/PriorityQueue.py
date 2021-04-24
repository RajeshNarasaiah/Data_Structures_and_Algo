class PQ:
    # DOESNT HANDLE RESIZING YET.
    def __init__(self, max_size):
        self.length = max_size
        self.heap_size = 0
        self.A = [0] * self.length
        
    def max_heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left <= self.heap_size and self.A[left] > self.A[i]:
            largest = left
        if right <= self.heap_size and self.A[right] > self.A[i]:
            largest = right
            
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)
            
    def parent(self, i):
        if i == 0:
            return 0
        else:
            return (i - 1) // 2
            
    def heap_increase_key(self, i, key):
        if key < self.A[i]:
            print("new key smaller than exisiting key")
            
        self.A[i] = key
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
            i = self.parent(i)
            
    def insert(self, key):
        self.heap_size += 1
        self.A[self.heap_size] = float('-inf')
        self.heap_increase_key(self.heap_size, key)
        
    def peek_max(self):
        return self.A[0]
        
    def extract_max(self):
        if self.heap_size < 1:
            print("underflow")
            return None
        
        m = self.A[0]
        self.A[0] = float('-inf')
        self.heap_size -= 1
        self.max_heapify(0)
        return m
        
pq = PQ(3)
pq.insert(3)
pq.insert(4)
pq.insert(1)
print(pq.peek_max())
print(pq.heap_size)
print(pq.extract_max())
print(pq.peek_max())
print(pq.heap_size)
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
