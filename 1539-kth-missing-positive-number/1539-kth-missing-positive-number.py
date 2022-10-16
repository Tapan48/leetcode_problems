class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        """ 
        n=1
                                   ## its so much easy,     find o(n) and o(log n ) soltn 
        array=[]
        
        while len(array)!=k:
            
            
            if n not in arr:         ## keeping track of elements not present in arr
                array.append(n)
                
            n+=1
            
        return array[-1]    
    
       """
        
        """
        n=1
        
        while k!=0:               ## tc worst case o(n^2)
            
            
            if n not in arr:
                x=n
                k-=1
                
            n+=1
            
        return x     
        """
        
        x=set(arr)
        prevsize=len(x)
        
        n=1
        
        while k!=0:
            
            x.add(n)
            
            if len(x)!=prevsize:
                prevsize=len(x)
                k-=1
            if k==0:
                return n
            n+=1   
        print(x)         
                
                
                
                