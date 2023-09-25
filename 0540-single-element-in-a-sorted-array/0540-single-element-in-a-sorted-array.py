class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
#         i=0
#         while i <len(nums):
            
#             if (i+1)<len(nums) and nums[i]==nums[i+1]:
                
#                 i+=2
#             else:
#                 return nums[i]

          l,r=0,len(nums)-1
    
          while l<=r:
            
            mid=l+ (r-l)//2
            
            if ((mid-1<0)or nums[mid]!=nums[mid-1]) and  ((mid+1)==len(nums)or nums[mid]!=nums[mid+1]):
                return nums[mid]
            
            leftsize=mid-1 if nums[mid]==nums[mid-1]else mid
            
            if leftsize%2:
                r=mid-1
            else:
                l=mid+1
                
                
            
            
                
            
        