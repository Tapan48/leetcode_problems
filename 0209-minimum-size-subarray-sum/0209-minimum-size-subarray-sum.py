class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        
        
        
        
        
        
        l,r=0,0
        
        cursum,minlength=0,float("inf")
        while l<=r and r<len(nums):
            
            
            cursum+=nums[r]
            
            if cursum<target:
                r+=1
                
            else:
                minlength=min(minlength,r-l+1)
                
                cursum-=(nums[l]+nums[r])
                
                l+=1
        
        print(l,r)
        return minlength if minlength!=float("inf") else 0
            
            
            
        
#         l,r=0,len(nums)-1
        
#         totalsum=sum(nums)
        
#         while l<=r:
            
#             if totalsum>=target:
#                 res=[l,r]
            
#                 if nums[l]<=nums[r]:
                
#                     totalsum-=nums[l]
#                     l+=1
                
#                 else:
                
#                     totalsum-=nums[r]
#                     r-=1
                    
#             if l>=r:
#                 break
            
            
        
#         res=[l,r]            
#         i,j=res
#         print(i,j)
#         return j-i+1                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         minlength=float("inf")
#         for i,num in enumerate(nums):
            
           
#             summ=0
#             for j in range(i,len(nums)):
                
                
                
#                 if j==i and num==target:
#                     return 1
                
#                 else:
                    
#                     summ+=nums[j]
                    
#                     if summ>=target:
                        
#                         length=j-i+1
#                         minlength=min(minlength,length)
#                         break
                        
#         if minlength!=float("inf"):
#             return minlength
        
#         else:
#             return 0
                    
                
                
                
                    