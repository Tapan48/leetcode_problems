class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        
        dp={}
        
        def dfs(l,r):
            
            if (r-l)==1:
                return 0
            
            if (l,r)in dp:
                return dp[(l,r)]
            
            res=float("inf")
            for cutpos in cuts:
                
                
                if l<cutpos<r:
                    
                    cost=(r-l)+dfs(l,cutpos)+dfs(cutpos,r)
                    res=min(res,cost)
                    
            dp[(l,r)]=res if res!=float("inf") else 0       
            return dp[(l,r)]      
                    
            
            
            
            
            
        return dfs(0,n)    
        