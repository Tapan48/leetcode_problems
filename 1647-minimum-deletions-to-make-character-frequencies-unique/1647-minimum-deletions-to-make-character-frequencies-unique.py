class Solution:
    def minDeletions(self, s: str) -> int:
        
        
        
        
        freqmap=Counter(s)
        
        res=0
        
        freq_added=set()
        
        
        for c,freq in freqmap.items():
            
            
            while freq>0 and freq in freq_added:
                
                
                freq-=1
                res+=1
            freq_added.add(freq)
            
        return res    
        