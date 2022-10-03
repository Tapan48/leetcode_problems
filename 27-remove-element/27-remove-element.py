class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        
        if len(nums)==1 and nums[0]==val:
            nums.remove(val)
            return l
        while l<=r:
            if nums[l]==val:
                while nums[r]==val and l<=r:
                    r=r-1
                nums[l]=nums[r]
                if r<l:
                    return r+1
                l=l+1
                r=r-1
            else:
                l=l+1
        return r+1     
        