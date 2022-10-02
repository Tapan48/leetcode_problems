class Solution:
    def trap(self, height: List[int]) -> int:
        """
        n=len(height)
        maxleft=[0 for i in range(n)]
        
        maxright=[0 for i in range(n)]
        minlr=[0 for i in range(n)]
        
        maxl,maxr=0,0
        
        for i in range(n):
            
            
            maxleft[i]=maxl
            
            maxl=max(maxl,height[i])
            
        for i in range(n-1,-1,-1):
            
            maxright[i]=maxr
            
            maxr=max(maxr,height[i])
            
        for i in range(n):
            minlr[i]=min(maxleft[i],maxright[i])
            
            
        for i in range(n):
            
            if minlr[i]-height[i]<=0:
                height[i]=0
                
            else:
                height[i]=minlr[i]-height[i]
                
                
        return sum(height)        
            """
        n=len(height)
        l=0
        r=n-1
        maxl=height[0]
        maxr=height[r]
        
        while l<=r:
            if maxl <=maxr:
                
                val=maxl-height[l]
                maxl=max(maxl,height[l])
                if val<=0:
                    height[l]=0
                    
                else:
                    height[l]=val
                l+=1
                
            else:
                val=maxr-height[r]
                maxr=max(maxr,height[r])
                if val<=0:
                    height[r]=0
                    
                else:
                    height[r]=val
                r-=1
        print(height)        
        return sum(height)       
                
                
            
            
            
        
            
            
              