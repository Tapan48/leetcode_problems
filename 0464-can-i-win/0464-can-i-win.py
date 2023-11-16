class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        
        
        dp={}
        
        def dfs(choices,remainder):     ### check how caching being applied and analyze tc
            
            if choices[-1]>=remainder:
                return True
            
            state=tuple(choices)
            if state in dp:
                return dp[state]
            
            
            for i in range(len(choices)):
                
                if not dfs(choices[:i]+choices[i+1:],remainder-choices[i]):
                    dp[state]=True
                    
                    return True
            dp[state]=False    
            return False
        
        
        
            
            
        
        
        n=maxChoosableInteger
        
        if (n*(n+1))/2<desiredTotal:
            return False
        
        choices=list(range(1,maxChoosableInteger+1))
        return dfs(choices,desiredTotal)
        

#         m=desiredTotal              ### check the approach
        
#         l,r=1,maxChoosableInteger
        
#         cnt=1
        
#         while l<=r:
            
#             if cnt%2:
                
#                 if r>=m:
#                     return True
#                 else:
#                     m-=l
#                     l+=1
#             else:
                
#                 if r>=m:
#                     return False
                
#                 else:
#                     m-=l
#                     l+=1
#             cnt+=1        
                    
            
            
        
        
       
                
                
        