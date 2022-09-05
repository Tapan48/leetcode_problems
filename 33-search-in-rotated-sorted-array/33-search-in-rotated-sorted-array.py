class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        for i,num in enumerate(nums):
            
            if num==target:
                return i
            
        return -1    
        """
        
        
        l,r=0,len(nums)-1
        
        
        while l<=r:
            
            mid=(l+r)//2
            
            
            if nums[mid]==target:
                return mid
            
            
            if nums[mid]>=nums[l]:          ##  mid index present in left sorted array condition,then check if target is with mid and leftmost element
                
                if target<nums[mid] and target>=nums[l]:
                    r=mid-1
                    
                    
                else:
                    l=mid+1
                    
            else:    ## mid index present in right sorted array condition
                      ## see if target is within mid and rightmost element                
                
                if target>nums[mid] and target<=nums[r]:
                    l=mid+1
                    
                else:
                    r=mid-1
                    
        return -1           
                
                
                
        