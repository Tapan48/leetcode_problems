class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        
        n=len(mat)
        
        
        i=0
        j=0
        k=n-1
        ts=0
        while i<n :
            
            
            if k!=j:
                sumr=mat[i][j] +mat[i][k]
           
                ts+=sumr
            
              
            else:
                ts+=mat[i][k]
                
            i+=1
            j+=1
            k-=1
                    
            
        return ts
            
            
        
        
   