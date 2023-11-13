class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        mod=10**9+7
        dp={}
        
        def dfs(i,steps):
            
            if steps==0:
                return 1 if i==0 else 0
            if  (i,steps)in dp:
                return dp[(i,steps)]
            
            elif i < 0 or i == arrLen:
                return 0
      
        
            
            
            x=dfs(i,steps-1)
            y=dfs(i+1,steps-1)
            z=dfs(i-1,steps-1)
            dp[(i,steps)]=x+y+z
            return (x+y+z)%mod
            
        return dfs(0,steps)    
                
            
            
            
        
        