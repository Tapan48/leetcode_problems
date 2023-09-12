class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        n=len(board)
        board.reverse()
        def squaretoposition(squareno): #### square int to coordinates
            
            r=(squareno-1)//n
            c=(squareno-1)%n
            
            if r%2:
                return [r,n-1-c]
            
            return [r,c]
            
            
            
            
            
         
                
            
            
            
            
        
        
        
        
        
        q=deque()
        q.append([1,0])       ###  [squareno,moves] 
        
        
        visit=set()
        
        
        while q:
            
            currsquare,moves=q.popleft()
            
            
            for i in range(1,7):
                nextsquare=currsquare+i
                
                r,c=squaretoposition(nextsquare)
                
                if board[r][c]!=-1:
                    nextsquare=board[r][c]
                    
                if nextsquare== (n*n):
                    return moves+1
                    
                if nextsquare not in visit:   
                    
                    visit.add(nextsquare)
                    q.append([nextsquare,moves+1])
                    
        return -1            
                
        
        
        