class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        
        
        q=deque([0])  ### hold indices of layer
        farthest=0
        
        while q:   
            
            i=q.popleft()
            
            start=max(i+minJump,farthest+1)
            
            for j in range(start,min(i+maxJump+1,len(s))):
                
                if s[j]=="0":
                    q.append(j)
                    if j==len(s)-1:
                        return True
            # farthest=i+maxJump
            farthest=i+maxJump
        return False    
            
            
        
        
        
                
        
#         dp={}
        
#         def dfs(i):
            
#             if i>len(s)-1:
#                 return False
           
#             if i in dp:
#                 return dp[i]
#             if  s[len(s)-1]=="0" and i==len(s)-1:
#                 return True
            
#             if s[i]=="1":
#                 return False
            
            
            
            
            
#             res=False
#             for j in range(minJump,maxJump+1):
                
#                 res=res or  dfs(i+j)
#             dp[i]=res
            
#             return dp[i]
#         return dfs(0)        
                
                
                
        
        
                
       
                






