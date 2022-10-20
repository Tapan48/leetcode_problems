class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        
        l,r=0,k-1
        
        mindiff = float('inf')

        while r<len(nums):
            
            
            diff=nums[r]-nums[l]
            mindiff=min(mindiff,diff)
            l+=1
            r+=1
            
        return mindiff    
            
        
        
              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        