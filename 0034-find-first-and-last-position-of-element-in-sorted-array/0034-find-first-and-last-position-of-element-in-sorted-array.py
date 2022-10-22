class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        leftposition=self.binarysearch(nums,target,True)
        rightposition=self.binarysearch(nums,target,False)
        return [leftposition,rightposition]
        
        
        
        
        
        
        
        
        
        
    def binarysearch(self,nums,target,leftsearch):
        
        l,r=0,len(nums)-1
        i=-1
        
        while l<=r:
            mid=(l+r)//2
            
            if nums[mid]==target:
                
                i=mid
                if leftsearch:
                    r=mid-1
                    
                else:
                    l=mid+1
                    
            elif target>nums[mid]:
                l=mid+1
            
            else:
                r=mid-1
                    
        return i            
                
                
        
        
        
        
        """
        
        l,r=0,len(nums)-1
        n=len(nums)
        
        
        
        while l<=r:
            
            
            mid=(l+r)//2
            
            
            
            if target==nums[mid]:
                
                x,y=mid,mid
                
                while x>=0 and nums[x]==target:
                    x-=1
                
                while y<n and nums[y]==target:
                    y+=1
                    
                    
                    
                    
                return [x+1,y-1]    
        
        
        
                                  
                
                
              
            
            elif target>nums[mid]:
                    l=mid+1
                    
            else:
                r=mid-1
                
                
        return [-1,-1]       
                
        """        
                
                
                
                