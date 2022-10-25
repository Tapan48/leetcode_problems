class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        
        """
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
        """
        
        x=set(nums)
        
        
        
        for n in range(1,len(nums)+1):
            
            if n not in x:
                
                return n
            
            if n==len(nums):
                return n+1
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        