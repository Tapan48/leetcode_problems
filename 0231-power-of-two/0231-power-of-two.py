class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        """
        def recfunc(n):
            if n==1:  
                return True
            elif n%2!=0:
                return False
            elif n>1:
                x=n/2
                return recfunc(x)
            else:
                return False
        res=recfunc(n)
        return res
        """
        
        
        
    ## iterative soltn
        while n>=0:
            
            if n==1:
                return True
            elif n%2!=0:
                return False
            
            elif n==0:
                return False
            
            n/=2
         
         
        
        """
        return n>0 and n & (n-1)==0          ##     if n is power of two then
          """                                   ## binary form of (n) & (n-1)==0