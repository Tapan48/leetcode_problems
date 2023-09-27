class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        
        """
        
        nr=len (matrix)
        nc=len(matrix[0])
        
        zero_rows=set()
        zero_col=set()
        
        
        for i in range(nr):
            for j  in range(nc):
                
                
                if matrix[i][j]==0:
                    
                    zero_rows.add(i)
                    zero_col.add(j)
        
        
        for row in zero_rows:
            for j in range(nc):
                matrix[row][j]=0
                
        for col in zero_col:
            for i in range(nr):
                matrix[i][col]=0        
                
                
                
                    
                    
        