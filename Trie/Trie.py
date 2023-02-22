class Trienode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.endofword = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword

    def startwith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
a = "apple"
b = "appl"
c = "app"
trie.insert(a)
trie.insert(b)
trie.insert(c)
result = trie.search(c)
print("Search result is:", result)
trie.startwith("a")




