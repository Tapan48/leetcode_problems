class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        
        l=max(weights)
        r=sum(weights)
        res=r
        
        
        def canaccom(m):
            shipw=m
            ndays=1
            
            
            
            for w in weights:
                
                if shipw-w<0:
                    
                    ndays+=1
                    shipw=m
                
                shipw-=w
            return ndays<=days
                
                
                    
                    
                    
                
            
            
           
                
             
                                     
            
            
            
        
        while l<=r:
            
            m=l+ (r-l)//2
            
            
            if canaccom(m):
                
                res=min(res,m)
                
                r=m-1
            else:
                l=m+1
                
        return res     
                
                
                
                
                
                
                
                
                
                
                 
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                  
        