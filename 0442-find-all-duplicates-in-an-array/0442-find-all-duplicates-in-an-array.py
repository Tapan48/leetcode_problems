class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        
        res=[]
        
        
        
        
        for i,num in enumerate(nums):
            
            
            val=nums[abs(num)-1]
            
            if val<0:
                
                res.append(abs(num))
                
            else:
                
                nums[abs(num)-1]=(-1)*nums[abs(num)-1]
                
            
            
      
                
        return res       