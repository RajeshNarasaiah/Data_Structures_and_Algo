class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        
    def search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
            
    def tree_search(self, k):
        return self.search(self.root, k)
        
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x
        
    def maximum(self, x):
        while x != None:
            x = x.right
        return x
        
    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y
        
    def predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y
        
    def insert(self, k):
        y = None
        x = self.root
        z = Node(k)
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        #replaces subtree rooted at u with subtree rooted at v
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def deletion(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
        
        del(z)
        
    def inorder(self, x):
        if x != None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)
    
    def inorder_tree_walk(self):
        x = self.root
        self.inorder(x)
        
    def delete(self, x):
        n = self.search(self.root, x)
        if n is None:
            print(x, " doesn't exist in the binary search tree ")
            return
        self.deletion(n)
        
n = Node(15)      
bst = BinarySearchTree(n)
bst.insert(6)
bst.insert(18)
bst.insert(3)
bst.insert(7)
bst.insert(17)
bst.insert(20)
bst.insert(2)
bst.insert(4)
bst.insert(13)
bst.insert(9)
bst.inorder_tree_walk()
print("------")
bst.delete(15)
bst.inorder_tree_walk()
print("------")
bst.delete(13)
bst.inorder_tree_walk()
print("------")
bst.delete(1)
bst.inorder_tree_walk()
print("------")
bst.delete(4)
bst.inorder_tree_walk()
print("------")
bst.delete(18)
bst.inorder_tree_walk()
print("------")
bst.delete(20)
bst.inorder_tree_walk()
print("------")
bst.delete(6)
bst.inorder_tree_walk()
print("------")
bst.delete(7)
bst.delete(2)
bst.delete(9)
bst.delete(3)
bst.delete(17)
bst.inorder_tree_walk()
print("------")
bst.inorder_tree_walk()
