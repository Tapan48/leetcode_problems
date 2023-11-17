class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        i,j=0,0
        sum1,sum2=0,0
        res=0
        n=len(nums1)
        m=len(nums2)
        
        while i<n and j<m:
            
            if nums1[i]<nums2[j]:
                sum1+=nums1[i]
                i+=1
                
            elif nums2[j]<nums1[i]:
                sum2+=nums2[j]
                j+=1
            
            else:
                
                res+=max(sum1,sum2)+nums1[i]   
                sum1,sum2=0,0
                i+=1
                j+=1
        while i<n:
            sum1+=nums1[i]
            i+=1
        while j<m:
            sum2+=nums2[j]
            j+=1
            
        return (res+max(sum1,sum2))%(10**9+7)        
                
            
            
            
        
        
        
        
        
     
        