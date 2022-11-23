class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        
        
        prefixsum={0:1}
        
        cursum,res=0,0
        
        for num in nums:                ## tc o(n)
                                        
            
            cursum+=num
            
            diff=cursum-k
            
            
            
                
            res+=prefixsum.get(diff,0)
                
            prefixsum[cursum]=prefixsum.get(cursum,0)+1    
                
                
        return res         
            
            
            
        
        
        
        
        
        
        
        
        
        
#         cnt=0                            ## hashmap is used
#         for i in range(len(nums)):
            
#             summ=0
#             for j in range(i,len(nums)):
                
               
                        
                
#                     summ+=nums[j]
#                     if summ>k:
#                         break
                    
#                     if summ==k:
#                         cnt+=1
                    
                    
                        
                    
                    
#         return cnt           
                    
                    
                        
                        
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        