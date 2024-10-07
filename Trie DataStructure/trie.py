class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=None
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_word=True
        
    def search(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.is_word==True
    def start_with(self,prefix):
        node=self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return True