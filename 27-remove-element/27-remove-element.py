class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        
     
        while l<=r:
            if nums[l]==val:                   ##  l pointer keeps track of elements=values
                                               ## r pointer keeps track of elements notequalto                                                               values
                while nums[r]==val and l<=r:  ## place nonvalues(r) at value position(l)
                    r=r-1
                nums[l]=nums[r]
                if r<l:
                    return r+1
                l=l+1
                r=r-1
            else:
                l=l+1
        return r+1     
        