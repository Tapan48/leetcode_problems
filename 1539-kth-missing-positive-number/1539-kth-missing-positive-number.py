class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        
        n=1
        
        array=[]
        
        while len(array)!=k:
            
            
            if n not in arr:
                array.append(n)
                
            n+=1
            
        return array[-1]    