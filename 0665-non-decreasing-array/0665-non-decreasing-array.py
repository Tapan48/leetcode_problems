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
        
        for i in range(len(nums)-1):              ## 1 3 4 6 5 10 
                                                ##          | part where + - 
            if nums[i]<=nums[i+1]:                            
                continue                                  ### find the pointer where element
                                            ## trasition from increase to decrease
                                        ## now two possibilities are either set left element 
                                        ## equal to right or vice versa
        
            
                                 
            if cnt>1:
                return False
                
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
                    
            else:
                nums[i+1]=nums[i]
                    
            cnt+=1
                
        return True       
                
                    
                
            

            