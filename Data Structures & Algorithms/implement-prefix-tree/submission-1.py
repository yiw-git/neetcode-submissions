class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        #monday
        curNode=self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char]=TrieNode()
            curNode=curNode.children[char]
        curNode.endOfWord=True

    def search(self, word: str) -> bool:
        curNode=self.root
        #catfish
        for char in word:
            if char not in curNode.children:
                return False
            curNode=curNode.children[char]
        return curNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        #monday 
        curNode=self.root
        for char in prefix:
            if char not in curNode.children:
                return False
            curNode=curNode.children[char]
        return True

class TrieNode:
    def __init__(self):
      self.children={}
      self.endOfWord=False
       


 #{'m':o}, m, o are nodes, 

 #root:{'':b, m, t}
 #{b:e}, {m:[a, o]} 
 #{e:e}, {o:n}
 #{e:''}






