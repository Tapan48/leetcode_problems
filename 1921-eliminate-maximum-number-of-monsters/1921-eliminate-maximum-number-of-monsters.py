class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        n=len(dist)
        time=[0]*n
        
        
        for i in range(n):
            
            time[i]=dist[i]/speed[i]
            
        
        
        minute=0
        cnt=0
        time.sort()
        
        for i in range(n):
            
            if minute<time[i]:
                cnt+=1
            
            else:
                return cnt
            
            minute+=1
        return cnt     
        
         