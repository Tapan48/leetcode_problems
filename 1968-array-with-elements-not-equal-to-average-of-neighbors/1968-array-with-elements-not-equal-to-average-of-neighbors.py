class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        
        
        nums.sort()
        
        res=[]
        l,r=0,len(nums)-1
        
        while len(res)!=len(nums):
            
            res.append(nums[l])
            l+=1
            
            if l<=r:
                res.append(nums[r])
                r-=1
        return res     
        
        
        
#         def swap(x,y):
            
#             temp=nums[x]
#             nums[x]=nums[y]
#             nums[y]=temp
            
            
#         for i in range(1,len(nums)-1):
            
#             avg=(nums[i-1]+nums[i+1])/2
            
#             if avg==nums[i]:
#                 swap(i,0)
                
                
#         return nums       wrong soltn

          







                
        
             
        
        
            
            
            
            