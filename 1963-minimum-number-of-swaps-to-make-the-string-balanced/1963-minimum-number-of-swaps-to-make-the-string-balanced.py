class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        
        closed=0
        maxclosed=0
        for char in s:
            
            
            if char=="]":
                closed+=1
                
                
            else:
                
                closed-=1
            maxclosed=max(closed,maxclosed)
        return (maxclosed+1)//2    
            
        