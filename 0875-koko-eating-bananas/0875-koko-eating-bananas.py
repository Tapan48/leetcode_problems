class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n=max(piles)
        
        l,r=1,n
        
        res=r
        while l<=r:
            
            
            k=(l+r)//2
            
            hrtaken=0
            
            for pile in piles:
                
                
                hrtaken+=math.ceil(pile/k)
                
            if hrtaken>h:
                
                l=k+1
                
            else:
                res=min(res,k)
                
                r=k-1
                
        return res        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        