class Solution:
    def mySqrt(self, x: int) -> int:
       
        l=1
        r=x
        
     
        while (r-l)>1:            ## solved using binary search
                                  ##  x=13
                                  ## 1 2 3 4 5 6 7 8 9 10 11 12 13
                                  ## l           m               r      
            mid=(l+r)//2
            
            if mid*mid==x:
                return mid
            
            elif mid*mid>x:
                r=mid
                
            else:
                l=mid
                
        return (l+r)//2        
      
        
            
            
        
        
        
        
        
        
        
        
        