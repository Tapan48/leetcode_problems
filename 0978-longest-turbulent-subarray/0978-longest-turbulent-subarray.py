class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        
        
        l,r=0,1
        res,prev=1,""                 
        
        
        while r<len(arr):   ### sliding window
            
            
            if arr[r-1]<arr[r] and prev!="<":
                
                res=max(res,r-l+1)
                prev="<"
                r+=1
                
            elif arr[r-1]>arr[r] and prev!=">":
                
                res=max(res,r-l+1)
                prev=">"
                r+=1
            else:          ####   arr[r-1]==arr[r] or current sign == prev sign
                
                if arr[r-1]==arr[r]:
                    l=r 
                    r+=1
                else:
                    l=r-1
                prev=""
        return res       
        
        
      
            
            
            
            
            
            
        