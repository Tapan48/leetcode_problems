
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
        
        while len(stonesnew)!=1 and len(stonesnew)>0:
            
           
            print(stonesnew)
            larg1=abs(heapq.heappop(stonesnew))
            larg2=abs(heapq.heappop(stonesnew))
            
            
            if larg1!=larg2:
                
                diff=larg1-larg2
                val=(-1)*diff
                heapq.heappush(stonesnew,val)
                
        if len(stonesnew)==0:
            return 0
        else:
            return abs(stonesnew[0])       
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        