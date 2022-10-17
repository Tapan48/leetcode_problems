class Solution:
    def isHappy(self, n: int) -> bool:
        
        """
        x=set()                          ## sc o(n)
        while n!=1:
            
            sumsq=0
            
            while n:
                
                ld=n%10
                sumsq+=(ld**2)
                n=n//10
            
            if sumsq in x:
                return False
            
            x.add(sumsq)
            n=sumsq
            
            
        return True
        
        """
        
        
        """
        x=set()
        while n not in x:
            
            x.add(n)
            
            sqrn=self.squaredig(n)
            
            
            if sqrn ==1:
                
                return True
            
            n=sqrn
            
            
        return False    
            
    def squaredig(self, n: int) -> int:
        sumsq=0
            
        while n:
                
            ld=n % 10
            sumsq+=(ld**2)
            n=n//10
            
        return sumsq    
        
        """
        def next(n):
            sumsq=0
            
            while n:
                
                ld=n % 10
                sumsq+=(ld**2)
                n=n//10
            
            return sumsq 
    
        
        slow,fast=n,next(n)       ## floyds cycle detection 
        
        if slow==fast:
            return True
    
    
        while slow !=fast:
            
            slow=next(slow)
            fast=next(next(fast))
            
            if  fast==1 :
                return True
            
        return False    
            
                
        
    
    
            
            
            
            
        
        
        
        
        
            
            
            
        
        
        
        
        
        
                   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        