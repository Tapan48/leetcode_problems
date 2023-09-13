class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        def merge(l,mid,h,arr):      ### merges two sorted subarrays 
            
            i=0
            j=0
            k=l
            
            left=arr[l:mid+1]
            right=arr[mid+1:h+1]
       
            
            while i<len(left) and j<len(right):
                
                if left[i]<right[j]:         
                    arr[k]=left[i]
                    k+=1
                    i+=1
                else:
                    arr[k]=right[j]
                    k+=1
                    j+=1
                        
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
            
            
                
                
                
                    
            
            
            
            
        def divide(l,h,arr):
            
            
            
            
            
            if l<h:
                
                mid=(l+h)//2
                
                divide(l,mid,arr)
                divide(mid+1,h,arr)
                merge(l,mid,h,arr) 
                return arr
                
        n=len(nums)        
                
                
        divide(0,n-1,nums)
        
        return nums
        