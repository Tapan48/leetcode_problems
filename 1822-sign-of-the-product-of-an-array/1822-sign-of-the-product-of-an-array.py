class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        
#         prod=1
#         for num in nums:
            
#             prod*=num          ### prod can be very large---> may lead to integer overflow
        
        
#         if prod>0:
#             return 1
        
#         elif prod<0:
#             return -1
#         else:
#             return 0

        noneg=0
    
        for num in nums:
            
            
            if num==0:
                return 0
            
            elif num<0:
                noneg+=1
        return -1 if noneg%2 else 1      
                
            
              
                
              
            
        