class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        l,res=0,0
        freq={}
       
        max_freq_count = 0
        
        for r in range(len(s)):
            
            freq[s[r]]=freq.get(s[r],0)+1
            
         
            max_freq_count = max(freq[s[r]],max_freq_count)
               
                
                
                
            while (r-l+1)- max_freq_count>k:
                
                freq[s[l]]-=1
                l+=1
            res=max(res,r-l+1)    
        return res
                
            
            
            
            
            
            
        