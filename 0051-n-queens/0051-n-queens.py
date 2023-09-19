class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board=[["."]*n for i in range(n)]
        
        res=[]
        
        posdiag=set()
        negdiag=set()
        col=set()
        
        
        
        
        
        
        
        def backtracking(r):
            
            if r==n:
                
                copy= ["".join(row) for row in board]
                
                res.append(copy)
                return 
                
                
            
            
            
            
            
            for c in range(n):
                
                if  c in col or (r+c)in posdiag or (r-c)in negdiag:
                    continue
                    
                board[r][c]="Q"
                posdiag.add(r+c)
                negdiag.add(r-c)
                col.add(c)
                
                backtracking(r+1)
                
                board[r][c]="."
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                col.remove(c)
                
        backtracking(0)
        return res
                
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        


















        















        