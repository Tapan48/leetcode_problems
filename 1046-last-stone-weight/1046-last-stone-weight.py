class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        