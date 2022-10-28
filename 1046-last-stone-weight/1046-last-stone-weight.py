
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        """
        stones.sort()
        
        
        while len(stones)!=1 and len(stones)>0:
            
            firlarg=stones.pop()
            seclarg=stones.pop()
            
            if firlarg!=seclarg:
                diff=firlarg-seclarg
                
                stones.append(diff)
                stones.sort()
                
        if len(stones)==0:
            return 0 
        else:
            return stones[0]
        """
        
        
        stonesnew=[-x for x in stones]
        heapq.heapify(stonesnew)
        
        while len(stonesnew)>1 :
            
           
            print(stonesnew)
            larg1=heapq.heappop(stonesnew)
            larg2=heapq.heappop(stonesnew)
            
            
            if larg1!=larg2:
                
                val=larg1-larg2
                heapq.heappush(stonesnew,val)
        
        
        stonesnew.append(0)
        return abs(stonesnew[0])        
                
           
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        