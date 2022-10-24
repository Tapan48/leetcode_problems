class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True
        
        for i in range(len(nums)-1):
            
            if nums[i]>nums[i+1]:
                
                temp=nums[i]
                nums[i]=nums[i+1]
                
                x=sorted(nums)
                if x==nums:
                    return True
                
                nums[i]=temp
                
                nums[i+1]=nums[i]
                
                y=sorted(nums)
                if y==nums:
                    return True
                
                return False            
        return True
                
                
            
