"""
Hashtable implementation with seperate chaining.

"""
INITIAL_CAPACITY = 3 #prime number

class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None
        
    def __str__(self):
        print("<Node: (%s, %s)", self.key, self.value)
        return
        
class hashTable:
    
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size     = 0
        self.buckets  = [None] * self.capacity
     
    # using multiplication hash function : k mod m, m = capacity, prime number closest to a power 
    # of 2.
    def hash(self, key):
        hashnum = 0
        
        for c in key:
            hashnum += ord(c)
            
        return hashnum % self.capacity
        
    def update(self, key, value):
        index = self.hash(key)
        node  = self.buckets[index]
        
        while node.key != key:
            node = node.next
            
        node.value = value
        
    def insert(self, key, value):
        
        #if key already present, update the value with new value and return
        val = self.find(key)
        if val is not None and val != value:
            self.update(key, value)
            return
        
        # key not present, create a new node and append at the index.
        self.size += 1
        
        index = self.hash(key)
        node  = self.buckets[index]
        
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        
        prev = node
        while node is not None:
            prev = node
            node = node.next
            
        prev.next = Node(key, value)
        
    def find(self, key):
        index = self.hash(key)
        node  = self.buckets[index]
        
        while node is not None and node.key != key:
            node = node.next
            
        if node is None:
            return None
        else:
            return node.value
            
    def remove(self, key):
        index = self.hash(key)
        node  = self.buckets[index]
        
        prev = None
        print('s: ', self.size)
        while node is not None and node.key != key:
            prev = node
            node = node.next
            
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            print('s: ', self.size)
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = node.next.next
            
            del(node)
            return result
            
            
ht = hashTable()
ht.insert('C', 25)
print(ht.size)
print(ht.find('C'))
ht.insert('C', 36)
print(ht.size)
print(ht.find('C'))
