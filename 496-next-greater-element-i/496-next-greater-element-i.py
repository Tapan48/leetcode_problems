class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                if nums1[i]==nums2[j]:
                    k=j+1
                    while k<len(nums2):
                        if nums2[k]>nums1[i]:
                            nums1[i]=nums2[k]
                            break
                        k+=1    
                    if k==len(nums2):
                        nums1[i]=-1
                    break    
        return nums1                
                            
        