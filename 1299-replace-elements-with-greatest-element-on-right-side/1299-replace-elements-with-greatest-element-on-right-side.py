class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n=len(arr)-1
        maxright=0
        for i in range(n,-1,-1):
            
            if i==n:
                maxright=arr[i]
                arr[i]=-1
            
            else:
                
                temp=arr[i]
                arr[i]=maxright
                maxright=max(maxright,temp)
            
        return arr    
            
                
        
        
        
    
        
        
        