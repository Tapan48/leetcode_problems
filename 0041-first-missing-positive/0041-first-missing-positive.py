class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        
        
        nums=list(set(nums))
        nums.sort()
        
        for i in range(len(nums)):
            
            
            
                
            if nums[i]<=0:
                continue
                
            
            
            j=i
            k=1
            
            while j<len(nums):
                
                
                
                if nums[j]!=k:
                    
                    return k
                
                else:
                    k+=1
                    j+=1
                    
            return k         
        return 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        