class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        n=len(arr)-1
        
        for i in range(n,-1,-1):
            
            if i==n:
                maxright=arr[i]
                arr[i]=-1
            
            else:
                
                temp=arr[i]
                arr[i]=maxright
                maxright=max(maxright,temp)
            
        return arr    
           """
        n=len(arr)-1
        
        maxright=-1
        
        for i in range(n,-1,-1):
            
            temp=arr[i]
            arr[i]=maxright
            
            newmax=max(maxright,temp)
            maxright=newmax
        return arr    
            
            
                
        
        
        
    
        
        
        