class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        """ 
        n=1
                                   ## its so much easy
        array=[]
        
        while len(array)!=k:
            
            
            if n not in arr:         ## keeping track of elements not present in arr
                array.append(n)
                
            n+=1
            
        return array[-1]    
    
       """
        
        
        n=1
        
        while k!=0:
            
            if n not in arr:
                x=n
                k-=1
                
            n+=1
            
        return x     
        