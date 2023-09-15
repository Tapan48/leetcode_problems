class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=collections.defaultdict(set)    ###  rowindex--->1-9 any value in set
        col=collections.defaultdict(set)     
        square=collections.defaultdict(set)
        
        
        for r in range(9):
            for c in range(9):
                
                
                if board[r][c]==".":
                    continue
                if board[r][c] in rows[r] or board[r][c]in col[c] or board[r][c]in square[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
                
        return True        
        
       
        
        
        
        
#         for i in range(9):            #### tc o(9^2)    sc o(9)
#             x=set()
#             cnt=0
#             for j in range(9):
                
                
#                 if board[i][j]!=".":
                    
#                     cnt+=1
#                     x.add(int(board[i][j]))
#             if len(x)!=cnt:
#                 return False
            
        
#         for j in range(9):
#             x=set()
#             cnt=0
#             for i in range(9):
                
                
#                 if board[i][j]!=".":
                    
#                     cnt+=1
#                     x.add(int(board[i][j]))
#             if len(x)!=cnt:
#                 return False 
            
#         for a in range(0,7,3):
#             for b in range(0,7,3):
#                 x=set()
#                 cnt=0
                
                
#                 for i in range(a,a+3):
#                     for j in range(b,b+3):
                        
#                         if board[i][j]!=".":
                    
#                            cnt+=1
#                            x.add(int(board[i][j]))
                    
#                 if len(x)!=cnt:
#                     return False
#         return True        
                    
            
            
            
            
            
                    
                    
                    
                    
                    
                
                
        
        
        
        
        
        