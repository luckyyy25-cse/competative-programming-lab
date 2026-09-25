class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end = True
    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return 0
            current = current.children[ch]
        if current.end:
            return 1
        return 0
N = int(input())
words = input().strip().split(",")
search_word = input().strip()
trie = Trie()
for word in words:
    trie.insert(word.strip())
print(trie.search(search_word))
