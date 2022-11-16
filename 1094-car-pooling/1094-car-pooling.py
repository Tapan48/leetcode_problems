class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        trips.sort(key=lambda x:x[1]) ## sorted according to start point of 2d array
        
        
        
        
        minheap=[]        ##  (end points,numpass of trip)
        currpass=0
        for trip in trips:
            
            
            numpass,start,end=trip
            currpass+=numpass
            
            while minheap and start>=minheap[0][0]:
                
                currpass-=minheap[0][1]
                heapq.heappop(minheap)
                
                
                
            if currpass>capacity:
                return False
                
            heapq.heappush(minheap,[end,numpass])
            
        return True   
            
            
        
        
        
        
        