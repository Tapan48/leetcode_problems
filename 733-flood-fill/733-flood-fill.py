class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        
        
        nr=len(image)
        nc=len(image[0])
        
        
        
        currcolor=image[sr][sc]
        
        
        
        def dfs(sr,sc):
            
            
            if 0<=sr<nr and 0<=sc<nc and image[sr][sc]==currcolor and currcolor!=color:
                
                image[sr][sc]=color
                
                dfs(sr,sc+1)
                dfs(sr,sc-1)
                
                dfs(sr-1,sc)
                dfs(sr+1,sc)
                
        dfs(sr,sc) 
        
        
        return image
                