class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        answer=[1]*len(nums)
        
        
        prefix=1
        
        
        for i in range(1,len(answer)):
            
            prefix*=nums[i-1]
            answer[i]=prefix
            
        postfix=1    
        print(answer)    
        for i in range(len(answer)-1,-1,-1):
            
            
            
            val=answer[i]*postfix
            
            answer[i]=val
            
            postfix*=nums[i]
            
        return answer    
            
            
            
            
            
            
            
            
           
            
            
            