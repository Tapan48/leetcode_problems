class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        dp={}
        res=float("inf")
        def dfs(i):
            nonlocal res
            
            
            if i>=len(nums)-1:
                return 0 
            
            
            if i in dp:
                return dp[i]
            
          
                
                
            
                
                
                
            
            for j in range(1,nums[i]+1):
                
                res=min(res,1+dfs(i+j))
                
            dp[i]=res
            return dp[i]
        return dfs(0)
                
                
                
                
        
        
        














        


        # dp=[0 for i in range(len(nums))]




        # for i in range(len(nums)-1,-1,-1):     ## dp[i]: represents min no of jumps from that index to last index
        #                                   #### so dp[i]=1+min(dp[i+1],dp[i+2].....dp[i+n])

        #                                    ###  tc o(n^2)      sc o(n)

        #     if i==(len(nums)-1):

        #         continue

        #     elif nums[i]==0:
        #         dp[i]=float("inf")

        #     n=nums[i]
        #     minjumps=float("inf")

        #     for j in range(1,n+1):


        #         if i+j<len(nums):


        #             minjumps=min(minjumps,dp[i+j])  


        #     dp[i]=1+minjumps

        # return dp[0]                  

            