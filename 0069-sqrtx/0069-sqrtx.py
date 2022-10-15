class Solution:
    def mySqrt(self, x: int) -> int:
        
        l=1
        r=x
        
        if x==0:
            return 0
        elif x==1:
            return 1
        while (r-l)>1:
            
            
            mid=(l+r)//2
            
            if mid*mid==x:
                return mid
            
            elif mid*mid>x:
                r=mid
                
            else:
                l=mid
                
        return l        

        
        
        
        
        
        
        
        
        