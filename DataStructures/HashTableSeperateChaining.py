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
        
    def insert(self, key, value):
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
ht.insert('A', 5)
print(ht.size)
print(ht.find('A'))
print(ht.remove('A'))
print(ht.find('A'))
print(ht.size)
ht.insert('A', 5)
ht.insert('B', 15)
ht.insert('C', 25)
ht.insert('D', 52)
ht.insert('E', 54)
print(ht.size)
print(ht.find('E'))
print(ht.buckets)

print(ht.find('E'))
ht.insert('C', 25)
print(ht.find('C'))
print(ht.remove('A'))
print(ht.remove('B'))
print(ht.size)
