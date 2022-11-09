class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        
        
        l,r=len(nums)-2,len(nums)-1
        
        
        i=l
        
        while l>=0:
            
            
            if nums[l]+i>=r:
                
                r=l
                l-=1
                i=l
            else:
                
                l-=1
                i=l
                
        if r==0:
            return True
        
        else:
                return False