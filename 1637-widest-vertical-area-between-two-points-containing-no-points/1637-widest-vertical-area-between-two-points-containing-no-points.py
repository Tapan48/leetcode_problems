class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        
        points.sort(key=lambda x:x[0])
        
        maxw=0
        
        for i,point in enumerate(points):
            
            if i>0:
                width=point[0]-points[i-1][0]
                maxw=max(width,maxw)
        return maxw       
            
            
        