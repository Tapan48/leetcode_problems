class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        """
        nums.sort()
        
        
        l,r=0,1
        
        if len(nums)==1:
            return nums[0]
        
        
        while r<len(nums):
            
            if nums[l]==nums[r]:
                
                l+=2
                r+=2
                
            else:
                
                return nums[l]
        
        return nums[l]
        """
        res=0
        for n in nums:
            res=n^res                          ##bit manipulation in o(n)time complexity
       
        return res             
            
        
        
        
        
        
        
        
        