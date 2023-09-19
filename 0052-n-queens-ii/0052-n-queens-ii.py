class Solution:
    def totalNQueens(self, n: int) -> int:
        
        board=[["."]*n for i in range(n)]
        
        res=[]
        
        posdiag=set()
        negdiag=set()
        col=set()
        
        
        
        
        
        
        cnt=0
        def backtracking(r):
            nonlocal cnt
            
            if r==n:
                
                cnt+=1
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
        return cnt
        