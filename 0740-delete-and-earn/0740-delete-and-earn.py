class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        
        
        freq=Counter(nums)
        
        x=set(nums)
        arr=list(x)
        arr.sort()
        
        dp={}     ### dp[i] represents max points that can be achieved from that index
        
        
        def dfs(i):
            
            
            if i==len(arr):
                return 0
            
            if i in dp:
                return dp[i]
            
            
            
            noreward=0
            reward=arr[i]*freq[arr[i]]
            
            if i+1<len(arr):
            
               reward+=(dfs(i+2) if arr[i+1]==arr[i]+1 else dfs(i+1))
                
            else:
                reward+=dfs(i+1)
            
            noreward+=(dfs(i+1))
            
            dp[i]=max(reward,noreward)
            
            return dp[i]
        return dfs(0)  
        
        
        
        
        
        
        


#         freq=Counter(nums)



#         nums.sort()


#         x=set(nums)
#         # arr = [0 for i in range(3)] 
#         arr=list(x)


#         dp=[1]*len(arr)

#         for i,num in enumerate(arr):


#             if i==0:

#                 dp[i]=freq[num]

#             else:


#                 if arr[i]==(arr[i-1]+1):

#                     arr[i]=max(arr[i-1],(arr[i]*freq[arr[i]])+arr[i-2] if  0<=i-2<len(arr))

#                 else:
#                     arr[i]=max(arr[i-1],(arr[i]*freq[arr[i]])+arr[i-1])

#         return arr[-1]                

                








        













        
























