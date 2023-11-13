class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        
        
        
        s1dictt=Counter(s1)
        s2dictt={}
        
        l=0
        for r in range(len(s2)):
            
            s2dictt[s2[r]]=s2dictt.get(s2[r],0)+1
            
            if (r-l+1)>len(s1):
                s2dictt[s2[l]]-=1
                if s2dictt[s2[l]] == 0:
                    del s2dictt[s2[l]]

                l+=1
            # Compare dictionaries
            if s1dictt == s2dictt:
                return True
        return False    
            
            
            
          
                
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        