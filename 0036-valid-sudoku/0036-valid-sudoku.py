class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
       
        
        
        
        
        for i in range(9):
            x=set()
            cnt=0
            for j in range(9):
                
                
                if board[i][j]!=".":
                    
                    cnt+=1
                    x.add(int(board[i][j]))
            if len(x)!=cnt:
                return False
            
        
        for j in range(9):
            x=set()
            cnt=0
            for i in range(9):
                
                
                if board[i][j]!=".":
                    
                    cnt+=1
                    x.add(int(board[i][j]))
            if len(x)!=cnt:
                return False 
            
        for a in range(0,7,3):
            for b in range(0,7,3):
                x=set()
                cnt=0
                
                
                for i in range(a,a+3):
                    for j in range(b,b+3):
                        
                        if board[i][j]!=".":
                    
                           cnt+=1
                           x.add(int(board[i][j]))
                    
                if len(x)!=cnt:
                    return False
        return True        
                    
            
            
            
            
            
                    
                    
                    
                    
                    
                
                
        
        
        
        
        
        