class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        
        nr=len(mat)
        
        nc=len(mat[0])
        
        arr=[[0 for i in range(c)]for j in range(r)]
        
        if (nr*nc)==(r*c):
            x,y=0,0
            for i in range(r):
                for j in range(c):
                    arr[i][j]=mat[x][y]
                    
                    if y<nc:
                        y+=1
                        
                    if y==nc:
                        y=0
                        
                        
                        x+=1
            return arr                   
        
        else:
            return mat
            
            
            