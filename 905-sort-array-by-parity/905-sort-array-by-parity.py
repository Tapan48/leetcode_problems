class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        """
        arr=[]
        
        
        for num in nums:
            
            
            if num%2==0:
                
                arr.append(num)
                
                
        for num in nums:
            if num%2!=0:
                
                arr.append(num)
                
                
        return arr        
        """
        l,r=0,len(nums)-1
        
        
        while l<r:
            
            
            while nums[l]%2==0 and l<r:          ## traverse till u get an odd number   
                
                l+=1
                
            while nums[r]%2!=0 and l<r :       ## traverse till u get an even number
                
                r-=1
            
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
            
            
        return nums    
            
                
                
                
        
        
        
        