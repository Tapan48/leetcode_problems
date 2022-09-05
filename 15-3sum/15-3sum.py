class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()              ## tc o(n^2+nlogn)
        res=[]                   ## concept of two sum 2 used 
        
        for i,num in enumerate(nums): 
            
            
            if i>0 and num==nums[i-1]:
                continue
                
                
            l,r=i+1,len(nums)-1
            
            while l<r:
                
                threesum=num+nums[l]+nums[r]
                
                if threesum>0:
                    r-=1
                    
                elif threesum<0:
                    l+=1
                    
                else:
                    
                    res.append([num,nums[l],nums[r]])
                    l+=1                                  ##   i    l   l'  r
                    while nums[l]==nums[l-1] and l<r: ## [-2,-2,0,0,2,2]
                        l+=1
                    
        
        return res
     
            
            
            
            
            