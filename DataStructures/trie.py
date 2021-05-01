class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.validChildren = 0
        
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key):
        node = self.root
        length = len(key)
        
        for idx in range(length):
            nxt_ch = key[idx]
            if nxt_ch not in node.children:
                node.children[nxt_ch] = TrieNode()
            
            node = node.children[nxt_ch]
            
        node.isEndOfWord = True
        
    def search(self, key):
        node = self.root
        length = len(key)
        
        for idx in range(length):
            nxt_ch = key[idx]
            if nxt_ch not in node.children:
                return False
            else:
                node = node.children[nxt_ch]
                
        return node.isEndOfWord

    def delete(self, node, key, idx):
        #base
        #print('nxt_ch: ', idx, 'idx: ', node.children)
        if len(key) == idx:
            if node.isEndOfWord:
                print("word present -- deleting")
                node.isEndOfWord = False
                return True, len(node.children)
            else:
                return False, len(node.children)
            
        if key[idx] not in node.children:
            return False, len(node.children)
            
        ret, num_children = self.delete(node.children[key[idx]], key, idx + 1)
        
        # if word present in Trie and no children -> delete the child and remove from
        #                                            parent map.
        # if node present in Trie and has children -> mark endofword in child to False
        if ret:
            child = node.children[key[idx]]
            if num_children == 0:
                node.children.pop(key[idx])
                del(child)
            else:
                child.isEndOfWord = False

        return False, len(node.children)
        
keys = ["the","a","there","answer","any", "by","their","theim"]
T = Trie()

for k in keys:
    T.insert(k)
    
#print(T.root.children)
#print(T.search("the"))
#print(T.search("you"))
#print(T.search("their"))
#print(T.search("thaw"))
#print(T.search("anymore"))
print(T.search("theim"))
#print("deletion")
#print(T.deleteKey("their"))
print(T.search("their"))

#print(T.delete(T.root, "their", 0))
print("theim: ", T.search("theim"))
print("their: ", T.search("their"))
print("the: ", T.search("the"))
print("answer: ", T.search("answer"))
print("a: ", T.search("a"))
print(T.delete(T.root, "a", 0))
print(T.delete(T.root, "a", 0))
print("answer: ", T.search("answer"))
print("a: ", T.search("a"))
print(T.delete(T.root, "a", 0))

for k in keys:
    T.delete(T.root, k, 0)
    
print("their: ", T.search("their"))
print(T.root.children)
        
        
