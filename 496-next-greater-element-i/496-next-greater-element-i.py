class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        
        
        
            dictt={num:i for i,num in enumerate(nums1)}
            res=[-1]*len(nums1) 
            stack=[]
            for i in range(len(nums2)):
            
                val2=nums2[i]
            
                while stack and val2>stack[-1]:
                    
                    value1=stack.pop()
                    ind=dictt[value1]
                    res[ind]=val2
                
                if val2 in dictt:
                    stack.append(val2)
                
            return res        
        
        
    
    
    
    
    
    
                            
        
        
    """
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
    """
        
    """ 
        res=[-1]*len(nums1)        ## tc : o(n^2)
                                    ## sc o(len(nums1))
        dictt={num:i for i,num in enumerate(nums1)}
        
        for i in range(len(nums2)):
            
            if nums2[i] in dictt:
                
                for j in range(i+1,len(nums2)):
                    
                    if nums2[j]>nums2[i]:
                        
                        ind=dictt[nums2[i]]
                        res[ind]=nums2[j]
                        break
        return res  
        
       """ 
                    
        
        
                    
    
    
    