class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
      
        """
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
           """
        
        cnt=1
        
        for i in range(len(nums)-1):
            
            
        
            
            if nums[i]>nums[i+1]:
                if cnt>1:
                    return False
                
                if i==0 or nums[i+1]>=nums[i-1]:
                    nums[i]=nums[i+1]
                    
                else:
                    nums[i+1]=nums[i]
                    
                cnt+=1
                
        return True       
                
                    
                
            

            