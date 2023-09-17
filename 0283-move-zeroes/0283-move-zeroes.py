class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
                
            if num==0:
                nums.remove(num)
                nums.append(0)
        
#         l=0
#         r=0
        
#         for r in range(len(nums)):
            
#             if nums[r]:
#                 nums[r],nums[l]=nums[l],nums[r]
#                 l+=1
                
              
                    
                    
                    
            
            
        