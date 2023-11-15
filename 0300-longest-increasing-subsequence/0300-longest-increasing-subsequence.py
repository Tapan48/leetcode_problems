class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:                     ####  subsequence of [1,2,3] : 
                                                                       ###            {(1),(2),(3),(1,2),(2,3),(1,3),(1,2,3)}

                                                                       ## relative order should be maintained

                                                                       ## no of subsequnces of array of size n is  2^n-1


                                                                       ### longest increasing subsequence would be a subset from the sample space which is sorted and of 
                                                                       ## longest length
                            
                            
                            

#         lis=[0]*len(nums)
#         lis[len(nums)-1]=1


#         for i in range(len(nums)-2,-1,-1):    ## tc o(n^2)  ## sc o(n)


#             maxsubseq=1

#             for j in range(i+1,len(nums)):

#                 if nums[i]<nums[j]:
#                     maxsubseq=max(maxsubseq,1+lis[j])

#             lis[i]=maxsubseq

#         return max(lis)

          dp={}
          def dfs(i):
            
              if i in dp:
                    return dp[i]
              
              dp[i]=1  
              for j in range(i+1,len(nums)):
                    
                    if nums[i]<nums[j]:
                
                       dp[i]=max(dp[i],1+dfs(j))
              return dp[i]
        
          res=0
          for i in range(len(nums)):
            res=max(res,dfs(i))
                
          return res
            
        
                
                
                




                                                                       


      

























