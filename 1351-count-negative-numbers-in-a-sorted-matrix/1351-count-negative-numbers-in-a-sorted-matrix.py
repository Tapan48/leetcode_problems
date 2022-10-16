class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        """
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    cnt+=1
                    
        return cnt
    """
        
        nr,nc=len(grid),len(grid[0])
        i,j=0,nc-1
        cnt=0
        
        while i<len(grid) and j>=0:
            
            if grid[i][j]>=0:
                i+=1
                
            else:
                cnt+=((nr-1)-i+1)
                j-=1
                
                
        return cnt        
            
        
    
    