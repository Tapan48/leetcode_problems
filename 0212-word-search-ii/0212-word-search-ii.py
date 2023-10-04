class Trienode:
    def __init__(self):
        self.children={}
        self.endofword=False
        
    def addword(self,word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=Trienode()
            curr=curr.children[c]
        curr.endofword=True
                
            
        
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        
        nr=len(board)
        nc=len(board[0])
        root=Trienode()
        for word in words:
            root.addword(word)
            
        visited=set()
        res=set()
        def dfs(i,j,node,word):
            
            if i<0 or j<0 or i==nr or j==nc or (i,j)in visited or board[i][j]not in node.children:
                return 
            
            visited.add((i,j))
            
            word+=board[i][j]
            node=node.children[board[i][j]]
            
            if node.endofword:
                res.add(word)
                
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            dfs(i-1,j,node,word)
            dfs(i+1,j,node,word)
            visited.remove((i,j))
            
        for i in range(nr):
            for j in range(nc):
                dfs(i,j,root,"")
        return list(res)
        
        
        
        
        
                      
            
        