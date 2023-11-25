class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
#         n=len(nums)
#         result=[0 for i in range(n)]
#         for i in range(n):
            
#             cursum=0
#             for j in range(n):
                
#                 cursum+=abs(nums[i]-nums[j])
#             result[i]=cursum
#         return result 
          
        n=len(nums)
        result=[0 for i in range(n)]
        cursum=0
        totalsum=sum(nums)
        for i in range(n):
            
            cursum+=nums[i]
            val=(nums[i]*(i+1)-cursum)+((totalsum-cursum)-(nums[i]*(n-1-i)))
            result[i]=val
        return result    
            
            
                
                
        