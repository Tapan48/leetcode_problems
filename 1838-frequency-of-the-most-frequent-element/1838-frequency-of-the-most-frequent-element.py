class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        res=0
        l=0
        nums.sort()
        
        cursum=0
        for r in range(len(nums)):
            
            winlen=r-l+1
            cursum+=nums[r]
            while (nums[r]*winlen)>cursum+k:
                
                cursum-=nums[l]
                l+=1
                winlen=r-l+1
            res=max(res,r-l+1)    
            
        return res     
                
                
            
            
        
        

        