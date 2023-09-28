class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums)%k!=0:
            return False
        
        nums.sort(reverse=True)
        
        
        target=sum(nums)/k
        
        
        
        
        
        used=[False]*len(nums)
        
        
        def backtracking(i,k,subsetsum):
            
            
            if k==0:
                return True
            if subsetsum==target:
                return backtracking(0,k-1,0)
                
            for j in range(i,len(nums)):
                
                # if  used[j] or subsetsum+nums[j]>target:
                #     continue
                if used[j] or subsetsum + nums[j] > target or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):        
                    continue
                    
                    
                used[j]=True
                if backtracking(j+1,k,subsetsum+nums[j]):
                    return True
                used[j]=False
                   
               
            return False        
        return backtracking(0,k,0) 
    
    
    
    
    
        
        
#         target=sum(nums)/k
        
#         if sum(nums)%k:
#             return False
        
#         nums.sort(reverse=True)
        
#         used=[False]*len(nums)
        
        
#         def backtracking(i,k,subsetsum):
            
            
#             if k==0:
#                 return True
#             if subsetsum==target:
#                 return backtracking(0,k-1,0)
                
#             for j in range(i,len(nums)):
                
#                 if not used[j] and subsetsum+nums[j]<=target:
#                     used[j]=True
#                     if backtracking(j+1,k,subsetsum+nums[j]):
#                         return True
#                     else:
#                         used[j]=False
#                 else:
#                     continue
#             return False        
#         return backtracking(0,k,0)            
                    
                    
   

        
        