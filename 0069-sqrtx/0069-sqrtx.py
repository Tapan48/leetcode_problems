class Solution:
    def mySqrt(self, x: int) -> int:
        
        l=1
        r=x
        
     
        while (r-l)>1:
            
            
            mid=(l+r)//2
            
            if mid*mid==x:
                return mid
            
            elif mid*mid>x:
                r=mid
                
            else:
                l=mid
                
        return (l+r)//2        

        
        
        
        
        
        
        
        
        