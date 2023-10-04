
     

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        nr=len(board)
        nc=len(board[0])
        
        visited=set()
        
        def dfs(i,j,k):
            
            if k==len(word):
                return True
            
            if i<0 or i==nr or j<0 or j==nc or (i,j)in visited or board[i][j]!=word[k]:
                return False
            
            
            
            
                
            visited.add((i,j))
            
                
            
            l=dfs(i,j-1,k+1)
            r=dfs(i,j+1,k+1)
            t=dfs(i-1,j,k+1)
            b=dfs(i+1,j,k+1)
            res=(l or r or t or b)
            visited.remove((i,j))
            return res
            
          
        
        
        
        
        
        
        
        
        
        
        
        for i in range(nr):
            for j in range(nc):
                
                if dfs(i,j,0):
                    return True
        return False        
        
        
        
        









    








               