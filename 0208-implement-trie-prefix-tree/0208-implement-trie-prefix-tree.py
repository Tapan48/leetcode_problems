class TrieNode():          ## trienode properties
    def __init__(self):

        self.children={}   

        self.endofword=False

class Trie:

    def __init__(self):

        self.root=TrieNode()     ### empty trie node
        

    def insert(self, word: str) -> None:

        curr=self.root       ### empty trie node

        for c in word:

            if c not in curr.children:

                curr.children[c]=TrieNode()

            curr=curr.children[c]

        curr.endofword=True




        

    def search(self, word: str) -> bool:

        curr=self.root 

        for c in word:

            if c not in curr.children:
                return False

            curr=curr.children[c]

        return curr.endofword           



        

    def startsWith(self, prefix: str) -> bool:

        curr=self.root 

        for c in prefix:

            if c not in curr.children:
                return False

            curr=curr.children[c]
        return True    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)