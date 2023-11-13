class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
         goal=len(nums)-1
        
         for i in range(len(nums)-1,-1,-1):
            
            if i+nums[i]>=goal:
                goal=i
        
         return True if goal==0 else False
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            
#         dp={} 
#         def dfs(i):
            
#             if i==len(nums)-1:
#                 return True
#             if i in dp:
#                 return dp[i]
            
#             for num in range(1,nums[i]+1):
                
#                 dp[i]=dfs(i+num)
#                 if dp[i]:
#                     return True
#             dp[i]=False    
#             return False
#         return dfs(0)
#         goal=len(nums)-1                 ## tc o(n) greedy
#                                               ## goal is to reach at end index from start 
#                                      ## index, goal is at end and we traverse array from                                      ## last index and check for each index if we can reach
#                                  ## the goal index, if we can then we update the goal                                    variable to current index
                    
#         for i in range(len(nums)-1,-1,-1):
            
#             if i+nums[i]>=goal:
                
#                 goal=i
                
                
#         return True if (goal==0) else False

    
    