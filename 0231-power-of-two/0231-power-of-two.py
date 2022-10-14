class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        """
        def recfunc(n):
            if n==1:  
                return True
            elif n>1:
                x=n/2
                return recfunc(x)
            else:
                return False
        res=recfunc(n)
        return res
        """
        
        
        
        
        while n>=0:
            
            if n==1:
                return True
            
            elif n==0:
                return False
            
            n/=2
            
            