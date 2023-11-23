class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        
        
#         nums.sort()
        
#         l,r=0,1
        
        
#         while r<len(nums):           ### tc o(n log n )  sc o(1)  
            
#             if nums[l]==nums[r]:
#                 return True
            
#             l+=1
#             r+=1
#         return False   

            x=set()
          
            for num in nums:
                
                if num in x:
                    return True
                x.add(num)
            return False      
                
                
                
                
                
        