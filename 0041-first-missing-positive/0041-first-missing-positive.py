class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        
        """
        nums=list(set(nums))
        nums.sort()         
        
        for i in range(len(nums)):
            
            
            
                
            if nums[i]<=0:
                continue
                
            
            
            j=i
            k=1
            
            while j<len(nums):
                
                
                
                if nums[j]!=k:
                    
                    return k
                
                else:
                    k+=1
                    j+=1
                    
            return k         
        return 1
        """
        
        
        
        
        
        x=set(nums)                 ## tc o(n)
                                     ## sc o(n)
        
        
        for n in range(1,len(nums)+1):        ## missing postive number lies between 
                                              ##    1<=answer<=len(nums)+1
                                            ##   worst case : eg [1,2,3,4]
                                             ## answwer =5 
            
            if n not in x:
                
                return n
            
        return n+1
           
        
        """
        for i in range(len(nums)):           ## tc o(n)
                                              ## sc o(1)
            if nums[i]<0:                        
                nums[i]=0                       ### if array size is n then answer range lies 
                                              ## between   1<=answer<=n+1
                                             
                                                          ##   1<=answer<=n
        for i in range(len(nums)):                      ##array 0<= arr[i]<=n-1  
            
            if (abs(nums[i])-1)<len(nums) and (abs(nums[i])-1)>=0:
                if nums[abs(nums[i])-1]==0:
                    nums[abs(nums[i])-1]=(-1)*(len(nums)+1)
                    
                else:    
                    
                    nums[abs(nums[i])-1]=(-1)*abs(nums[abs(nums[i])-1])
        print(nums)            
                    
        for n in range(1,len(nums)+1):
            
            
            if nums[n-1]>=0:
                return n
            
            
        return n+1     
                
       """     
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        