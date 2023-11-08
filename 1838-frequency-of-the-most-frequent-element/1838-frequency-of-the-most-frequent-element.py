class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        res=0
        l=0
        nums.sort()
        
        cursum=0
        for r in range(len(nums)):
            
          
            cursum+=nums[r]
            while (nums[r]*(r-l+1))>cursum+k:
                
                cursum-=nums[l]
                l+=1
               
            res=max(res,r-l+1)    
            
        return res     
                
                
            
            
        
        

        