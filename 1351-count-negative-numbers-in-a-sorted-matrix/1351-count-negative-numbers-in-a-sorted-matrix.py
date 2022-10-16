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
        """
        nr,nc=len(grid),len(grid[0])         ###  
        i,j=0,nc-1
        cnt=0
        
        while i<len(grid) and j>=0:        
            
            
            if grid[i][j]>=0:                ## we start iterating from top rightest element 
                                            ## if element is +ve then all elements present 
                                            ## at left side of element is +ve,so we increment                                             ## the row
                                            ##
                            
                                            ##if element is -ve all elements below it in that                                             ## column will be -ve as col sorted in desc order
                                             ## cnt all -ve values and decrement col
                i+=1
                
            else:
                cnt+=((nr-1)-i+1)
                j-=1
                
                
        return cnt        
           """
      
        def binarysearch(row):
            
            
            l,r=0,len(row)
            while l<r:
                
                mid=(l+r)//2
                if row[mid]<0:
                    r=mid
                else:
                    l=mid+1
            return (len(row)-l)        
        cnt=0
        for row in grid:
            
            cnt+=binarysearch(row)
            
        return cnt    
        
        
        
        
    
    