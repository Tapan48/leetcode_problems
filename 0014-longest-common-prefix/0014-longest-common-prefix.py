class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        minlen=float("inf")
        
        for string in strs:
            
                                  
            
            if len(string)<minlen:
                
                minlen=len(string)
                
        s=""        
        for i in range(minlen):
            
            char=strs[0][i]
            cnt=0
            for string in strs:
                
                
                if string[i]==char:
                    cnt+=1
                    
                else:
                    return s
            if cnt==len(strs):
                s+=char
                
        return s        
                
                
                
                
            
            
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        