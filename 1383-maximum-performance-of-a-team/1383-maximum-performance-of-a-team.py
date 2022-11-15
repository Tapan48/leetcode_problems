class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        arr=[]
        for spd,eff in zip(speed,efficiency):
            
            
            arr.append([eff,spd])
            
            
        arr.sort(reverse=True)
        
        heap=[]
        speedsum,res=0,0    
        for eff,spd in arr:
            
            
            if len(heap)==k:
                
                speedsum-=heapq.heappop(heap)
            speedsum+=spd
            heapq.heappush(heap,spd)
            res=max(res,eff*speedsum)
            
        return res%(10**9 +7)    
            
            
            
            